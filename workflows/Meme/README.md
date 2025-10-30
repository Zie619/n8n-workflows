# Automated Meme Creation & Publishing Workflow

This workflow automates the creation and publishing of memes to multiple social media platforms, optimized specifically for deployment on Heroku's free/hobby tier.

## 🎯 What These Workflows Do

### Image Memes (Workflows 2055-2057)
1. **Generates** meme concepts automatically using predefined topics
2. **Creates** meme images using ImgFlip API (free tier)
3. **Hosts** images on Cloudinary CDN (optional, free tier)
4. **Publishes** to Instagram feed automatically
5. **Runs** every 6-12 hours (2-4 posts per day)

### Video Memes (Workflows 2058-2061) 🎬 NEW!
1. **Generates** video meme concepts with AI-optimized prompts
2. **Creates** short videos using external APIs (Replicate, Runway ML, Google Veo 2/3)
3. **No local processing** - all video generation happens via API
4. **Publishes** to Instagram Reels, YouTube Shorts, and/or TikTok
5. **Backs up** to Google Drive (2TB available!) - Workflow 2061 📦
6. **Runs** every 8 hours (3 video posts per day)
7. **Cost**: ~$13-32/month total (Heroku + API costs)

### Google Drive Backup (Workflow 2061) 📦 NEW!
1. **Automatic backup** of every generated video to Google Drive
2. **2TB storage** = ~200,000 videos = 182 years of daily posting!
3. **Organized folders** by topic (AI, Comedy, Lifestyle, etc.)
4. **Permanent archive** - recover deleted content anytime
5. **Zero cost** - included with your Google account
6. **No performance impact** - only +5-8 seconds per execution

## 🏗️ Why Heroku-Optimized?

This workflow is specifically designed for Heroku's limitations:

- **Memory Efficient**: Uses < 200MB RAM (Free tier: 512MB, Eco tier: 512MB)
- **Fast Execution**: Completes in < 25 seconds (Heroku timeout: 30s)
- **No Local Storage**: All files hosted externally (Heroku ephemeral filesystem)
- **Minimal CPU**: Simple operations, perfect for shared CPU (Eco dyno)
- **Free APIs**: All services have generous free tiers
- **PostgreSQL Ready**: Optional database integration for tracking and deduplication

### Recommended Setup by Heroku Tier

| Tier | Workflow | Frequency | Features |
|------|----------|-----------|----------|
| **Free** | 2056 (Minimal) | 1x/day | Basic posting |
| **Eco** | 2057 (PostgreSQL) | 4x/day | Full tracking, dedup |
| **Hobby** | 2055 (Full) | 4-6x/day | Cloudinary, advanced |

## 📁 Files in This Directory

### Workflows
- **2055_Meme_Instagram_Automation_Scheduled.json** - Full-featured workflow with Cloudinary
- **2056_Meme_Instagram_Minimal_Scheduled.json** - Ultra-minimal workflow (5 nodes only)
- **2057_Meme_Instagram_EcoDyno_PostgreSQL_Scheduled.json** - **RECOMMENDED** for Eco Dyno with PostgreSQL
- **2058_Meme_Video_API_Instagram_Reels_Scheduled.json** - 🎬 Video generation with Replicate API
- **2059_Meme_Video_GoogleVeo_MultiAPI_Scheduled.json** - 🎬 Video with Google Veo 2/3 + fallback
- **2060_Meme_Video_MultiPlatform_All_Scheduled.json** - 🚀 Posts to Instagram + YouTube Shorts + TikTok
- **2061_Meme_Video_MultiPlatform_GoogleDrive_Scheduled.json** - 📦 **NEW!** Multi-platform + Google Drive backup (2TB storage!)

### Documentation
- **README.md** - This file (overview and quick start)
- **QUICK_REFERENCE.md** - One-page cheat sheet for common tasks
- **HEROKU_DEPLOYMENT.md** - Complete deployment guide for Heroku Free/Hobby tier
- **HEROKU_CLI_GUIDE.md** - Step-by-step CLI deployment guide (in Spanish)
- **ECO_DYNO_POSTGRES_GUIDE.md** - Specific guide for Eco Dyno + PostgreSQL setup
- **VIDEO_API_GUIDE.md** - 🎬 Complete guide for video generation APIs
- **GOOGLE_VEO_SETUP.md** - 🎬 Google Veo 2/3 setup for Google Pro users
- **MULTIPLATFORM_GUIDE.md** - 🚀 Setup for YouTube Shorts + TikTok posting
- **GOOGLE_DRIVE_SETUP.md** - 📦 **NEW!** Google Drive backup setup (2TB storage!)
- **.env.example** - Environment variables template
- **setup_postgres.sql** - PostgreSQL database setup script (for image memes)
- **setup_video_postgres.sql** - 🎬 PostgreSQL setup for video memes
- **setup_multiplatform_postgres.sql** - 🚀 PostgreSQL for multi-platform tracking
- **setup_gdrive_postgres.sql** - 📦 **NEW!** PostgreSQL for Google Drive backup tracking
- **validate.sh** - Validation script for pre-deployment checks
- **deploy-heroku.sh** - Interactive deployment helper script

