import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@supabase/supabase-js'

// Supabase service role client — used by webhook handlers (no user session)
function getServiceClient() {
  return createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!
  )
}

/**
 * POST /api/webhooks/twilio
 *
 * Receives inbound SMS and WhatsApp messages from Twilio.
 * Forwards the raw payload to the n8n workflow for processing.
 *
 * Twilio validates webhooks via signature (X-Twilio-Signature header).
 * In production, validate with twilio.validateRequest() before processing.
 */
export async function POST(request: NextRequest) {
  try {
    const formData = await request.formData()
    const payload = Object.fromEntries(formData.entries())

    const isWhatsApp = (payload.From as string)?.startsWith('whatsapp:')
    const channel = isWhatsApp ? 'whatsapp' : 'sms'

    // Log raw webhook event
    const supabase = getServiceClient()
    await supabase.from('events_log').insert({
      event_type: 'message.received',
      actor_type: 'webhook',
      actor_id: 'twilio',
      payload: payload as Record<string, unknown>,
      workflow_trace_id: (payload.MessageSid as string) ?? null,
      status: 'success',
    })

    // Forward to n8n for processing
    const n8nWebhookUrl = process.env[
      isWhatsApp ? 'N8N_WEBHOOK_WHATSAPP' : 'N8N_WEBHOOK_SMS'
    ]

    if (n8nWebhookUrl) {
      // Fire-and-forget — do not await to keep Twilio response fast
      fetch(n8nWebhookUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Webhook-Secret': process.env.N8N_WEBHOOK_SECRET ?? '',
        },
        body: JSON.stringify({ channel, ...payload }),
      }).catch((err) => {
        console.error(`[twilio-webhook] n8n forward failed (${channel}):`, err)
      })
    }

    // Twilio expects a 200 with TwiML or empty body
    return new NextResponse('', { status: 200 })
  } catch (error) {
    console.error('[twilio-webhook] Error:', error)
    return new NextResponse('Internal error', { status: 500 })
  }
}
