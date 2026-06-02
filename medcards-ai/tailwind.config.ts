import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        // MEDCARDS.AI Brand Colors
        brand: {
          // Deep blue - Medical trust and professionalism
          primary: {
            DEFAULT: "#0A2463", // Deep medical blue
            light: "#1E3A8A",
            dark: "#051333",
          },
          // Surgical green - Success and validation
          success: {
            DEFAULT: "#06D6A0", // Surgical green
            light: "#4ADE80",
            dark: "#059669",
          },
          // Medical alert red - Critical errors
          error: {
            DEFAULT: "#EF4444",
            light: "#F87171",
            dark: "#DC2626",
          },
          // Neutral medical grays
          gray: {
            50: "#F9FAFB",
            100: "#F3F4F6",
            200: "#E5E7EB",
            300: "#D1D5DB",
            400: "#9CA3AF",
            500: "#6B7280",
            600: "#4B5563",
            700: "#374151",
            800: "#1F2937",
            900: "#111827",
          },
        },
        // Shadcn UI compatibility
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        chart: {
          "1": "hsl(var(--chart-1))",
          "2": "hsl(var(--chart-2))",
          "3": "hsl(var(--chart-3))",
          "4": "hsl(var(--chart-4))",
          "5": "hsl(var(--chart-5))",
        },
      },
      fontFamily: {
        // Interface font - excellent digital legibility
        sans: ["var(--font-inter)", "system-ui", "sans-serif"],
        // Clinical content font - serious medical literature feel
        serif: ["var(--font-crimson)", "Georgia", "serif"],
      },
      spacing: {
        // Mathematical spacing scale (8px base)
        // Creates subconscious visual consistency
        "18": "4.5rem", // 72px
        "88": "22rem", // 352px
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      animation: {
        "fade-in": "fadeIn 0.5s ease-in-out",
        "slide-up": "slideUp 0.4s ease-out",
        "pulse-success": "pulseSuccess 2s ease-in-out infinite",
        "confetti": "confetti 1s ease-out",
      },
      keyframes: {
        fadeIn: {
          "0%": { opacity: "0" },
          "100%": { opacity: "1" },
        },
        slideUp: {
          "0%": { transform: "translateY(20px)", opacity: "0" },
          "100%": { transform: "translateY(0)", opacity: "1" },
        },
        pulseSuccess: {
          "0%, 100%": { boxShadow: "0 0 0 0 rgba(6, 214, 160, 0.7)" },
          "50%": { boxShadow: "0 0 0 10px rgba(6, 214, 160, 0)" },
        },
        confetti: {
          "0%": { transform: "scale(1) rotate(0deg)", opacity: "1" },
          "100%": { transform: "scale(0) rotate(360deg)", opacity: "0" },
        },
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
};

export default config;
