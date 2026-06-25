import { redirect } from 'next/navigation'
import { createClient } from '@/lib/supabase/server'
import LoginForm from '@/components/auth/LoginForm'

export default async function LoginPage() {
  const supabase = await createClient()
  const { data: { user } } = await supabase.auth.getUser()

  if (user) {
    redirect('/inbox')
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-[#07070A]">
      <div className="w-full max-w-sm px-6">
        {/* Logo / wordmark */}
        <div className="mb-10 text-center">
          <span className="text-2xl font-bold tracking-tight text-white">
            Luxee<span className="text-[#8B5CF6]">.</span>
          </span>
          <p className="mt-2 text-sm text-[rgba(255,255,255,0.45)]">
            Sign in to your workspace
          </p>
        </div>

        <LoginForm />
      </div>
    </div>
  )
}
