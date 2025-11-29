# MEDCARDS.AI - Scalability Architecture & Technical Infrastructure

## 🎯 Scaling Philosophy

**Build for 10k users, architect for 1M users.**

This document outlines how MEDCARDS.AI scales from MVP (1k users) to platform (1M+ users) without major rewrites.

---

## 📊 Growth Stages & Infrastructure Evolution

### Stage 1: MVP (0-10k users)
**Monthly Active Users**: 0-10,000
**Daily Interactions**: 0-100k
**Infrastructure Cost**: $500-1,000/month

**Stack:**
```
Frontend: Vercel Edge Network
Backend: Next.js Server Actions (Vercel Serverless)
Database: Supabase Free/Pro (PostgreSQL)
AI: Anthropic Claude API (pay-per-use)
Cache: None (database only)
CDN: Vercel automatic
```

**Why it works:**
- Serverless scales automatically
- No DevOps required
- Pay only for usage
- Deploy in minutes

**Bottlenecks:**
- None at this scale
- Database has 10GB limit (sufficient for 10k users)

---

### Stage 2: Growth (10k-100k users)
**Monthly Active Users**: 10,000-100,000
**Daily Interactions**: 100k-1M
**Infrastructure Cost**: $2,000-5,000/month

**Stack Upgrades:**
```
Frontend: Vercel Edge Network (same)
Backend: Next.js Server Actions (same)
Database: Supabase Pro → Team plan
  - Connection pooling (pgBouncer)
  - Read replicas for analytics
  - 100GB storage
AI: Anthropic Claude API + Response caching
Cache: Upstash Redis (Vercel KV)
  - Cache AI responses (24h TTL)
  - Cache user sessions
  - Rate limiting
CDN: CloudFlare in front of Vercel (optional)
Monitoring: Vercel Analytics + Sentry
```

**Architecture Pattern:**

```typescript
// lib/cache/redis.ts
import { Redis } from '@upstash/redis';

const redis = Redis.fromEnv();

export async function getCachedAIResponse(cacheKey: string) {
  return await redis.get(cacheKey);
}

export async function setCachedAIResponse(
  cacheKey: string,
  response: any,
  ttlSeconds: number = 86400 // 24 hours
) {
  await redis.setex(cacheKey, ttlSeconds, JSON.stringify(response));
}

// Usage in AI feedback generation
export async function generateFeedback(context: FeedbackContext): Promise<AIFeedback> {
  const cacheKey = `feedback:${context.case.id}:${context.student_answer.selected_answer_id}`;

  // Try cache first
  const cached = await getCachedAIResponse(cacheKey);
  if (cached) {
    console.log('Cache hit for feedback');
    return JSON.parse(cached as string);
  }

  // Generate new feedback
  const feedback = await callClaudeAPI(context);

  // Cache for future students
  await setCachedAIResponse(cacheKey, feedback);

  return feedback;
}
```

**Database Optimizations:**

```sql
-- Partition interactions table by month (reduces query time)
CREATE TABLE interactions_2025_01 PARTITION OF interactions
FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');

CREATE TABLE interactions_2025_02 PARTITION OF interactions
FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');

-- Indexes for hot queries
CREATE INDEX CONCURRENTLY idx_interactions_user_recent
ON interactions(user_id, created_at DESC)
WHERE created_at > NOW() - INTERVAL '30 days';

-- Materialized view for dashboard stats (refresh every hour)
CREATE MATERIALIZED VIEW user_stats_cache AS
SELECT
  user_id,
  COUNT(*) as total_cases,
  AVG(CASE WHEN is_correct THEN 1.0 ELSE 0.0 END) as success_rate,
  MAX(created_at) as last_activity
FROM interactions
GROUP BY user_id;

CREATE UNIQUE INDEX ON user_stats_cache(user_id);

-- Auto-refresh via pg_cron
SELECT cron.schedule('refresh-user-stats', '0 * * * *',
  'REFRESH MATERIALIZED VIEW CONCURRENTLY user_stats_cache');
```

