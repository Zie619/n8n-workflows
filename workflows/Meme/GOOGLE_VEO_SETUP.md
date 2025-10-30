# Google Veo 2/3 Setup Guide for n8n

Complete setup guide for integrating Google Veo 2 and Veo 3 video generation with your n8n meme automation workflow.

## 🎯 Prerequisites

### What You Need
- ✅ Google Pro account (you have this!)
- ✅ Google Cloud Project
- ✅ Vertex AI API enabled
- ✅ Service Account with permissions
- ✅ Billing enabled (Google Pro credits apply)

## 📋 Step-by-Step Setup

### Step 1: Create Google Cloud Project

```bash
# Using gcloud CLI (or use Cloud Console)
gcloud projects create meme-automation-veo --name="Meme Automation"

# Set as active project
gcloud config set project meme-automation-veo

# Get project ID
gcloud config get-value project
```

**Via Cloud Console:**
1. Go to https://console.cloud.google.com
2. Click "Select a project" → "New Project"
3. Name: "Meme Automation Veo"
4. Click "Create"
5. Note your Project ID

### Step 2: Enable Vertex AI API

```bash
# Enable required APIs
gcloud services enable aiplatform.googleapis.com
gcloud services enable compute.googleapis.com
gcloud services enable storage.googleapis.com
```

**Via Cloud Console:**
1. Go to **APIs & Services** → **Library**
2. Search for "Vertex AI API"
3. Click **Enable**
4. Search for "Cloud Storage API"
5. Click **Enable**

### Step 3: Create Service Account

```bash
# Create service account
gcloud iam service-accounts create n8n-veo-service \
    --display-name="n8n Veo Service Account" \
    --description="Service account for n8n video generation"

# Get service account email
SA_EMAIL=$(gcloud iam service-accounts list \
    --filter="displayName:n8n Veo Service Account" \
    --format="value(email)")

echo $SA_EMAIL
# Should be: n8n-veo-service@your-project-id.iam.gserviceaccount.com
```

### Step 4: Grant Permissions

```bash
# Grant Vertex AI User role
gcloud projects add-iam-policy-binding meme-automation-veo \
    --member="serviceAccount:${SA_EMAIL}" \
    --role="roles/aiplatform.user"

# Grant Storage Admin (for video output)
gcloud projects add-iam-policy-binding meme-automation-veo \
    --member="serviceAccount:${SA_EMAIL}" \
    --role="roles/storage.admin"

# Verify permissions
gcloud projects get-iam-policy meme-automation-veo \
    --flatten="bindings[].members" \
    --filter="bindings.members:${SA_EMAIL}"
```

### Step 5: Create and Download Key

```bash
# Create JSON key
gcloud iam service-accounts keys create ~/veo-key.json \
    --iam-account=${SA_EMAIL}

# View key (be careful - this is sensitive!)
cat ~/veo-key.json

# The output will be JSON like:
# {
#   "type": "service_account",
#   "project_id": "your-project",
#   "private_key_id": "...",
#   "private_key": "-----BEGIN PRIVATE KEY-----\n...",
#   "client_email": "n8n-veo-service@...",
#   ...
# }
```

### Step 6: Check Veo Model Availability

```bash
# List available models in Vertex AI
gcloud ai models list \
    --region=us-central1 \
    --filter="displayName:veo"

# Or check via API
curl -X GET \
  "https://us-central1-aiplatform.googleapis.com/v1/projects/$(gcloud config get-value project)/locations/us-central1/models" \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  | grep -i veo
```

**Note:** Veo 2 is currently in preview. Veo 3 availability may be limited. If not listed, you may need to:
1. Request access via Google Cloud Console
2. Join waitlist for Veo preview
3. Check https://cloud.google.com/vertex-ai/docs/generative-ai/video/generate-video

### Step 7: Test Veo API Access

```bash
# Get access token
ACCESS_TOKEN=$(gcloud auth print-access-token)
PROJECT_ID=$(gcloud config get-value project)

# Test Veo 2 API call
curl -X POST \
  "https://us-central1-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/us-central1/publishers/google/models/veo-002:predict" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "instances": [{
      "prompt": "A person drinking coffee and becoming energized, cinematic style",
      "parameters": {
        "aspectRatio": "9:16",
        "durationSeconds": 8
      }
    }]
  }'
```

