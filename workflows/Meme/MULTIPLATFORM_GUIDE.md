# Multi-Platform Publishing Guide
## Instagram Reels + YouTube Shorts + TikTok

Complete guide for posting AI-generated video memes to all three major short-form video platforms simultaneously.

## 🎯 Overview

**Workflow 2060** automates posting to:
- ✅ Instagram Reels
- ✅ YouTube Shorts  
- ✅ TikTok

**Benefits:**
- 3x exposure from same video
- Diversified audience reach
- Maximum viral potential
- Algorithm advantages on each platform

## 📋 Prerequisites

### Required Accounts

1. **Instagram Business Account** (already have)
2. **YouTube Channel** with monetization/Shorts access
3. **TikTok Creator/Business Account**
4. **TikTok Developer Account** (requires approval)

### API Access Needed

- Instagram Graph API ✅ (you have this)
- YouTube Data API v3
- TikTok Content Posting API

## 🔧 Setup Instructions

### Part 1: YouTube Shorts Setup

#### Step 1: Create Google Cloud Project (if not done for Veo)

```bash
# If you already have project for Veo, use same one
gcloud config get-value project

# Or create new
gcloud projects create meme-automation-multiplatform
gcloud config set project meme-automation-multiplatform
```

#### Step 2: Enable YouTube Data API v3

```bash
# Enable API
gcloud services enable youtube.googleapis.com

# Via Console:
# 1. Go to https://console.cloud.google.com/apis/library
# 2. Search "YouTube Data API v3"
# 3. Click Enable
```

#### Step 3: Create OAuth 2.0 Credentials for YouTube

```bash
# Via Cloud Console (recommended):
# 1. Go to APIs & Services → Credentials
# 2. Create Credentials → OAuth 2.0 Client ID
# 3. Application type: Web application
# 4. Authorized redirect URIs: https://your-n8n-app.herokuapp.com/rest/oauth2-credential/callback
# 5. Note Client ID and Client Secret
```

#### Step 4: Configure YouTube OAuth in n8n

In n8n UI:
1. **Credentials** → **New**
2. Select **YouTube OAuth2 API**
3. Enter Client ID and Client Secret
4. Add scopes:
   - `https://www.googleapis.com/auth/youtube.upload`
   - `https://www.googleapis.com/auth/youtube`
5. Click **Connect my account**
6. Authorize access to your YouTube channel
7. Save as "YouTube Shorts Account"

#### Step 5: Test YouTube Upload

```bash
# Test with curl
ACCESS_TOKEN="your_youtube_oauth_token"

curl -X POST "https://www.googleapis.com/upload/youtube/v3/videos?part=snippet,status" \
  -H "Authorization: ******" \
  -H "Content-Type: application/json" \
  -d '{
    "snippet": {
      "title": "Test Short #Shorts",
      "description": "Test video",
      "tags": ["test", "shorts"],
      "categoryId": "23"
    },
    "status": {
      "privacyStatus": "unlisted",
      "selfDeclaredMadeForKids": false
    }
  }'
```

**Note:** YouTube auto-detects Shorts for vertical videos under 60 seconds.

### Part 2: TikTok Setup

#### Step 1: Apply for TikTok Developer Account

1. Go to https://developers.tiktok.com
2. Sign up with your TikTok creator account
3. Create new app:
   - App name: "Meme Automation"
   - Category: "Content Creation"
   - Description: "Automated video posting"
4. Wait for approval (can take 1-7 days)

#### Step 2: Get TikTok API Credentials

Once approved:
1. Go to your app dashboard
2. Navigate to **Content Posting API**
3. Request access to Content Posting API
4. Note your:
   - Client Key
   - Client Secret
   - Redirect URI

#### Step 3: Generate Access Token

TikTok uses OAuth 2.0:

