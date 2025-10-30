# Meme Automation - Quick Reference

## 🚀 Quick Start (5 Minutes)

### 1. Choose Your Workflow
```
Free Tier?     → Use 2056_Minimal (1 post/day)
Eco Dyno?      → Use 2057_EcoDyno_PostgreSQL (4 posts/day) ⭐ RECOMMENDED
Hobby Dyno?    → Use 2055_Full (6 posts/day)
```

### 2. Set Environment Variables
```bash
heroku config:set IMGFLIP_USERNAME=your_username -a your-app
heroku config:set IMGFLIP_PASSWORD=your_password -a your-app
heroku config:set INSTAGRAM_USER_ID=your_ig_id -a your-app
heroku config:set INSTAGRAM_ACCESS_TOKEN=your_token -a your-app
```

### 3. Import & Activate
1. Open n8n → Import workflow JSON
2. Configure PostgreSQL credentials (if using 2057)
3. Toggle "Active" switch
4. Done! 🎉

## 📊 Cost Comparison

| Tier | Cost | Posts/Day | Features |
|------|------|-----------|----------|
| **Free** | $0 | 1 | Basic |
| **Eco** | $5 | 4 | PostgreSQL, tracking |
| **Hobby** | $7 | 6 | Full featured |

## 🔑 Required Accounts

### ImgFlip (Free)
- Sign up: https://imgflip.com
- Get: Username & Password
- Limit: 100 requests/day

### Instagram
- Need: Business account
- Create: Facebook App
- Get: User ID & Access Token
- Guide: https://developers.facebook.com/docs/instagram-api

### PostgreSQL (Eco Dyno)
- Included with Eco/Hobby dyno
- Auto-configured by Heroku
- No manual setup needed

## 📝 Common Commands

### Heroku CLI
```bash
# View logs
heroku logs --tail -a your-app

# Check dyno status
heroku ps -a your-app

# Restart dyno
heroku restart -a your-app

# View config
heroku config -a your-app
```

### PostgreSQL
```bash
# Connect to database
heroku pg:psql -a your-app

# Check recent posts
SELECT * FROM meme_posts ORDER BY posted_at DESC LIMIT 10;

# Check success rate
SELECT COUNT(*), AVG(CASE WHEN success THEN 1.0 ELSE 0.0 END) * 100 
FROM meme_posts WHERE posted_at > NOW() - INTERVAL '7 days';

# View analytics
SELECT * FROM meme_analytics LIMIT 7;
```

## 🛠️ Troubleshooting

### Workflow Not Running
```
1. Check if active (toggle in n8n)
2. Check dyno hours: heroku ps -a your-app
3. Check logs: heroku logs --tail -a your-app
```

### ImgFlip Fails
```
1. Verify credentials in Heroku config
2. Check API limit (100/day)
3. Test credentials on ImgFlip.com
```

### Instagram Fails
```
1. Check if token expired (60 days)
2. Verify Business account linked
3. Check rate limit (25 posts/day)
4. Ensure image URL is public
```

### Database Errors
```
1. Verify PostgreSQL add-on attached
2. Check connection in n8n credentials
3. Run setup script: setup_postgres.sql
4. Enable SSL in connection settings
```

## 📈 Performance Expectations

### Eco Dyno + PostgreSQL (2057)
```
Execution time:   15-25 seconds
Memory usage:     80-120 MB
CPU usage:        < 100ms
Database queries: 2 per run
Success rate:     97-99%
Dyno hours/month: ~8 hours (0.8%)
```

## 🎨 Customization

### Change Frequency
Edit "Schedule Trigger" node:
- `hoursInterval: 6` → 4 posts/day
- `hoursInterval: 12` → 2 posts/day
- `hoursInterval: 24` → 1 post/day

### Add Topics
Edit "Generate Meme" node, add to array:
```javascript
{id: '181913649', t0: 'Your text', t1: 'Your text', topic: 'newtopic', hashtags: '#tags'}
```

### Modify Caption
Edit "Prepare Data" node:
```javascript
caption: `${text0} ➡️ ${text1}\n\n${hashtags} #meme #funny`
```

## 📚 File Reference

| File | Purpose |
|------|---------|
| `2057_*.json` | Workflow (Eco Dyno recommended) |
| `ECO_DYNO_POSTGRES_GUIDE.md` | Full setup guide |
| `setup_postgres.sql` | Database setup script |
| `.env.example` | Environment variables template |
| `validate.sh` | Pre-deployment validation |

## 🎯 Best Practices

### Security
- ✅ Use environment variables
- ✅ Enable n8n basic auth
- ✅ Rotate tokens every 60 days
- ❌ Never commit credentials

### Performance
- ✅ Keep database clean (< 90 days)
- ✅ Monitor success rate weekly
- ✅ Run vacuum monthly
- ❌ Don't store binary data in DB

### Content
- ✅ Vary meme topics
- ✅ Use trending hashtags
- ✅ Monitor engagement
- ❌ Don't spam same content

## 🔗 Important Links

- [n8n Docs](https://docs.n8n.io/)
- [Heroku Docs](https://devcenter.heroku.com/)
- [ImgFlip API](https://imgflip.com/api)
- [Instagram API](https://developers.facebook.com/docs/instagram-api)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)

## 💡 Pro Tips

1. **Start Small**: Use minimal workflow first, then scale
2. **Monitor Daily**: Check logs and success rate
3. **Backup Weekly**: Heroku auto-backups, but download important data
4. **Test First**: Run manual execution before activating schedule
5. **Keep Simple**: Don't over-complicate, keep it lightweight

## 🆘 Get Help

- **n8n Community**: https://community.n8n.io/
- **Heroku Support**: https://help.heroku.com/
- **GitHub Issues**: Open an issue in the repository

## 📊 Success Metrics

Good performance indicators:
- ✅ Success rate > 95%
- ✅ Execution time < 30s
- ✅ Memory usage < 200MB
- ✅ Database size < 10MB
- ✅ Zero timeouts

Red flags:
- ❌ Success rate < 80%
- ❌ Frequent timeouts
- ❌ Memory spikes > 400MB
- ❌ Database errors
- ❌ API rate limit hits

---

**Need more details?** See full documentation:
- Setup: `ECO_DYNO_POSTGRES_GUIDE.md`
- Deployment: `HEROKU_DEPLOYMENT.md`
- Overview: `README.md`
