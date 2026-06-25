import type { ChannelType } from '@/types/database'
import { cn } from '@/lib/utils'

const CHANNEL_CONFIG: Record<ChannelType, { label: string; color: string; bg: string }> = {
  sms: { label: 'SMS', color: '#10B981', bg: 'rgba(16,185,129,0.12)' },
  whatsapp: { label: 'WA', color: '#25D366', bg: 'rgba(37,211,102,0.12)' },
  linkedin: { label: 'LI', color: '#0A66C2', bg: 'rgba(10,102,194,0.15)' },
  outlook: { label: 'Mail', color: '#0078D4', bg: 'rgba(0,120,212,0.15)' },
  internal: { label: 'INT', color: 'rgba(255,255,255,0.5)', bg: 'rgba(255,255,255,0.08)' },
}

interface Props {
  channel: ChannelType
  compact?: boolean
  className?: string
}

export default function ChannelBadge({ channel, compact, className }: Props) {
  const config = CHANNEL_CONFIG[channel] ?? CHANNEL_CONFIG.internal

  return (
    <span
      className={cn(
        'inline-flex items-center font-mono font-medium rounded',
        compact ? 'text-[9px] px-1 py-0.5' : 'text-xs px-1.5 py-0.5',
        className
      )}
      style={{ color: config.color, background: config.bg }}
    >
      {config.label}
    </span>
  )
}
