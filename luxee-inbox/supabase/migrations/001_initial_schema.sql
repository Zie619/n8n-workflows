-- ============================================================================
-- LUXEE INBOX — Initial Schema
-- Migration: 001_initial_schema.sql
-- Created: 2026-04-03
-- Description: Full schema for the Luxee multi-channel inbox application.
--              Supports SMS (Twilio), WhatsApp, LinkedIn, Outlook.
--              Designed for Supabase Postgres with RLS and Realtime.
-- ============================================================================

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ============================================================================
-- ENUM TYPES
-- ============================================================================

CREATE TYPE channel_type AS ENUM ('sms', 'whatsapp', 'linkedin', 'outlook', 'internal');
CREATE TYPE conversation_status AS ENUM ('open', 'in_progress', 'waiting', 'resolved', 'archived', 'spam');
CREATE TYPE message_direction AS ENUM ('inbound', 'outbound');
CREATE TYPE message_status AS ENUM ('received', 'queued', 'sent', 'delivered', 'failed', 'read');
CREATE TYPE priority_level AS ENUM ('low', 'normal', 'high', 'urgent');
CREATE TYPE qualification_stage AS ENUM ('unqualified', 'prospect', 'qualified', 'opportunity', 'disqualified');
CREATE TYPE ai_intent AS ENUM (
  'inquiry', 'support_request', 'sales_interest', 'booking_request',
  'complaint', 'follow_up', 'out_of_scope', 'spam', 'unknown'
);

-- ============================================================================
-- PROFILES
-- Extends Supabase auth.users. One profile per authenticated user.
-- ============================================================================

CREATE TABLE profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),

  full_name TEXT NOT NULL,
  display_name TEXT,
  avatar_url TEXT,
  role TEXT DEFAULT 'agent' CHECK (role IN ('admin', 'agent', 'viewer')),

  -- Notification preferences
  notify_on_new_message BOOLEAN DEFAULT true,
  notify_on_assignment BOOLEAN DEFAULT true,
  notify_channel TEXT DEFAULT 'email' CHECK (notify_channel IN ('email', 'slack', 'none'))
);

-- ============================================================================
-- CHANNEL_CONNECTIONS
-- One row per connected channel account (e.g., a Twilio phone number, an Outlook mailbox).
-- Multiple connections per channel type are supported.
-- ============================================================================

CREATE TABLE channel_connections (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),

  channel channel_type NOT NULL,
  label TEXT NOT NULL,                        -- Human-readable: "Twilio +33600000001", "contact@luxee.fr"
  external_identifier TEXT NOT NULL,          -- Phone number, email, LinkedIn profile ID, etc.
  is_active BOOLEAN DEFAULT true,

  -- Webhook / API config (stored as JSONB to avoid rigid per-channel columns)
  config JSONB DEFAULT '{}'::jsonb,
  /*
  SMS/WhatsApp (Twilio): {
    "account_sid": "...",
    "phone_number": "+33600000001",
    "webhook_url": "https://..."
  }
  Outlook: {
    "tenant_id": "...",
    "client_id": "...",
    "mailbox": "contact@luxee.fr",
    "subscription_id": "..." (Graph API webhook)
  }
  LinkedIn: {
    "profile_urn": "urn:li:person:...",
    "integration_method": "phantombuster|official"
  }
  */

  UNIQUE(channel, external_identifier)
);

-- ============================================================================
-- CONTACTS
-- Normalized contact records, one per external person across all channels.
-- De-duplication is manual or AI-assisted for now.
-- ============================================================================

CREATE TABLE contacts (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),

  full_name TEXT,
  email TEXT,
  phone TEXT,
  company TEXT,
  linkedin_url TEXT,

  -- AI-enriched fields
  enrichment JSONB DEFAULT '{}'::jsonb,
  tags TEXT[] DEFAULT '{}',

  -- Known identifiers across channels (for dedup)
  external_ids JSONB DEFAULT '{}'::jsonb,
  /*
  {
    "twilio_phone": "+33600000000",
    "outlook_email": "contact@example.com",
    "linkedin_urn": "urn:li:person:abc123"
  }
  */

  notes TEXT
);

-- ============================================================================
-- CONVERSATIONS
-- Central table. One conversation = one ongoing thread with one contact
-- on one channel.
-- ============================================================================

