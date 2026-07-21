from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping, Optional


class Decision(str, Enum):
    CREATE_DRAFT = "CREATE_DRAFT"
    NOTIFY_DISCORD = "NOTIFY_DISCORD"
    ESCALATE = "ESCALATE"
    FINALIZE = "FINALIZE"
    QUARANTINE = "QUARANTINE"
    WAIT = "WAIT"


@dataclass(frozen=True)
class RecoveryDecision:
    status: str
    attempts: int
    retry_delay_seconds: Optional[int]


_TERMINAL = {"PROCESSED", "QUARANTINED"}
_BACKOFF_SECONDS = (60, 300, 900, 1800, 3600)


def _as_int(value: object) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float, str)):
        try:
            return int(value)
        except (TypeError, ValueError):
            return 0
    return 0


def select_action(state: Mapping[str, object]) -> Decision:
    status = str(state.get("status") or "")
    category = str(state.get("category") or "")
    attempts = _as_int(state.get("attempts"))
    draft_created = bool(state.get("draft_created"))
    discord_notified = bool(state.get("discord_notified"))

    if status in _TERMINAL:
        return Decision.WAIT
    if attempts >= 5 or category == "PROMPT_INJECTION":
        return Decision.QUARANTINE
    if category == "SPAM" and status in {"CLASSIFIED", "RETRY"}:
        return Decision.FINALIZE
    if status == "NEEDS_ESCALATION" and discord_notified:
        return Decision.ESCALATE
    if status in {"ESCALATED", "NOTIFIED"}:
        return Decision.FINALIZE
    if draft_created and not discord_notified:
        return Decision.NOTIFY_DISCORD
    if status in {"CLASSIFIED", "RETRY"} and not draft_created:
        return Decision.CREATE_DRAFT
    return Decision.WAIT


def queue_health(rows: list[Mapping[str, object]], *, now_epoch: int) -> str:
    terminal = {"PROCESSED", "QUARANTINED"}
    pending = [row for row in rows if str(row.get("status") or "") not in terminal]
    quarantined = [row for row in rows if str(row.get("status") or "") == "QUARANTINED"]
    stale = [
        row
        for row in pending
        if now_epoch - _as_int(row.get("updated_at_epoch")) > 600
    ]
    if stale or len(pending) > 20 or len(quarantined) > 5:
        return "CRITICAL"
    if pending or quarantined:
        return "DEGRADED"
    return "HEALTHY"


def decide_recovery(
    state: Mapping[str, object], *, now_epoch: int
) -> Optional[RecoveryDecision]:
    status = str(state.get("status") or "")
    attempts = _as_int(state.get("attempts"))

    if status in _TERMINAL:
        return None
    if attempts >= 5:
        return RecoveryDecision("QUARANTINED", attempts, None)
    if status not in {"RECEIVED", "PROCESSING"}:
        return None

    updated_at = _as_int(state.get("updated_at_epoch"))
    if now_epoch - updated_at <= 600:
        return None

    new_attempts = attempts + 1
    delay = _BACKOFF_SECONDS[min(new_attempts - 1, len(_BACKOFF_SECONDS) - 1)]
    return RecoveryDecision("RETRY", new_attempts, delay)