**Expected Response:**
```json
{
  "predictions": [{
    "videoUri": "gs://your-bucket/generated-video.mp4",
    "mimeType": "video/mp4"
  }],
  "metadata": {
    "generationTime": "25.3s"
  }
}
```

**If you get error 404:** Veo 2/3 may not be available in your region yet. Try:
- Different region (us-central1, us-west1, europe-west4)
- Request beta access
- Use Imagen 2 video as alternative

## 🔧 Configure Heroku Environment

### Upload Service Account JSON

**Option 1: Environment Variable (Recommended for Heroku)**

```bash
# Convert JSON to single-line string
SA_JSON=$(cat ~/veo-key.json | jq -c .)

# Set in Heroku
heroku config:set GOOGLE_APPLICATION_CREDENTIALS_JSON="$SA_JSON" -a your-app-name
heroku config:set GOOGLE_CLOUD_PROJECT="meme-automation-veo" -a your-app-name
heroku config:set GOOGLE_CLOUD_REGION="us-central1" -a your-app-name
```

**Option 2: Upload to Heroku Config Files (Alternative)**

```bash
# This requires buildpack that supports credential files
# Not recommended for Eco Dyno - use Option 1 instead
```

### Configure n8n OAuth2

In n8n UI:
1. Go to **Credentials** → **New**
2. Select **Google OAuth2 API**
3. Choose "Service Account" tab
4. Paste content from `veo-key.json`
5. Add scopes:
   - `https://www.googleapis.com/auth/cloud-platform`
   - `https://www.googleapis.com/auth/aiplatform`
6. Save as "Google Veo Service Account"

### Alternative: Direct JSON in Workflow

If OAuth2 setup is complex, use direct authentication:

```javascript
// In HTTP Request node, add header:
{
  "Authorization": "Bearer {{$env.GOOGLE_ACCESS_TOKEN}}"
}

// Generate token with script (run periodically):
// workflows/Meme/scripts/refresh-google-token.sh
```

## 📊 Veo 2 vs Veo 3 Comparison

| Feature | Veo 2 | Veo 3 |
|---------|-------|-------|
| **Availability** | Preview | Limited/TBD |
| **Quality** | High (1080p) | Ultra-high |
| **Speed** | 20-40s | 15-30s (est) |
| **Prompt Understanding** | Excellent | Superior |
| **Cost/Video** | ~$0.30 | ~$0.50 (est) |
| **Max Duration** | 30s | 60s (est) |
| **Aspect Ratios** | 16:9, 9:16, 1:1 | Same + more |
| **Recommended For** | Production | Premium content |

## 🎨 Veo-Optimized Prompts

### Prompt Structure for Best Results

```
[Camera Movement] + [Subject Action] + [Visual Style] + [Lighting] + [Text Overlay]
```

**Examples for Veo:**

```javascript
// Good Veo 2 Prompt
"Cinematic tracking shot: Developer at modern desk typing code. Camera slowly orbits around, revealing AI assistant on adjacent screen writing perfect code. Warm professional lighting. Text overlay fades in: 'THE FUTURE'. 4K quality, smooth camera movement."

// Better Veo 3 Prompt (more detail)
"Professional cinematic sequence with smooth gimbal movement. Opening: Close-up of tired developer's hands typing code, shallow depth of field. Camera pulls back revealing cluttered desk with multiple monitors. Slow dolly right reveals AI assistant screen with code auto-completing. Golden hour lighting through window. Color grade: warm tones. Text overlay: 'AI REVOLUTION' with clean typography. Aspect ratio: 9:16 vertical for social media. Duration: 10 seconds."
```

### Veo Prompt Best Practices

✅ **Do:**
- Specify camera movements (dolly, orbit, tracking)
- Describe lighting (golden hour, studio, natural)
- Mention quality (4K, cinematic, professional)
- Include aspect ratio in prompt
- Specify smooth transitions
- Add color grading details
- Keep duration realistic (8-12s ideal)

❌ **Don't:**
- Use abstract concepts
- Request impossible physics
- Overcomplicate single shot
- Expect multiple scene transitions
- Use copyrighted references

## 🚀 Production Workflow Setup

### Complete Environment Configuration