CREATE TABLE conversations (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  last_message_at TIMESTAMPTZ,

  -- Core references
  channel_connection_id UUID NOT NULL REFERENCES channel_connections(id),
  contact_id UUID REFERENCES contacts(id),

  -- Identity on the channel side (sender/recipient identifier)
  external_contact_id TEXT NOT NULL,          -- Phone number, email, LinkedIn URN of the other party

  -- Status and classification
  status conversation_status DEFAULT 'open',
  priority priority_level DEFAULT 'normal',
  qualification qualification_stage DEFAULT 'unqualified',

  -- Assignment
  assigned_to UUID REFERENCES profiles(id),
  assigned_at TIMESTAMPTZ,

  -- AI-derived fields (populated by n8n workflows)
  ai_summary TEXT,
  ai_priority priority_level,
  ai_intent ai_intent DEFAULT 'unknown',
  ai_score NUMERIC(4,2),                      -- 0.00 to 10.00 lead/engagement score
  ai_next_action TEXT,
  ai_labels TEXT[] DEFAULT '{}',
  ai_last_analyzed_at TIMESTAMPTZ,

  -- Operational flags
  is_read BOOLEAN DEFAULT false,
  requires_human_review BOOLEAN DEFAULT false,
  snoozed_until TIMESTAMPTZ,

  -- n8n trace
  last_workflow_trace_id TEXT,

  -- Subject (for email threads)
  subject TEXT
);

-- ============================================================================
-- MESSAGES
-- Individual messages within a conversation.
-- ============================================================================

CREATE TABLE messages (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),

  conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
  channel_connection_id UUID NOT NULL REFERENCES channel_connections(id),

  -- Direction and status
  direction message_direction NOT NULL,
  status message_status DEFAULT 'received',

  -- Content
  body TEXT,
  subject TEXT,                               -- Email subject (non-null for outlook)
  attachments JSONB DEFAULT '[]'::jsonb,
  /*
  [{
    "filename": "contract.pdf",
    "mime_type": "application/pdf",
    "url": "https://...",
    "size_bytes": 102400
  }]
  */

  -- Source system reference
  external_message_id TEXT,                   -- Twilio SID, Outlook message ID, etc.
  source_system TEXT NOT NULL,                -- 'twilio', 'whatsapp', 'outlook', 'linkedin', 'internal'
  raw_payload JSONB,                          -- Full original payload from source

  -- Outbound tracking
  sent_at TIMESTAMPTZ,
  delivered_at TIMESTAMPTZ,
  read_at TIMESTAMPTZ,
  error_message TEXT,

  -- Author (for outbound)
  sent_by UUID REFERENCES profiles(id),       -- Null for inbound

  -- n8n trace
  workflow_trace_id TEXT
);

-- ============================================================================
-- MESSAGE_DRAFTS
-- Auto-saved draft or AI-generated draft reply for a conversation.
-- One active draft per conversation per user.
-- ============================================================================

CREATE TABLE message_drafts (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),

  conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
  author_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,

  body TEXT NOT NULL,
  is_ai_generated BOOLEAN DEFAULT false,
  ai_suggestion_id UUID,                      -- FK set after ai_suggestions table created

  UNIQUE(conversation_id, author_id)
);

-- ============================================================================
-- AI_SUGGESTIONS
-- Claude-generated reply suggestions for a conversation.
-- Multiple suggestions can exist; the user picks one.
-- ============================================================================

CREATE TABLE ai_suggestions (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),

  conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
  trigger_message_id UUID REFERENCES messages(id),

  -- Content
  suggested_body TEXT NOT NULL,
  suggested_subject TEXT,                     -- For email
  tone TEXT,                                  -- 'professional', 'warm', 'concise', etc.
  reasoning TEXT,                             -- Why Claude suggested this

  -- Metadata
  model_used TEXT DEFAULT 'claude-sonnet-4-6',
  workflow_trace_id TEXT,
  was_used BOOLEAN DEFAULT false,
  was_edited BOOLEAN DEFAULT false,
  was_discarded BOOLEAN DEFAULT false,

  CONSTRAINT at_most_one_used CHECK (NOT (was_used AND was_discarded))
);

-- Add FK back to message_drafts
ALTER TABLE message_drafts
  ADD CONSTRAINT fk_ai_suggestion
  FOREIGN KEY (ai_suggestion_id) REFERENCES ai_suggestions(id);

