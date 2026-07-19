from __future__ import annotations

from src.audit_stress_run import (
    compare_results,
    extract_execution_classifications,
    extract_test_id,
)


def expected_row(test_id: str = "STRESS-RUN-001") -> dict:
    return {
        "test_id": test_id,
        "expected": {
            "category": "OFFER_INQUIRY",
            "status": "PROCESSED",
            "draft_created": True,
            "discord_notified": True,
            "admin_alert": False,
            "labels": ["AUTO/PROCESSED"],
        },
    }


def test_extracts_test_id_from_subject():
    assert extract_test_id("Re: [STRESS-20260719-A-031] Long subject") == "STRESS-20260719-A-031"
    assert extract_test_id("ordinary subject") is None


def test_extracts_classification_mapping_from_both_intake_branches():
    execution = {
        "data": {
            "resultData": {
                "runData": {
                    "Finalize and Validate": [{
                        "data": {"main": [[{"json": {
                            "subject": "[STRESS-RUN-001] Offer",
                            "gmail_message_id": "gmail-1",
                            "category": "OFFER_INQUIRY",
                        }}]]}
                    }],
                    "Local Safety Result": [{
                        "data": {"main": [[{"json": {
                            "subject": "[STRESS-RUN-002] Injection",
                            "gmail_message_id": "gmail-2",
                            "category": "PROMPT_INJECTION",
                        }}]]}
                    }],
                }
            }
        }
    }
    assert extract_execution_classifications(execution) == {
        "STRESS-RUN-001": {"gmail_message_id": "gmail-1", "intake_category": "OFFER_INQUIRY"},
        "STRESS-RUN-002": {"gmail_message_id": "gmail-2", "intake_category": "PROMPT_INJECTION"},
    }


def test_reports_a_fully_matching_result():
    expected = [expected_row()]
    actual = {
        "STRESS-RUN-001": {
            "category": "OFFER_INQUIRY",
            "status": "PROCESSED",
            "draft_created": True,
            "discord_notified": True,
        }
    }
    report = compare_results(expected, actual)
    assert report["matched"] == 1
    assert report["pending"] == []
    assert report["missing"] == []
    assert report["mismatches"] == []


def test_distinguishes_pending_missing_and_wrong_classification():
    expected = [
        expected_row("STRESS-RUN-001"),
        expected_row("STRESS-RUN-002"),
        expected_row("STRESS-RUN-003"),
    ]
    actual = {
        "STRESS-RUN-001": {
            "category": "OTHER",
            "status": "PROCESSED",
            "draft_created": True,
            "discord_notified": True,
        },
        "STRESS-RUN-002": {
            "category": "OFFER_INQUIRY",
            "status": "DRAFT_CREATED",
            "draft_created": True,
            "discord_notified": False,
        },
    }
    report = compare_results(expected, actual)
    assert report["matched"] == 0
    assert report["missing"] == ["STRESS-RUN-003"]
    assert report["pending"] == ["STRESS-RUN-002"]
    assert report["mismatches"][0]["test_id"] == "STRESS-RUN-001"
    assert report["mismatches"][0]["fields"]["category"] == {
        "expected": "OFFER_INQUIRY",
        "actual": "OTHER",
    }
