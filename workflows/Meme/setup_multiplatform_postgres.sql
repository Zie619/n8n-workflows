-- PostgreSQL Setup for Multi-Platform Video Automation
-- Supports Instagram Reels + YouTube Shorts + TikTok

-- ==============================================
-- 1. Create Multi-Platform Posts Table
-- ==============================================

CREATE TABLE IF NOT EXISTS meme_videos_multiplatform (
  id SERIAL PRIMARY KEY,
  topic VARCHAR(100) NOT NULL,
  video_prompt TEXT NOT NULL,
  video_url TEXT,
  instagram_id VARCHAR(100),
  youtube_id VARCHAR(100),
  tiktok_id VARCHAR(100),
  api_provider VARCHAR(50) DEFAULT 'veo2',
  posted_at TIMESTAMP DEFAULT NOW(),
  success BOOLEAN DEFAULT TRUE,
  generation_time_seconds INTEGER,
  platforms_posted TEXT[], -- Array of successful platforms
  failure_reason TEXT
);

COMMENT ON TABLE meme_videos_multiplatform IS 'Tracks videos posted to Instagram, YouTube Shorts, and TikTok';
COMMENT ON COLUMN meme_videos_multiplatform.instagram_id IS 'Instagram Reel media ID';
COMMENT ON COLUMN meme_videos_multiplatform.youtube_id IS 'YouTube video ID';
COMMENT ON COLUMN meme_videos_multiplatform.tiktok_id IS 'TikTok video ID';
COMMENT ON COLUMN meme_videos_multiplatform.platforms_posted IS 'Array of platforms successfully posted: [instagram, youtube, tiktok]';

-- ==============================================
-- 2. Create Indexes for Performance
-- ==============================================

CREATE INDEX IF NOT EXISTS idx_multiplatform_posted_at 
ON meme_videos_multiplatform(posted_at DESC);

CREATE INDEX IF NOT EXISTS idx_multiplatform_topic 
ON meme_videos_multiplatform(topic);

CREATE INDEX IF NOT EXISTS idx_multiplatform_success 
ON meme_videos_multiplatform(success);

CREATE INDEX IF NOT EXISTS idx_multiplatform_instagram 
ON meme_videos_multiplatform(instagram_id) 
WHERE instagram_id IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_multiplatform_youtube 
ON meme_videos_multiplatform(youtube_id) 
WHERE youtube_id IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_multiplatform_tiktok 
ON meme_videos_multiplatform(tiktok_id) 
WHERE tiktok_id IS NOT NULL;

-- ==============================================
-- 3. Platform Success Analytics View
-- ==============================================

CREATE OR REPLACE VIEW multiplatform_analytics AS
SELECT 
  DATE(posted_at) as date,
  COUNT(*) as total_videos,
  COUNT(instagram_id) as instagram_posts,
  COUNT(youtube_id) as youtube_posts,
  COUNT(tiktok_id) as tiktok_posts,
  ROUND(100.0 * COUNT(instagram_id) / NULLIF(COUNT(*), 0), 2) as instagram_success_rate,
  ROUND(100.0 * COUNT(youtube_id) / NULLIF(COUNT(*), 0), 2) as youtube_success_rate,
  ROUND(100.0 * COUNT(tiktok_id) / NULLIF(COUNT(*), 0), 2) as tiktok_success_rate,
  COUNT(CASE WHEN instagram_id IS NOT NULL AND youtube_id IS NOT NULL AND tiktok_id IS NOT NULL THEN 1 END) as all_platforms_success
FROM meme_videos_multiplatform
WHERE posted_at > NOW() - INTERVAL '30 days'
GROUP BY DATE(posted_at)
ORDER BY date DESC;

COMMENT ON VIEW multiplatform_analytics IS 'Daily success rates for each platform';

-- ==============================================
-- 4. Platform Comparison View
-- ==============================================

CREATE OR REPLACE VIEW platform_comparison AS
SELECT 
  'Instagram' as platform,
  COUNT(instagram_id) as successful_posts,
  COUNT(*) - COUNT(instagram_id) as failed_posts,
  ROUND(100.0 * COUNT(instagram_id) / COUNT(*), 2) as success_rate
FROM meme_videos_multiplatform
WHERE posted_at > NOW() - INTERVAL '30 days'
UNION ALL
SELECT 
  'YouTube' as platform,
  COUNT(youtube_id) as successful_posts,
  COUNT(*) - COUNT(youtube_id) as failed_posts,
  ROUND(100.0 * COUNT(youtube_id) / COUNT(*), 2) as success_rate
