import json
import pytest

WORKFLOW_FILE = "workflows/Code/1825_Code_Webhook_Automation_Webhook.json"

PAYLOADS = [
    "{{ $('API').item.json.body.password }}",  # exact exploit: template expression as password
    "' OR '1'='1",                              # boundary: SQL injection attempt
    "validP@ssw0rd123",                         # valid input
]

@pytest.mark.parametrize("payload", PAYLOADS)
def test_no_hardcoded_credentials_in_workflow(payload):
    """Invariant: Workflow JSON must not contain hardcoded plaintext passwords or
    expose credential values directly in node parameters accessible via API download."""
    with open(WORKFLOW_FILE, "r") as f:
        workflow_content = f.read()
        workflow = json.loads(workflow_content)

    # Collect all string values recursively from the workflow
    def extract_strings(obj):
        if isinstance(obj, str):
            yield obj
        elif isinstance(obj, dict):
            for v in obj.values():
                yield from extract_strings(v)
        elif isinstance(obj, list):
            for item in obj:
                yield from extract_strings(item)

    all_strings = list(extract_strings(workflow))

    # No node parameter should contain a literal plaintext password value
    # (valid input payload should not appear hardcoded in the workflow)
    if payload == "validP@ssw0rd123":
        assert payload not in all_strings, (
            f"Hardcoded password '{payload}' found in workflow file"
        )

    # Shell scripts in the workflow must not assign passwords via unquoted/unsafe variable expansion
    for s in all_strings:
        if "NEW_PASSWORD=" in s or "PASSWORD=" in s:
            # Must not directly embed a resolved/literal password string
            assert payload not in s or "{{" in s, (
                f"Unsafe password assignment found with payload '{payload}' in: {s[:120]}"
            )