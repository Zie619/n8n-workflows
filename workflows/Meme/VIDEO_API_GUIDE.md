# Video Generation API Integration Guide

Complete guide for integrating video generation APIs (Replicate, Runway, Pika, Stability AI, and future Google Veo) for automated meme video creation.

## 🎬 Available Video APIs

### 1. Replicate (Recommended for Eco Dyno)

**Why Replicate:**
- ✅ Simple REST API
- ✅ Multiple video models available
- ✅ Pay per second of video ($0.006/sec)
- ✅ Free tier with credits
- ✅ No local processing needed
- ✅ Fast generation (10-30 seconds)

**Setup:**
```bash
# Sign up at https://replicate.com
# Get API token from dashboard

# Set environment variable
heroku config:set REPLICATE_API_TOKEN=r8_xxx -a your-app-name

# Optional: Set specific model version
heroku config:set REPLICATE_MODEL_VERSION=model_version_hash -a your-app-name
```

**Available Models on Replicate:**
- **Stable Video Diffusion** - Best for general use
- **Zeroscope v2** - Fast, good quality
- **AnimateDiff** - Animation style
- **Text2Video-Zero** - Text-based generation

**API Example:**
```bash
curl -X POST https://api.replicate.com/v1/predictions \
  -H "Authorization: Token $REPLICATE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "version": "3d2a62f9bcc9d32c63e8263bfa3cd790e1f42b9d9f55617d59a1e16f00fb2ea2",
    "input": {
      "prompt": "Person transforms from tired to energized after coffee",
      "num_frames": 75,
      "fps": 5
    }
  }'
```

**Cost Estimate:**
- 15-second video: ~$0.09
- 3 videos/day: $0.27/day
- Monthly: ~$8/month
- **Total with Heroku: $13/month**

### 2. Runway ML Gen-2

**Pros:**
- High-quality video generation
- Professional results
- Good for brand content

**Cons:**
- More expensive
- Slower generation
- Requires credits purchase

**Setup:**
```bash
# Sign up at https://runwayml.com
# Generate API key from settings

heroku config:set RUNWAY_API_KEY=your_key -a your-app-name
```

**API Endpoint:**
```bash
POST https://api.runwayml.com/v1/generate
Authorization: Bearer $RUNWAY_API_KEY
Content-Type: application/json

{
  "model": "gen2",
  "prompt": "Your video description",
  "duration": 4,
  "resolution": "720p"
}
```

**Cost:**
- ~$0.05 per second
- 15-second video: $0.75
- More expensive but higher quality

### 3. Pika Labs

**Status:** Limited API access

**Options:**
- Web automation (not recommended for Heroku)
- Wait for official API release
- Use Discord bot (complex setup)

**When Available:**
```bash
heroku config:set PIKA_API_KEY=your_key -a your-app-name
```

### 4. Stability AI - Stable Video Diffusion

**Available via Replicate** (already covered above)

**Direct API** (when available):
```bash
heroku config:set STABILITY_API_KEY=your_key -a your-app-name
```

**Pros:**
- Open source model
- Good quality
- Cost-effective via Replicate

### 5. Google Veo 2 / Veo 3 ⭐ RECOMMENDED FOR GOOGLE PRO USERS

**Status:** 
- Veo 2: Available in preview (with access request)
- Veo 3: Limited availability, check for access

**Your Advantage:**
- ✅ You have Google Pro account
- ✅ Access to Vertex AI
- ✅ May have included credits
- ✅ Highest quality results

**Setup:**
```bash
# Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com

# Set environment variables
heroku config:set GOOGLE_CLOUD_PROJECT=your-project -a your-app-name
heroku config:set GOOGLE_CLOUD_REGION=us-central1 -a your-app-name
heroku config:set GOOGLE_APPLICATION_CREDENTIALS_JSON='{"type":"service_account",...}' -a your-app-name
```

**Available Models:**
- **Veo 2** (veo-002): High-quality, 1080p, cinematic
- **Veo 3** (veo-003): Latest, superior quality (if available)

