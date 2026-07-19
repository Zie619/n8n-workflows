from __future__ import annotations

import json
import re

from src.generate_stress_fixtures import (
    SCENARIOS,
    generate_fixtures,
    write_fixture_set,
)


RUN_ID = "stress-20260719"
EXISTING_CATEGORIES = {
    "OFFER_INQUIRY",
    "EXISTING_CLIENT",
    "COMPLAINT_ESCALATION",
    "BILLING",
    "TECHNICAL_INCIDENT",
    "LEGAL_PRIVACY",
    "PARTNERSHIP_RECRUITMENT",
    "SPAM",
    "OTHER",
}
SCENARIO_GROUPS = EXISTING_CATEGORIES | {"PROMPT_INJECTION", "UNEXPECTED"}


def fixtures() -> list[dict]:
    return generate_fixtures(RUN_ID)


def test_generates_110_balanced_scenarios():
    rows = fixtures()
    assert len(rows) == 110
    assert {row["scenario_group"] for row in rows} == SCENARIO_GROUPS
    for group in SCENARIO_GROUPS:
        assert sum(row["scenario_group"] == group for row in rows) == 10


def test_first_30_cover_every_scenario_group():
    first_30 = fixtures()[:30]
    counts = {
        group: sum(row["scenario_group"] == group for row in first_30)
        for group in SCENARIO_GROUPS
    }
    assert set(counts) == SCENARIO_GROUPS
    assert all(count in {2, 3} for count in counts.values())


def test_every_fixture_is_long_and_unique():
    rows = fixtures()
    assert min(len(row["body"]) for row in rows) >= 1_200
    assert max(len(row["body"]) for row in rows) <= 4_500
    assert len({row["test_id"] for row in rows}) == 110
    assert len({row["subject"] for row in rows}) == 110
    assert len({row["body"] for row in rows}) == 110
    assert all(row["test_id"] in row["subject"] for row in rows)
    assert all(row["test_id"] in row["body"] for row in rows)


def test_subjects_are_unique_but_do_not_reveal_category_or_case_topic():
    rows = fixtures()
    forbidden_fragments = {
        "case", "scenario", "variant", "offer", "proposal", "client", "complaint",
        "billing", "invoice", "payment", "technical", "incident", "legal", "privacy",
        "partnership", "recruitment", "spam", "promotion", "inquiry", "request",
        "account", "service", "urgent", "escalation", "clarification", "report",
        "assistance", "refund", "compensation", "breach", "violation", "deadline",
        "formal", "serious", "critical", "failed", "oferta", "klient", "reklamac", "faktur",
        "płat", "plat", "technic", "awari", "prawn", "prywat", "partner",
        "rekrut", "piln", "пропоз", "клієнт", "клиент", "скарг", "жалоб",
        "рахунок", "счет", "платіж", "платеж", "техніч", "техничес",
        "інцидент", "инцидент", "конфіденц", "конфиденц", "ваканс",
    }
    scenario_phrases = {
        phrase.lower()
        for scenario in SCENARIOS
        for phrase in (scenario.subject, *scenario.details)
    }
    for row in rows:
        neutral = re.sub(r"^\[[^]]+\]\s*", "", row["subject"]).lower()
        assert 12 <= len(neutral) <= 120
        assert not any(fragment in neutral for fragment in forbidden_fragments)
        assert not any(phrase in neutral for phrase in scenario_phrases)


def test_expected_categories_and_side_effects_are_explicit():
    rows = fixtures()
    for row in rows:
        expected = row["expected"]
        assert expected["category"] in EXISTING_CATEGORIES | {"PROMPT_INJECTION"}
        assert expected["status"] in {"PROCESSED", "QUARANTINED"}
        assert isinstance(expected["draft_created"], bool)
        assert isinstance(expected["discord_notified"], bool)
        assert isinstance(expected["admin_alert"], bool)
        assert expected["labels"]

        if row["scenario_group"] == "PROMPT_INJECTION":
            assert expected == {
                "category": "PROMPT_INJECTION",
                "status": "QUARANTINED",
                "draft_created": False,
                "discord_notified": True,
                "admin_alert": True,
                "labels": ["AUTO/QUARANTINED"],
            }
        elif row["scenario_group"] == "SPAM":
            assert expected["category"] == "SPAM"
            assert expected["draft_created"] is False
            assert expected["discord_notified"] is False
            assert expected["admin_alert"] is False
        else:
            assert expected["status"] == "PROCESSED"
            assert expected["draft_created"] is True
            assert expected["discord_notified"] is True
            assert expected["admin_alert"] is False

    assert all(
        row["expected"]["category"] == "OTHER"
        for row in rows
        if row["scenario_group"] == "UNEXPECTED"
    )


def test_fixture_set_is_multilingual_and_json_serializable():
    rows = fixtures()
    languages = {row["language"] for row in rows}
    assert languages == {"pl", "en", "uk", "ru"}
    json.dumps(rows, ensure_ascii=False)


def test_fixture_set_can_be_written_as_auditable_artifacts(tmp_path):
    output = write_fixture_set(RUN_ID, tmp_path)
    assert output == tmp_path
    manifest = json.loads((tmp_path / "fixtures.json").read_text())
    assert len(manifest) == 110
    assert (tmp_path / "ground_truth.csv").exists()
    message_files = sorted((tmp_path / "messages").glob("*.txt"))
    assert len(message_files) == 110
    assert manifest[0]["body"] == message_files[0].read_text()


def test_no_real_secrets_or_live_tracking_links_are_embedded():
    raw = json.dumps(fixtures(), ensure_ascii=False)
    forbidden = [
        r"discord(?:app)?\.com/api/webhooks/",
        r"AIza[0-9A-Za-z_-]{20,}",
        r"Bearer\s+[A-Za-z0-9._-]{20,}",
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        r"https?://(?![A-Za-z0-9.-]*example\.invalid)",
    ]
    for pattern in forbidden:
        assert re.search(pattern, raw, flags=re.IGNORECASE) is None
