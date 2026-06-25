'use client'

import { useState, useTransition } from 'react'
import type { ChannelType } from '@/types/database'
import { cn } from '@/lib/utils'

interface Props {
  conversationId: string
  channel: ChannelType
  draftBody: string
  onDraftChange: (value: string) => void
  onSent: () => void
}

export default function ReplyComposer({
  conversationId,
  channel,
  draftBody,
  onDraftChange,
  onSent,
}: Props) {
  const [isPending, startTransition] = useTransition()
  const [error, setError] = useState<string | null>(null)

  const characterLimit = channel === 'sms' ? 160 : null
  const overLimit = characterLimit ? draftBody.length > characterLimit : false

  const handleSend = () => {
    if (!draftBody.trim() || isPending || overLimit) return
    setError(null)

    startTransition(async () => {
      try {
        const res = await fetch(`/api/conversations/${conversationId}/send`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ body: draftBody }),
        })

        if (!res.ok) {
          const data = await res.json()
          setError(data.error ?? 'Failed to send message')
          return
        }

        onSent()
      } catch {
        setError('Network error — please try again')
      }
    })
  }

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <div className="space-y-2">
      {error && (
        <p className="text-xs text-red-400">{error}</p>
      )}

      <div className={cn(
        'rounded-lg border bg-[#111118] transition-colors',
        overLimit ? 'border-red-500/50' : 'border-[rgba(255,255,255,0.08)] focus-within:border-[rgba(124,58,237,0.5)]'
      )}>
        <textarea
          value={draftBody}
          onChange={(e) => onDraftChange(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={`Reply via ${channel}… (⌘↵ to send)`}
          rows={3}
          className="w-full bg-transparent px-3 pt-3 text-sm text-white placeholder:text-[rgba(255,255,255,0.25)] resize-none outline-none"
        />

        <div className="flex items-center justify-between px-3 pb-2">
          {characterLimit ? (
            <span className={cn(
              'text-xs',
              overLimit ? 'text-red-400' : 'text-[rgba(255,255,255,0.3)]'
            )}>
              {draftBody.length}/{characterLimit}
            </span>
          ) : (
            <span />
          )}

          <button
            onClick={handleSend}
            disabled={!draftBody.trim() || isPending || overLimit}
            className={cn(
              'px-3 py-1.5 rounded text-xs font-medium transition-colors',
              draftBody.trim() && !overLimit
                ? 'bg-[#7C3AED] text-white hover:bg-[#6D28D9]'
                : 'bg-[rgba(255,255,255,0.06)] text-[rgba(255,255,255,0.3)] cursor-not-allowed'
            )}
          >
            {isPending ? 'Sending…' : 'Send'}
          </button>
        </div>
      </div>
    </div>
  )
}