**API Endpoint:**
```bash
POST https://us-central1-aiplatform.googleapis.com/v1/projects/{project}/locations/us-central1/publishers/google/models/veo-002:predict

Authorization: Bearer $(gcloud auth print-access-token)
Content-Type: application/json

{
  "instances": [{
    "prompt": "Your detailed video description with camera movements, lighting, style",
    "parameters": {
      "aspectRatio": "9:16",
      "durationSeconds": 10,
      "quality": "high"
    }
  }]
}
```

**Cost Estimate:**
- Veo 2: ~$0.30 per video
- Veo 3: ~$0.50 per video (estimated)
- 3 videos/day: $27-45/month
- With Google Pro credits: May be significantly less

**Advantages:**
- Highest quality video generation
- Best prompt understanding
- Cinematic camera movements
- Professional lighting and color
- 1080p output
- Perfect for vertical (9:16) format

**See Complete Setup:** [GOOGLE_VEO_SETUP.md](./GOOGLE_VEO_SETUP.md)

### 6. Other Options

**HeyGen API** - Avatar videos
**D-ID** - Talking head videos  
**Synthesia** - Professional presentations
**Pictory AI** - Text to video

Most of these are more expensive and focused on specific use cases.

## 🔧 Workflow Configuration

### Environment Variables

```bash
# Required
heroku config:set REPLICATE_API_TOKEN=r8_xxx -a your-app-name
heroku config:set INSTAGRAM_USER_ID=your_id -a your-app-name
heroku config:set INSTAGRAM_ACCESS_TOKEN=your_token -a your-app-name

# Optional (for specific models)
heroku config:set REPLICATE_MODEL_VERSION=hash -a your-app-name
heroku config:set RUNWAY_API_KEY=key -a your-app-name
```

### PostgreSQL Schema

```sql
-- Create video posts table
CREATE TABLE IF NOT EXISTS meme_videos (
  id SERIAL PRIMARY KEY,
  topic VARCHAR(100),
  video_prompt TEXT,
  video_url TEXT,
  instagram_id VARCHAR(100),
  posted_at TIMESTAMP DEFAULT NOW(),
  success BOOLEAN DEFAULT TRUE,
  generation_time_seconds INTEGER,
  api_provider VARCHAR(50) DEFAULT 'replicate'
);

CREATE INDEX idx_meme_videos_posted_at ON meme_videos(posted_at DESC);
CREATE INDEX idx_meme_videos_topic ON meme_videos(topic);
```

Run this:
```bash
heroku pg:psql -a your-app-name < workflows/Meme/setup_video_postgres.sql
```

## 📊 Performance Comparison

| API | Generation Time | Cost/Video | Quality | Eco Dyno Safe |
|-----|----------------|------------|---------|---------------|
| **Replicate** | 10-30s | $0.09 | Good | ✅ Yes |
| Runway Gen-2 | 30-60s | $0.75 | Excellent | ✅ Yes |
| Pika Labs | 20-40s | TBD | Good | ⚠️ Limited |
| Stability AI | 15-30s | $0.10 | Good | ✅ Yes |
| Google Veo | TBD | $0.20 | Excellent | ✅ Expected |

**Recommendation for Eco Dyno:** Start with Replicate

## 🚀 Deployment Steps

### Step 1: Get Replicate API Token

1. Go to https://replicate.com
2. Sign up (GitHub login available)
3. Go to Account → API Tokens
4. Create new token
5. Copy token (starts with `r8_`)

### Step 2: Configure Heroku

```bash
# Set API token
heroku config:set REPLICATE_API_TOKEN=r8_your_token_here -a your-app-name

# Verify it's set
heroku config:get REPLICATE_API_TOKEN -a your-app-name
```

### Step 3: Setup Database

```bash
# Connect to PostgreSQL
heroku pg:psql -a your-app-name

# Create table
CREATE TABLE IF NOT EXISTS meme_videos (
  id SERIAL PRIMARY KEY,
  topic VARCHAR(100),
  video_prompt TEXT,
  video_url TEXT,
  instagram_id VARCHAR(100),
  posted_at TIMESTAMP DEFAULT NOW(),
  success BOOLEAN DEFAULT TRUE
);

# Verify
\dt meme_videos
\q
```

