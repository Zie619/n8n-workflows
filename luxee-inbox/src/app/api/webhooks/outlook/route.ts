import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@supabase/supabase-js'

function getServiceClient() {
  return createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!
  )
}

/**
 * POST /api/webhooks/outlook
 *
 * Receives Microsoft Graph change notifications (Outlook inbound email).
 * Microsoft validates the endpoint first via a GET with validationToken.
 *
 * Docs: https://learn.microsoft.com/graph/webhooks
 */

// Microsoft Graph validates the subscription endpoint
export async function GET(request: NextRequest) {
  const validationToken = request.nextUrl.searchParams.get('validationToken')
  if (validationToken) {
    return new NextResponse(validationToken, {
      status: 200,
      headers: { 'Content-Type': 'text/plain' },
    })
  }
  return new NextResponse('Not found', { status: 404 })
}

export async function POST(request: NextRequest) {
  try {
    // Validate Microsoft client state secret
    const body = await request.json()
    const notifications = body.value ?? []

    const supabase = getServiceClient()

    for (const notification of notifications) {
      // Validate client state if set
      if (
        process.env.MICROSOFT_WEBHOOK_SECRET &&
        notification.clientState !== process.env.MICROSOFT_WEBHOOK_SECRET
      ) {
        console.warn('[outlook-webhook] Invalid client state, skipping notification')
        continue
      }

      await supabase.from('events_log').insert({
        event_type: 'message.received',
        actor_type: 'webhook',
        actor_id: 'outlook',
        payload: notification,
        workflow_trace_id: notification.resource ?? null,
        status: 'success',
      })

      // Forward to n8n
      const n8nWebhookUrl = process.env.N8N_WEBHOOK_OUTLOOK
      if (n8nWebhookUrl) {
        fetch(n8nWebhookUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-Webhook-Secret': process.env.N8N_WEBHOOK_SECRET ?? '',
          },
          body: JSON.stringify({ channel: 'outlook', notification }),
        }).catch((err) => {
          console.error('[outlook-webhook] n8n forward failed:', err)
        })
      }
    }

    // Microsoft requires a 202 Accepted response
    return new NextResponse('', { status: 202 })
  } catch (error) {
    console.error('[outlook-webhook] Error:', error)
    return new NextResponse('Internal error', { status: 500 })
  }
}
