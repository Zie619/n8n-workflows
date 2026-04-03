import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Luxee Inbox',
  description: 'Multi-channel command center — SMS, WhatsApp, LinkedIn, Outlook',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="dark">
      <body className={`${inter.className} bg-[#07070A] text-white antialiased`}>
        {children}
      </body>
    </html>
  )
}
