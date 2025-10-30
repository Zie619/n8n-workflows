# Eco Dyno + PostgreSQL Configuration Guide

## 🎯 Overview

This guide is specifically for **Heroku Eco Dynos** with **PostgreSQL database**. The workflow is optimized for:
- Shared CPU (low processing power)
- 1000 dyno hours/month
- PostgreSQL database for history tracking
- 4 posts per day (every 6 hours)

## 💰 Cost Breakdown

### Eco Dyno
- **Cost**: $5/month
- **Hours**: 1000 hours/month
- **Usage**: ~8 hours/month (0.8%)
- **Remaining**: 992 hours for other tasks

### PostgreSQL
- **Mini Plan**: $5/month (included with Eco)
- **Storage**: 1GB
- **Connections**: 20
- **Usage**: < 1MB for meme metadata

**Total**: ~$5-10/month for fully automated meme posting!

## 🗄️ PostgreSQL Setup

### Step 1: Verify PostgreSQL Add-on

```bash
# Check if PostgreSQL is attached
heroku addons -a your-app-name

# Should show something like:
# heroku-postgresql (postgresql-xxxxx-xxxxx) mini

# Get database credentials
heroku config:get DATABASE_URL -a your-app-name
```

### Step 2: Database Schema

The workflow automatically creates the table on first run, but you can manually create it:

```bash
# Connect to database
heroku pg:psql -a your-app-name

# Create table manually
CREATE TABLE IF NOT EXISTS meme_posts (
  id SERIAL PRIMARY KEY,
  template_id VARCHAR(50),
  topic VARCHAR(100),
  text0 VARCHAR(255),
  text1 VARCHAR(255),
  meme_url TEXT,
  instagram_id VARCHAR(100),
  posted_at TIMESTAMP DEFAULT NOW(),
  success BOOLEAN DEFAULT TRUE
);

# Create index for performance
CREATE INDEX idx_posted_at ON meme_posts(posted_at DESC);
CREATE INDEX idx_topic ON meme_posts(topic);

# Exit
\q
```

### Step 3: Configure n8n PostgreSQL Credentials

In n8n UI:
1. Go to **Credentials** → **New**
2. Select **Postgres**
3. Enter details from `DATABASE_URL`:

```
Format: postgres://user:password@host:port/database

Fields to fill:
- Host: [host from DATABASE_URL]
- Port: 5432
- Database: [database from DATABASE_URL]
- User: [user from DATABASE_URL]
- Password: [password from DATABASE_URL]
- SSL: Enable
```

Or use the full connection string:
- Select "Connection String" mode
- Paste entire `DATABASE_URL`

## ⚙️ Workflow Configuration

### Environment Variables

```bash
# ImgFlip (Free tier: 100 requests/day)
heroku config:set IMGFLIP_USERNAME=your_username -a your-app-name
heroku config:set IMGFLIP_PASSWORD=your_password -a your-app-name

# Instagram Graph API
heroku config:set INSTAGRAM_USER_ID=your_instagram_business_id -a your-app-name
heroku config:set INSTAGRAM_ACCESS_TOKEN=your_long_lived_token -a your-app-name

# n8n configuration
heroku config:set N8N_BASIC_AUTH_ACTIVE=true -a your-app-name
heroku config:set N8N_BASIC_AUTH_USER=admin -a your-app-name
heroku config:set N8N_BASIC_AUTH_PASSWORD=your_secure_password -a your-app-name

# PostgreSQL is auto-configured by Heroku
# DATABASE_URL is automatically available
```

### Import Workflow

1. Download: `2057_Meme_Instagram_EcoDyno_PostgreSQL_Scheduled.json`
2. In n8n: **Workflows** → **Import from File**
3. Configure PostgreSQL credentials in the workflow
4. Activate the workflow

## 📊 Performance Optimization

### Eco Dyno Specifics

**Shared CPU**: Your dyno shares CPU with other apps
- **Implication**: Avoid CPU-intensive operations
- **Solution**: This workflow uses minimal CPU
  - Simple random selection (no AI)
  - External API calls (CPU offloaded)
  - Lightweight database queries
  - No file processing

**Sleep Behavior**: Eco dynos don't sleep
- **Benefit**: Workflows run reliably on schedule
- **Better than Free**: No 30-minute idle timeout