FROM meme_videos_multiplatform
WHERE posted_at > NOW() - INTERVAL '30 days'
UNION ALL
SELECT 
  'TikTok' as platform,
  COUNT(tiktok_id) as successful_posts,
  COUNT(*) - COUNT(tiktok_id) as failed_posts,
  ROUND(100.0 * COUNT(tiktok_id) / COUNT(*), 2) as success_rate
FROM meme_videos_multiplatform
WHERE posted_at > NOW() - INTERVAL '30 days'
ORDER BY successful_posts DESC;

COMMENT ON VIEW platform_comparison IS 'Compare success rates across all platforms';

-- ==============================================
-- 5. Topic Performance by Platform View
-- ==============================================

CREATE OR REPLACE VIEW topic_platform_performance AS
SELECT 
  topic,
  COUNT(*) as total_posts,
  COUNT(instagram_id) as instagram,
  COUNT(youtube_id) as youtube,
  COUNT(tiktok_id) as tiktok,
  ROUND(AVG(CASE WHEN instagram_id IS NOT NULL THEN 1 ELSE 0 END) * 100, 2) as instagram_rate,
  ROUND(AVG(CASE WHEN youtube_id IS NOT NULL THEN 1 ELSE 0 END) * 100, 2) as youtube_rate,
  ROUND(AVG(CASE WHEN tiktok_id IS NOT NULL THEN 1 ELSE 0 END) * 100, 2) as tiktok_rate
FROM meme_videos_multiplatform
WHERE posted_at > NOW() - INTERVAL '30 days'
GROUP BY topic
ORDER BY total_posts DESC;

COMMENT ON VIEW topic_platform_performance IS 'Shows which topics perform best on each platform';

-- ==============================================
-- 6. Failed Posts View
-- ==============================================

CREATE OR REPLACE VIEW failed_platform_posts AS
SELECT 
  id,
  topic,
  posted_at,
  CASE WHEN instagram_id IS NULL THEN 'Instagram ' ELSE '' END ||
  CASE WHEN youtube_id IS NULL THEN 'YouTube ' ELSE '' END ||
  CASE WHEN tiktok_id IS NULL THEN 'TikTok ' ELSE '' END as failed_platforms,
  failure_reason,
  video_url
FROM meme_videos_multiplatform
WHERE instagram_id IS NULL OR youtube_id IS NULL OR tiktok_id IS NULL
ORDER BY posted_at DESC;

COMMENT ON VIEW failed_platform_posts IS 'Videos that failed to post to one or more platforms';

-- ==============================================
-- 7. Function: Get Platform Statistics
-- ==============================================

CREATE OR REPLACE FUNCTION get_platform_stats(days INTEGER DEFAULT 30)
RETURNS TABLE (
  platform TEXT,
  total_attempts INTEGER,
  successful_posts INTEGER,
  failed_posts INTEGER,
  success_rate NUMERIC
) AS $$
BEGIN
  RETURN QUERY
  SELECT 
    'Instagram'::TEXT as platform,
    COUNT(*)::INTEGER as total_attempts,
    COUNT(instagram_id)::INTEGER as successful_posts,
    (COUNT(*) - COUNT(instagram_id))::INTEGER as failed_posts,
    ROUND(100.0 * COUNT(instagram_id) / COUNT(*), 2) as success_rate
  FROM meme_videos_multiplatform
  WHERE posted_at > NOW() - (days || ' days')::INTERVAL
  UNION ALL
  SELECT 
    'YouTube'::TEXT,
    COUNT(*)::INTEGER,
    COUNT(youtube_id)::INTEGER,
    (COUNT(*) - COUNT(youtube_id))::INTEGER,
    ROUND(100.0 * COUNT(youtube_id) / COUNT(*), 2)
  FROM meme_videos_multiplatform
  WHERE posted_at > NOW() - (days || ' days')::INTERVAL
  UNION ALL
  SELECT 
    'TikTok'::TEXT,
    COUNT(*)::INTEGER,
    COUNT(tiktok_id)::INTEGER,
    (COUNT(*) - COUNT(tiktok_id))::INTEGER,
    ROUND(100.0 * COUNT(tiktok_id) / COUNT(*), 2)
  FROM meme_videos_multiplatform
  WHERE posted_at > NOW() - (days || ' days')::INTERVAL;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION get_platform_stats IS 'Get success statistics for all platforms for specified days';

-- ==============================================
-- 8. Function: Check Platform Health
-- ==============================================