## 🚀 Quick Start

### Prerequisites

1. Heroku account (free tier works)
2. n8n instance running on Heroku
3. ImgFlip account (free)
4. Cloudinary account (free) - only for workflow 2055
5. Instagram Business account

### Installation Options

#### Option 1: Automated Script (Recommended)
```bash
# Make script executable
chmod +x workflows/Meme/deploy-heroku.sh

# Run interactive deployment
./workflows/Meme/deploy-heroku.sh

# Follow the prompts - it will:
# - Create Heroku app
# - Add PostgreSQL
# - Configure environment variables
# - Deploy n8n
# - Setup database
```

#### Option 2: Heroku CLI (Manual)
See complete guide: [HEROKU_CLI_GUIDE.md](./HEROKU_CLI_GUIDE.md)

```bash
# Quick version:
heroku create your-meme-bot
heroku addons:create heroku-postgresql:mini -a your-meme-bot
heroku config:set IMGFLIP_USERNAME=xxx IMGFLIP_PASSWORD=xxx -a your-meme-bot
# ... (see full guide for all variables)
git clone https://github.com/n8n-io/n8n-heroku.git
cd n8n-heroku && heroku git:remote -a your-meme-bot
git push heroku main
heroku ps:scale web=1:eco -a your-meme-bot
```

#### Option 3: Heroku Web UI
See: [HEROKU_DEPLOYMENT.md](./HEROKU_DEPLOYMENT.md)

### Post-Installation

```bash
# 1. Import workflow to your n8n instance
# Download: 2057_Meme_Instagram_EcoDyno_PostgreSQL_Scheduled.json
# In n8n: Workflows → Import from File

# 2. Configure PostgreSQL credentials in n8n UI
# Get DATABASE_URL: heroku config:get DATABASE_URL -a your-app
# In n8n: Credentials → New → Postgres

# 3. Activate workflow
# Toggle "Active" in the workflow editor

# 4. Monitor
heroku logs --tail -a your-app
```

For detailed instructions, see [HEROKU_CLI_GUIDE.md](./HEROKU_CLI_GUIDE.md)

## 🎨 Features

### Current Implementation

✅ Automated meme generation every 12 hours  
✅ Multiple meme templates (Drake, Two Buttons, etc.)  
✅ Random topic selection (coding, work, coffee, etc.)  
✅ Instagram feed posting  
✅ Hashtag generation  
✅ Error handling and logging  
✅ Heroku-optimized (low memory, fast execution)  

### Platforms Supported

- ✅ **Instagram** - Fully implemented (posts to feed)
- 🔄 **YouTube Shorts** - Requires video conversion (commented out)
- ⚠️ **TikTok** - Not recommended for free tier (too memory-intensive)

### Free Tier Limits

| Service | Free Tier Limit | Usage |
|---------|----------------|-------|
| ImgFlip | 100 requests/day | 2 per day (1%) |
| Cloudinary | 25GB bandwidth/month | ~5MB per day (0.6%) |
| Instagram | 25 posts/day | 2 per day (8%) |
| Heroku | 550-1000 dyno hours | ~2 hours/day (8%) |

**Result**: Can run indefinitely on free tiers! 🎉

## 🔧 Customization

### Change Posting Frequency

Edit the "Schedule Trigger" node:

```javascript
// Current: Every 12 hours
interval: 12

// Options:
// - Every 6 hours: 4 posts/day
// - Every 8 hours: 3 posts/day
// - Every 24 hours: 1 post/day
```

### Add Custom Topics

Edit the "Generate Meme Concept" node:

```javascript
const topics = [
  'coding', 'remote work', 'monday', 'coffee', 'deadline',
  // Add yours here:
  'crypto', 'gaming', 'fitness', 'travel', 'food'
];
```

### Use Different Meme Templates

Popular ImgFlip template IDs:

```javascript
const templates = [
  '181913649', // Drake Hotline Bling
  '87743020',  // Two Buttons
  '101470',    // Ancient Aliens
  '438680',    // Batman Slapping Robin
  '112126428', // Distracted Boyfriend
  '217743513', // UNO Draw 25 Cards
  '129242436', // Change My Mind
];
```