```bash
# Authorization URL
https://www.tiktok.com/v2/auth/authorize/?client_key={CLIENT_KEY}&scope=user.info.basic,video.upload,video.publish&response_type=code&redirect_uri={REDIRECT_URI}&state=random_state

# Exchange code for token
curl -X POST "https://open.tiktokapis.com/v2/oauth/token/" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_key={CLIENT_KEY}" \
  -d "client_secret={CLIENT_SECRET}" \
  -d "code={AUTH_CODE}" \
  -d "grant_type=authorization_code" \
  -d "redirect_uri={REDIRECT_URI}"
```

#### Step 4: Configure TikTok in n8n

```javascript
// Option 1: Generic OAuth2 in n8n
// Credentials → New → OAuth2 API
{
  "authUrl": "https://www.tiktok.com/v2/auth/authorize/",
  "accessTokenUrl": "https://open.tiktokapis.com/v2/oauth/token/",
  "clientId": "your_client_key",
  "clientSecret": "your_client_secret",
  "scope": "user.info.basic,video.upload,video.publish"
}

// Option 2: Set as environment variable
heroku config:set TIKTOK_ACCESS_TOKEN=your_token -a your-app-name
```

#### Step 5: Test TikTok Upload

```bash
# Initialize upload
curl -X POST "https://open.tiktokapis.com/v2/post/publish/video/init/" \
  -H "Authorization: ******" \
  -H "Content-Type: application/json" \
  -d '{
    "post_info": {
      "title": "Test video",
      "privacy_level": "SELF_ONLY",
      "disable_duet": false,
      "disable_comment": false,
      "disable_stitch": false
    },
    "source_info": {
      "source": "PULL_FROM_URL",
      "video_url": "https://example.com/video.mp4"
    }
  }'
```

### Part 3: Heroku Environment Configuration

```bash
# YouTube (if not using OAuth2 in n8n)
heroku config:set YOUTUBE_CLIENT_ID=your_client_id -a your-app-name
heroku config:set YOUTUBE_CLIENT_SECRET=your_client_secret -a your-app-name
heroku config:set YOUTUBE_ACCESS_TOKEN=your_access_token -a your-app-name
heroku config:set YOUTUBE_REFRESH_TOKEN=your_refresh_token -a your-app-name

# TikTok
heroku config:set TIKTOK_CLIENT_KEY=your_client_key -a your-app-name
heroku config:set TIKTOK_CLIENT_SECRET=your_client_secret -a your-app-name
heroku config:set TIKTOK_ACCESS_TOKEN=your_access_token -a your-app-name

# Verify all set
heroku config -a your-app-name | grep -E "YOUTUBE|TIKTOK"
```

### Part 4: Database Setup

```bash
# Connect to PostgreSQL
heroku pg:psql -a your-app-name

# Create multi-platform table
CREATE TABLE IF NOT EXISTS meme_videos_multiplatform (
  id SERIAL PRIMARY KEY,
  topic VARCHAR(100),
  video_prompt TEXT,
  video_url TEXT,
  instagram_id VARCHAR(100),
  youtube_id VARCHAR(100),
  tiktok_id VARCHAR(100),
  api_provider VARCHAR(50),
  posted_at TIMESTAMP DEFAULT NOW(),
  success BOOLEAN DEFAULT TRUE
);

CREATE INDEX idx_multiplatform_posted_at ON meme_videos_multiplatform(posted_at DESC);

\dt
\q
```

### Part 5: Import and Activate Workflow

1. Download `2060_Meme_Video_MultiPlatform_All_Scheduled.json`
2. In n8n: **Workflows** → **Import from File**
3. Configure credentials:
   - PostgreSQL (existing)
   - YouTube OAuth2 (new)
   - TikTok OAuth2 (new)
4. Test with manual execution
5. Activate workflow

## 📊 Platform-Specific Considerations

### Instagram Reels

**Format:**
- Aspect ratio: 9:16 (vertical)
- Duration: 3-90 seconds
- Max size: 100MB
- Format: MP4

**Best Practices:**
- Use trending audio (if adding)
- Hashtags: 20-30 optimal
- Post during peak hours (your audience timezone)
- Engage with comments quickly

