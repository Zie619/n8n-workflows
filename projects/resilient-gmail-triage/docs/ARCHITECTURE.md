# Architecture — Resilient Gmail Triage

## Scope

The project is a portable n8n 2.30.x solution that:

1. polls new or still-unprocessed Gmail messages every minute;
2. deduplicates work by Gmail message ID;
3. normalizes untrusted email content;
4. applies deterministic spam and prompt-injection guards;
5. classifies safe content with Gemini structured JSON;
6. creates at most one Gmail draft per message;
7. routes at most one Discord notification with category, urgency, owner role, summary and proposed reply;
8. reconciles Gmail labels and finalizes the message;
9. retries stale work with bounded exponential backoff;
10. logs and reports workflow failures without placing credentials or raw email bodies in technical alerts.

## Workflow boundaries

- `01 - Gmail Triage - Intake and Classify`
- `02 - Gmail Triage - Act and Notify`
- `03 - Gmail Triage - Recovery and Diagnostics`
- `04 - Gmail Triage - Global Error Handler`
- `05 - Gmail Triage - Controlled Failure` (test only)

Every exported workflow is inactive. Workflow 05 exists only to demonstrate the automatic error path and should not run as part of normal operations.

## State machine

```text
Normal intake:       PROCESSING → CLASSIFIED
Gemini retry:        PROCESSING → RETRY_CLASSIFICATION → PROCESSING
Normal action:       CLASSIFIED → DRAFT_CREATED → NOTIFIED → PROCESSED
Spam:                CLASSIFIED → PROCESSED
Prompt injection:    PROCESSING → QUARANTINED
Retry exhaustion:    PROCESSING|RETRY_CLASSIFICATION → QUARANTINED
Orphan recovery:     RECEIVED → PROCESSING → CLASSIFIED|RETRY_CLASSIFICATION
```

Critical urgency does not create a separate textual state. It changes the Gmail labels and Discord roles: the crisis owner and optional backup role are mentioned directly.

`draft_created` and `discord_notified` are durable checkpoints. A retry must not repeat a completed side effect even if an older textual status is still visible.

## Discord routing

The route map is stored in workflow code and the current team assignment is stored in Discord roles supplied through environment variables:

```text
DISCORD_ROLE_SALES
DISCORD_ROLE_CLIENT_SUCCESS
DISCORD_ROLE_CRISIS
DISCORD_ROLE_CRISIS_BACKUP
DISCORD_ROLE_FINANCE
DISCORD_ROLE_LEGAL_PRIVACY
DISCORD_ROLE_ADMIN
```

Changing a person normally requires changing Discord role membership, not editing the workflow. The seven webhook credentials separate business queues at the channel boundary.

## Data and privacy boundary

Data Tables are referenced by name:

- `message_processing_state` stores state, classification, summary and draft checkpoints;
- `system_health` stores component health and queue telemetry;
- `system_events` stores sanitized technical events.

A normal Discord notification contains an AI-generated summary and proposed reply. It does not include the raw body or sender address, but the generated text may still reproduce personal or confidential information. Production access to Discord should therefore match access to the shared mailbox, or a dedicated PII-redaction step should be added.

Prompt-injection alerts are stricter: they contain only a technical reference, quarantine timestamp and Gmail link.

## Recovery and diagnostics

Workflow 03 performs three independent jobs:

- bounded recovery of stale intake and classification rows;
- a safety scan for recent Gmail messages missing from Data Tables;
- queue and component health reporting.

Pending work produces `DEGRADED`; stale backlog or retry-exhausted quarantine produces `CRITICAL`; telemetry older than 30 minutes produces `UNKNOWN`.

## Portability and secrets

- Credentials are referenced by expected n8n names and resolved at deploy time.
- Discord role IDs come from n8n environment variables.
- Gmail labels are replaced from an ignored local label map.
- API keys, OAuth tokens, webhook URLs, passwords and credential values never enter Git.
- Deployment reads the n8n API key from an environment variable or an ignored local file.
- The browser test console reads its recipient and transport configuration only on the server side.

## Manual trust boundary

A human must still:

- authorize or reconnect Gmail OAuth;
- configure Gemini and Discord credentials;
- create or confirm Gmail labels;
- assign people to Discord roles;
- inspect one synthetic end-to-end execution;
- activate workflows 01–04 after acceptance;
- keep workflow 05 inactive outside a supervised error test.

Everything else is generated, tested, imported inactive and verified automatically.
