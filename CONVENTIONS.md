# CONVENTIONS.md — Luxee Workflow Library

> Ce fichier est la référence unique pour la création, l'adaptation et la révision de workflows n8n dans l'écosystème Luxee.  
> Tout workflow importé, généré ou modifié **doit** respecter ces conventions.

---

## 0. Design principles

Tout workflow Luxee doit respecter ces principes :

- Prefer clarity over compactness
- Prefer explicit routing over implicit logic
- Prefer deterministic processing over magic transformations
- Prefer native nodes over fragile custom code when possible
- Prefer modularity, but avoid unnecessary fragmentation
- Every production workflow must be debuggable by a third party
- Every workflow must remain readable after 3 months without prior context

---

## 1. Architecture type d'un workflow

Chaque workflow Luxee suit une structure en couches ordonnées. Les couches marquées `[required]` sont obligatoires sur tout workflow de production.

```text
[TRIGGER]       → Point d'entrée (webhook, schedule, event)            [required]
[BRIDGE]        → Normalisation du payload entrant                     [required if external payload]
[VALIDATION]    → Vérification des champs requis, formats, types       [required]
[IDEMPOTENCY]   → Détection et blocage des doublons / re-runs          [required if replay risk]
[ROUTER]        → Dispatch conditionnel selon le contexte              [if multi-path]
[PROCESSING]    → Logique métier principale                            [required]
[OUTPUT]        → Écriture / sync vers les outils cibles               [required]
[LOGGING]       → Trace structurée de l'exécution                      [required]
[NOTIFICATION]  → Alerte humaine si action requise                     [depending on criticality]
[ERROR]         → Capture, classification, retry, fallback             [required]
```

**Rule:** One node should have one clear responsibility and belong to one dominant layer.

Do not combine routing, business logic, output writing, and error handling in the same node.  
A single node may perform multiple micro-operations only if they clearly belong to the same layer.

---

## 2. Naming convention des nœuds

**Standard format:** `[LAYER] Verb Object`

Optional detail may be added in parentheses when needed.

### Examples by layer

| Layer | Valid examples |
|---|---|
| `[TRIGGER]` | `[TRIGGER] Receive Webhook`, `[TRIGGER] Schedule Daily Run` |
| `[BRIDGE]` | `[BRIDGE] Normalize Payload`, `[BRIDGE] Map Calendly Fields` |
| `[VALIDATION]` | `[VALIDATION] Check Required Fields`, `[VALIDATION] Assert Email Format` |
| `[IDEMPOTENCY]` | `[IDEMPOTENCY] Check Duplicate Run`, `[IDEMPOTENCY] Lock Execution ID` |
| `[ROUTER]` | `[ROUTER] Dispatch by Event Type`, `[ROUTER] Branch on Status` |
| `[PROCESSING]` | `[PROCESSING] Generate Email Draft (Claude)`, `[PROCESSING] Enrich Lead Data` |
| `[OUTPUT]` | `[OUTPUT] Update Notion Record`, `[OUTPUT] Send Gmail`, `[OUTPUT] Sync Airtable` |
| `[LOGGING]` | `[LOGGING] Write Execution Log`, `[LOGGING] Trace to Notion` |
| `[NOTIFICATION]` | `[NOTIFICATION] Alert on Failure`, `[NOTIFICATION] Notify Client Booking` |
| `[ERROR]` | `[ERROR] Classify Error`, `[ERROR] Handle Retry`, `[ERROR] Fallback to Manual` |

### Naming rules
- English only
- Title Case for node labels
- No ambiguous abbreviations
- No generic node names

**Forbidden:** ❌ `HTTP Request` ❌ `Set` ❌ `Code` ❌ `Merge` ❌ `Notion`

**Correct:** ✅ `[OUTPUT] Push to Notion` ✅ `[BRIDGE] Normalize Fields` ✅ `[PROCESSING] Transform Lead Payload` ✅ `[ROUTER] Branch on Booking Status`

---

## 3. Payload conventions

> Luxee workflows are not only workflow standards. They are data circulation standards.  
> Every workflow must normalize its input early and maintain a stable, traceable payload throughout execution.

---

### 3.1 Three payload layers

Luxee distinguishes three distinct payload layers:

