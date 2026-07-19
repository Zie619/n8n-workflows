from __future__ import annotations

import re

TERMINAL_STATUSES = {"PROCESSED", "QUARANTINED"}
TEST_ID_PATTERN = re.compile(r"\[(STRESS-[A-Z0-9-]+-\d{3})\]", re.IGNORECASE)


def extract_test_id(subject: str) -> str | None:
    match = TEST_ID_PATTERN.search(subject or "")
    return match.group(1).upper() if match else None


def extract_execution_classifications(execution: dict) -> dict[str, dict]:
    run_data = execution.get("data", {}).get("resultData", {}).get("runData", {})
    found: dict[str, dict] = {}
    for node_name in ("Finalize and Validate", "Local Safety Result"):
        for run in run_data.get(node_name, []):
            for branch in run.get("data", {}).get("main", []):
                for item in branch or []:
                    value = item.get("json", {})
                    test_id = extract_test_id(str(value.get("subject") or ""))
                    message_id = value.get("gmail_message_id")
                    if test_id and message_id:
                        found[test_id] = {
                            "gmail_message_id": message_id,
                            "intake_category": value.get("category"),
                        }
    return found


def compare_results(fixtures: list[dict], actual_by_test_id: dict[str, dict]) -> dict:
    report = {
        "total": len(fixtures),
        "matched": 0,
        "pending": [],
        "missing": [],
        "mismatches": [],
    }
    compared_fields = ("category", "status", "draft_created", "discord_notified")

    for fixture in fixtures:
        test_id = fixture["test_id"]
        expected = fixture["expected"]
        actual = actual_by_test_id.get(test_id)
        if actual is None:
            report["missing"].append(test_id)
            continue
        if actual.get("status") not in TERMINAL_STATUSES:
            report["pending"].append(test_id)
            continue

        differences = {}
        for field in compared_fields:
            expected_value = expected[field]
            actual_value = bool(actual.get(field)) if isinstance(expected_value, bool) else actual.get(field)
            if actual_value != expected_value:
                differences[field] = {"expected": expected_value, "actual": actual_value}
        if differences:
            report["mismatches"].append({"test_id": test_id, "fields": differences})
        else:
            report["matched"] += 1

    return report