### CPU Usage per Execution

| Operation | CPU Time | Notes |
|-----------|----------|-------|
| Schedule Trigger | < 1ms | Minimal |
| PostgreSQL Query | 20-50ms | Fast with index |
| Generate Meme Code | 5-10ms | Simple JS |
| ImgFlip API | 2-5s | External (no CPU) |
| Instagram API | 4-10s | External (no CPU) |
| PostgreSQL Insert | 10-30ms | Fast |
| **Total** | **< 100ms CPU** | Rest is I/O wait |

**Result**: Eco dyno shared CPU is more than sufficient!

### Memory Usage

- Peak: ~80-120MB per execution
- Eco dyno limit: 512MB
- Safe margin: 400MB+ free
- No memory leaks (stateless execution)

## 📈 Scaling Strategy

### Current Setup (4 posts/day)

```
Schedule: Every 6 hours
Posts per day: 4
Posts per month: ~120
Dyno hours used: ~8/month (0.8%)
Cost: $5-10/month
```

### Scale Up (If Needed)

**Option 1: More Frequent Posts**
```bash
# Every 4 hours = 6 posts/day
# Edit Schedule Trigger node: hoursInterval: 4
# Dyno hours: ~12/month (1.2%)
# Still well within 1000 hours
```

**Option 2: Multiple Platforms**
```bash
# Add TikTok + YouTube
# 3 platforms x 4 posts = 12 posts/day
# Dyno hours: ~24/month (2.4%)
# Still excellent
```

**Option 3: Multiple Accounts**
```bash
# 3 Instagram accounts
# 3 accounts x 4 posts = 12 posts/day
# Dyno hours: ~24/month (2.4%)
# Diversify content
```

### You Have Room For

With 1000 hours/month, you can run:
- ✅ This meme workflow (8 hours)
- ✅ 10+ other similar workflows
- ✅ API monitoring workflows
- ✅ Data sync workflows
- ✅ Notification workflows

**Total usage**: Still < 10% of available hours!

## 🔍 Monitoring

### Database Queries

```bash
# Connect to PostgreSQL
heroku pg:psql -a your-app-name

# Check recent posts
SELECT * FROM meme_posts ORDER BY posted_at DESC LIMIT 10;

# Check success rate
SELECT 
  COUNT(*) as total,
  SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful,
  ROUND(100.0 * SUM(CASE WHEN success THEN 1 ELSE 0 END) / COUNT(*), 2) as success_rate
FROM meme_posts
WHERE posted_at > NOW() - INTERVAL '30 days';

# Check most used topics
SELECT topic, COUNT(*) as count
FROM meme_posts
WHERE posted_at > NOW() - INTERVAL '30 days'
GROUP BY topic
ORDER BY count DESC;

# Check storage usage
SELECT pg_size_pretty(pg_database_size(current_database()));
```

### Dyno Hours Usage

```bash
# Check current month usage
heroku ps -a your-app-name

# View metrics
heroku metrics -a your-app-name

# View logs
heroku logs --tail -a your-app-name
```

### n8n Execution History

In n8n UI:
1. Go to **Executions** tab
2. View recent workflow runs
3. Check success/failure rate
4. Debug any errors

## 🛠️ Troubleshooting

### Issue: Database Connection Failed

**Check:**
```bash
# Verify DATABASE_URL exists
heroku config:get DATABASE_URL -a your-app-name

# Test connection
heroku pg:psql -a your-app-name
```

**Solution:**
- Ensure PostgreSQL add-on is attached
- Verify SSL is enabled in n8n credentials
- Check connection string format

### Issue: Slow Execution

**Check:**
```sql
-- Check database query performance
EXPLAIN ANALYZE 
SELECT * FROM meme_posts 
WHERE posted_at > NOW() - INTERVAL '7 days';
```

**Solutions:**
- Add indexes (already included in schema)
- Reduce data retention (keep only last 30 days)
- Vacuum database: `heroku pg:vacuum -a your-app-name`

### Issue: Table Not Created

**Solution:**
```bash
# Manually create table
heroku pg:psql -a your-app-name

CREATE TABLE IF NOT EXISTS meme_posts (
  id SERIAL PRIMARY KEY,
  template_id VARCHAR(50),
  topic VARCHAR(100),
  text0 VARCHAR(255),
  text1 VARCHAR(255),
  meme_url TEXT,
  instagram_id VARCHAR(100),
  posted_at TIMESTAMP DEFAULT NOW(),
  success BOOLEAN DEFAULT TRUE
);
```

