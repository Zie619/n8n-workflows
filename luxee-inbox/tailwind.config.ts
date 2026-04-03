import type { Config } from 'tailwindcss'

const config: Config = {
  darkMode: 'class',
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Luxee design tokens — mirrors CSS variables in globals.css
        bg: {
          base: '#07070A',
          surface: '#0A0A0F',
          elevated: '#111118',
          panel: '#14141C',
          hover: '#1A1A24',
          active: '#1F1F2E',
        },
        accent: {
          DEFAULT: '#7C3AED',
          mid: '#8B5CF6',
          light: '#A78BFA',
          muted: 'rgba(124, 58, 237, 0.15)',
        },
        channel: {
          sms: '#10B981',
          whatsapp: '#25D366',
          linkedin: '#0A66C2',
          outlook: '#0078D4',
        },
        border: {
          DEFAULT: 'rgba(255, 255, 255, 0.06)',
          subtle: 'rgba(255, 255, 255, 0.04)',
          strong: 'rgba(255, 255, 255, 0.12)',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
      },
      animation: {
        'fade-in': 'fadeIn 0.15s ease-in-out',
        'slide-up': 'slideUp 0.2s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(8px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
}

export default config
