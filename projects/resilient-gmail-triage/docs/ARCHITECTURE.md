# Architecture — Resilient Gmail Triage

## Scope

Build a portable n8n 2.30.x project that:

1. polls unread Gmail messages;
2. deduplicates by Gmail message ID;
3. normalizes untrusted email content;
4. applies deterministic spam/prompt-injection guards;
5. classifies safe content with Gemini structured JSON;
6. creates at most one Gmail draft per message;
7. sends at most one privacy-minimized Discord notification;
8. labels and finalizes the Gmail message;
9. retries stale work with bounded exponential backoff;
10. logs and alerts on workflow errors without leaking secrets or email content.

## Workflows

- `01 - Gmail Triage - Intake and Classify`
- `02 - Gmail Triage - Act and Notify`
- `03 - Gmail Triage - Recovery and Diagnostics` — bounded stale-item recovery, orphan-message safety scan, queue diagnostics, and daily health reporting
- `04 - Gmail Triage - Global Error Handler`

Every exported workflow is inactive. Production activation is an explicit post-verification action.

## State machine

```text
Normal intake: PROCESSING -> CLASSIFIED
Safety scan orphan: RECEIVED -> PROCESSING -> CLASSIFIED
Normal action: CLASSIFIED -> DRAFT_CREATED -> NOTIFIED -> PROCESSED
Critical action: CLASSIFIED -> DRAFT_CREATED -> NEEDS_ESCALATION -> ESCALATED -> PROCESSED
RECEIVED|PROCESSING -> RETRY -> PROCESSING
* -> QUARANTINED (terminal after policy violation or max retries)
```

The normal intake atomically upserts `PROCESSING`; `RECEIVED` is reserved for orphan messages found by the recovery safety scan. This avoids an extra state write on the primary path while retaining explicit recovery visibility.

`draft_created` and `discord_notified` are durable checkpoints. A retry must never repeat a side effect whose checkpoint is true.

## Portability and secrets

- Data Tables are referenced by name.
- Credentials are referenced by expected n8n names/types and resolved at deploy time.
- Discord role IDs are read through n8n environment variables.
- API keys, OAuth tokens, webhook URLs, passwords and credential values never enter Git.
- Deployment reads the n8n API key from an environment variable or an ignored local file.

## Source repository use

This project is built inside the MIT-licensed `Zie619/n8n-workflows` collection. Existing Gmail, Gemini, Discord and error-handler workflows are treated as pattern references only. They are not imported directly because several use sanitized `noOp` nodes, incomplete connections, hardcoded account metadata, or destructive actions.

## Manual UI boundary

The user performs only operations that require an interactive trust boundary:

- confirm/reconnect Gmail OAuth;
- confirm Gemini and Discord credentials if automatic name binding is unavailable;
- create/confirm Gmail labels;
- inspect one synthetic email execution;
- activate workflows after acceptance checks.

Everything else is generated, tested, imported inactive, and verified automatically.