### Issue: Out of Database Connections

**Check:**
```sql
SELECT count(*) FROM pg_stat_activity;
```

**Solution:**
- Mini plan has 20 connections
- n8n uses 1-2 connections per workflow
- Close unused connections
- Upgrade to Basic plan if needed ($9/month, 120 connections)

## 🔧 Maintenance

### Weekly Tasks

```bash
# Check success rate
heroku pg:psql -a your-app-name -c "SELECT COUNT(*), SUM(CASE WHEN success THEN 1 ELSE 0 END)::FLOAT / COUNT(*) * 100 as success_rate FROM meme_posts WHERE posted_at > NOW() - INTERVAL '7 days';"

# Check storage
heroku pg:info -a your-app-name
```

### Monthly Tasks

```bash
# Clean old data (optional - keep last 90 days)
heroku pg:psql -a your-app-name -c "DELETE FROM meme_posts WHERE posted_at < NOW() - INTERVAL '90 days';"

# Vacuum database
heroku pg:vacuum -a your-app-name

# Renew Instagram access token (every 60 days)
# Get new token from Facebook Graph API Explorer
heroku config:set INSTAGRAM_ACCESS_TOKEN=new_token -a your-app-name
```

## 📊 Database Optimization

### Keep Database Small

```sql
-- Add automatic cleanup trigger (optional)
CREATE OR REPLACE FUNCTION cleanup_old_posts() RETURNS trigger AS $$
BEGIN
  DELETE FROM meme_posts WHERE posted_at < NOW() - INTERVAL '90 days';
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER cleanup_trigger
  AFTER INSERT ON meme_posts
  EXECUTE FUNCTION cleanup_old_posts();
```

### Backup Data

```bash
# Backup database
heroku pg:backups:capture -a your-app-name

# List backups
heroku pg:backups -a your-app-name

# Download backup
heroku pg:backups:download -a your-app-name
```

## 🎓 Why This Approach?

### Why Store Metadata Only?

**❌ Bad: Store meme images in PostgreSQL**
- Binary data (1-2MB per image)
- Fills database quickly
- Slow queries
- Expensive bandwidth

**✅ Good: Store URLs only**
- Text data (< 200 bytes per record)
- Fast queries
- Minimal storage
- Images hosted by ImgFlip (free)

**Storage Comparison:**
- 1000 memes with images: ~1-2GB (exceeded Mini limit!)
- 1000 memes with URLs: ~200KB (0.02% of limit!)

### Why Not Use Cloudinary?

For this workflow, Cloudinary is **optional** because:
- ImgFlip URLs are already public
- Instagram accepts ImgFlip URLs directly
- One less service to configure
- Simpler workflow
- Less API calls = faster execution

You can add Cloudinary later if needed for:
- Custom branding/watermarks
- Image transformations
- Better CDN performance

## 🚀 Advanced Features

### Add Analytics

```sql
-- Create analytics view
CREATE VIEW meme_analytics AS
SELECT 
  DATE(posted_at) as date,
  COUNT(*) as posts_count,
  SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful,
  COUNT(DISTINCT topic) as unique_topics
FROM meme_posts
GROUP BY DATE(posted_at)
ORDER BY date DESC;

-- Query analytics
SELECT * FROM meme_analytics LIMIT 30;
```

### Add Webhook for Notifications

Add a webhook node at the end to:
- Send Telegram notification on success
- Alert on failures
- Track daily statistics

### Schedule Reports

Create a separate workflow that:
- Runs once per week
- Queries PostgreSQL for stats
- Sends summary email

## 📚 Resources

- [Heroku Eco Dynos](https://www.heroku.com/pricing)
- [Heroku PostgreSQL](https://devcenter.heroku.com/articles/heroku-postgresql)
- [n8n PostgreSQL Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres/)
- [PostgreSQL Performance Tips](https://wiki.postgresql.org/wiki/Performance_Optimization)

---

**Created**: 2025-10-30  
**Version**: 1.0  
**Optimized for**: Heroku Eco Dyno + PostgreSQL Mini  
**Perfect for**: Low-cost automated content posting
