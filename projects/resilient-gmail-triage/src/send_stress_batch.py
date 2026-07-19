from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Callable

HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
HERMES_PYTHON = Path(os.environ.get("HERMES_PYTHON", sys.executable))
GOOGLE_API = Path(
    os.environ.get(
        "HERMES_GOOGLE_API",
        HERMES_HOME / "skills/productivity/google-workspace/scripts/google_api.py",
    )
)

Sender = Callable[..., dict]
Sleeper = Callable[[float], None]


def _load_state(path: Path, recipient: str) -> dict:
    if path.exists():
        state = json.loads(path.read_text())
        existing_recipient = state.get("recipient")
        if existing_recipient and existing_recipient != recipient:
            raise ValueError("send state recipient does not match requested recipient")
    else:
        state = {"recipient": recipient, "sent": {}, "last_error_test_id": None}
    state.setdefault("recipient", recipient)
    state.setdefault("sent", {})
    return state


def _save_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def gmail_sender(*, recipient: str, subject: str, body: str) -> dict:
    result = subprocess.run(
        [
            str(HERMES_PYTHON),
            str(GOOGLE_API),
            "gmail",
            "send",
            "--to",
            recipient,
            "--subject",
            subject,
            "--body",
            body,
        ],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=90,
    )
    if result.returncode != 0:
        raise RuntimeError("Gmail API send failed; stopped to prevent ambiguous retries")
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError("Gmail API returned non-JSON output") from error
    if not payload.get("id"):
        raise RuntimeError("Gmail API did not return a message ID")
    return payload


def send_range(
    fixtures: list[dict],
    *,
    recipient: str,
    start: int,
    stop: int,
    state_path: Path,
    sender: Sender = gmail_sender,
    sleep: Sleeper = time.sleep,
    interval_seconds: float = 180,
) -> dict:
    if start < 1 or stop < start:
        raise ValueError("invalid fixture sequence range")

    state_path = Path(state_path)
    state = _load_state(state_path, recipient)
    selected = sorted(
        (row for row in fixtures if start <= int(row["sequence"]) <= stop),
        key=lambda row: int(row["sequence"]),
    )
    selected_sequences = [int(row["sequence"]) for row in selected]
    if selected_sequences != list(range(start, stop + 1)):
        raise ValueError("fixture set does not fully cover requested range")

    grouped: dict[int, list[dict]] = defaultdict(list)
    for row in selected:
        grouped[int(row["batch"])].append(row)

    completed_nonempty_batches = 0
    for batch_number in sorted(grouped):
        pending = [row for row in grouped[batch_number] if row["test_id"] not in state["sent"]]
        if not pending:
            continue
        if completed_nonempty_batches:
            sleep(interval_seconds)
        print(f"BATCH_START batch={batch_number} pending={len(pending)}", flush=True)
        for row in pending:
            try:
                response = sender(
                    recipient=recipient,
                    subject=row["subject"],
                    body=row["body"],
                )
            except Exception:
                state["last_error_test_id"] = row["test_id"]
                _save_state(state_path, state)
                print(f"SEND_STOPPED test_id={row['test_id']}", flush=True)
                raise
            state["sent"][row["test_id"]] = {
                "sequence": row["sequence"],
                "gmail_message_id": response["id"],
                "gmail_thread_id": response.get("threadId"),
            }
            state["last_error_test_id"] = None
            _save_state(state_path, state)
            print(
                f"SEND_CONFIRMED batch={batch_number} test_id={row['test_id']} gmail_id={response['id']}",
                flush=True,
            )
        completed_nonempty_batches += 1
        print(f"BATCH_COMPLETE batch={batch_number}", flush=True)

    confirmed_in_range = sum(row["test_id"] in state["sent"] for row in selected)
    result = {
        "requested_start": start,
        "requested_stop": stop,
        "confirmed_sent": confirmed_in_range,
        "recipient": recipient,
    }
    print("SEND_RANGE_COMPLETE " + json.dumps(result, sort_keys=True), flush=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Send an idempotent range of stress-test fixtures")
    parser.add_argument("--fixtures", required=True, type=Path)
    parser.add_argument("--recipient", required=True)
    parser.add_argument("--start", required=True, type=int)
    parser.add_argument("--stop", required=True, type=int)
    parser.add_argument("--state", required=True, type=Path)
    parser.add_argument("--interval-seconds", type=float, default=180)
    args = parser.parse_args()

    fixtures = json.loads(args.fixtures.read_text())
    send_range(
        fixtures,
        recipient=args.recipient,
        start=args.start,
        stop=args.stop,
        state_path=args.state,
        interval_seconds=args.interval_seconds,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
