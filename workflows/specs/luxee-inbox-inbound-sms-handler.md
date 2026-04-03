# Workflow Spec — `[Luxee] Inbox — Inbound SMS Handler`

**Version:** 1.0  
**Author:** Luxee  
**Client:** luxee-internal  
**Domain:** inbox  
**Tags:** `client:luxee-internal`, `domain:inbox`  
**Priority:** P0 — required for MVP  
**Depends on:** Supabase schema migration 001, Twilio webhook configured, channel_connections record seeded

---

## Purpose

Receive inbound SMS messages from Twilio, normalize to the Luxee canonical message payload,
persist the message in Supabase, route to the AI analysis sub-workflow, and update the
conversation status. If no conversation exists for the sender, create one.

---

## Trigger

- **Node name:** `[TRIGGER] Receive Twilio SMS Webhook`
- **Type:** Webhook (POST)
- **Path:** Configured in n8n, forwarded from the Next.js `/api/webhooks/twilio` route
- **Authentication:** Header secret (`X-Webhook-Secret`)
- **Expected body:** JSON with Twilio SMS fields (`Body`, `From`, `To`, `MessageSid`, etc.)

---

## Layer architecture

```
[TRIGGER]      Receive Twilio SMS Webhook
    ↓
[BRIDGE]       Normalize SMS Payload
    ↓
[VALIDATION]   Check Required Fields (From, Body, MessageSid)
    ↓
[IDEMPOTENCY]  Check Duplicate Message (by external_message_id in Supabase)
    ↓
[PROCESSING]   Resolve Channel Connection (lookup by To phone number)
    ↓
[PROCESSING]   Resolve or Create Conversation
    ↓
[PROCESSING]   Resolve or Create Contact
    ↓
[OUTPUT]       Insert Message to Supabase
    ↓
[OUTPUT]       Update Conversation (last_message_at, is_read=false)
    ↓
[OUTPUT]       Trigger AI Analysis Sub-Workflow (async, fire-and-forget)
    ↓
[LOGGING]      Write Execution Log to events_log
    ↓
[ERROR]        Classify Error (connected to critical nodes via error path)
```

---

## Node specifications

### `[TRIGGER] Receive Twilio SMS Webhook`
- Type: Webhook
- Method: POST
- Response: 200 immediately (Twilio requires fast ACK)
- Respond before processing to avoid Twilio timeout

---

### `[BRIDGE] Normalize SMS Payload`
- Type: Code node
- Reads from: raw trigger output (`$json`)
- Produces: Full canonical message payload (see CONVENTIONS.md section 13.4)
- Key assignments:
  - `trace_id` = `input.MessageSid`
  - `entity_id` = `input.MessageSid`
  - `source_system` = `"twilio"`
  - `channel.type` = `"sms"`
  - `message.direction` = `"inbound"`
- Sets `raw_payload: input`

---

### `[VALIDATION] Check Required Fields`
- Type: IF node (or Code node for complex checks)
- Checks:
  - `message.external_message_id` is not null
  - `channel.from` matches E.164 phone format (`/^\+\d{7,15}$/`)
  - `message.body` is not empty string
- On fail: route to `[ERROR] Classify Error` with `error_type: "validation_failed"`
- On pass: continue

---

### `[IDEMPOTENCY] Check Duplicate Message`
- Type: Supabase node (HTTP Request or native)
- Query: `SELECT id FROM messages WHERE external_message_id = '{{trace_id}}' LIMIT 1`
- On record found: route to `[LOGGING] Write Execution Log` with `status: "skipped"`, then stop
- On no record: continue

---

### `[PROCESSING] Resolve Channel Connection`
- Type: Supabase node
- Query: `SELECT id FROM channel_connections WHERE channel = 'sms' AND external_identifier = '{{channel.to}}' AND is_active = true LIMIT 1`
- Assigns `conversation.channel_connection_id` in the payload
- On not found: route to `[ERROR] Classify Error` with `error_type: "channel_not_configured"`

---

### `[PROCESSING] Resolve or Create Conversation`
- Type: Supabase node (upsert pattern)
- Logic:
  1. SELECT conversation WHERE `channel_connection_id = X` AND `external_contact_id = {{channel.from}}` AND `status NOT IN ('resolved', 'archived', 'spam')` ORDER BY created_at DESC LIMIT 1
  2. If found: use existing `conversation.id`
  3. If not found: INSERT new conversation with `status = 'open'`, `is_read = false`
- Sets `conversation.id` and `conversation.is_new` in the payload

---

