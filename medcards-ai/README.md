# MEDCARDS.AI 🏥

> AI-powered medical residency exam preparation platform for Brazilian medical students

**MEDCARDS.AI** is not a traditional course platform. It's an intelligent study companion that adapts to each student's learning journey, delivering personalized clinical case training powered by Claude AI.

---

## 🎯 Product Vision

Students don't access modules or lessons. They engage with an AI coach that knows:
- Exactly where they are in their preparation
- What clinical patterns they need to master
- How to get them to approval

**Three core screens:**
1. **Battle Dashboard** - Real-time clinical competency metrics
2. **Training Arena** - Adaptive case presentations with AI feedback
3. **War Room** - Personal AI tutor with complete memory

---

## 🏗️ Architecture

### Brutally Simple Stack

```
Frontend:  Next.js 14 (App Router) + Tailwind CSS + Shadcn UI
Backend:   Next.js Server Actions (no separate backend)
Database:  Supabase (PostgreSQL with RLS)
AI:        Anthropic Claude Sonnet 4 API
Deploy:    Vercel (one-click deployment)
```

### Why This Stack?

- **Next.js 14**: Server Components + Server Actions = full-stack in one codebase
- **Supabase**: PostgreSQL with built-in auth, RLS, real-time subscriptions
- **Shadcn UI**: Copy-paste beautiful components, customize instantly
- **Claude AI**: State-of-the-art reasoning for medical education
- **Vercel**: Push to deploy, automatic scaling, zero DevOps

**Deploy time**: 30 minutes from zero to production.

---

## 📁 Project Structure

```
medcards-ai/
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── (auth)/            # Authentication routes
│   │   ├── dashboard/         # Battle Dashboard
│   │   ├── arena/             # Training Arena
│   │   ├── war-room/          # AI Tutor Chat
│   │   └── layout.tsx         # Root layout
│   ├── components/            # React components
│   │   ├── ui/               # Shadcn UI components
│   │   ├── dashboard/        # Dashboard-specific
│   │   ├── arena/            # Arena-specific
│   │   └── shared/           # Shared components
│   ├── lib/                   # Core business logic
│   │   ├── ai/               # Claude AI integration
│   │   │   └── claude.ts     # AI functions (coach, feedback, tutor)
│   │   ├── supabase/         # Database utilities
│   │   │   └── client.ts     # Supabase clients
│   │   ├── adaptive/         # Adaptive engine logic
│   │   ├── gamification/     # Badges & progression
│   │   └── utils/            # Helpers
│   └── types/                # TypeScript types
│       └── database.ts       # Database schema types
├── supabase/
│   ├── schema.sql            # Database schema
│   ├── seed-cases.sql        # Initial clinical cases
│   └── migrations/           # Database migrations
├── prompts/
│   ├── coach-prompt.md       # AI Coach instructions
│   ├── feedback-prompt.md    # AI Feedback generator
│   └── tutor-prompt.md       # AI Tutor (chat)
├── public/                   # Static assets
├── .env.example              # Environment template
├── package.json
├── tsconfig.json
├── tailwind.config.ts
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Node.js 18+
- npm or yarn
- Supabase account (free tier works)
- Anthropic API key (Claude access)

### 1. Clone and Install

```bash
git clone <repository-url>
cd medcards-ai
npm install
```

### 2. Set Up Supabase

1. Create project at [supabase.com](https://supabase.com)
2. Run the schema:
   ```bash
   # Copy schema to Supabase SQL Editor and run
   cat supabase/schema.sql
   ```
3. (Optional) Seed initial cases:
   ```bash
   cat supabase/seed-cases.sql
   ```
4. Get your credentials from Project Settings → API

### 3. Configure Environment

```bash
cp .env.example .env.local
```

Edit `.env.local`:
```env
NEXT_PUBLIC_SUPABASE_URL=your-project-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
ANTHROPIC_API_KEY=sk-ant-your-api-key
```

### 4. Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

### 5. Deploy to Production

```bash
# Connect to Vercel
npx vercel

# Deploy
npx vercel --prod
```

Add environment variables in Vercel dashboard.

**Done.** Your platform is live.

---

## 🧠 Core Systems

### 1. Adaptive Engine

**Purpose**: Select next optimal case for each student

**Algorithm**:
```
1. Calculate competency by specialty (weighted by recency)
2. Identify gaps (success_rate < 65%)
3. Select next case:
   - 60%: Address critical gaps
   - 30%: Reinforce strengths
   - 10%: Explore new areas