**Expected Performance:**
- API response time: <200ms (p95)
- Database query time: <50ms (p95)
- AI response time: 1-3s (depending on Claude API)
- Cache hit rate: 70-80% for common operations

---

### Stage 3: Scale (100k-1M users)
**Monthly Active Users**: 100,000-1,000,000
**Daily Interactions**: 1M-10M
**Infrastructure Cost**: $10,000-30,000/month

**Major Architecture Changes:**

#### 1. **Database Sharding Strategy**

**Shard by User ID** (most queries are user-scoped):

```sql
-- Shard 1: Users with ID hash % 4 = 0
-- Shard 2: Users with ID hash % 4 = 1
-- Shard 3: Users with ID hash % 4 = 2
-- Shard 4: Users with ID hash % 4 = 3

-- Routing logic in application
function getShardForUser(userId: string): number {
  const hash = hashUserId(userId);
  return hash % 4;
}

// Connection pool per shard
const shardConnections = {
  0: createSupabaseClient(SHARD_0_URL),
  1: createSupabaseClient(SHARD_1_URL),
  2: createSupabaseClient(SHARD_2_URL),
  3: createSupabaseClient(SHARD_3_URL),
};

export function getDbForUser(userId: string) {
  const shard = getShardForUser(userId);
  return shardConnections[shard];
}
```

**Cross-shard queries** (leaderboards, analytics) go to read replicas or data warehouse.

#### 2. **AI Infrastructure Optimization**

**Problem**: Claude API costs scale linearly ($1M+ users = $50k+/month in AI costs)

**Solution**: Multi-tier AI strategy

```typescript
// Tier 1: Pre-computed responses (instant, free)
// For common case + answer combinations (80% of traffic)
const precomputedFeedback = await db
  .from('precomputed_feedback')
  .select('*')
  .eq('case_id', caseId)
  .eq('selected_answer', answerId)
  .single();

if (precomputedFeedback) return precomputedFeedback;

// Tier 2: Cached responses (fast, cheap)
// For less common combinations (15% of traffic)
const cached = await redis.get(`feedback:${caseId}:${answerId}`);
if (cached) return JSON.parse(cached);

// Tier 3: Real-time AI generation (slow, expensive)
// For rare combinations or premium users (5% of traffic)
const feedback = await generateWithClaude(context);
await redis.setex(`feedback:${caseId}:${answerId}`, 86400, JSON.stringify(feedback));
return feedback;
```

**Cost Impact:**
- Before: 1M API calls/day × $0.003 = $3,000/day = $90,000/month
- After: 50k API calls/day × $0.003 = $150/day = $4,500/month
- **Savings**: $85,500/month (95% reduction)

#### 3. **Background Job Processing**

**Move heavy operations off request path:**

```typescript
// lib/jobs/queue.ts
import { Inngest } from 'inngest';

const inngest = new Inngest({ name: 'MedCards' });

// Heavy operations run async
export const calculateUserMetrics = inngest.createFunction(
  { name: 'Calculate User Metrics' },
  { event: 'user/interaction.created' },
  async ({ event }) => {
    const userId = event.data.userId;

    // Recalculate all user stats
    const stats = await computeComprehensiveStats(userId);

    // Update database
    await db.from('users').update({ progress: stats }).eq('id', userId);

    // Check for badge unlocks
    await checkBadgeUnlocks(userId, stats);

    // Update leaderboards
    await updateLeaderboards(userId, stats);
  }
);

// Badge unlock notifications
export const notifyBadgeUnlock = inngest.createFunction(
  { name: 'Notify Badge Unlock' },
  { event: 'badge/unlocked' },
  async ({ event }) => {
    // Send email
    // Push notification
    // Update UI via WebSocket
  }
);
```

**Benefits:**
- API response time: 2s → 200ms
- Better user experience
- Can retry failed jobs
- Scale workers independently

#### 4. **Read/Write Separation**