```bash
# Required for Veo
heroku config:set GOOGLE_CLOUD_PROJECT="your-project-id" -a your-app-name
heroku config:set GOOGLE_CLOUD_REGION="us-central1" -a your-app-name
heroku config:set GOOGLE_APPLICATION_CREDENTIALS_JSON='{"type":"service_account",...}' -a your-app-name

# Optional: Preferred API
heroku config:set PREFERRED_VIDEO_API="veo2" -a your-app-name
# Options: veo2, veo3, replicate, runway

# Fallback API
heroku config:set REPLICATE_API_TOKEN="r8_xxx" -a your-app-name

# Instagram
heroku config:set INSTAGRAM_USER_ID="your_id" -a your-app-name
heroku config:set INSTAGRAM_ACCESS_TOKEN="your_token" -a your-app-name

# Verify all set
heroku config -a your-app-name | grep -E "GOOGLE|VIDEO|INSTAGRAM"
```

### Import Workflow

1. Download `2059_Meme_Video_GoogleVeo_MultiAPI_Scheduled.json`
2. In n8n: **Workflows** → **Import from File**
3. Configure Google OAuth2 credentials
4. Update PostgreSQL credentials
5. Test with manual execution
6. Activate for scheduled runs

## 💰 Cost Estimation

### Google Veo Pricing (Estimated)

**Veo 2:**
- Per video: ~$0.30
- 3 videos/day: $0.90/day
- Monthly: ~$27/month

**With Google Pro Credits:**
- May have included credits
- Check: https://console.cloud.google.com/billing
- Could reduce to $0-15/month

**Total Cost:**
- Heroku Eco: $5/month
- PostgreSQL: Included
- Veo 2 API: $15-27/month (with Pro credits)
- **Total: $20-32/month** for premium video memes

### Cost Optimization

1. **Mix APIs:**
   - Veo for important posts: 1/day ($9/month)
   - Replicate for regular: 2/day ($6/month)
   - Total: $15/month + $5 Heroku = $20/month

2. **Reduce Frequency:**
   - 2 videos/day instead of 3
   - Save 33% on API costs

3. **Use Google Pro Credits:**
   - Check if video generation included
   - May significantly reduce costs

## 🔍 Monitoring & Debugging

### Check Veo API Calls

```bash
# View recent API calls
gcloud logging read "resource.type=aiplatform.googleapis.com/Endpoint" \
    --limit=10 \
    --format=json

# Check costs
gcloud beta billing accounts list
gcloud beta billing projects describe meme-automation-veo
```

### Test Veo Availability

```bash
# Check current model access
curl -X GET \
  "https://us-central1-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/us-central1/publishers/google/models/veo-002" \
  -H "Authorization: Bearer $(gcloud auth print-access-token)"
```

### Common Issues

**Issue: 403 Permission Denied**
```bash
# Fix: Grant proper IAM roles
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:${SA_EMAIL}" \
    --role="roles/aiplatform.user"
```

**Issue: 404 Model Not Found**
- Veo may not be available in your region
- Try different regions
- Check if you need to request access
- Use Replicate as fallback

**Issue: Token Expired**
```bash
# Tokens expire after 1 hour
# n8n OAuth2 should handle this automatically
# Manual refresh:
gcloud auth print-access-token
```

## 🔄 Veo 3 Setup (When Available)

When Veo 3 becomes publicly available:

1. **Check Availability:**
```bash
gcloud ai models list --region=us-central1 --filter="displayName:veo-003"
```

2. **Update Workflow:**
   - Change model name from `veo-002` to `veo-003`
   - Test with same prompts
   - Compare quality and cost

3. **A/B Testing:**
   - Run both Veo 2 and Veo 3
   - Compare results
   - Choose based on quality/cost ratio

## 📚 Resources

- [Google Vertex AI Docs](https://cloud.google.com/vertex-ai/docs)
- [Veo Model Card](https://deepmind.google/technologies/veo/)
- [Vertex AI Pricing](https://cloud.google.com/vertex-ai/pricing)
- [Service Account Best Practices](https://cloud.google.com/iam/docs/best-practices-service-accounts)
- [n8n Google OAuth2](https://docs.n8n.io/integrations/builtin/credentials/google/)

## 🎯 Next Steps

1. ✅ Complete Google Cloud setup
2. ✅ Test Veo API access
3. ✅ Configure Heroku environment
4. ✅ Import workflow 2059
5. ✅ Run test execution
6. ✅ Monitor first few posts
7. ✅ Optimize prompts based on results
8. ✅ Track costs and adjust frequency

---

**Created:** 2025-10-30  
**Version:** 1.0  
**For:** Google Pro users with Vertex AI access  
**Cost:** ~$20-32/month for premium AI video memes
