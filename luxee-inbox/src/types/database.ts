// ============================================================================
// LUXEE INBOX — Database Types
// Generated from schema: 001_initial_schema.sql
// Run `npm run db:types` to regenerate from live Supabase instance.
// ============================================================================

export type ChannelType = 'sms' | 'whatsapp' | 'linkedin' | 'outlook' | 'internal'
export type ConversationStatus = 'open' | 'in_progress' | 'waiting' | 'resolved' | 'archived' | 'spam'
export type MessageDirection = 'inbound' | 'outbound'
export type MessageStatus = 'received' | 'queued' | 'sent' | 'delivered' | 'failed' | 'read'
export type PriorityLevel = 'low' | 'normal' | 'high' | 'urgent'
export type QualificationStage = 'unqualified' | 'prospect' | 'qualified' | 'opportunity' | 'disqualified'
export type AiIntent =
  | 'inquiry' | 'support_request' | 'sales_interest' | 'booking_request'
  | 'complaint' | 'follow_up' | 'out_of_scope' | 'spam' | 'unknown'

export interface Profile {
  id: string
  created_at: string
  updated_at: string
  full_name: string
  display_name: string | null
  avatar_url: string | null
  role: 'admin' | 'agent' | 'viewer'
  notify_on_new_message: boolean
  notify_on_assignment: boolean
  notify_channel: 'email' | 'slack' | 'none'
}

export interface ChannelConnection {
  id: string
  created_at: string
  updated_at: string
  channel: ChannelType
  label: string
  external_identifier: string
  is_active: boolean
  config: Record<string, unknown>
}

export interface Contact {
  id: string
  created_at: string
  updated_at: string
  full_name: string | null
  email: string | null
  phone: string | null
  company: string | null
  linkedin_url: string | null
  enrichment: Record<string, unknown>
  tags: string[]
  external_ids: Record<string, string>
  notes: string | null
}

export interface Conversation {
  id: string
  created_at: string
  updated_at: string
  last_message_at: string | null
  channel_connection_id: string
  contact_id: string | null
  external_contact_id: string
  status: ConversationStatus
  priority: PriorityLevel
  qualification: QualificationStage
  assigned_to: string | null
  assigned_at: string | null
  ai_summary: string | null
  ai_priority: PriorityLevel | null
  ai_intent: AiIntent
  ai_score: number | null
  ai_next_action: string | null
  ai_labels: string[]
  ai_last_analyzed_at: string | null
  is_read: boolean
  requires_human_review: boolean
  snoozed_until: string | null
  last_workflow_trace_id: string | null
  subject: string | null
}

export interface Message {
  id: string
  created_at: string
  conversation_id: string
  channel_connection_id: string
  direction: MessageDirection
  status: MessageStatus
  body: string | null
  subject: string | null
  attachments: MessageAttachment[]
  external_message_id: string | null
  source_system: string
  raw_payload: Record<string, unknown> | null
  sent_at: string | null
  delivered_at: string | null
  read_at: string | null
  error_message: string | null
  sent_by: string | null
  workflow_trace_id: string | null
}

export interface MessageAttachment {
  filename: string
  mime_type: string
  url: string
  size_bytes: number
}

export interface MessageDraft {
  id: string
  created_at: string
  updated_at: string
  conversation_id: string
  author_id: string
  body: string
  is_ai_generated: boolean
  ai_suggestion_id: string | null
}

export interface AiSuggestion {
  id: string
  created_at: string
  conversation_id: string
  trigger_message_id: string | null
  suggested_body: string
  suggested_subject: string | null
  tone: string | null
  reasoning: string | null
  model_used: string
  workflow_trace_id: string | null
  was_used: boolean
  was_edited: boolean
  was_discarded: boolean
}

export interface ConversationQualification {
  id: string
  created_at: string
  updated_at: string
  conversation_id: string
  budget_signal: string | null
  authority_signal: string | null
  need_signal: string | null
  timeline_signal: string | null
  qualification_score: number | null
  ai_qualification_summary: string | null
  ai_recommended_action: string | null
  ai_disqualification_reason: string | null
  model_used: string
  workflow_trace_id: string | null
}

export interface Tag {
  id: string
  created_at: string
  name: string
  color: string
  description: string | null
}

export interface EventLog {
  id: string
  created_at: string
  event_type: string
  actor_type: 'user' | 'workflow' | 'system' | 'webhook' | null
  actor_id: string | null
  conversation_id: string | null
  message_id: string | null
  contact_id: string | null
  payload: Record<string, unknown>
  workflow_trace_id: string | null
  status: 'success' | 'failure' | 'skipped'
  error_message: string | null
}

// ── Joined / extended types used by the frontend ──────────────────────────────

export interface ConversationWithDetails extends Conversation {
  contact: Contact | null
  channel_connection: ChannelConnection
  last_message: Message | null
  unread_count?: number
  tags?: Tag[]
  assigned_profile?: Profile | null
}

export interface MessageWithSender extends Message {
  sender_profile?: Profile | null
}
