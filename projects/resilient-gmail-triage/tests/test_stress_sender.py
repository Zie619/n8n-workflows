from __future__ import annotations

import json

import pytest

from src.send_stress_batch import send_range


def sample_rows(count: int = 40) -> list[dict]:
    return [
        {
            "sequence": i,
            "batch": (i - 1) // 10 + 1,
            "test_id": f"STRESS-{i:03d}",
            "subject": f"[STRESS-{i:03d}] Subject {i}",
            "body": f"Body {i}",
        }
        for i in range(1, count + 1)
    ]


def test_sends_only_requested_30_in_three_batches(tmp_path):
    sent = []
    sleeps = []

    def sender(*, recipient, subject, body):
        sent.append((recipient, subject, body))
        return {"id": f"gmail-{len(sent)}", "threadId": f"thread-{len(sent)}"}

    result = send_range(
        sample_rows(),
        recipient="target@example.invalid",
        start=1,
        stop=30,
        state_path=tmp_path / "send_state.json",
        sender=sender,
        sleep=sleeps.append,
        interval_seconds=180,
    )

    assert result["confirmed_sent"] == 30
    assert len(sent) == 30
    assert all("STRESS-031" not in subject for _, subject, _ in sent)
    assert sleeps == [180, 180]
    state = json.loads((tmp_path / "send_state.json").read_text())
    assert len(state["sent"]) == 30


def test_rerun_does_not_send_duplicates_or_extend_range(tmp_path):
    calls = []

    def sender(**kwargs):
        calls.append(kwargs)
        return {"id": f"gmail-{len(calls)}"}

    kwargs = {
        "fixtures": sample_rows(),
        "recipient": "target@example.invalid",
        "start": 1,
        "stop": 30,
        "state_path": tmp_path / "send_state.json",
        "sender": sender,
        "sleep": lambda _: None,
        "interval_seconds": 0,
    }
    send_range(**kwargs)
    send_range(**kwargs)
    assert len(calls) == 30


def test_failure_stops_without_marking_failed_message_as_sent(tmp_path):
    calls = []

    def sender(**kwargs):
        calls.append(kwargs)
        if len(calls) == 6:
            raise RuntimeError("synthetic send failure")
        return {"id": f"gmail-{len(calls)}"}

    with pytest.raises(RuntimeError, match="synthetic send failure"):
        send_range(
            sample_rows(),
            recipient="target@example.invalid",
            start=1,
            stop=30,
            state_path=tmp_path / "send_state.json",
            sender=sender,
            sleep=lambda _: None,
            interval_seconds=0,
        )

    state = json.loads((tmp_path / "send_state.json").read_text())
    assert len(state["sent"]) == 5
    assert state["last_error_test_id"] == "STRESS-006"


def test_incomplete_fixture_range_is_rejected_before_sending(tmp_path):
    incomplete = [row for row in sample_rows(30) if row["sequence"] != 17]
    calls = []
    with pytest.raises(ValueError, match="fully cover requested range"):
        send_range(
            incomplete,
            recipient="target@example.invalid",
            start=1,
            stop=30,
            state_path=tmp_path / "send_state.json",
            sender=lambda **kwargs: calls.append(kwargs) or {"id": "never"},
            sleep=lambda _: None,
            interval_seconds=0,
        )
    assert calls == []


def test_existing_state_cannot_be_reused_for_another_recipient(tmp_path):
    state_path = tmp_path / "send_state.json"
    state_path.write_text(json.dumps({"recipient": "first@example.invalid", "sent": {}}))

    with pytest.raises(ValueError, match="recipient"):
        send_range(
            sample_rows(),
            recipient="second@example.invalid",
            start=1,
            stop=30,
            state_path=state_path,
            sender=lambda **_: {"id": "never"},
            sleep=lambda _: None,
            interval_seconds=0,
        )
