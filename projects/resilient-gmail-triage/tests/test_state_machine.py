from __future__ import annotations

import pytest

from src.state_machine import (
    Decision,
    decide_recovery,
    queue_health,
    select_action,
)


def test_classified_message_without_draft_selects_draft_once():
    state = {
        "status": "CLASSIFIED",
        "category": "BILLING",
        "draft_created": False,
        "discord_notified": False,
        "attempts": 1,
    }
    assert select_action(state) == Decision.CREATE_DRAFT


def test_draft_checkpoint_prevents_duplicate_draft():
    state = {
        "status": "DRAFT_CREATED",
        "category": "BILLING",
        "draft_created": True,
        "discord_notified": False,
        "attempts": 1,
    }
    assert select_action(state) == Decision.NOTIFY_DISCORD


def test_discord_checkpoint_prevents_duplicate_notification():
    state = {
        "status": "NOTIFIED",
        "category": "BILLING",
        "draft_created": True,
        "discord_notified": True,
        "attempts": 1,
    }
    assert select_action(state) == Decision.FINALIZE


def test_prompt_injection_never_creates_draft_or_discord_notification():
    state = {
        "status": "CLASSIFIED",
        "category": "PROMPT_INJECTION",
        "draft_created": False,
        "discord_notified": False,
        "attempts": 1,
    }
    assert select_action(state) == Decision.QUARANTINE


def test_spam_skips_side_effects_and_finalizes():
    state = {
        "status": "CLASSIFIED",
        "category": "SPAM",
        "draft_created": False,
        "discord_notified": False,
        "attempts": 1,
    }
    assert select_action(state) == Decision.FINALIZE


def test_max_attempts_quarantines():
    state = {
        "status": "RETRY",
        "category": "OTHER",
        "draft_created": False,
        "discord_notified": False,
        "attempts": 5,
    }
    assert select_action(state) == Decision.QUARANTINE


def test_stale_processing_retries_with_bounded_backoff():
    result = decide_recovery(
        {
            "status": "PROCESSING",
            "attempts": 2,
            "updated_at_epoch": 1_000,
        },
        now_epoch=1_000 + 601,
    )
    assert result.status == "RETRY"
    assert result.attempts == 3
    assert result.retry_delay_seconds == 900


def test_fresh_processing_is_left_alone():
    result = decide_recovery(
        {
            "status": "PROCESSING",
            "attempts": 1,
            "updated_at_epoch": 1_000,
        },
        now_epoch=1_100,
    )
    assert result is None


def test_empty_queue_is_healthy():
    assert queue_health([], now_epoch=10_000) == "HEALTHY"


def test_any_pending_work_is_degraded_even_before_stale_threshold():
    rows = [{"status": "DRAFT_CREATED", "updated_at_epoch": 9_950}]
    assert queue_health(rows, now_epoch=10_000) == "DEGRADED"


def test_stale_work_is_critical():
    rows = [{"status": "PROCESSING", "updated_at_epoch": 9_000}]
    assert queue_health(rows, now_epoch=10_000) == "CRITICAL"