| Layer | Name | Description |
|---|---|---|
| 1 | `raw_payload` | The original, unmodified input from the source system. Always preserved. Never modified. |
| 2 | **Canonical payload** | The normalized, stable Luxee representation. Produced by `[BRIDGE]`. Used by all downstream nodes. |
| 3 | **Processing fields** | Temporary fields added during `[PROCESSING]` for intermediate computation. Must not pollute the canonical structure. |

**Rule:** After `[BRIDGE]` normalization, all downstream nodes must read from the canonical payload. Raw payload access is only allowed in `[BRIDGE]` and `[ERROR]` nodes.

---

### 3.2 Canonical payload — reference template

```json
{
  "trace_id": "uuid-or-stable-execution-id",
  "workflow_name": "string",
  "execution_timestamp": "2026-04-03T14:00:00Z",
  "source_system": "calendly",
  "source_event": "invitee.created",
  "entity_type": "booking",
  "entity_id": "evt_123456",
  "client_id": "luxee-internal",
  "domain": "onboarding",
  "status": "normalized",
  "customer": {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "phone": "+33600000000",
    "company": "Acme"
  },
  "booking": {
    "status": "confirmed",
    "start_at": "2026-04-05T09:00:00Z",
    "end_at": "2026-04-05T09:30:00Z",
    "timezone": "Europe/Paris",
    "event_type": "discovery-call"
  },
  "lead": {
    "source": "calendly",
    "owner": null,
    "score": null,
    "tags": []
  },
  "content": {
    "subject": null,
    "message": null,
    "summary": null
  },
  "routing": {
    "path": "default",
    "priority": "normal",
    "requires_human_review": false
  },
  "meta": {
    "raw_payload_available": true,
    "schema_version": "1.0",
    "notes": null
  },
  "raw_payload": {}
}
```

---

### 3.3 Required top-level fields

| Field | Type | Description |
|---|---|---|
| `trace_id` | string | Unique identifier for the execution. Use `crypto.randomUUID()` if not provided by source. |
| `workflow_name` | string | Exact name of the workflow as defined in n8n. |
| `execution_timestamp` | ISO 8601 | Timestamp of normalization, not of the source event. |
| `source_system` | string | Origin system identifier (`calendly`, `gmail`, `notion`, `webhook`, etc.) |
| `source_event` | string \| null | Event type from source system if applicable. |
| `entity_type` | string | Type of the primary entity (`booking`, `lead`, `contact`, `task`, etc.) |
| `entity_id` | string \| null | Stable identifier for the primary entity in the source system. |
| `client_id` | string | Luxee client identifier. Must match the `client:` tag of the workflow. |
| `domain` | string | Business domain. Must match the `domain:` tag of the workflow. |
| `status` | string | Lifecycle status of the canonical payload (`normalized`, `processed`, `failed`, etc.) |
| `raw_payload` | object | Full, unmodified original input. Always present. |

---

### 3.4 Canonical field groups

| Group | Purpose |
|---|---|
| `customer` | Normalized contact/person data. Always use these fields instead of source-specific names. |
| `booking` | Scheduling data. Used in Calendly, meeting, and appointment workflows. |
| `lead` | Lead qualification and enrichment fields. Used in prospection workflows. |
| `content` | Generated or processed content (email subject, message body, AI summary). |
| `routing` | Routing decisions and priority flags. Set by `[BRIDGE]` or `[ROUTER]`. |
| `meta` | Schema metadata, versioning, and internal notes. |

Unused groups must still be present with `null` or empty default values to ensure schema stability across workflows.

---

### 3.5 Bridge rules for `[BRIDGE]` nodes

- The `[BRIDGE]` node is the **only** node allowed to read directly from the raw trigger output
- It must produce a complete canonical payload as its output item
- It must store the original input in `raw_payload`
- It must never drop or silently ignore source fields — unknown fields go into `meta.notes` or `raw_payload`
- It must assign a `trace_id` if none is provided
- It must set `status: "normalized"` upon successful normalization
- If normalization fails, it must route to `[ERROR] Classify Error` — never output a partial canonical payload

---

### 3.6 Mapping example — Calendly → Luxee canonical

| Source field (Calendly) | Canonical field |
|---|---|
| `payload.invitee.name` | `customer.name` |
| `payload.invitee.email` | `customer.email` |
| `payload.invitee.phone` | `customer.phone` |
| `payload.invitee.organization` | `customer.company` |
| `payload.event.uuid` | `entity_id` |
| `payload.event.start_time` | `booking.start_at` |
| `payload.event.end_time` | `booking.end_at` |
| `payload.invitee.timezone` | `booking.timezone` |
| `payload.event_type.name` | `booking.event_type` |
| `event` | `source_event` |
| *(full input)* | `raw_payload` |

