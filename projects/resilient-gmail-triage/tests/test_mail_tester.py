from __future__ import annotations

import json
import random
import ssl
from email import policy
from email.parser import BytesParser

import pytest

from tools.mail_tester.app import (
    GmailApiSender,
    MailRequest,
    SMTPSender,
    load_scenarios,
    resolve_messages,
    validate_custom_message,
)


def scenarios_file(tmp_path):
    path = tmp_path / "fixtures.json"
    path.write_text(
        json.dumps(
            [
                {
                    "id": "offer",
                    "category": "OFFER_INQUIRY",
                    "urgency": "normal",
                    "title": "Zapytanie ofertowe",
                    "description": "Standardowe zapytanie sprzedażowe",
                    "subject": "Prośba o ofertę",
                    "body": "Dzień dobry, proszę o ofertę wdrożenia automatyzacji.",
                },
                {
                    "id": "incident",
                    "category": "TECHNICAL_INCIDENT",
                    "urgency": "critical",
                    "title": "Awaria usługi",
                    "description": "Pilna wiadomość techniczna",
                    "subject": "PILNE: system nie działa",
                    "body": "Od rana nie możemy korzystać z usługi. Proszę o pilną pomoc.",
                },
            ]
        ),
        encoding="utf-8",
    )
    return path


def test_load_scenarios_rejects_duplicate_ids(tmp_path):
    path = scenarios_file(tmp_path)
    rows = json.loads(path.read_text())
    rows.append(rows[0])
    path.write_text(json.dumps(rows))

    with pytest.raises(ValueError, match="duplicate scenario id"):
        load_scenarios(path)


def test_custom_message_validation_rejects_empty_and_oversized_values():
    with pytest.raises(ValueError, match="subject"):
        validate_custom_message("", "Treść")
    with pytest.raises(ValueError, match="body"):
        validate_custom_message("Temat", "")
    with pytest.raises(ValueError, match="subject"):
        validate_custom_message("x" * 201, "Treść")
    with pytest.raises(ValueError, match="body"):
        validate_custom_message("Temat", "x" * 5001)


def test_gmail_api_transport_fails_early_without_optional_adapter(tmp_path):
    with pytest.raises(FileNotFoundError, match="optional Hermes Google Workspace adapter"):
        GmailApiSender(google_api=tmp_path / "missing-google-api.py")


def test_resolve_selected_messages_adds_unique_test_marker(tmp_path):
    scenarios = load_scenarios(scenarios_file(tmp_path))
    request = MailRequest(mode="selected", scenario_ids=("offer", "incident"))

    messages = resolve_messages(request, scenarios, rng=random.Random(2), now_token="20260720-120001")

    assert len(messages) == 2
    assert messages[0].subject.startswith("[E2E-20260720-120001-01]")
    assert messages[1].subject.startswith("[E2E-20260720-120001-02]")
    assert {message.scenario_id for message in messages} == {"offer", "incident"}


def test_resolve_messages_rejects_more_than_twelve_selected(tmp_path):
    scenarios = load_scenarios(scenarios_file(tmp_path))
    scenarios = {f"offer-{index}": value for index, value in enumerate([next(iter(scenarios.values()))] * 13)}
    request = MailRequest(mode="selected", scenario_ids=tuple(scenarios))

    with pytest.raises(ValueError, match="maximum batch size"):
        resolve_messages(request, scenarios, rng=random.Random(1), now_token="token")


def test_random_mode_chooses_one_known_scenario(tmp_path):
    scenarios = load_scenarios(scenarios_file(tmp_path))
    request = MailRequest(mode="random")

    messages = resolve_messages(request, scenarios, rng=random.Random(0), now_token="token")

    assert len(messages) == 1
    assert messages[0].scenario_id in scenarios


def test_custom_mode_never_accepts_recipient_from_request(tmp_path):
    scenarios = load_scenarios(scenarios_file(tmp_path))
    request = MailRequest(mode="custom", subject="Mój temat", body="Moja treść")

    [message] = resolve_messages(request, scenarios, rng=random.Random(0), now_token="token")

    assert not hasattr(message, "recipient")
    assert message.subject == "[E2E-token-01] Mój temat"


def test_smtp_sender_uses_server_side_sender_and_recipient():
    calls = []

    class FakeSMTP:
        def __init__(self, host, port, timeout):
            calls.append(("connect", host, port, timeout))

        def __enter__(self):
            return self

        def __exit__(self, *_):
            return None

        def starttls(self):
            calls.append(("starttls",))

        def login(self, username, password):
            calls.append(("login", username, password))

        def send_message(self, message):
            calls.append(("message", message.as_bytes()))
            return {}

    sender = SMTPSender(
        host="127.0.0.1",
        port=1025,
        from_address="tester@example.invalid",
        username=None,
        password=None,
        starttls=False,
        smtp_factory=FakeSMTP,
    )
    result = sender.send(
        recipient="contact@example.invalid",
        subject="Test",
        body="Treść",
    )

    raw = next(call[1] for call in calls if call[0] == "message")
    parsed = BytesParser(policy=policy.default).parsebytes(raw)
    plain = parsed.get_body(preferencelist=("plain",))
    assert plain is not None
    assert parsed["To"] == "contact@example.invalid"
    assert parsed["From"] == "tester@example.invalid"
    assert parsed["Subject"] == "Test"
    assert plain.get_content().strip() == "Treść"
    assert result["transport"] == "smtp"
    assert result["id"]


def test_smtp_starttls_verifies_server_certificate():
    seen = []

    class FakeSMTP:
        def __init__(self, host, port, timeout):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *_):
            return None

        def starttls(self, *, context):
            seen.append(context)

        def send_message(self, message):
            return {}

    sender = SMTPSender(
        host="smtp.example.invalid",
        port=587,
        from_address="tester@example.invalid",
        username=None,
        password=None,
        starttls=True,
        smtp_factory=FakeSMTP,
    )
    sender.send(recipient="contact@example.invalid", subject="Test TLS", body="Treść")

    assert len(seen) == 1
    assert isinstance(seen[0], ssl.SSLContext)
    assert seen[0].check_hostname is True
    assert seen[0].verify_mode == ssl.CERT_REQUIRED
