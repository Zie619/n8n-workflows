#!/usr/bin/env python3
"""Preflight and import generated workflows into n8n, always inactive."""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / "workflows"

CREDENTIAL_SPECS = {
    ("Gmail - Contact Mailbox", "gmailOAuth2"): "__CREDENTIAL_GMAIL_ID__",
    ("Gemini - Mail Triage", "googlePalmApi"): "__CREDENTIAL_GEMINI_ID__",
    ("Discord - Mail Triage", "discordWebhookApi"): "__CREDENTIAL_DISCORD_TRIAGE_ID__",
    ("Discord - Automation Alerts", "discordWebhookApi"): "__CREDENTIAL_DISCORD_ERROR_ID__",
}

LABEL_SPECS = {
    "AUTO/PROCESSING": "__LABEL_AUTO_PROCESSING__",
    "AUTO/PROCESSED": "__LABEL_AUTO_PROCESSED__",
    "AUTO/URGENT": "__LABEL_AUTO_URGENT__",
    "AUTO/MANUAL_REVIEW": "__LABEL_AUTO_MANUAL_REVIEW__",
    "AUTO/QUARANTINED": "__LABEL_AUTO_QUARANTINED__",
    "AUTO/SPAM": "__LABEL_AUTO_SPAM__",
}

EXPECTED_TABLES = {
    "message_processing_state",
    "system_health",
    "system_events",
}

ORDER = [
    "04_error_handler.json",
    "01_intake_classify.json",
    "02_act_notify.json",
    "03_recovery_diagnostics.json",
]

_PLACEHOLDER = re.compile(r"__[A-Z0-9_]+__")


class DeploymentError(RuntimeError):
    pass


def resolve_credential_ids(rows: Iterable[dict[str, Any]]) -> dict[str, str]:
    grouped: dict[tuple[str, str], list[str]] = {}
    for row in rows:
        key = (str(row.get("name") or ""), str(row.get("type") or ""))
        grouped.setdefault(key, []).append(str(row.get("id") or ""))

    resolved: dict[str, str] = {}
    for spec, placeholder in CREDENTIAL_SPECS.items():
        ids = [value for value in grouped.get(spec, []) if value]
        if len(ids) > 1:
            raise DeploymentError(
                f"ambiguous credential reference: {spec[0]} ({spec[1]})"
            )
        if ids:
            resolved[placeholder] = ids[0]
    return resolved


def replace_placeholders(value: Any, replacements: dict[str, str]) -> Any:
    def replace(current: Any) -> Any:
        if isinstance(current, dict):
            return {key: replace(item) for key, item in current.items()}
        if isinstance(current, list):
            return [replace(item) for item in current]
        if isinstance(current, str):
            result = current
            for placeholder, replacement in replacements.items():
                result = result.replace(placeholder, replacement)
            return result
        return current

    result = replace(copy.deepcopy(value))
    unresolved = sorted(set(_PLACEHOLDER.findall(json.dumps(result))))
    if unresolved:
        raise DeploymentError("unresolved placeholders: " + ", ".join(unresolved))
    return result


def build_api_payload(
    workflow: dict[str, Any], *, require_inactive: bool = False
) -> dict[str, Any]:
    if require_inactive and workflow.get("active") is not False:
        raise DeploymentError(f"workflow {workflow.get('name')} must be inactive")
    required = {"name", "nodes", "connections", "settings"}
    missing = required - workflow.keys()
    if missing:
        raise DeploymentError("workflow missing keys: " + ", ".join(sorted(missing)))
    return {key: copy.deepcopy(workflow[key]) for key in required}


