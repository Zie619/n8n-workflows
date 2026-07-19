# Resilient Gmail → Gemini → Discord Triage

A tested n8n 2.30.x project for idempotent Gmail intake, deterministic safety checks, Gemini structured classification, Gmail draft creation, privacy-minimized Discord routing, bounded recovery, and truthful health reporting.

## Workflows

| File | Imported workflow |
|---|---|
| `workflows/01_intake_classify.json` | `01 - Gmail Triage - Intake and Classify` |
| `workflows/02_act_notify.json` | `02 - Gmail Triage - Act and Notify` |
| `workflows/03_recovery_diagnostics.json` | `03 - Gmail Triage - Recovery and Diagnostics` |
| `workflows/04_error_handler.json` | `04 - Gmail Triage - Global Error Handler` |

All generated exports are inactive. Deployment never activates a workflow.

## Why actions advance over multiple ticks

`02` uses durable checkpoint workers. Draft, Discord and finalization read the state independently at the start of each execution:

```text
Tick 1: CLASSIFIED -> create one draft -> DRAFT_CREATED
Tick 2: DRAFT_CREATED -> send one Discord alert -> NOTIFIED
Tick 3: NOTIFIED -> apply labels -> PROCESSED
```

This deliberate eventual-consistency design prevents a Discord retry from recreating a Gmail draft. During manual testing, run `Manual Act` three times. With the schedule active, the transitions happen automatically on subsequent minute ticks.

## Safety properties

- Gmail message ID is the idempotency key.
- `draft_created` and `discord_notified` are durable side-effect checkpoints.
- Prompt injection is handled by deterministic multilingual code (English, Polish, Russian, Ukrainian), never creates a draft, and never enters normal Discord routing.
- Requests to reveal `.env`, secrets, tokens, passwords, or API keys are quarantined before Gemini.
- Finalization reconciles managed labels before applying the result, so a corrected decision cannot leave conflicting `SPAM`, `URGENT`, `PROCESSED`, or `QUARANTINED` labels.
- Durable side-effect checkpoints take precedence over a stale textual status during concurrent minute ticks.
- Discord receives category, urgency, owner role and Gmail thread ID only—never the message body or sender address.
- Credential values and webhook URLs never enter Git.
- Gemini authenticates through the n8n credential, never `?key=` in a URL.
- Recovery is bounded to five attempts with exponential backoff.
- A pending item is `DEGRADED`; a stale item is `CRITICAL`.
- Health telemetry older than 30 minutes is `UNKNOWN`, not falsely green.

## Source repository

This package is developed in a fork of the MIT-licensed [`Zie619/n8n-workflows`](https://github.com/Zie619/n8n-workflows) collection. Existing templates were used as pattern references only; none was imported directly because some collection exports contain sanitized `noOp` nodes, incomplete connections, or hardcoded account metadata.

Reference workflows reviewed:

- `workflows/Gmail/1914_Gmail_Stickynote_Send_Triggered.json`
- `workflows/Telegram/1841_Telegram_Manual_Automate_Triggered.json`
- `workflows/Error/0945_Error_Code_Send_Triggered.json`
- `workflows/Schedule/1345_Schedule_Discord_Automation_Scheduled.json`

## Generate and test

```bash
cd projects/resilient-gmail-triage
python3 src/generate_workflows.py
python3 -m pytest -q
```

## Preflight deployment

```bash
python3 src/deploy.py \
  --api-key-file /path/to/ignored/n8n-api-key \
  --label-map-file /path/to/ignored/label_ids.json
```

## Import inactive

```bash
python3 src/deploy.py \
  --api-key-file /path/to/ignored/n8n-api-key \
  --label-map-file /path/to/ignored/label_ids.json \
  --apply
```

The deployer:

1. resolves credential IDs by exact name and type;
2. verifies the three Data Tables;
3. replaces Gmail label placeholders locally;
4. imports or updates the error handler first;
5. assigns its ID to the operational workflows;
6. deactivates defensively and verifies every imported workflow is inactive.

## Required n8n credentials

- `Gmail - Contact Mailbox` (`gmailOAuth2`)
- `Gemini - Mail Triage` (`googlePalmApi`)
- `Discord - Mail Triage` (`discordWebhookApi`)
- `Discord - Automation Alerts` (`discordWebhookApi`)

## Required Data Tables

- `message_processing_state`
- `system_health`
- `system_events`

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) and [`docs/UI_ACCEPTANCE_PL.md`](docs/UI_ACCEPTANCE_PL.md).
