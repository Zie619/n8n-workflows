import json
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEMO_BATCH = PROJECT_ROOT / "video" / "final_demo_batch.json"
CYRILLIC = re.compile(r"[\u0400-\u04FF]")
TECHNICAL_MARKER = re.compile(r"PREZENTACJA|FILM|DEMO|identyfikator-prezentacji", re.IGNORECASE)


def test_all_demo_email_subjects_and_bodies_are_polish() -> None:
    messages = json.loads(DEMO_BATCH.read_text(encoding="utf-8"))

    assert messages, "Paczka demonstracyjna nie może być pusta"
    for message in messages:
        subject = message["subject"]
        body = message["body"]
        assert not subject.startswith("["), subject
        assert not TECHNICAL_MARKER.search(subject), subject
        assert not TECHNICAL_MARKER.search(body), subject
        assert not CYRILLIC.search(subject), subject
        assert not CYRILLIC.search(body), subject

        assert body.startswith(("Dzień dobry", "Szanowni Państwo")), subject
        assert "Pozdrawiam" in body or "Z poważaniem" in body, subject