---

### 3.7 Downstream node rule

> After `[BRIDGE]` normalization, no downstream node may access the original trigger output directly.  
> All nodes from `[VALIDATION]` onward must read exclusively from the canonical payload.  
> This rule is not optional.

---

### 3.8 Code node expectation (for Claude Code)

When generating a `[BRIDGE]` node as a Code node:

- Always output a single item: `return [{ ... }]`
- Always use nullish coalescing (`??`) for optional source fields — never assume presence
- Always assign `trace_id` with fallback: `input.trace_id ?? crypto.randomUUID()`
- Always set `raw_payload: input` as the last field
- Never use `try/catch` inside the bridge to silently swallow errors — let failures surface to the error path
- Always hardcode `workflow_name`, `client_id`, and `domain` as string literals matching the workflow definition

---

### 3.9 Reference implementation — `[BRIDGE] Normalize Payload` (Calendly)

```js
const input = $json;

return [{
  trace_id: input.trace_id ?? crypto.randomUUID(),
  workflow_name: "Calendly Booking Handler",
  execution_timestamp: new Date().toISOString(),
  source_system: "calendly",
  source_event: input.event ?? null,
  entity_type: "booking",
  entity_id: input.payload?.event?.uuid ?? null,
  client_id: "luxee-internal",
  domain: "onboarding",
  status: "normalized",
  customer: {
    name: input.payload?.invitee?.name ?? null,
    email: input.payload?.invitee?.email ?? null,
    phone: input.payload?.invitee?.phone ?? null,
    company: input.payload?.invitee?.organization ?? null
  },
  booking: {
    status: "confirmed",
    start_at: input.payload?.event?.start_time ?? null,
    end_at: input.payload?.event?.end_time ?? null,
    timezone: input.payload?.invitee?.timezone ?? null,
    event_type: input.payload?.event_type?.name ?? null
  },
  lead: {
    source: "calendly",
    owner: null,
    score: null,
    tags: []
  },
  content: {
    subject: null,
    message: null,
    summary: null
  },
  routing: {
    path: "default",
    priority: "normal",
    requires_human_review: false
  },
  meta: {
    raw_payload_available: true,
    schema_version: "1.0",
    notes: null
  },
  raw_payload: input
}];
```

---

## 4. Gestion des erreurs (layered error handling)

Luxee applies a layered error-handling model. Each level has a distinct responsibility.

### Error-handling levels

1. **Early validation** — Block invalid payloads in `[VALIDATION]`. Never let malformed data continue silently.
2. **Controlled failure paths** — Every critical node should have an explicit error path when relevant.
3. **Workflow-level capture** — Use n8n Error Trigger workflows to capture unhandled failures.
4. **Trace logging** — Every significant error must be logged with: timestamp, workflow name, node name, error message, execution context, payload snapshot when non-sensitive.
5. **Actionable alerting** — Critical failures should trigger a notification only when human action may be required.
6. **Retry policy** — Transient failures only: max 3 retries, exponential backoff, no infinite retries.
7. **Manual fallback** — Unrecoverable failures must create a manual review task with full context.

### Critical node definition

A node is considered critical if it:
- writes data to an external system
- triggers a customer-facing action
- performs irreversible changes
- controls routing, validation, or idempotency
- depends on a paid, rate-limited, or unstable external API

### Standard error template

```
[ERROR] Classify Error
  → If retriable → [ERROR] Retry with Backoff
  → If fatal     → [LOGGING] Write Error Log + [NOTIFICATION] Alert + [OUTPUT] Create Manual Review Task
```

### Error design rules

- Do not use silent failures
- Do not retry fatal business logic errors
- Do not alert on non-actionable noise
- Do not lose the trace context on retry or fallback

---

## 5. Stack principal

These are the reference integrations. Generated workflows should prioritize native nodes when possible.

| Tool | Primary usage | Preferred n8n node |
|---|---|---|
| **Notion** | Client operations, manual review tasks, lightweight logs | Notion node |
| **Gmail / SMTP** | Notifications, outreach, confirmations | Gmail node / SMTP |
| **OpenAI / Claude** | Content generation, enrichment, classification | OpenAI node / HTTP Request to API |
| **Webhooks custom** | Incoming triggers, third-party integrations | Webhook node |
| **Calendly** | Booking, cancellation, rescheduling events | Webhook / HTTP Request |