### `[PROCESSING] Resolve or Create Contact`
- Type: Supabase node
- Logic:
  1. SELECT contact WHERE `phone = {{contact.phone}}`
  2. If found: set `contact.known_contact_id`
  3. If not found: INSERT new contact with `phone` only — name/company enrichment happens in AI workflow

---

### `[OUTPUT] Insert Message to Supabase`
- Type: Supabase node (INSERT into `messages`)
- Fields to insert:
  ```
  conversation_id, channel_connection_id, direction='inbound', status='received',
  body, subject=null, external_message_id, source_system='twilio',
  raw_payload, workflow_trace_id=trace_id
  ```
- On error: route to `[ERROR] Classify Error` with retry (transient DB error)

---

### `[OUTPUT] Update Conversation`
- Type: Supabase node (UPDATE `conversations`)
- Updates: `last_message_at = NOW()`, `is_read = false`, `last_workflow_trace_id = trace_id`
- Also updates `contact_id` if contact was resolved and was previously null

---

### `[OUTPUT] Trigger AI Analysis Sub-Workflow`
- Type: HTTP Request (POST to n8n webhook)
- Target workflow: `[Luxee] Inbox — AI Message Analyzer`
- Payload: `{ conversation_id, message_id, trace_id }`
- Fire-and-forget: do not wait for response (use async sub-workflow call)
- This prevents blocking the inbound pipeline on AI latency

---

### `[LOGGING] Write Execution Log`
- Type: Supabase node (INSERT into `events_log`)
- Fields:
  ```
  event_type = 'message.received',
  actor_type = 'workflow',
  actor_id = '[Luxee] Inbox — Inbound SMS Handler',
  conversation_id, message_id,
  workflow_trace_id = trace_id,
  status = 'success' | 'skipped',
  payload = { source_system, channel, from, is_new_conversation }
  ```

---

### `[ERROR] Classify Error`
- Type: Code node (reads `$error` or explicit error routing)
- Classifies errors:
  - `validation_failed` → log + stop (no retry, no alert)
  - `duplicate_message` → log + stop (expected, no alert)
  - `channel_not_configured` → log + alert (Slack/email) — needs human action
  - `db_error` → retry up to 3x with exponential backoff, then fatal
  - `unknown` → fatal path
- Fatal path:
  - `[LOGGING] Write Error Log` → INSERT into events_log with `status: 'failure'`
  - `[NOTIFICATION] Alert on Fatal Failure` → Slack or email to ops
  - `[OUTPUT] Create Manual Review Task` → Insert into Supabase or Notion

---

## Header Sticky Note (to be placed in n8n)

```
Workflow    : [Luxee] Inbox — Inbound SMS Handler
Client      : luxee-internal
Domain      : inbox
Author      : Luxee
Version     : 1.0
Last update : 2026-04-03
Description : Receives inbound Twilio SMS, normalizes to Luxee canonical payload,
              persists message and conversation in Supabase, and triggers async AI analysis.
              Idempotent — duplicate MessageSids are safely discarded.
```

---

## Dependencies

| Dependency | Type | Notes |
|---|---|---|
| Supabase `messages` table | Required | Migration 001 must be applied |
| Supabase `conversations` table | Required | Migration 001 must be applied |
| Supabase `channel_connections` table | Required | Must have SMS record seeded |
| Twilio webhook configured | Required | Pointing to Next.js `/api/webhooks/twilio` |
| `[Luxee] Inbox — AI Message Analyzer` workflow | Optional at launch | AI features degraded if missing, not broken |
| `N8N_WEBHOOK_SMS` env var | Required | Set in Next.js `.env.local` |

---

## Test payload (Twilio SMS format)

```json
{
  "MessageSid": "SM1234567890abcdef",
  "SmsSid": "SM1234567890abcdef",
  "AccountSid": "AC0000000000000000",
  "From": "+33600000000",
  "To": "+33600000001",
  "Body": "Hello, I am interested in your services. Can we schedule a call?",
  "NumMedia": "0",
  "FromCountry": "FR",
  "FromCity": "Paris",
  "MessageStatus": "received"
}
```

---

## Production checklist

- [x] Layered architecture respected
- [x] All nodes follow `[LAYER] Verb Object`
- [x] Critical nodes (`[OUTPUT] Insert Message`, `[OUTPUT] Update Conversation`) have explicit error paths
- [x] Workflow-level Error Trigger configured
- [x] Logging layer present
- [x] Tags `client:luxee-internal` and `domain:inbox` defined
- [x] Header Sticky Note included
- [x] No `Function` node
- [x] No `Wait` node
- [ ] Tested on real Twilio payload (pending)
- [x] Idempotency handled
- [x] Manual fallback exists for fatal failures