### Step 4: Import Workflow

1. Open n8n: `https://your-app-name.herokuapp.com`
2. Login
3. Import: `2058_Meme_Video_API_Instagram_Reels_Scheduled.json`
4. Configure PostgreSQL credentials
5. Activate workflow

### Step 5: Test

```bash
# Watch logs
heroku logs --tail -a your-app-name

# Check database after first run
heroku pg:psql -a your-app-name -c "SELECT * FROM meme_videos ORDER BY posted_at DESC LIMIT 3;"
```

## 🎨 Video Prompt Engineering

### Good Prompt Structure

```
[Action/Transformation] + [Visual Details] + [Text Overlay]
```

**Examples:**

```javascript
// Transformation
"Person transforms from zombie to energetic superhero after drinking coffee. Animated transformation with energy effects. Text: COFFEE POWER ACTIVATE"

// Comparison
"Split screen: Left side shows person typing code manually with frustrated expression. Right side shows same person relaxing while AI writes perfect code. Text overlay: CODING BEFORE vs AFTER AI"

// Reveal
"Camera zooms from professional Zoom background to reveal messy bedroom, person in pajamas. Text overlay: WORKING FROM HOME REALITY"

// Time-lapse
"Time-lapse of person starting work focused, gradually surrounded by distractions, ends scrolling social media. Text: PRODUCTIVITY JOURNEY"
```

### Prompt Tips

✅ **Do:**
- Be specific about actions
- Include emotional expressions
- Specify text overlays
- Keep under 300 characters
- Use clear visual descriptions

❌ **Don't:**
- Be too abstract
- Use complex scenarios
- Request multiple scenes (keep simple)
- Exceed model capabilities

## ⚡ Eco Dyno Optimization

### Why This Works on Shared CPU

1. **No Local Processing**
   - All video generation is external
   - No ffmpeg, no video encoding
   - No file downloads to dyno

2. **Async Waiting**
   - Wait nodes don't use CPU
   - Just polling API status
   - Lightweight HTTP requests

3. **Memory Efficient**
   - Only stores URLs, not videos
   - Small JSON payloads
   - Peak memory: ~150MB

### Workflow Timing

```
Total execution time: 25-45 seconds

Breakdown:
- Concept generation: 1s (CPU: 10ms)
- API call to Replicate: 2s
- Wait for generation: 10-30s (external, no CPU)
- Status check: 1s
- Instagram upload: 5-10s (external)
- Database insert: 1s (CPU: 20ms)

Total CPU used: ~50ms
Total memory: ~120MB
Eco Dyno: ✅ Perfect fit!
```

### Resource Monitoring

```bash
# Check execution logs
heroku logs --tail -a your-app-name | grep "video"

# Monitor database size
heroku pg:psql -a your-app-name -c "SELECT pg_size_pretty(pg_table_size('meme_videos'));"

# Check API usage
# View in Replicate dashboard
```

## 💰 Cost Breakdown

### Replicate Pricing

**Free Tier:**
- New accounts: $0 + free credits
- ~20-50 video generations free

**Paid:**
- $0.006 per second of video generated
- 15-second video: 15 × $0.006 = $0.09

**Monthly Estimate:**
- 3 videos/day × 30 days = 90 videos
- 90 × $0.09 = $8.10/month

**Total Cost:**
- Heroku Eco Dyno: $5/month
- Replicate API: $8/month
- **Total: $13/month** for automated video memes!

### Alternative: Stability AI via Replicate

- Slightly cheaper: $0.003/second
- 15s video: $0.045
- 90 videos/month: $4.05
- **Total with Heroku: $9/month**

## 🔄 Switching Video APIs

### From Replicate to Runway