### Architecture maturity rule

For lightweight operational systems, Notion may be used as operational database, manual fallback workspace, and lightweight logging layer.

For larger or more critical systems, a dedicated backend/database should be preferred, with Notion used only as an operational interface when relevant.

> Notion for operating. Dedicated backend for building serious systems.

---

## 6. Organisation des workflows dans n8n

### Mandatory tags

Each workflow must have at least 2 tags:

```
client:[client-name]     → ex: client:luxee-internal, client:dupont-sarl
domain:[business-domain] → ex: domain:prospection, domain:onboarding, domain:reporting, domain:monitoring, domain:finance
```

### Workflow naming

Format: `[Client] Domain — Short Description`

Examples:
- `[Luxee] Prospection — LinkedIn Outreach Automation`
- `[Client A] Onboarding — Calendly Booking Handler`
- `[Luxee Internal] Monitoring — Daily Execution Report`

**Organizational rule:** Primary logic grouping = business function. Operational separation = client. Never organize the workflow library primarily by tool alone.

---

## 7. Nœuds interdits / à éviter

### Forbidden or discouraged nodes

| Node | Reason | Preferred alternative |
|---|---|---|
| `Function` (legacy) | Deprecated, old syntax, hard to maintain | `Code` node |
| `Wait` | Timeout risk, execution blocking, weak production reliability | External trigger, callback webhook, resumed workflow pattern |

### Allowed with constraints

| Node | Usage condition |
|---|---|
| `Execute Workflow` | Allowed only if the sub-workflow is documented, named correctly, and the call path is traceable in `[LOGGING]` |
| `Merge` (complex mode) | Allowed only if the behavior is explicitly documented in a nearby Sticky Note |

### Anti-patterns to avoid

- Hidden dependencies
- Implicit timing logic
- Unclear merge behavior
- Deep sub-workflow chains without traceability
- Magic transformations inside generic code blocks

---

## 8. Code node rules

Use Code nodes only when:
- native nodes cannot express the logic clearly
- transformation logic would otherwise become harder to maintain
- the logic remains bounded to one dominant layer

Avoid Code nodes for:
- simple field mapping
- basic IF/ELSE routing
- trivial formatting
- tasks already handled well by native nodes

**Rule:** A Code node must never become a hidden black box for routing, business logic, output writing, and error handling all at once. If a Code node is non-obvious, document it with a Sticky Note.

---

## 9. Documentation inline (Sticky Notes)

Any workflow with more than 5 nodes must contain at least:

### 1. Header Sticky Note

Placed at the top-left of the workflow:

```
Workflow    : [name]
Client      : [client]
Domain      : [domain]
Author      : Luxee
Version     : [version]
Last update : [date]
Description : [1–2 sentences about the workflow purpose]
```

### 2. Section Sticky Notes

Required if the workflow has more than 10 nodes. Each major logical section should be labeled:

- Trigger / Input
- Validation
- Routing
- Processing
- Outputs
- Logging / Error handling

Sticky Notes are mandatory near: complex routing, merge logic, retry / fallback logic, non-obvious Code nodes, any exception to the default conventions.

---

## 10. Credentials — Nommage standard

Format: `[Tool] — [Scope/Usage]`

Examples:
- `Notion — Luxee Workspace`
- `Gmail — contact@luxee.fr`
- `OpenAI — Production Key`
- `Anthropic — Claude API`
- `Webhook — Calendly Events`

**Rules:**
- Keep names explicit
- Avoid personal nicknames
- Avoid unnamed duplicates
- Separate sandbox and production credentials clearly (e.g. `OpenAI — Sandbox` / `OpenAI — Production`)

---

## 11. Versioning rules

Increment the version when:
- routing logic changes
- payload structure changes
- output targets change
- retry / fallback behavior changes
- critical business logic changes

Minor edits do not require a version bump: label cleanup, Sticky Note wording, layout adjustments, non-functional formatting changes.

**Format:** `Major.Minor` — Examples: `1.0`, `1.1`, `2.0`

---

## 12. Checklist avant mise en production

Before activating a workflow:

- [ ] Layered architecture is respected
- [ ] All nodes follow `[LAYER] Verb Object`
- [ ] Critical nodes have explicit error handling where relevant
- [ ] Workflow-level Error Trigger is configured
- [ ] Logging layer is present
- [ ] Tags `client:` and `domain:` are defined
- [ ] Header Sticky Note is present
- [ ] No legacy `Function` node
- [ ] No fragile `Wait` node unless formally justified
- [ ] Tested on at least one real or simulated payload
- [ ] Traceability fields are preserved
- [ ] Output actions are clearly identifiable
- [ ] Retry policy is bounded and documented
- [ ] Manual fallback exists for unrecoverable critical failures

---

## 13. Multi-channel message payload (Luxee Inbox)

> This section extends section 3 for the Luxee Inbox domain (`domain:inbox`).
> All inbound messages from SMS, WhatsApp, LinkedIn, and Outlook must be normalized
> to this canonical structure before entering any downstream processing.

---

### 13.1 Message entity type

When `entity_type` is `"message"`, the canonical payload must include the following groups
in addition to the standard top-level fields defined in section 3.3:

| Group | Purpose |
|---|---|
| `message` | Core message content, direction, and status |
| `conversation` | Conversation thread context |
| `contact` | Sender/recipient identity |
| `channel` | Channel-specific metadata |
| `ai` | AI processing results (populated by downstream workflows) |
| `routing` | Routing decisions |
| `meta` | Schema metadata |

---

### 13.2 Canonical message payload — reference template

```json
{
  "trace_id": "uuid",
  "workflow_name": "string",
  "execution_timestamp": "2026-04-03T14:00:00Z",
  "source_system": "twilio | whatsapp | outlook | linkedin | internal",
  "source_event": "message.received | message.delivered | message.failed",
  "entity_type": "message",
  "entity_id": "source-system-message-id",
  "client_id": "luxee-internal",
  "domain": "inbox",
  "status": "normalized",

  "message": {
    "direction": "inbound | outbound",
    "body": "Message text content",
    "subject": null,
    "attachments": [],
    "external_message_id": "twilio-sid or outlook-message-id",
    "received_at": "2026-04-03T14:00:00Z",
    "status": "received | sent | delivered | failed | read"
  },

  "conversation": {
    "id": null,
    "external_contact_id": "+33600000000 or email or linkedin-urn",
    "channel": "sms | whatsapp | outlook | linkedin",
    "channel_connection_id": "uuid-of-channel-connection",
    "is_new": true,
    "thread_id": null
  },

  "contact": {
    "name": null,
    "email": null,
    "phone": null,
    "company": null,
    "external_identifier": "+33600000000 or email or linkedin-urn",
    "known_contact_id": null
  },

  "channel": {
    "type": "sms | whatsapp | outlook | linkedin",
    "from": "+33600000000 or email or linkedin-urn",
    "to": "+33600000001 or inbox-email",
    "metadata": {}
  },

  "ai": {
    "intent": null,
    "summary": null,
    "priority": null,
    "score": null,
    "next_action": null,
    "labels": [],
    "suggestion": null,
    "qualification": {
      "budget": null,
      "authority": null,
      "need": null,
      "timeline": null
    },
    "processed_at": null
  },

  "routing": {
    "path": "default",
    "priority": "normal",
    "requires_human_review": false,
    "assigned_to": null
  },

  "meta": {
    "raw_payload_available": true,
    "schema_version": "1.0",
    "notes": null
  },

  "raw_payload": {}
}
```

---

### 13.3 Channel-specific source field mappings

#### Twilio SMS → Canonical

| Source field (Twilio) | Canonical field |
|---|---|
| `Body` | `message.body` |
| `MessageSid` | `message.external_message_id`, `entity_id` |
| `From` | `channel.from`, `contact.external_identifier`, `conversation.external_contact_id` |
| `To` | `channel.to`, `conversation.channel_connection_id` (resolved by lookup) |
| `MessageStatus` | `message.status` |
| *(full webhook body)* | `raw_payload` |

`channel.type` = `"sms"`, `source_system` = `"twilio"`, `source_event` = `"message.received"`

#### WhatsApp (via Twilio) → Canonical

Same as SMS mapping, with:
- `channel.type` = `"whatsapp"`, `source_system` = `"whatsapp"`
- `channel.metadata.profile_name` from `ProfileName` field

#### Outlook (Microsoft Graph) → Canonical