-- ============================================================================
-- CONVERSATION_QUALIFICATIONS
-- Structured qualification data, populated by n8n AI workflow.
-- One record per conversation, upserted on each analysis pass.
-- ============================================================================

CREATE TABLE conversation_qualifications (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),

  conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE UNIQUE,

  -- BANT-style qualification fields
  budget_signal TEXT,                         -- 'confirmed', 'possible', 'none', 'unknown'
  authority_signal TEXT,                      -- 'decision_maker', 'influencer', 'unknown'
  need_signal TEXT,                           -- 'explicit', 'implicit', 'none', 'unknown'
  timeline_signal TEXT,                       -- 'immediate', 'near_term', 'exploratory', 'unknown'

  -- Qualification score (0–10)
  qualification_score NUMERIC(4,2),

  -- AI raw analysis
  ai_qualification_summary TEXT,
  ai_recommended_action TEXT,
  ai_disqualification_reason TEXT,

  -- Model used
  model_used TEXT DEFAULT 'claude-sonnet-4-6',
  workflow_trace_id TEXT
);

-- ============================================================================
-- TAGS
-- Global tag registry. Tags can be applied to conversations.
-- ============================================================================

CREATE TABLE tags (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),

  name TEXT UNIQUE NOT NULL,
  color TEXT DEFAULT '#7C3AED',              -- Hex color for UI
  description TEXT
);

CREATE TABLE conversation_tags (
  conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
  tag_id UUID NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
  tagged_at TIMESTAMPTZ DEFAULT NOW(),
  tagged_by UUID REFERENCES profiles(id),

  PRIMARY KEY (conversation_id, tag_id)
);

-- ============================================================================
-- ASSIGNMENTS
-- History of conversation assignments (for audit trail and analytics).
-- ============================================================================

CREATE TABLE assignments (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),

  conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
  assigned_to UUID REFERENCES profiles(id),  -- Null = unassigned
  assigned_by UUID REFERENCES profiles(id),
  reason TEXT
);

-- ============================================================================
-- EVENTS_LOG
-- Immutable audit log for all significant events in the system.
-- Written by n8n workflows and by the application backend.
-- Never updated, only appended.
-- ============================================================================

CREATE TABLE events_log (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),

  -- What happened
  event_type TEXT NOT NULL,
  /*
  Examples:
  'conversation.created', 'conversation.status_changed', 'conversation.assigned',
  'message.received', 'message.sent', 'message.failed',
  'ai.analysis_completed', 'ai.suggestion_generated',
  'workflow.executed', 'workflow.failed',
  'channel.connected', 'channel.disconnected'
  */

  -- Who/what
  actor_type TEXT CHECK (actor_type IN ('user', 'workflow', 'system', 'webhook')),
  actor_id TEXT,                              -- user UUID, workflow name, system

  -- Context
  conversation_id UUID REFERENCES conversations(id),
  message_id UUID REFERENCES messages(id),
  contact_id UUID REFERENCES contacts(id),

  -- Payload
  payload JSONB DEFAULT '{}'::jsonb,
  workflow_trace_id TEXT,

  -- Outcome
  status TEXT DEFAULT 'success' CHECK (status IN ('success', 'failure', 'skipped')),
  error_message TEXT
);

-- ============================================================================
-- INDEXES
-- ============================================================================

-- conversations
CREATE INDEX idx_conversations_status ON conversations(status);
CREATE INDEX idx_conversations_channel_conn ON conversations(channel_connection_id);
CREATE INDEX idx_conversations_contact ON conversations(contact_id);
CREATE INDEX idx_conversations_assigned ON conversations(assigned_to);
CREATE INDEX idx_conversations_priority ON conversations(priority);
CREATE INDEX idx_conversations_last_msg ON conversations(last_message_at DESC);
CREATE INDEX idx_conversations_open ON conversations(status) WHERE status = 'open';
CREATE INDEX idx_conversations_needs_review ON conversations(requires_human_review) WHERE requires_human_review = true;
CREATE INDEX idx_conversations_external ON conversations(external_contact_id);

-- messages
CREATE INDEX idx_messages_conversation ON messages(conversation_id);
CREATE INDEX idx_messages_created ON messages(created_at DESC);
CREATE INDEX idx_messages_direction ON messages(direction);
CREATE INDEX idx_messages_external_id ON messages(external_message_id) WHERE external_message_id IS NOT NULL;