class N8nClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "X-N8N-API-KEY": api_key,
            "Content-Type": "application/json",
        }

    def request(self, method: str, path: str, payload: Any = None) -> Any:
        body = None if payload is None else json.dumps(payload).encode()
        request = urllib.request.Request(
            self.base_url + path,
            method=method,
            headers=self.headers,
            data=body,
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                raw = response.read()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as error:
            detail = error.read().decode(errors="replace")[:500]
            raise DeploymentError(
                f"n8n API {method} {path} failed with HTTP {error.code}: {detail}"
            ) from error

    def list_all(self, path: str) -> list[dict[str, Any]]:
        result = self.request("GET", path)
        if not isinstance(result, dict):
            raise DeploymentError(f"unexpected response from {path}")
        return list(result.get("data", []))


def load_api_key(args: argparse.Namespace) -> str:
    if os.environ.get("N8N_API_KEY"):
        return os.environ["N8N_API_KEY"].strip()
    if args.api_key_file:
        path = Path(args.api_key_file).expanduser()
        if path.exists():
            return path.read_text().strip()
    raise DeploymentError(
        "set N8N_API_KEY or pass --api-key-file; the key is never printed"
    )


def load_label_replacements(path: str) -> dict[str, str]:
    data = json.loads(Path(path).expanduser().read_text())
    missing = sorted(set(LABEL_SPECS) - set(data))
    if missing:
        raise DeploymentError("label map missing names: " + ", ".join(missing))
    return {placeholder: str(data[name]) for name, placeholder in LABEL_SPECS.items()}


def load_templates() -> dict[str, dict[str, Any]]:
    templates = {}
    for filename in ORDER:
        path = WORKFLOW_DIR / filename
        if not path.exists():
            raise DeploymentError(f"missing generated workflow: {path}")
        templates[filename] = json.loads(path.read_text())
    return templates


def upsert_inactive(
    client: N8nClient,
    payload: dict[str, Any],
    current_by_name: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    existing = current_by_name.get(payload["name"])
    if existing:
        workflow_id = str(existing["id"])
        if existing.get("active"):
            client.request("POST", f"/api/v1/workflows/{workflow_id}/deactivate")
        result = client.request("PUT", f"/api/v1/workflows/{workflow_id}", payload)
    else:
        result = client.request("POST", "/api/v1/workflows", payload)
        workflow_id = str(result["id"])

    # Deactivate defensively even though create/update does not activate.
    if result.get("active"):
        client.request("POST", f"/api/v1/workflows/{workflow_id}/deactivate")
        result = client.request("GET", f"/api/v1/workflows/{workflow_id}")
    if result.get("active"):
        raise DeploymentError(f"workflow remained active after import: {payload['name']}")
    return result


def preflight(client: N8nClient) -> tuple[dict[str, str], set[str]]:
    credentials = client.list_all("/api/v1/credentials?limit=100")
    credential_ids = resolve_credential_ids(credentials)
    missing_credentials = sorted(
        set(CREDENTIAL_SPECS.values()) - set(credential_ids)
    )
    if missing_credentials:
        missing_names = [
            name
            for (name, _type), placeholder in CREDENTIAL_SPECS.items()
            if placeholder in missing_credentials
        ]
        raise DeploymentError(
            "missing n8n credentials: " + ", ".join(missing_names)
        )

    tables = client.list_all("/api/v1/data-tables?limit=100")
    table_names = {str(row.get("name") or "") for row in tables}
    missing_tables = sorted(EXPECTED_TABLES - table_names)
    if missing_tables:
        raise DeploymentError("missing Data Tables: " + ", ".join(missing_tables))
    return credential_ids, table_names


def deploy(args: argparse.Namespace) -> dict[str, Any]:
    client = N8nClient(args.base_url, load_api_key(args))
    credential_ids, table_names = preflight(client)
    replacements = {
        **credential_ids,
        **load_label_replacements(args.label_map_file),
    }
    templates = load_templates()

    if not args.apply:
        # Check all static replacements except the runtime error workflow ID.
        dry_replacements = {**replacements, "__ERROR_WORKFLOW_ID__": "dry-run-error-id"}
        for template in templates.values():
            replace_placeholders(build_api_payload(template, require_inactive=True), dry_replacements)
        return {
            "mode": "dry-run",
            "workflows": [templates[name]["name"] for name in ORDER],
            "credentials_resolved": len(credential_ids),
            "tables_found": sorted(table_names & EXPECTED_TABLES),
        }

    current = client.list_all("/api/v1/workflows?limit=250")
    current_by_name = {str(row.get("name") or ""): row for row in current}
    deployed = []

    error_template = templates["04_error_handler.json"]
    error_payload = replace_placeholders(
        build_api_payload(error_template, require_inactive=True), replacements
    )
    error_result = upsert_inactive(client, error_payload, current_by_name)
    error_id = str(error_result["id"])
    deployed.append({"name": error_result["name"], "id": error_id, "active": False})
    current_by_name[error_result["name"]] = error_result

    runtime_replacements = {
        **replacements,
        "__ERROR_WORKFLOW_ID__": error_id,
    }
    for filename in ORDER[1:]:
        payload = replace_placeholders(
            build_api_payload(templates[filename], require_inactive=True),
            runtime_replacements,
        )
        result = upsert_inactive(client, payload, current_by_name)
        deployed.append({"name": result["name"], "id": result["id"], "active": False})
        current_by_name[result["name"]] = result

    state_path = ROOT / ".deploy-state.json"
    state_path.write_text(json.dumps({"workflows": deployed}, indent=2) + "\n")
    return {"mode": "apply", "deployed": deployed, "all_inactive": True}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--base-url", default="http://127.0.0.1:5678")
    result.add_argument("--api-key-file")
    result.add_argument("--label-map-file", required=True)
    result.add_argument(
        "--apply",
        action="store_true",
        help="write to n8n; without this flag only preflight is performed",
    )
    return result


def main() -> None:
    try:
        result = deploy(parser().parse_args())
    except DeploymentError as error:
        raise SystemExit(f"deployment failed: {error}") from error
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