CREATE OR REPLACE FUNCTION check_platform_health()
RETURNS TABLE (
  platform TEXT,
  status TEXT,
  last_successful_post TIMESTAMP,
  hours_since_success NUMERIC,
  recent_failures INTEGER
) AS $$
BEGIN
  RETURN QUERY
  WITH platform_data AS (
    SELECT 
      'Instagram' as plat,
      MAX(CASE WHEN instagram_id IS NOT NULL THEN posted_at END) as last_success,
      COUNT(CASE WHEN instagram_id IS NULL AND posted_at > NOW() - INTERVAL '24 hours' THEN 1 END) as failures
    FROM meme_videos_multiplatform
    UNION ALL
    SELECT 
      'YouTube',
      MAX(CASE WHEN youtube_id IS NOT NULL THEN posted_at END),
      COUNT(CASE WHEN youtube_id IS NULL AND posted_at > NOW() - INTERVAL '24 hours' THEN 1 END)
    FROM meme_videos_multiplatform
    UNION ALL
    SELECT 
      'TikTok',
      MAX(CASE WHEN tiktok_id IS NOT NULL THEN posted_at END),
      COUNT(CASE WHEN tiktok_id IS NULL AND posted_at > NOW() - INTERVAL '24 hours' THEN 1 END)
    FROM meme_videos_multiplatform
  )
  SELECT 
    plat::TEXT as platform,
    CASE 
      WHEN last_success > NOW() - INTERVAL '12 hours' THEN '✅ Healthy'
      WHEN last_success > NOW() - INTERVAL '24 hours' THEN '⚠️  Warning'
      ELSE '❌ Critical'
    END::TEXT as status,
    last_success as last_successful_post,
    ROUND(EXTRACT(EPOCH FROM (NOW() - last_success)) / 3600, 1) as hours_since_success,
    failures::INTEGER as recent_failures
  FROM platform_data
  ORDER BY hours_since_success;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION check_platform_health IS 'Quick health check for all platforms';

-- ==============================================
-- 9. Sample Queries
-- ==============================================

-- View recent multi-platform posts
-- SELECT * FROM meme_videos_multiplatform ORDER BY posted_at DESC LIMIT 10;

-- Check platform health
-- SELECT * FROM check_platform_health();

-- Get 30-day statistics
-- SELECT * FROM get_platform_stats(30);

-- View daily analytics
-- SELECT * FROM multiplatform_analytics LIMIT 30;

-- Compare platforms
-- SELECT * FROM platform_comparison;

-- Find failed posts
-- SELECT * FROM failed_platform_posts LIMIT 20;

-- Success rate by topic and platform
-- SELECT * FROM topic_platform_performance;

-- Find posts that succeeded on all platforms
-- SELECT * FROM meme_videos_multiplatform 
-- WHERE instagram_id IS NOT NULL 
--   AND youtube_id IS NOT NULL 
--   AND tiktok_id IS NOT NULL
-- ORDER BY posted_at DESC;

-- Find posts that failed completely
-- SELECT * FROM meme_videos_multiplatform 
-- WHERE instagram_id IS NULL 
--   AND youtube_id IS NULL 
--   AND tiktok_id IS NULL
-- ORDER BY posted_at DESC;

-- ==============================================
-- 10. Triggers for Automatic Platform Tracking
-- ==============================================

CREATE OR REPLACE FUNCTION update_platforms_posted()
RETURNS TRIGGER AS $$
BEGIN
  NEW.platforms_posted := ARRAY(
    SELECT platform FROM (
      SELECT 'instagram' as platform WHERE NEW.instagram_id IS NOT NULL
      UNION ALL
      SELECT 'youtube' WHERE NEW.youtube_id IS NOT NULL
      UNION ALL
      SELECT 'tiktok' WHERE NEW.tiktok_id IS NOT NULL
    ) platforms
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_update_platforms ON meme_videos_multiplatform;
CREATE TRIGGER trg_update_platforms
  BEFORE INSERT OR UPDATE ON meme_videos_multiplatform
  FOR EACH ROW
  EXECUTE FUNCTION update_platforms_posted();

COMMENT ON FUNCTION update_platforms_posted IS 'Automatically updates platforms_posted array based on which IDs are present';

-- ==============================================
-- Setup Complete!
-- ==============================================

-- Verify setup
SELECT 
  'meme_videos_multiplatform' as table_name,
  COUNT(*) as row_count,
  pg_size_pretty(pg_table_size('meme_videos_multiplatform')) as table_size
FROM meme_videos_multiplatform;

-- Show views
SELECT viewname, definition 
FROM pg_views 
WHERE schemaname = 'public' 
  AND viewname LIKE '%multiplatform%' 
  OR viewname LIKE '%platform%';

-- Test health check
SELECT * FROM check_platform_health();

RAISE NOTICE 'Multi-platform video automation database setup complete!';
RAISE NOTICE 'Table: meme_videos_multiplatform';
RAISE NOTICE 'Views: multiplatform_analytics, platform_comparison, topic_platform_performance';
RAISE NOTICE 'Functions: get_platform_stats(), check_platform_health()';
RAISE NOTICE 'Ready to track Instagram + YouTube Shorts + TikTok posts!';
