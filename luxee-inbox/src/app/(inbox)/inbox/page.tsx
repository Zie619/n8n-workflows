import { createClient } from '@/lib/supabase/server'
import ConversationList from '@/components/inbox/ConversationList'
import ConversationPlaceholder from '@/components/inbox/ConversationPlaceholder'

export default async function InboxPage() {
  const supabase = await createClient()

  const { data: conversations } = await supabase
    .from('conversations')
    .select(`
      *,
      contact:contacts(*),
      channel_connection:channel_connections(*),
      last_message:messages(
        id, direction, body, subject, created_at, status
      )
    `)
    .in('status', ['open', 'in_progress', 'waiting'])
    .order('last_message_at', { ascending: false })
    .limit(50)

  return (
    <div className="flex h-full">
      {/* Conversation list panel */}
      <div className="w-[360px] flex-shrink-0 border-r border-[rgba(255,255,255,0.06)] flex flex-col">
        <ConversationList conversations={conversations ?? []} />
      </div>

      {/* Thread pane — empty state */}
      <div className="flex-1 flex items-center justify-center">
        <ConversationPlaceholder />
      </div>
    </div>
  )
}
