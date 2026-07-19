from __future__ import annotations

import json
from pathlib import Path

import pytest

from src.deploy import (
    DeploymentError,
    build_api_payload,
    replace_placeholders,
    resolve_credential_ids,
)


def test_resolve_credential_ids_matches_name_and_type():
    rows = [
        {"id": "gmail-id", "name": "Gmail - Contact Mailbox", "type": "gmailOAuth2"},
        {"id": "gemini-id", "name": "Gemini - Mail Triage", "type": "googlePalmApi"},
    ]
    assert resolve_credential_ids(rows) == {
        "__CREDENTIAL_GMAIL_ID__": "gmail-id",
        "__CREDENTIAL_GEMINI_ID__": "gemini-id",
    }


def test_duplicate_credential_name_and_type_is_rejected():
    rows = [
        {"id": "one", "name": "Gmail - Contact Mailbox", "type": "gmailOAuth2"},
        {"id": "two", "name": "Gmail - Contact Mailbox", "type": "gmailOAuth2"},
    ]
    with pytest.raises(DeploymentError, match="ambiguous"):
        resolve_credential_ids(rows)


def test_replace_placeholders_is_recursive_and_rejects_unresolved_values():
    data = {"a": ["__ONE__", {"b": "prefix __TWO__ suffix"}]}
    assert replace_placeholders(data, {"__ONE__": "1", "__TWO__": "2"}) == {
        "a": ["1", {"b": "prefix 2 suffix"}]
    }
    with pytest.raises(DeploymentError, match="unresolved"):
        replace_placeholders({"a": "__MISSING__"}, {})


def test_build_api_payload_drops_activation_and_export_metadata():
    workflow = {
        "name": "Example",
        "nodes": [],
        "connections": {},
        "settings": {},
        "active": True,
        "versionId": "unsafe",
        "pinData": {"secret": "must not deploy"},
        "id": "old-id",
    }
    payload = build_api_payload(workflow)
    assert payload == {
        "name": "Example",
        "nodes": [],
        "connections": {},
        "settings": {},
    }
    assert "active" not in payload


def test_build_api_payload_requires_inactive_export():
    workflow = {
        "name": "Example",
        "nodes": [],
        "connections": {},
        "settings": {},
        "active": True,
    }
    with pytest.raises(DeploymentError, match="must be inactive"):
        build_api_payload(workflow, require_inactive=True)
