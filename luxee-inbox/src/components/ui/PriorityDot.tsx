import type { PriorityLevel } from '@/types/database'
import { cn } from '@/lib/utils'

const COLORS: Record<PriorityLevel, string> = {
  low: 'bg-[rgba(255,255,255,0.2)]',
  normal: 'bg-[#3B82F6]',
  high: 'bg-[#F59E0B]',
  urgent: 'bg-[#EF4444]',
}

interface Props {
  priority: PriorityLevel | null
}

export default function PriorityDot({ priority }: Props) {
  return (
    <div className={cn('w-1.5 h-1.5 rounded-full flex-shrink-0', COLORS[priority ?? 'normal'])} />
  )
}