**Rate Limits:**
- 25 Reels per day
- This workflow: 3 per day ✅

### YouTube Shorts

**Format:**
- Aspect ratio: 9:16 (vertical)
- Duration: Up to 60 seconds
- Max size: 256GB (but we use URLs)
- Format: MP4, MOV, AVI, FLV, WMV

**Auto-Detection:**
- Shorts automatically detected for:
  - Vertical videos (9:16)
  - Under 60 seconds
  - Title or description contains #Shorts

**Best Practices:**
- Include #Shorts in title
- Hook in first 3 seconds
- Clear CTA at end
- Optimize thumbnail (first frame)

**Rate Limits:**
- Quota: 10,000 units/day
- Upload costs: 1600 units
- This workflow: 3 uploads = 4800 units ✅

### TikTok

**Format:**
- Aspect ratio: 9:16 (vertical) or 1:1
- Duration: 15-60 seconds (up to 10 min for some accounts)
- Max size: 4GB
- Format: MP4, WebM, MOV

**Best Practices:**
- Use trending sounds
- Hook within 2 seconds
- Text overlays for engagement
- Hashtag strategy: 3-5 relevant tags

**Rate Limits:**
- Content Posting API: Varies by approval level
- Typical: 10-20 posts per day
- This workflow: 3 per day ✅

**Special Considerations:**
- Requires TikTok Developer approval
- API access may have waiting period
- Some regions have restrictions

## ⚡ Performance & Optimization

### Execution Flow

```
1. Generate video (Veo/Replicate): 15-40s
2. Get video URL: instant
3. Parallel uploads:
   ├─ Instagram: 5-10s
   ├─ YouTube: 10-15s
   └─ TikTok: 10-15s
4. Save to database: 1s

Total: 35-60 seconds
```

### Eco Dyno Safety

**Memory Usage:**
- Video generation: 120-150MB
- Parallel uploads: +30MB
- Total peak: ~180MB
- ✅ Well under 512MB limit

**CPU Usage:**
- Concept generation: 20ms
- API calls: External (no CPU)
- Database insert: 10ms
- Total: < 50ms CPU
- ✅ Perfect for shared CPU

**Execution Time:**
- Target: < 60 seconds
- Typical: 40-55 seconds
- ✅ Under Heroku timeout

### Cost Analysis

**APIs:**
- Video generation (Veo 2): $0.30/video
- Instagram: Free
- YouTube: Free (quota included)
- TikTok: Free

**Monthly Cost (3 videos/day):**
- Heroku Eco: $5/month
- Video API: $27/month (3/day × 30 days × $0.30)
- **Total: $32/month**

**Reach multiplier:**
- Same $32, 3x platforms
- Cost per platform: ~$11/month
- Excellent ROI for multi-platform presence

## 🎨 Content Optimization by Platform

### Platform-Specific Formatting

Workflow automatically formats content for each platform:

```javascript
// Instagram
const instagramCaption = `${description}\n\n#${tags.join(' #')} #viral #reels`;

// YouTube
const youtubeTitle = `${title} #Shorts`;
const youtubeDescription = `${description}\n\n${tags.map(t => '#' + t).join(' ')}\n\nSubscribe for more!`;