-- ai_suggestions
CREATE INDEX idx_ai_suggestions_conversation ON ai_suggestions(conversation_id);

-- events_log
CREATE INDEX idx_events_log_type ON events_log(event_type);
CREATE INDEX idx_events_log_conversation ON events_log(conversation_id);
CREATE INDEX idx_events_log_created ON events_log(created_at DESC);
CREATE INDEX idx_events_log_trace ON events_log(workflow_trace_id) WHERE workflow_trace_id IS NOT NULL;

-- contacts
CREATE INDEX idx_contacts_email ON contacts(email) WHERE email IS NOT NULL;
CREATE INDEX idx_contacts_phone ON contacts(phone) WHERE phone IS NOT NULL;

-- ============================================================================
-- UPDATED_AT TRIGGER
-- ============================================================================

CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_profiles_updated_at BEFORE UPDATE ON profiles
  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE TRIGGER trg_channel_connections_updated_at BEFORE UPDATE ON channel_connections
  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE TRIGGER trg_contacts_updated_at BEFORE UPDATE ON contacts
  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE TRIGGER trg_conversations_updated_at BEFORE UPDATE ON conversations
  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE TRIGGER trg_message_drafts_updated_at BEFORE UPDATE ON message_drafts
  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE TRIGGER trg_conversation_qualifications_updated_at BEFORE UPDATE ON conversation_qualifications
  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

-- ============================================================================
-- CONVERSATION last_message_at AUTO-UPDATE
-- ============================================================================

CREATE OR REPLACE FUNCTION update_conversation_last_message_at()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE conversations
  SET
    last_message_at = NEW.created_at,
    updated_at = NOW(),
    is_read = CASE WHEN NEW.direction = 'inbound' THEN false ELSE is_read END
  WHERE id = NEW.conversation_id;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_message_update_conversation
  AFTER INSERT ON messages
  FOR EACH ROW EXECUTE FUNCTION update_conversation_last_message_at();

-- ============================================================================
-- ROW LEVEL SECURITY (RLS)
-- ============================================================================

ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE channel_connections ENABLE ROW LEVEL SECURITY;
ALTER TABLE contacts ENABLE ROW LEVEL SECURITY;
ALTER TABLE conversations ENABLE ROW LEVEL SECURITY;
ALTER TABLE messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE message_drafts ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai_suggestions ENABLE ROW LEVEL SECURITY;
ALTER TABLE conversation_qualifications ENABLE ROW LEVEL SECURITY;
ALTER TABLE tags ENABLE ROW LEVEL SECURITY;
ALTER TABLE conversation_tags ENABLE ROW LEVEL SECURITY;
ALTER TABLE assignments ENABLE ROW LEVEL SECURITY;
ALTER TABLE events_log ENABLE ROW LEVEL SECURITY;

-- Profiles: own profile only
CREATE POLICY "profiles_select_own" ON profiles FOR SELECT USING (auth.uid() = id);
CREATE POLICY "profiles_update_own" ON profiles FOR UPDATE USING (auth.uid() = id);

-- Authenticated users can read all channel connections (agents need to see them)
CREATE POLICY "channel_connections_select_auth" ON channel_connections
  FOR SELECT USING (auth.role() = 'authenticated');

-- Authenticated users can read/write all contacts
CREATE POLICY "contacts_select_auth" ON contacts FOR SELECT USING (auth.role() = 'authenticated');
CREATE POLICY "contacts_insert_auth" ON contacts FOR INSERT WITH CHECK (auth.role() = 'authenticated');
CREATE POLICY "contacts_update_auth" ON contacts FOR UPDATE USING (auth.role() = 'authenticated');

-- Conversations: all authenticated agents can see all conversations
CREATE POLICY "conversations_select_auth" ON conversations
  FOR SELECT USING (auth.role() = 'authenticated');
CREATE POLICY "conversations_insert_auth" ON conversations
  FOR INSERT WITH CHECK (auth.role() = 'authenticated');
CREATE POLICY "conversations_update_auth" ON conversations
  FOR UPDATE USING (auth.role() = 'authenticated');

-- Messages: all authenticated agents
CREATE POLICY "messages_select_auth" ON messages FOR SELECT USING (auth.role() = 'authenticated');
CREATE POLICY "messages_insert_auth" ON messages FOR INSERT WITH CHECK (auth.role() = 'authenticated');