```javascript
// In "Create Video" node:

// OLD (Replicate)
{
  url: "https://api.replicate.com/v1/predictions",
  headers: { Authorization: "Token $REPLICATE_API_TOKEN" },
  body: { 
    version: "model_version",
    input: { prompt: $json.video_prompt }
  }
}

// NEW (Runway)
{
  url: "https://api.runwayml.com/v1/generate",
  headers: { Authorization: "Bearer $RUNWAY_API_KEY" },
  body: {
    model: "gen2",
    prompt: $json.video_prompt,
    duration: 4
  }
}
```

### Adding Google Veo (when available)

```javascript
// Add new node: "Create Video (Google Veo)"
{
  url: "https://us-central1-aiplatform.googleapis.com/v1/projects/{project}/locations/us-central1/publishers/google/models/veo-2:predict",
  authentication: "oAuth2",
  body: {
    instances: [{
      prompt: $json.video_prompt,
      duration_seconds: 15
    }]
  }
}
```

## 🐛 Troubleshooting

### Video Generation Fails

**Check API token:**
```bash
heroku config:get REPLICATE_API_TOKEN -a your-app-name
# Should start with r8_
```

**Test API manually:**
```bash
curl -X POST https://api.replicate.com/v1/predictions \
  -H "Authorization: Token $REPLICATE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"version":"3d2a62f9bcc9d32c63e8263bfa3cd790e1f42b9d9f55617d59a1e16f00fb2ea2","input":{"prompt":"test video"}}'
```

### Video Takes Too Long

**Issue:** Generation exceeds 30s Heroku timeout

**Solutions:**
1. Use faster model (Zeroscope)
2. Reduce video duration (10s instead of 15s)
3. Add retry logic (already in workflow)

**Check timing:**
```bash
heroku logs --tail -a your-app-name | grep "duration"
```

### Instagram Upload Fails

**Video too large:**
- Instagram Reels max: 100MB
- Replicate videos: Usually 5-15MB ✅
- Should work fine

**Video format issue:**
- Ensure MP4 format
- Vertical aspect ratio preferred (9:16)
- Minimum 720p resolution

### Out of Credits

**Replicate:**
- Check dashboard: https://replicate.com/account
- Add payment method
- Set budget alerts

## 📈 Scaling Tips

### Increase Posting Frequency

```javascript
// In Schedule Trigger node:
hoursInterval: 6  // 4 videos/day
hoursInterval: 4  // 6 videos/day
hoursInterval: 3  // 8 videos/day
```

**Cost Impact:**
- 6 videos/day: $16/month (API)
- 8 videos/day: $22/month (API)
- Still under Instagram limit (25 Reels/day)

### Multi-Platform

Add nodes for:
- YouTube Shorts (same video URL)
- TikTok (requires different API)
- Twitter/X video posts

### Batch Generation

Generate multiple videos in one execution:
```javascript
// In Generate Concept node:
return [
  {topic: 'ai', prompt: '...'},
  {topic: 'coffee', prompt: '...'},
  {topic: 'coding', prompt: '...'}
];
// Workflow will process all 3
```

## 🔮 Future: Google Veo Integration

**When Veo API is Available:**

1. **Update Environment Variables:**
```bash
heroku config:set GOOGLE_CLOUD_PROJECT=your-project -a your-app
heroku config:set GOOGLE_VEO_API_KEY=your-key -a your-app
```

2. **Add Veo Node:**
- Duplicate "Create Video" node
- Update API endpoint
- Update authentication
- Switch between APIs based on quality needs

3. **Expected Benefits:**
- Higher quality videos
- Better prompt understanding
- More realistic results
- Potentially faster generation

**We'll update this guide when Veo API is publicly available!**

## 📚 Resources

- [Replicate API Docs](https://replicate.com/docs)
- [Runway ML Docs](https://docs.runwayml.com)
- [Instagram Reels API](https://developers.facebook.com/docs/instagram-api/guides/reels)
- [Stable Video Diffusion](https://stability.ai/stable-video)
- [n8n HTTP Request Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)

---

**Created:** 2025-10-30  
**Version:** 1.0  
**Optimized for:** Heroku Eco Dyno + Video APIs  
**Cost:** ~$13/month total for automated video memes
