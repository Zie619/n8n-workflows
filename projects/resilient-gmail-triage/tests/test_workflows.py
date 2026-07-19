from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / "workflows"
EXPECTED = {
    "01_intake_classify.json": "01 - Gmail Triage - Intake and Classify",
    "02_act_notify.json": "02 - Gmail Triage - Act and Notify",
    "03_recovery_diagnostics.json": "03 - Gmail Triage - Recovery and Diagnostics",
    "04_error_handler.json": "04 - Gmail Triage - Global Error Handler",
}


def load_workflows() -> dict[str, dict]:
    loaded = {}
    for filename in EXPECTED:
        path = WORKFLOW_DIR / filename
        assert path.exists(), f"missing generated workflow: {path}"
        loaded[filename] = json.loads(path.read_text())
    return loaded


def node_by_name(workflow: dict, name: str) -> dict:
    matches = [node for node in workflow["nodes"] if node["name"] == name]
    assert len(matches) == 1, f"expected one node named {name}, got {len(matches)}"
    return matches[0]


def all_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def test_generated_exports_do_not_use_fake_version_ids():
    for workflow in load_workflows().values():
        assert "versionId" not in workflow


def test_discord_selector_requires_durable_draft_created_status():
    act = load_workflows()["02_act_notify.json"]
    code_text = node_by_name(act, "Select Discord Work")["parameters"]["jsCode"]
    assert "j.status === 'DRAFT_CREATED'" in code_text
    assert "['DRAFT_CREATED','CLASSIFIED','RETRY']" not in code_text


def test_queue_health_tracks_a_real_consecutive_failure_counter():
    recovery = load_workflows()["03_recovery_diagnostics.json"]
    code_text = node_by_name(recovery, "Compute Queue Health")["parameters"]["jsCode"]
    assert "$getWorkflowStaticData('global')" in code_text
    assert "queueFailures" in code_text


def test_all_expected_workflows_exist_and_are_inactive():
    workflows = load_workflows()
    assert {data["name"] for data in workflows.values()} == set(EXPECTED.values())
    assert all(data.get("active") is False for data in workflows.values())


def test_workflows_have_unique_node_ids_and_valid_connection_targets():
    for filename, workflow in load_workflows().items():
        ids = [node["id"] for node in workflow["nodes"]]
        names = {node["name"] for node in workflow["nodes"]}
        assert len(ids) == len(set(ids)), filename
        for source, outputs in workflow["connections"].items():
            assert source in names, f"{filename}: missing connection source {source}"
            for channel in outputs.values():
                for branch in channel:
                    for edge in branch:
                        assert edge["node"] in names, f"{filename}: missing target {edge['node']}"


def test_no_embedded_secrets_or_raw_webhooks():
    forbidden = [
        r"discord(?:app)?\.com/api/webhooks/",
        r"generativelanguage\.googleapis\.com[^\"\s]*[?&]key=",
        r"(?i)authorization[\"']?\s*:\s*[\"']?bearer\s+[A-Za-z0-9._-]+",
        r"(?i)(?:api[_-]?key|password|client_secret)[\"']?\s*[:=]\s*[\"'][^{{$][^\"']+",
    ]
    for filename, workflow in load_workflows().items():
        raw = all_text(workflow)
        for pattern in forbidden:
            assert not re.search(pattern, raw), f"{filename}: matched secret pattern {pattern}"


def test_expected_credentials_are_references_only():
    allowed = {
        ("gmailOAuth2", "Gmail - Contact Mailbox"),
        ("googlePalmApi", "Gemini - Mail Triage"),
        ("discordWebhookApi", "Discord - Mail Triage"),
        ("discordWebhookApi", "Discord - Automation Alerts"),
    }
    seen = set()
    for workflow in load_workflows().values():
        for node in workflow["nodes"]:
            for credential_type, ref in node.get("credentials", {}).items():
                assert set(ref) <= {"id", "name"}
                pair = (credential_type, ref.get("name"))
                assert pair in allowed, pair
                seen.add(pair)
    assert seen == allowed


def test_data_tables_are_referenced_by_name():
    allowed = {"message_processing_state", "system_health", "system_events"}
    seen = set()
    for workflow in load_workflows().values():
        for node in workflow["nodes"]:
            if node["type"] != "n8n-nodes-base.dataTable":
                continue
            locator = node["parameters"]["dataTableId"]
            assert locator["mode"] == "name"
            assert locator["value"] in allowed
            seen.add(locator["value"])
    assert seen == allowed


def test_gemini_uses_json_body_and_credential_auth_without_key_in_url():
    main = load_workflows()["01_intake_classify.json"]
    node = node_by_name(main, "Gemini Structured Classify")
    p = node["parameters"]
    assert p["authentication"] == "predefinedCredentialType"
    assert p["nodeCredentialType"] == "googlePalmApi"
    assert p["sendBody"] is True
    assert p["contentType"] == "raw"
    assert p["rawContentType"] == "application/json"
    assert "JSON.stringify($json.gemini_payload)" in p["body"]
    assert "?key=" not in p["url"]
    assert node["retryOnFail"] is True
    assert node["maxTries"] == 3


def test_side_effect_checkpoint_filters_reference_pre_side_effect_items():
    act = load_workflows()["02_act_notify.json"]
    expectations = {
        "Mark DRAFT_CREATED": "Select Draft Work",
        "Mark NOTIFIED": "Build Discord",
        "Mark ESCALATED": "Select Critical Escalation",
        "Save Final Status": "Select Finalize Work",
    }
    for update_name, source_name in expectations.items():
        node = node_by_name(act, update_name)
        raw = all_text(node["parameters"].get("filters", {}))
        assert source_name in raw, f"{update_name} must reference {source_name}"
        assert "gmail_message_id" in raw


def test_code_nodes_use_per_item_mode_when_their_code_returns_single_item():
    main = load_workflows()["01_intake_classify.json"]
    for name in ["Normalize and Guard", "Local Safety Result", "Finalize and Validate"]:
        node = node_by_name(main, name)
        assert node["parameters"].get("mode") == "runOnceForEachItem"


def test_every_operational_workflow_references_global_error_handler_placeholder():
    workflows = load_workflows()
    for filename in ["01_intake_classify.json", "02_act_notify.json", "03_recovery_diagnostics.json"]:
        assert workflows[filename]["settings"]["errorWorkflow"] == "__ERROR_WORKFLOW_ID__"


def test_error_alert_does_not_depend_on_data_table_output():
    error_workflow = load_workflows()["04_error_handler.json"]
    branches = error_workflow["connections"]["Sanitize"]["main"][0]
    targets = {edge["node"] for edge in branches}
    assert targets == {"Log Event", "Discord Error"}


def test_processing_label_uses_gate_item_after_state_write():
    main = load_workflows()["01_intake_classify.json"]
    node = node_by_name(main, "Add PROCESSING Label")
    assert "Gate" in all_text(node["parameters"])
    state_write = node_by_name(main, "Mark PROCESSING")
    assert state_write.get("alwaysOutputData") is True


def test_no_destructive_gmail_operations():
    destructive = {"delete", "trash", "send"}
    for filename, workflow in load_workflows().items():
        for node in workflow["nodes"]:
            if node["type"] != "n8n-nodes-base.gmail":
                continue
            operation = node.get("parameters", {}).get("operation", "send")
            resource = node.get("parameters", {}).get("resource", "message")
            if resource == "draft" and operation == "create":
                continue
            assert operation not in destructive, f"{filename}: destructive Gmail operation {operation}"
