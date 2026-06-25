'use client'

import { useEffect, useRef, useState } from 'react'
import { useRouter } from 'next/navigation'
import { createClient } from '@/lib/supabase/client'
import type { AiSuggestion, ConversationWithDetails, MessageWithSender } from '@/types/database'
import MessageBubble from '@/components/inbox/MessageBubble'
import ReplyComposer from '@/components/inbox/ReplyComposer'
import ConversationHeader from '@/components/inbox/ConversationHeader'
import AiSuggestionBar from '@/components/inbox/AiSuggestionBar'

interface Props {
  conversation: ConversationWithDetails
  messages: MessageWithSender[]
  aiSuggestions: AiSuggestion[]
}

export default function ConversationThread({ conversation, messages: initial, aiSuggestions }: Props) {
  const router = useRouter()
  const supabase = createClient()
  const bottomRef = useRef<HTMLDivElement>(null)

  // Scroll to bottom on load
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'instant' })
  }, [conversation.id])

  // Realtime: subscribe to new messages in this conversation
  useEffect(() => {
    const channel = supabase
      .channel(`messages-${conversation.id}`)
      .on(
        'postgres_changes',
        {
          event: 'INSERT',
          schema: 'public',
          table: 'messages',
          filter: `conversation_id=eq.${conversation.id}`,
        },
        () => {
          router.refresh()
          setTimeout(() => bottomRef.current?.scrollIntoView({ behavior: 'smooth' }), 100)
        }
      )
      .subscribe()

    return () => { supabase.removeChannel(channel) }
  }, [supabase, conversation.id, router])

  const [draftBody, setDraftBody] = useState('')

  const handleUseSuggestion = (suggestion: AiSuggestion) => {
    setDraftBody(suggestion.suggested_body)
  }

  return (
    <div className="flex flex-col h-full">
      {/* Header */}
      <ConversationHeader conversation={conversation} />

      {/* Messages */}
      <div className="flex-1 overflow-y-auto px-6 py-4 space-y-3">
        {initial.map((message) => (
          <MessageBubble key={message.id} message={message} />
        ))}
        <div ref={bottomRef} />
      </div>

      {/* AI suggestions */}
      {aiSuggestions.length > 0 && (
        <AiSuggestionBar
          suggestions={aiSuggestions}
          onUseSuggestion={handleUseSuggestion}
        />
      )}

      {/* Reply composer */}
      <div className="border-t border-[rgba(255,255,255,0.06)] p-4">
        <ReplyComposer
          conversationId={conversation.id}
          channel={conversation.channel_connection.channel}
          draftBody={draftBody}
          onDraftChange={setDraftBody}
          onSent={() => {
            setDraftBody('')
            router.refresh()
          }}
        />
      </div>
    </div>
  )
}
