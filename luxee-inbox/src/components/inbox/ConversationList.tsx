'use client'

import { useEffect, useRef } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { formatDistanceToNowStrict } from 'date-fns'
import { createClient } from '@/lib/supabase/client'
import type { ConversationWithDetails } from '@/types/database'
import ChannelBadge from '@/components/ui/ChannelBadge'
import PriorityDot from '@/components/ui/PriorityDot'
import { cn } from '@/lib/utils'

interface Props {
  conversations: ConversationWithDetails[]
  activeId?: string
}

export default function ConversationList({ conversations: initial, activeId }: Props) {
  const router = useRouter()
  const supabase = createClient()
  const listRef = useRef(initial)

  // Subscribe to realtime updates — new messages update the list order
  useEffect(() => {
    const channel = supabase
      .channel('conversations-list')
      .on(
        'postgres_changes',
        { event: '*', schema: 'public', table: 'conversations' },
        () => {
          router.refresh()
        }
      )
      .subscribe()

    return () => { supabase.removeChannel(channel) }
  }, [supabase, router])

  return (
    <div className="flex flex-col h-full">
      {/* Header */}
      <div className="px-4 py-3 border-b border-[rgba(255,255,255,0.06)]">
        <h2 className="text-sm font-semibold text-white">Inbox</h2>
        <p className="text-xs text-[rgba(255,255,255,0.35)] mt-0.5">
          {initial.length} open
        </p>
      </div>

      {/* Conversation rows */}
      <div className="flex-1 overflow-y-auto">
        {initial.length === 0 ? (
          <div className="flex items-center justify-center h-full text-sm text-[rgba(255,255,255,0.3)]">
            No open conversations
          </div>
        ) : (
          initial.map((conv) => (
            <ConversationRow key={conv.id} conversation={conv} isActive={conv.id === activeId} />
          ))
        )}
      </div>
    </div>
  )
}

function ConversationRow({
  conversation: conv,
  isActive,
}: {
  conversation: ConversationWithDetails
  isActive: boolean
}) {
  const lastMsg = conv.last_message
  const lastMsgText = lastMsg?.body ?? lastMsg?.subject ?? '—'
  const timeAgo = conv.last_message_at
    ? formatDistanceToNowStrict(new Date(conv.last_message_at), { addSuffix: false })
    : null

  return (
    <Link
      href={`/inbox/${conv.id}`}
      className={cn(
        'block px-4 py-3 border-b border-[rgba(255,255,255,0.04)]',
        'hover:bg-[rgba(255,255,255,0.03)] transition-colors',
        isActive && 'bg-[rgba(124,58,237,0.12)] border-l-2 border-l-[#7C3AED]',
        !conv.is_read && !isActive && 'bg-[rgba(255,255,255,0.025)]'
      )}
    >
      <div className="flex items-start gap-3">
        {/* Priority + unread indicator */}
        <div className="flex flex-col items-center gap-1.5 pt-1">
          <PriorityDot priority={conv.ai_priority ?? conv.priority} />
          {!conv.is_read && (
            <div className="w-1.5 h-1.5 rounded-full bg-[#8B5CF6]" />
          )}
        </div>

        {/* Content */}
        <div className="flex-1 min-w-0">
          <div className="flex items-center justify-between gap-2 mb-0.5">
            <span className={cn(
              'text-sm truncate',
              conv.is_read ? 'text-[rgba(255,255,255,0.7)]' : 'text-white font-medium'
            )}>
              {conv.contact?.full_name ?? conv.external_contact_id}
            </span>
            <div className="flex items-center gap-1.5 flex-shrink-0">
              <ChannelBadge channel={conv.channel_connection.channel} compact />
              {timeAgo && (
                <span className="text-[10px] text-[rgba(255,255,255,0.3)]">{timeAgo}</span>
              )}
            </div>
          </div>

          <p className="text-xs text-[rgba(255,255,255,0.4)] truncate">
            {lastMsgText}
          </p>

          {/* AI intent badge */}
          {conv.ai_intent && conv.ai_intent !== 'unknown' && (
            <span className="inline-block mt-1 text-[10px] px-1.5 py-0.5 rounded bg-[rgba(124,58,237,0.15)] text-[#A78BFA]">
              {conv.ai_intent.replace('_', ' ')}
            </span>
          )}
        </div>
      </div>
    </Link>
  )
}