Find more at: https://imgflip.com/memetemplates

### Customize Captions

Edit the "Prepare Post Data" node:

```javascript
caption: `${text0} vs ${text1} 😄

${hashtags}

Follow for more memes! 🔥`
```

## 📊 Architecture

### Workflow Flow

```
Schedule (12h) → Generate Concept → Create Meme (ImgFlip)
                                          ↓
                                    Check Success
                                          ↓
                                   Prepare Data
                                          ↓
                                Upload (Cloudinary)
                                          ↓
                        Instagram: Create → Publish → Summary
```

### Memory Optimization

- **No file downloads**: Only URL references
- **Streaming**: Data passes through without storage
- **External processing**: All heavy work done by APIs
- **Minimal state**: Stateless execution

### Performance

| Phase | Time | Memory |
|-------|------|--------|
| Concept Generation | < 1s | 10MB |
| ImgFlip API | 2-5s | 20MB |
| Cloudinary Upload | 3-8s | 30MB |
| Instagram Post | 4-10s | 40MB |
| **Total** | **15-25s** | **~150MB** |

## 🔍 Monitoring

### Check Workflow Status

In n8n:
- Go to **Executions** tab
- View recent runs
- Check success/failure rate

### View Logs

```bash
# Heroku logs
heroku logs --tail -a your-app-name

# Filter for n8n
heroku logs --tail -a your-app-name | grep n8n
```

### Monitor API Usage

1. **ImgFlip**: https://imgflip.com/account
2. **Cloudinary**: https://cloudinary.com/console
3. **Instagram**: Facebook Graph API Explorer

## ⚠️ Troubleshooting

### Workflow Doesn't Run

**Check:**
1. Is workflow activated? (toggle in top right)
2. Are dyno hours remaining? `heroku ps -a your-app`
3. Is n8n instance running? Check Heroku dashboard

### Meme Generation Fails

**Check:**
1. ImgFlip credentials correct?
2. API limit reached? (100/day)
3. Check execution logs for error details

### Instagram Post Fails

**Check:**
1. Access token expired? (valid for 60 days)
2. Rate limit reached? (25 posts/day)
3. Image URL publicly accessible?
4. Instagram account is Business account?

### Out of Memory Error

**Solutions:**
1. Upgrade to Hobby dyno ($7/month)
2. Reduce concurrent operations
3. Check for memory leaks in custom code

## 🔐 Security

### Best Practices

✅ Use environment variables for all credentials  
✅ Enable basic auth on n8n  
✅ Use HTTPS for all webhooks  
✅ Rotate Instagram tokens every 60 days  
✅ Monitor API usage for anomalies  

❌ Never commit credentials to git  
❌ Don't share access tokens publicly  
❌ Don't disable basic auth in production  

### Credential Storage

All credentials should be stored as Heroku config vars:

```bash
heroku config:set KEY=value -a your-app
```

Access in workflow using: `{{ $env.KEY }}`

## 📈 Scaling

### Current Setup (Free/Hobby)
- 2 posts per day
- 100% automated
- ~$0-7/month
- Good for personal use

### Scale Up Options

**More Posts:**
- Reduce interval to 6 hours → 4 posts/day
- Stay within free tier limits

**More Platforms:**
- Add YouTube Shorts (requires video conversion)
- Add Twitter/X (requires API access)
- Add Facebook Pages

**More Reliability:**
- Upgrade to Standard dyno ($25/month)
- Add monitoring (Sentry, Datadog)
- Implement retry logic

## 🤝 Contributing

Improvements welcome! Ideas:

- [ ] Add AI-generated meme text (GPT-3.5 API)
- [ ] Support for video memes
- [ ] Multi-language support
- [ ] Analytics dashboard
- [ ] A/B testing for meme formats
- [ ] Scheduling specific times
- [ ] Content moderation

## 📚 Resources

- [ImgFlip API Documentation](https://imgflip.com/api)
- [Cloudinary Documentation](https://cloudinary.com/documentation)
- [Instagram Graph API](https://developers.facebook.com/docs/instagram-api)
- [n8n Documentation](https://docs.n8n.io/)
- [Heroku Dev Center](https://devcenter.heroku.com/)

## 📄 License

Part of the n8n-workflows repository. Use freely for your projects!

## 📞 Support

- **Issues**: Open an issue in the repository
- **n8n Help**: https://community.n8n.io/
- **Heroku Help**: https://help.heroku.com/

---

**Version**: 1.0  
**Created**: 2025-10-30  
**Optimized for**: Heroku Free/Hobby Tier  
**Tested with**: n8n 1.0+

Happy meme automation! 🎉😄
