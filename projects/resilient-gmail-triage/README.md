# Resilient Gmail → Gemini → Discord Triage

A tested n8n 2.30.x project for handling a shared contact mailbox. It classifies incoming Gmail messages with Gemini, creates review-only drafts, routes notifications to the right Discord channel and role, applies Gmail labels, and reports failures instead of silently dropping work.

## What is included

| File | Workflow | Purpose |
|---|---|---|
| `workflows/01_intake_classify.json` | `01 - Gmail Triage - Intake and Classify` | Gmail polling, deduplication, safety guard and Gemini classification |
| `workflows/02_act_notify.json` | `02 - Gmail Triage - Act and Notify` | Gmail draft, Discord routing and final labels |
| `workflows/03_recovery_diagnostics.json` | `03 - Gmail Triage - Recovery and Diagnostics` | Retry, orphan scan, queue health and daily report |
| `workflows/04_error_handler.json` | `04 - Gmail Triage - Global Error Handler` | Sanitized error log and Discord alert |
| `workflows/05_controlled_failure.json` | `05 - Gmail Triage - Controlled Failure` | Demonstration-only test of the automatic error path |

All JSON exports are inactive. Workflow 05 must stay inactive except during a supervised error-handler demonstration.

## Processing model

Workflow 01 polls Gmail every minute and upserts one durable state row per Gmail message ID. Workflow 02 uses three checkpoint workers that read state independently:

```text
Tick 1: CLASSIFIED    → create one Gmail draft → DRAFT_CREATED
Tick 2: DRAFT_CREATED → send one Discord alert → NOTIFIED
Tick 3: NOTIFIED      → reconcile labels       → PROCESSED
```

This is deliberate eventual consistency. A Discord retry cannot recreate a draft whose `draft_created` checkpoint is already true.

A normal Discord notification contains:

- category and urgency;
- the responsible role;
- a short AI-generated summary;
- the proposed reply prepared for human review;
- a link to the Gmail thread.

Prompt injection does not enter this route. It is quarantined before Gemini and produces one metadata-only security alert without sender, subject or message content.

## Categories and routing

| Category | Discord route |
|---|---|
| `OFFER_INQUIRY` | Sprzedaż |
| `EXISTING_CLIENT` | Obsługa klienta |
| `COMPLAINT_ESCALATION` | Incydenty i eskalacje |
| `TECHNICAL_INCIDENT` | Incydenty i eskalacje |
| `BILLING` | Finanse |
| `LEGAL_PRIVACY` | Prawo i prywatność |
| `PARTNERSHIP_RECRUITMENT` | Administracja |
| `OTHER` | Inne |
| `SPAM` | no Discord notification |
| `PROMPT_INJECTION` | metadata-only security alert to Inne |

Critical messages also mention the crisis backup role and receive the urgent Gmail label.

## Reliability and safety

- Gmail message ID is the idempotency key.
- `draft_created` and `discord_notified` are durable side-effect checkpoints.
- Gemini uses structured JSON and temperature 0.
- Prompt injection and secret-exfiltration requests are checked deterministically before the model call.
- Retries are bounded to five attempts with exponential backoff.
- Recovery scans stale state and recent Gmail messages missing from Data Tables.
- Health older than 30 minutes becomes `UNKNOWN`, not falsely green.
- Error alerts are sanitized before they enter Discord or `system_events`.
- Credential values, API keys, OAuth tokens and webhook URLs never enter Git.

The normal Discord summary and draft may still contain personal information inferred from the email. A production rollout should align Discord channel access with mailbox access or add PII redaction.

## Required n8n configuration

Credentials:

- `Gmail - Contact Mailbox` (`gmailOAuth2`)
- `Gemini - Mail Triage` (`googlePalmApi`)
- `Discord - Sprzedaż` (`discordWebhookApi`)
- `Discord - Obsługa klienta` (`discordWebhookApi`)
- `Discord - Incydenty i eskalacje` (`discordWebhookApi`)
- `Discord - Finanse` (`discordWebhookApi`)
- `Discord - Prawo i prywatność` (`discordWebhookApi`)
- `Discord - Administracja` (`discordWebhookApi`)
- `Discord - Inne` (`discordWebhookApi`)

Data Tables:

- `message_processing_state`
- `system_health`
- `system_events`

Discord role IDs are supplied through n8n environment variables. See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the full list.

## Generate and test

```bash
python3 src/generate_workflows.py
pytest -q
```

## Import safely

Preflight only:

```bash
python3 src/deploy.py \
  --api-key-file /path/to/ignored/n8n-api-key \
  --label-map-file /path/to/ignored/label_ids.json
```

Import or update, still inactive:

```bash
python3 src/deploy.py \
  --api-key-file /path/to/ignored/n8n-api-key \
  --label-map-file /path/to/ignored/label_ids.json \
  --apply
```

The deployer resolves credential IDs by exact name and type, verifies the Data Tables, replaces label placeholders, wires the global error workflow, imports the workflows and verifies that every imported export remains inactive.

## Browser-based test console

`tools/mail_tester/` contains a local web application for a client acceptance test. It can send one prepared fixture, a selected batch, a custom message or a random scenario. The recipient is fixed on the server side.

Dry-run:

```bash
TEST_MAIL_TRANSPORT=dry-run \
TEST_MAIL_RECIPIENT=contact@example.invalid \
python3 -m tools.mail_tester.app --port 8040
```

Open `http://127.0.0.1:8040`. See [`tools/mail_tester/README.md`](tools/mail_tester/README.md) for Gmail API and local SMTP/Mailpit modes.

## Documentation

- [`DOKUMENTACJA_REKRUTACYJNA_PL.md`](DOKUMENTACJA_REKRUTACYJNA_PL.md) — short submission document
- [`DOKUMENTACJA_TECHNICZNA_PL.md`](DOKUMENTACJA_TECHNICZNA_PL.md) — detailed technical appendix
- [`docs/UI_ACCEPTANCE_PL.md`](docs/UI_ACCEPTANCE_PL.md) — acceptance procedure
- [`ODPOWIEDZI_NA_CASEY_PL.md`](ODPOWIEDZI_NA_CASEY_PL.md) — client communication cases
- [`WYZWANIA_I_DECYZJE_PL.md`](WYZWANIA_I_DECYZJE_PL.md) — challenges, trade-offs and next steps

This project is developed in a fork of the MIT-licensed [`Zie619/n8n-workflows`](https://github.com/Zie619/n8n-workflows) collection. Existing workflows were used as pattern references only; the five workflows in this directory were generated for this solution.