-- Message drafts: only own drafts
CREATE POLICY "drafts_select_own" ON message_drafts FOR SELECT USING (auth.uid() = author_id);
CREATE POLICY "drafts_insert_own" ON message_drafts FOR INSERT WITH CHECK (auth.uid() = author_id);
CREATE POLICY "drafts_update_own" ON message_drafts FOR UPDATE USING (auth.uid() = author_id);
CREATE POLICY "drafts_delete_own" ON message_drafts FOR DELETE USING (auth.uid() = author_id);

-- AI suggestions: all authenticated agents (suggestions are shared)
CREATE POLICY "ai_suggestions_select_auth" ON ai_suggestions FOR SELECT USING (auth.role() = 'authenticated');

-- Qualifications: all authenticated agents
CREATE POLICY "qualifications_select_auth" ON conversation_qualifications FOR SELECT USING (auth.role() = 'authenticated');

-- Tags: all authenticated agents can read
CREATE POLICY "tags_select_auth" ON tags FOR SELECT USING (auth.role() = 'authenticated');
CREATE POLICY "conv_tags_select_auth" ON conversation_tags FOR SELECT USING (auth.role() = 'authenticated');
CREATE POLICY "conv_tags_insert_auth" ON conversation_tags FOR INSERT WITH CHECK (auth.role() = 'authenticated');
CREATE POLICY "conv_tags_delete_auth" ON conversation_tags FOR DELETE USING (auth.role() = 'authenticated');

-- Assignments: all authenticated agents
CREATE POLICY "assignments_select_auth" ON assignments FOR SELECT USING (auth.role() = 'authenticated');
CREATE POLICY "assignments_insert_auth" ON assignments FOR INSERT WITH CHECK (auth.role() = 'authenticated');

-- Events log: read-only for agents, inserts from service role (n8n workflows)
CREATE POLICY "events_log_select_auth" ON events_log FOR SELECT USING (auth.role() = 'authenticated');

-- ============================================================================
-- REALTIME
-- Enable Supabase Realtime on tables the frontend needs for live updates
-- ============================================================================

ALTER PUBLICATION supabase_realtime ADD TABLE conversations;
ALTER PUBLICATION supabase_realtime ADD TABLE messages;
ALTER PUBLICATION supabase_realtime ADD TABLE ai_suggestions;
ALTER PUBLICATION supabase_realtime ADD TABLE conversation_qualifications;

-- ============================================================================
-- SEED DATA — Tags
-- ============================================================================

INSERT INTO tags (name, color, description) VALUES
  ('hot-lead', '#EF4444', 'High-intent prospect, act fast'),
  ('needs-follow-up', '#F59E0B', 'Requires a follow-up within 48h'),
  ('demo-requested', '#8B5CF6', 'Contact requested a product demo'),
  ('not-responding', '#6B7280', 'Contact has not replied in 7+ days'),
  ('qualified', '#10B981', 'Fully qualified, move to opportunity'),
  ('disqualified', '#374151', 'Does not match ICP'),
  ('vip', '#F59E0B', 'High-value account or contact'),
  ('complaint', '#EF4444', 'Contact expressed a complaint'),
  ('partnership', '#3B82F6', 'Potential partnership inquiry');

-- ============================================================================
-- HELPFUL COMMENTS
-- ============================================================================

COMMENT ON TABLE conversations IS
  'Central table for the Luxee inbox. One row per ongoing thread with a contact on a channel.
   Status lifecycle: open → in_progress → waiting → resolved | archived.
   AI fields (ai_summary, ai_intent, etc.) are populated asynchronously by n8n workflows.';

COMMENT ON TABLE messages IS
  'Every inbound and outbound message. raw_payload preserves the original webhook data from
   the source system (Twilio, Outlook Graph API, etc.).
   The workflow_trace_id links to the n8n execution that created this record.';

COMMENT ON TABLE events_log IS
  'Immutable audit log. Written by n8n workflows (via service role) and by the Next.js API routes.
   Never update or delete rows. Used for debugging, compliance, and analytics.';

COMMENT ON TABLE channel_connections IS
  'Each row represents one connected account on one channel.
   config JSONB holds channel-specific settings. Never expose raw API credentials here —
   use Supabase Vault or environment variables for secrets.';
