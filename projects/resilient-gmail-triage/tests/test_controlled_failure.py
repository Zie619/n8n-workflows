import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = PROJECT_ROOT / "workflows" / "05_controlled_failure.json"


def test_controlled_failure_is_isolated_and_uses_global_handler() -> None:
    workflow = json.loads(WORKFLOW.read_text(encoding="utf-8"))
    nodes = {node["name"]: node for node in workflow["nodes"]}

    assert workflow["active"] is False
    assert workflow["settings"]["errorWorkflow"] == "__ERROR_WORKFLOW_ID__"
    assert nodes["Manual Test Launcher"]["type"] == "n8n-nodes-base.manualTrigger"
    assert nodes["Invoke Automatic Failure"]["type"] == "n8n-nodes-base.httpRequest"
    assert nodes["Invoke Automatic Failure"]["parameters"]["method"] == "POST"
    assert nodes["Invoke Automatic Failure"]["parameters"]["url"] == (
        "http://127.0.0.1:5678/webhook/gmail-triage-controlled-failure"
    )
    assert nodes["Webhook - Symulacja błędu"]["parameters"]["path"] == (
        "gmail-triage-controlled-failure"
    )
    assert "throw new Error" in nodes["Kontrolowany błąd"]["parameters"]["jsCode"]
    assert workflow["connections"]["Manual Test Launcher"]["main"][0][0]["node"] == (
        "Invoke Automatic Failure"
    )
    assert workflow["connections"]["Webhook - Symulacja błędu"]["main"][0][0]["node"] == (
        "Kontrolowany błąd"
    )
    assert all("credentials" not in node for node in workflow["nodes"])