| Source field (Graph API) | Canonical field |
|---|---|
| `bodyPreview` | `message.body` (full body in `message.body` via Graph call) |
| `id` | `message.external_message_id`, `entity_id` |
| `from.emailAddress.address` | `channel.from`, `contact.email`, `conversation.external_contact_id` |
| `from.emailAddress.name` | `contact.name` |
| `subject` | `message.subject` |
| `receivedDateTime` | `message.received_at` |
| `conversationId` | `conversation.thread_id` |
| `hasAttachments` + `attachments[]` | `message.attachments` |
| *(full Graph notification payload)* | `raw_payload` |

`channel.type` = `"outlook"`, `source_system` = `"outlook"`, `source_event` = `"message.received"`

#### LinkedIn DM → Canonical

| Source field (LinkedIn/integration) | Canonical field |
|---|---|
| `message_text` | `message.body` |
| `message_id` | `message.external_message_id`, `entity_id` |
| `sender_urn` | `channel.from`, `contact.external_identifier`, `conversation.external_contact_id` |
| `sender_name` | `contact.name` |
| `conversation_urn` | `conversation.thread_id` |
| *(full payload)* | `raw_payload` |

`channel.type` = `"linkedin"`, `source_system` = `"linkedin"`

> ⚠️ Risk flag: LinkedIn has no official DM API for automation. Integration depends on
> unofficial tooling (Phantombuster, Clay, etc.) or LinkedIn Partner Program access.
> Treat this channel as fragile. Always log `meta.notes` with integration method used.

---

### 13.4 `[BRIDGE]` Code node — Twilio SMS reference

```js
const input = $json;

return [{
  trace_id: input.MessageSid ?? crypto.randomUUID(),
  workflow_name: "[Luxee] Inbox — Inbound SMS Handler",
  execution_timestamp: new Date().toISOString(),
  source_system: "twilio",
  source_event: "message.received",
  entity_type: "message",
  entity_id: input.MessageSid ?? null,
  client_id: "luxee-internal",
  domain: "inbox",
  status: "normalized",

  message: {
    direction: "inbound",
    body: input.Body ?? null,
    subject: null,
    attachments: [],
    external_message_id: input.MessageSid ?? null,
    received_at: new Date().toISOString(),
    status: "received"
  },

  conversation: {
    id: null,
    external_contact_id: input.From ?? null,
    channel: "sms",
    channel_connection_id: null, // resolved by [PROCESSING] lookup
    is_new: null,                // determined by [IDEMPOTENCY] check
    thread_id: null
  },

  contact: {
    name: null,
    email: null,
    phone: input.From ?? null,
    company: null,
    external_identifier: input.From ?? null,
    known_contact_id: null      // resolved by [PROCESSING] lookup
  },

  channel: {
    type: "sms",
    from: input.From ?? null,
    to: input.To ?? null,
    metadata: {
      num_media: input.NumMedia ?? "0",
      from_country: input.FromCountry ?? null,
      from_city: input.FromCity ?? null
    }
  },

  ai: {
    intent: null,
    summary: null,
    priority: null,
    score: null,
    next_action: null,
    labels: [],
    suggestion: null,
    qualification: { budget: null, authority: null, need: null, timeline: null },
    processed_at: null
  },

  routing: {
    path: "default",
    priority: "normal",
    requires_human_review: false,
    assigned_to: null
  },

  meta: {
    raw_payload_available: true,
    schema_version: "1.0",
    notes: null
  },

  raw_payload: input
}];
```

---

### 13.5 AI group update — by downstream AI workflow

After the AI analysis workflow processes the message, it updates `conversations.ai_*` fields
in Supabase directly. The canonical payload `ai` group is also updated in the workflow chain:

```json
"ai": {
  "intent": "sales_interest",
  "summary": "Contact is asking about pricing for the enterprise plan.",
  "priority": "high",
  "score": 7.5,
  "next_action": "Send pricing deck and schedule a call",
  "labels": ["enterprise", "pricing-inquiry"],
  "suggestion": "Hi {{name}}, thanks for reaching out! I'd be happy to share...",
  "qualification": {
    "budget": "possible",
    "authority": "unknown",
    "need": "explicit",
    "timeline": "near_term"
  },
  "processed_at": "2026-04-03T14:01:32Z"
}
```

---

## 14. Final rule

If a generated or imported workflow does not clearly comply with these conventions, it must be renamed, restructured, documented, and secured before being considered production-ready.

**No exception for speed.**
