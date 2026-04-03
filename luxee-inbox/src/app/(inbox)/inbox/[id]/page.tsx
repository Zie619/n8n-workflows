import { notFound } from 'next/navigation'
import { createClient } from '@/lib/supabase/server'
import ConversationList from '@/components/inbox/ConversationList'
import ConversationThread from '@/components/inbox/ConversationThread'
import ConversationSidebar from '@/components/inbox/ConversationSidebar'

interface Props {
  params: Promise<{ id: string }>
}

export default async function ConversationPage({ params }: Props) {
  const { id } = await params
  const supabase = await createClient()

  // Load conversation list (for left panel)
  const { data: conversations } = await supabase
    .from('conversations')
    .select(`
      *,
      contact:contacts(*),
      channel_connection:channel_connections(*),
      last_message:messages(id, direction, body, subject, created_at, status)
    `)
    .in('status', ['open', 'in_progress', 'waiting'])
    .order('last_message_at', { ascending: false })
    .limit(50)

  // Load active conversation
  const { data: conversation } = await supabase
    .from('conversations')
    .select(`
      *,
      contact:contacts(*),
      channel_connection:channel_connections(*),
      assigned_profile:profiles(id, full_name, display_name, avatar_url)
    `)
    .eq('id', id)
    .single()

  if (!conversation) notFound()

  // Load messages for this conversation
  const { data: messages } = await supabase
    .from('messages')
    .select('*, sender_profile:profiles(id, full_name, avatar_url)')
    .eq('conversation_id', id)
    .order('created_at', { ascending: true })

  // Load AI suggestions
  const { data: aiSuggestions } = await supabase
    .from('ai_suggestions')
    .select('*')
    .eq('conversation_id', id)
    .eq('was_discarded', false)
    .order('created_at', { ascending: false })
    .limit(3)

  // Load qualification
  const { data: qualification } = await supabase
    .from('conversation_qualifications')
    .select('*')
    .eq('conversation_id', id)
    .maybeSingle()

  // Mark conversation as read
  await supabase
    .from('conversations')
    .update({ is_read: true })
    .eq('id', id)

  return (
    <div className="flex h-full">
      {/* Left: conversation list */}
      <div className="w-[360px] flex-shrink-0 border-r border-[rgba(255,255,255,0.06)] flex flex-col">
        <ConversationList conversations={conversations ?? []} activeId={id} />
      </div>

      {/* Center: thread */}
      <div className="flex-1 flex flex-col overflow-hidden min-w-0">
        <ConversationThread
          conversation={conversation}
          messages={messages ?? []}
          aiSuggestions={aiSuggestions ?? []}
        />
      </div>

      {/* Right: context sidebar */}
      <div className="w-[300px] flex-shrink-0 border-l border-[rgba(255,255,255,0.06)] overflow-y-auto">
        <ConversationSidebar
          conversation={conversation}
          qualification={qualification}
        />
      </div>
    </div>
  )
}