```typescript
// lib/db/routing.ts

// Write operations → Primary database
export async function writeInteraction(data: InteractionData) {
  return await primaryDb.from('interactions').insert(data);
}

// Read operations → Read replicas (distribute load)
const readReplicas = [replicaDb1, replicaDb2, replicaDb3];
let currentReplica = 0;

export async function getUser Interactions(userId: string) {
  const db = readReplicas[currentReplica % readReplicas.length];
  currentReplica++;

  return await db
    .from('interactions')
    .select('*')
    .eq('user_id', userId)
    .order('created_at', { ascending: false })
    .limit(20);
}
```

#### 5. **CDN & Static Asset Optimization**

```typescript
// next.config.ts
export default {
  images: {
    loader: 'cloudinary', // Or imgix, cloudflare
    domains: ['res.cloudinary.com'],
  },
  // Serve heavy assets from CDN
  assetPrefix: process.env.CDN_URL,
};
```

**Asset Strategy:**
- Case images → CloudFlare R2 (S3-compatible, cheaper)
- User avatars → CloudFlare Images (auto-optimization)
- Video explanations → Mux (video streaming CDN)

---

### Stage 4: Platform (1M+ users)
**Monthly Active Users**: 1M+
**Daily Interactions**: 10M+
**Infrastructure Cost**: $50,000-100,000/month

**Full Microservices Architecture:**

```
┌─────────────────────────────────────────────────────────┐
│                    CloudFlare CDN                        │
└─────────────────────┬───────────────────────────────────┘
                      │
        ┌─────────────┴─────────────┐
        │     Load Balancer         │
        └─────────────┬─────────────┘
                      │
        ┌─────────────┴─────────────────────────────┐
        │                                             │
┌───────▼────────┐                          ┌────────▼────────┐
│  Web Frontend  │                          │   Mobile API    │
│  (Vercel Edge) │                          │   (Dedicated)   │
└───────┬────────┘                          └────────┬────────┘
        │                                             │
        └─────────────┬───────────────────────────────┘
                      │
        ┌─────────────▼──────────────────────┐
        │         API Gateway                │
        │    (Rate limiting, Auth)           │
        └─────────────┬──────────────────────┘
                      │
        ┌─────────────┴──────────────────────────────┐
        │                                              │
┌───────▼──────────┐  ┌────────────┐  ┌─────────────▼────────┐
│  User Service    │  │   Cache    │  │   Case Service       │
│  (Supabase)      │  │  (Redis)   │  │   (Dedicated DB)     │
└──────────────────┘  └────────────┘  └──────────────────────┘
        │                                              │
        │              ┌─────────────┐                 │
        └──────────────►   AI Service ◄────────────────┘
                       │  (Claude +   │
                       │   Fine-tune) │
                       └──────┬───────┘
                              │
                    ┌─────────▼──────────┐
                    │  Analytics Service │
                    │   (ClickHouse)     │
                    └────────────────────┘
```

**Service Breakdown:**

| Service | Tech | Purpose |
|---------|------|---------|
| User Service | Supabase | User profiles, auth, progress |
| Case Service | Dedicated PostgreSQL | Clinical cases, interactions |
| AI Service | Claude API + Custom models | Feedback, coaching, adaptive |
| Analytics | ClickHouse | Real-time analytics, dashboards |
| Search | Elasticsearch | Case search, user search |
| Notifications | Pusher / Socket.io | Real-time updates |
| Jobs | Temporal | Background processing |
| Cache | Redis Cluster | Multi-layer caching |

---

## 💰 Cost Breakdown by Stage

### Stage 1: MVP (10k users)
```
Vercel Pro:              $20/month
Supabase Pro:           $25/month
Anthropic API:         $300/month  (100k AI calls)
Domain + SSL:           $15/month
Monitoring:            $50/month
──────────────────────────────────
TOTAL:                 $410/month
Cost per user:         $0.041/month
```

### Stage 2: Growth (100k users)
```
Vercel Enterprise:     $500/month
Supabase Team:         $599/month
Anthropic API:       $1,500/month  (500k AI calls, 70% cached)
Upstash Redis:         $200/month
CloudFlare Pro:         $20/month
Sentry:                $100/month
──────────────────────────────────
TOTAL:               $2,919/month
Cost per user:        $0.029/month
```