// TikTok  
const tiktokCaption = `${description} ${tags.map(t => '#' + t).join(' ')}`;
```

### Customization

Edit the "Generate Multi-Platform Content" node:

```javascript
{
  topic: 'your_topic',
  prompt: 'Video generation prompt',
  title: 'Engaging Title',
  description: 'Short description',
  tags: ['tag1', 'tag2', 'tag3'],
  // ... rest of config
}
```

## 🐛 Troubleshooting

### YouTube Upload Fails

**Error: Insufficient permissions**
```bash
# Fix: Add required scopes
# In n8n OAuth2 credentials, ensure these scopes:
https://www.googleapis.com/auth/youtube.upload
https://www.googleapis.com/auth/youtube
```

**Error: Quota exceeded**
```bash
# Check quota usage
# Go to: https://console.cloud.google.com/apis/api/youtube.googleapis.com/quotas
# Default: 10,000 units/day
# Each upload: 1600 units
# Solution: Reduce posting frequency or request quota increase
```

**Shorts not showing in Shorts feed**
- Ensure video is vertical (9:16)
- Duration must be < 60 seconds
- Add #Shorts to title
- Wait 24-48 hours for indexing

### TikTok Upload Fails

**Error: Developer account not approved**
```bash
# Solution: Wait for TikTok approval
# Typical: 1-7 days
# Meanwhile: Use workflow 2058 or 2059 (Instagram only)
```

**Error: Invalid access token**
```bash
# TikTok tokens expire
# Refresh token:
curl -X POST "https://open.tiktokapis.com/v2/oauth/token/" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_key={CLIENT_KEY}" \
  -d "client_secret={CLIENT_SECRET}" \
  -d "grant_type=refresh_token" \
  -d "refresh_token={REFRESH_TOKEN}"
```

**Error: Video processing failed**
- Check video format (MP4 recommended)
- Ensure vertical orientation
- Verify duration < 60 seconds
- Check file size < 100MB

### General Issues

**Workflow times out**
```bash
# Solution 1: Increase individual node timeouts
# In HTTP Request nodes, set timeout to 30000ms

# Solution 2: Remove TikTok temporarily
# If TikTok is slowest, post to it separately

# Solution 3: Sequential instead of parallel
# Change workflow to post one platform at a time
```

**Database errors**
```bash
# Verify table exists
heroku pg:psql -a your-app-name -c "\d meme_videos_multiplatform"

# Recreate if needed
heroku pg:psql -a your-app-name < workflows/Meme/setup_multiplatform_postgres.sql
```

## 📈 Monitoring & Analytics

### Track Performance

```sql
-- View recent posts
SELECT * FROM meme_videos_multiplatform 
ORDER BY posted_at DESC LIMIT 10;

-- Success rate by platform
SELECT 
  COUNT(*) as total,
  COUNT(instagram_id) as instagram_success,
  COUNT(youtube_id) as youtube_success,
  COUNT(tiktok_id) as tiktok_success
FROM meme_videos_multiplatform
WHERE posted_at > NOW() - INTERVAL '30 days';

-- Most successful topics
SELECT topic, COUNT(*) as posts
FROM meme_videos_multiplatform
WHERE posted_at > NOW() - INTERVAL '30 days'
GROUP BY topic
ORDER BY posts DESC;
```

### Platform Analytics

**Instagram:**
- Check Instagram Insights for Reels
- Track reach, engagement, shares

**YouTube:**
- YouTube Studio → Analytics → Shorts
- Monitor views, watch time, CTR

**TikTok:**
- TikTok Analytics (Creator account)
- Track views, likes, shares, comments

## 🚀 Scaling Strategies

### Increase Frequency

```javascript
// In Schedule Trigger node:
hoursInterval: 6  // 4 posts/day
hoursInterval: 4  // 6 posts/day

// Cost impact:
// 4 posts/day: $36/month
// 6 posts/day: $54/month
```

### Add More Platforms

Future expansions:
- Facebook Reels (similar to Instagram)
- Twitter/X Video
- LinkedIn Video
- Pinterest Video Pins

### A/B Testing

Create multiple workflows:
- Different video styles
- Different prompts
- Different posting times
- Track which performs best

## 📚 API Documentation

- [YouTube Data API v3](https://developers.google.com/youtube/v3/docs)
- [TikTok Content Posting API](https://developers.tiktok.com/doc/content-posting-api-get-started)
- [Instagram Graph API](https://developers.facebook.com/docs/instagram-api)

---

**Created:** 2025-10-30  
**Version:** 1.0  
**For:** Multi-platform automated video posting  
**Cost:** ~$32/month for 3 platforms
