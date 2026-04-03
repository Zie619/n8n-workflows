import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@/lib/supabase/server'
import { z } from 'zod'

const sendSchema = z.object({
  body: z.string().min(1).max(5000),
  subject: z.string().optional(),
})

/**
 * POST /api/conversations/[id]/send
 *
 * Send a message in a conversation. Routes to the appropriate channel.
 * The actual send is delegated to the n8n outbound dispatcher workflow.
 */
export async function POST(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id } = await params
  const supabase = await createClient()

  // Auth check
  const { data: { user } } = await supabase.auth.getUser()
  if (!user) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 })
  }

  // Validate body
  const rawBody = await request.json()
  const parsed = sendSchema.safeParse(rawBody)
  if (!parsed.success) {
    return NextResponse.json({ error: 'Invalid request', details: parsed.error.issues }, { status: 400 })
  }

  const { body, subject } = parsed.data

  // Load conversation + channel
  const { data: conversation, error: convError } = await supabase
    .from('conversations')
    .select('*, channel_connection:channel_connections(*)')
    .eq('id', id)
    .single()

  if (convError || !conversation) {
    return NextResponse.json({ error: 'Conversation not found' }, { status: 404 })
  }

  // Create outbound message record (queued)
  const { data: message, error: msgError } = await supabase
    .from('messages')
    .insert({
      conversation_id: id,
      channel_connection_id: conversation.channel_connection_id,
      direction: 'outbound',
      status: 'queued',
      body,
      subject: subject ?? null,
      source_system: conversation.channel_connection.channel,
      sent_by: user.id,
    })
    .select()
    .single()

  if (msgError || !message) {
    return NextResponse.json({ error: 'Failed to create message' }, { status: 500 })
  }

  // Dispatch to n8n outbound workflow
  const n8nWebhookUrl = process.env.N8N_WEBHOOK_OUTBOUND
  if (n8nWebhookUrl) {
    fetch(n8nWebhookUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Webhook-Secret': process.env.N8N_WEBHOOK_SECRET ?? '',
      },
      body: JSON.stringify({
        message_id: message.id,
        conversation_id: id,
        channel: conversation.channel_connection.channel,
        to: conversation.external_contact_id,
        body,
        subject,
        sent_by: user.id,
      }),
    }).catch((err) => {
      console.error('[send-api] n8n dispatch failed:', err)
    })
  }

  // Log event
  await supabase.from('events_log').insert({
    event_type: 'message.sent',
    actor_type: 'user',
    actor_id: user.id,
    conversation_id: id,
    message_id: message.id,
    payload: { channel: conversation.channel_connection.channel },
    status: 'success',
  })

  return NextResponse.json({ message })
}