### Stage 3: Scale (1M users)
```
Vercel Enterprise:   $2,000/month
Supabase (4 shards): $2,400/month  ($600 each)
Anthropic API:       $4,500/month  (cached 95%)
Redis Cluster:       $1,000/month
CloudFlare:            $200/month
Sentry:                $500/month
Inngest (jobs):        $300/month
Datadog:               $800/month
──────────────────────────────────
TOTAL:              $11,700/month
Cost per user:       $0.012/month
```

**Key Insight**: Cost per user DECREASES as you scale (economies of scale).

---

## 🔥 Performance Targets

### API Response Times (p95)
- **Homepage load**: <500ms
- **Dashboard load**: <800ms
- **Case presentation**: <300ms
- **Submit answer**: <400ms
- **AI feedback**: <2s (with streaming)
- **Chat message**: <500ms (streaming)

### Database Query Times (p95)
- **Simple SELECT**: <10ms
- **Complex JOIN**: <50ms
- **Analytics query**: <200ms
- **Leaderboard**: <100ms (cached)

### Availability
- **Uptime SLA**: 99.9% (8.76 hours downtime/year)
- **Zero-downtime deployments**: Required
- **Disaster recovery**: <15 minute RPO/RTO

---

## 🛡️ Reliability & Monitoring

### Error Budget
```
Monthly Uptime Target: 99.9%
Error Budget: 0.1% = 43 minutes downtime/month

Week 1: 5 minutes → 37 minutes left
Week 2: 10 minutes → 27 minutes left
Week 3: 30 minutes → -3 minutes (EXCEEDED!)
  → Freeze feature releases
  → Focus on stability
  → Root cause analysis
```

### Monitoring Stack

```typescript
// lib/monitoring/metrics.ts
import * as Sentry from '@sentry/nextjs';
import { track } from '@vercel/analytics';

// Track all API calls
export async function monitoredAPICall<T>(
  operation: string,
  fn: () => Promise<T>
): Promise<T> {
  const startTime = Date.now();

  try {
    const result = await fn();
    const duration = Date.now() - startTime;

    // Success metrics
    track('api_call_success', {
      operation,
      duration,
    });

    return result;
  } catch (error) {
    // Error tracking
    Sentry.captureException(error, {
      tags: { operation },
      extra: { duration: Date.now() - startTime },
    });

    // Error metrics
    track('api_call_error', {
      operation,
      error: error.message,
    });

    throw error;
  }
}

// Usage
export async function submitAnswer(data: AnswerData) {
  return monitoredAPICall('submit_answer', async () => {
    // ... actual implementation
  });
}
```

### Alerts Configuration

```yaml
alerts:
  - name: High Error Rate
    condition: error_rate > 5%
    window: 5 minutes
    severity: critical
    notify: pagerduty

  - name: Slow API Responses
    condition: p95_latency > 2 seconds
    window: 10 minutes
    severity: warning
    notify: slack

  - name: Database Connection Pool Exhaustion
    condition: available_connections < 10
    severity: critical
    notify: pagerduty

  - name: AI API Rate Limit Approaching
    condition: anthropic_remaining_requests < 100
    severity: warning
    notify: slack

  - name: Daily Active Users Drop
    condition: dau_vs_yesterday_decrease > 20%
    severity: warning
    notify: slack
```

---

## 📈 Capacity Planning

### User Growth Projections

```
Month 1:     100 users
Month 3:   1,000 users  (10x growth)
Month 6:  10,000 users  (10x growth)
Month 12: 50,000 users  (5x growth)
Month 18: 150,000 users (3x growth)
Month 24: 500,000 users (3.3x growth)
```

### Infrastructure Scaling Triggers