4. Claude AI validates selection and prepares coaching
```

**Location**: `src/lib/adaptive/engine.ts`

### 2. AI Coach System

**Three Specialized Prompts**:

1. **Coach Prompt** (`prompts/coach-prompt.md`)
   - Analyzes student history
   - Selects optimal next case
   - Prepares graduated hints
   - Returns structured JSON

2. **Feedback Prompt** (`prompts/feedback-prompt.md`)
   - Analyzes student's answer
   - Identifies reasoning gaps
   - Provides detailed clinical explanation
   - Suggests next practice steps

3. **Tutor Prompt** (`prompts/tutor-prompt.md`)
   - Conversational coaching
   - Complete memory of student journey
   - Specific, data-driven advice
   - Motivational support

**Integration**: `src/lib/ai/claude.ts`

### 3. Gamification System

**Badges**:
- First Win, Streaks, Speed, Specialty Mastery
- Auto-unlock via Supabase triggers
- Animated celebrations (Framer Motion)

**Progression**:
- Experience points per case
- Level-up system
- Unlock advanced cases at higher levels

**Location**: `src/lib/gamification/`

---

## 📊 Database Schema

### Core Tables

**users**
- Profile, progress (JSONB), preferences, subscription

**clinical_cases**
- Case content, options, explanations
- Difficulty, specialty, tags
- Global statistics (success rate, avg time)

**interactions**
- Every student answer recorded
- AI feedback stored as JSONB
- Used for adaptive algorithm

**chat_history**
- AI Tutor conversations
- Full context maintained

**badges** + **user_badges**
- Gamification achievements

### Key Features

- **Row Level Security (RLS)**: Users only see their own data
- **Automatic triggers**: Update case statistics on interaction
- **JSONB fields**: Flexible progress tracking without schema changes
- **Indexes**: Optimized for common queries

**Full schema**: `supabase/schema.sql`

---

## 🎨 Design System

### Colors

- **Primary Blue** (`#0A2463`): Medical trust, main actions
- **Surgical Green** (`#06D6A0`): Success, correct answers
- **Alert Red** (`#EF4444`): Errors, critical alerts
- **Gray Scale**: Interface neutrals

### Typography

- **Interface**: Inter (excellent legibility)
- **Clinical Content**: Crimson Pro (serious medical feel)

### Spacing

Mathematical scale (8px base): 8, 16, 24, 32, 48, 64
Creates subconscious visual consistency.

### Animations

- Fade in: Content loading
- Slide up: New cases
- Pulse success: Correct answer feedback
- Confetti: Badge unlocked

**Config**: `tailwind.config.ts`

---

## 🛠️ Development Workflow

### Sprint-Based Implementation

**8 weeks to MVP** (following spec in `CLAUDE.md`):

1. **Week 1**: Foundation (schema, auth, deploy)
2. **Week 2**: Battle Dashboard
3. **Week 3**: Training Arena (basic)
4. **Week 4**: AI Integration (Claude feedback)
5. **Week 5**: War Room (chat)
6. **Week 6**: Adaptive Engine
7. **Week 7**: Gamification
8. **Week 8**: Polish & Analytics

### Key Commands

```bash
# Development
npm run dev              # Start dev server
npm run build            # Production build
npm run type-check       # TypeScript validation
npm run lint             # ESLint

# Database
npm run db:migrate       # Run migrations (if using Supabase CLI)
npm run db:seed          # Seed initial cases

# Deployment
npx vercel --prod        # Deploy to production
```

---

## 📈 Metrics That Matter

Track **only these four** weekly:

1. **Retention Day 7**: % users returning after 1 week
   - Target: 40% (initial) → 60% (post-PMF)

2. **Cases per Session**: How many cases per study session
   - Target: 8-12 cases

3. **Time to First Win**: Minutes until first 3-case streak
   - Target: < 15 minutes

4. **Conversion Free→Paid**: % paying after 50 cases
   - Target: 10% (initial) → 25% (optimized)

**Ignore**: Total users, page views, time on app (vanity metrics)

---

## 🔐 Security & Privacy

- **Authentication**: Supabase Auth (email/password, social login)
- **Authorization**: Row Level Security (RLS) on all tables
- **API Keys**: Server-side only (never exposed to client)
- **Data Privacy**: Student data never shared, LGPD compliant

---

## 🧪 Testing Strategy

### Current State
Manual testing during development (indie hacker MVP approach)

### Future (Post-PMF)
- Unit tests: Critical business logic (adaptive engine)
- Integration tests: AI response parsing
- E2E tests: Critical user flows (Playwright)

**Philosophy**: Ship fast, test what breaks in production, then add tests.

---

## 📚 Key Files Reference

| File | Purpose |
|------|---------|
| `supabase/schema.sql` | Complete database schema |
| `prompts/coach-prompt.md` | AI case selection instructions |
| `prompts/feedback-prompt.md` | AI answer analysis instructions |
| `prompts/tutor-prompt.md` | AI chat conversation instructions |
| `src/lib/ai/claude.ts` | Claude API integration |
| `src/lib/supabase/client.ts` | Database utilities |
| `src/types/database.ts` | TypeScript type definitions |
| `tailwind.config.ts` | Design system configuration |

---

## 🤝 Contributing

This is an indie hacker project optimized for solo development. Contributions welcome but keep these principles:

1. **Simplicity over features**: No unnecessary complexity
2. **Ship fast**: Working code > perfect code
3. **Data-driven**: Every feature must move core metrics
4. **User-first**: If students don't need it, don't build it

---

## 📄 License

[Add your license here]

---

## 🙋 Support

- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Email**: [your-email]

---

## 🎓 For Medical Students

**MEDCARDS.AI** is built by developers who understand:
- The stress of residency exams
- The need for personalized, adaptive learning
- That your time is precious

Our mission: **Get you approved with minimum study time and maximum confidence.**

Start training: [Deploy your instance or visit medcards.ai]

---

**Built with ❤️ for Brazilian medical residents**

*Stack: Next.js 14 • Supabase • Claude AI • Vercel*