| Metric | Trigger | Action |
|--------|---------|--------|
| Database CPU | >70% for 1h | Add read replica |
| Database Storage | >80% used | Upgrade plan OR archive old data |
| API Error Rate | >5% for 5min | Scale up serverless OR rollback |
| Redis Memory | >80% used | Upgrade OR implement LRU eviction |
| AI API Costs | >$10k/month | Implement aggressive caching |

### Scaling Checklist

**At 10k users:**
- [ ] Enable Redis caching
- [ ] Add database indexes
- [ ] Set up monitoring
- [ ] Implement rate limiting

**At 50k users:**
- [ ] Add read replicas
- [ ] Implement job queue
- [ ] Aggressive AI response caching
- [ ] CloudFlare Pro

**At 100k users:**
- [ ] Database sharding
- [ ] Microservices architecture
- [ ] Dedicated analytics database
- [ ] Content delivery optimization

---

## 🚀 Deployment Strategy

### Zero-Downtime Deployments

```bash
# Blue-Green Deployment on Vercel
1. Deploy new version to staging
2. Run smoke tests
3. Deploy to production (Vercel handles canary rollout)
4. Monitor error rates for 15 minutes
5. If errors spike: automatic rollback
6. If stable: full rollout
```

### Database Migrations

```typescript
// migrations/0015_add_community_cases.ts
export async function up() {
  // Safe migration: additive only
  await db.schema
    .createTable('community_cases')
    .addColumn('id', 'uuid', (col) => col.primaryKey())
    .addColumn('created_at', 'timestamp')
    // ... other columns
    .execute();
}

export async function down() {
  // Rollback (but never run in production!)
  await db.schema.dropTable('community_cases').execute();
}
```

**Migration Rules:**
1. Never drop columns (deprecate instead)
2. Add new columns as nullable
3. Backfill data async
4. Test on staging with production data snapshot

---

## 🔒 Security at Scale

### Rate Limiting

```typescript
// middleware.ts
import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(100, '1 m'), // 100 requests per minute
});

export async function middleware(request: Request) {
  const ip = request.headers.get('x-forwarded-for') ?? 'unknown';
  const { success, limit, remaining } = await ratelimit.limit(ip);

  if (!success) {
    return new Response('Rate limit exceeded', { status: 429 });
  }

  return NextResponse.next();
}
```

### DDoS Protection

```
CloudFlare WAF → Vercel → Application

- CloudFlare: Block malicious IPs, rate limit per IP
- Vercel: Edge protection, DDoS mitigation
- Application: User-level rate limits
```

### Data Encryption

```
- At Rest: Supabase encrypts all data (AES-256)
- In Transit: TLS 1.3 everywhere
- Backups: Encrypted, geographically distributed
- Secrets: Managed via Vercel environment variables
```

---

## 📊 Analytics Architecture

### Real-Time Analytics

```sql
-- ClickHouse table for real-time analytics (better than PostgreSQL for OLAP)
CREATE TABLE analytics.interactions (
    user_id UUID,
    case_id UUID,
    is_correct Boolean,
    time_to_answer Int32,
    created_at DateTime,
    specialty String
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(created_at)
ORDER BY (created_at, user_id);

-- Fast aggregations
SELECT
    specialty,
    COUNT(*) as total,
    AVG(is_correct) as success_rate
FROM analytics.interactions
WHERE created_at > now() - INTERVAL 7 DAY
GROUP BY specialty;

-- Executes in <50ms on 100M rows
```

### Data Warehouse Strategy

```
Operational DB (PostgreSQL) → CDC → Data Warehouse (ClickHouse)
                                   ↓
                            Analytics Dashboard (Metabase/Looker)
```

---

## 🎯 Summary: Scaling Path

```
MVP (0-10k):        Simple stack, manual processes, good enough
Growth (10-100k):   Add caching, optimize database, automate
Scale (100k-1M):    Sharding, microservices, background jobs
Platform (1M+):     Full distribution, dedicated services, ML ops

Philosophy: Scale progressively, not prematurely.
Build what you need TODAY, architect for TOMORROW.
```

**Next Steps**: Implement MVP stack, monitor metrics, scale when triggers hit.
