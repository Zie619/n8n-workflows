-- PostgreSQL Setup for Perplexity AI Integration
-- Tracks AI-generated trending video content with multi-platform support

-- Drop existing objects if they exist (for clean reinstall)
DROP VIEW IF EXISTS perplexity_analytics CASCADE;
DROP VIEW IF EXISTS trending_vs_manual_performance CASCADE;
DROP VIEW IF EXISTS perplexity_platform_success CASCADE;
DROP VIEW IF EXISTS top_trending_topics CASCADE;
DROP VIEW IF EXISTS perplexity_cost_analysis CASCADE;
DROP FUNCTION IF EXISTS get_perplexity_stats(integer) CASCADE;
DROP FUNCTION IF EXISTS get_trending_topic_performance() CASCADE;
DROP TABLE IF EXISTS meme_videos_multiplatform_gdrive_perplexity CASCADE;

-- Main table for Perplexity AI generated content
CREATE TABLE meme_videos_multiplatform_gdrive_perplexity (
  id SERIAL PRIMARY KEY,
  
  -- Content metadata
  topic VARCHAR(100) NOT NULL,
  video_prompt TEXT NOT NULL,
  video_url TEXT,
  
  -- Platform IDs
  instagram_id VARCHAR(100),
  youtube_id VARCHAR(100),
  tiktok_id VARCHAR(100),
  
  -- Google Drive backup
  google_drive_id VARCHAR(255),
  google_drive_url TEXT,
  drive_folder VARCHAR(100),
  
  -- Platform tracking
  platforms_posted TEXT[] DEFAULT ARRAY[]::TEXT[],
  
  -- Video generation
  api_provider VARCHAR(50), -- 'veo2', 'veo3', 'replicate', 'runway'
  
  -- Perplexity metadata
  perplexity_source BOOLEAN DEFAULT false, -- true if from Perplexity, false if fallback
  trending_topic BOOLEAN DEFAULT false,     -- true if currently trending
  
  -- Status tracking
  posted_at TIMESTAMP DEFAULT NOW(),
  success BOOLEAN DEFAULT true,
  error_message TEXT,
  
  -- Cost tracking
  estimated_cost DECIMAL(10,4) DEFAULT 0.00,
  
  -- Engagement metrics (optional - can be updated via webhook)
  instagram_likes INTEGER,
  instagram_comments INTEGER,
  youtube_views INTEGER,
  youtube_likes INTEGER,
  tiktok_views INTEGER,
  tiktok_likes INTEGER,
  
  -- Timestamps
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_perplexity_source ON meme_videos_multiplatform_gdrive_perplexity(perplexity_source);
CREATE INDEX idx_trending_topic ON meme_videos_multiplatform_gdrive_perplexity(trending_topic);
CREATE INDEX idx_posted_at ON meme_videos_multiplatform_gdrive_perplexity(posted_at DESC);
CREATE INDEX idx_topic ON meme_videos_multiplatform_gdrive_perplexity(topic);
CREATE INDEX idx_api_provider ON meme_videos_multiplatform_gdrive_perplexity(api_provider);
CREATE INDEX idx_platforms_posted ON meme_videos_multiplatform_gdrive_perplexity USING GIN(platforms_posted);

-- Trigger to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_perplexity_modtime
BEFORE UPDATE ON meme_videos_multiplatform_gdrive_perplexity
FOR EACH ROW
EXECUTE FUNCTION update_modified_column();

-- View: Daily Perplexity Analytics
CREATE VIEW perplexity_analytics AS
SELECT 
  DATE(posted_at) as date,
  COUNT(*) as total_posts,
  SUM(CASE WHEN perplexity_source THEN 1 ELSE 0 END) as perplexity_posts,
  SUM(CASE WHEN NOT perplexity_source THEN 1 ELSE 0 END) as fallback_posts,
  ROUND(AVG(CASE WHEN perplexity_source THEN 1 ELSE 0 END) * 100, 2) as perplexity_success_rate,
  SUM(CASE WHEN trending_topic THEN 1 ELSE 0 END) as trending_posts,
  COUNT(DISTINCT topic) as unique_topics,
  COUNT(instagram_id) as instagram_posts,
  COUNT(youtube_id) as youtube_posts,
  COUNT(tiktok_id) as tiktok_posts,
  COUNT(google_drive_id) as gdrive_backups,
  SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful_posts,
  ROUND(AVG(CASE WHEN success THEN 1 ELSE 0 END) * 100, 2) as success_rate,
  SUM(estimated_cost) as daily_cost
FROM meme_videos_multiplatform_gdrive_perplexity
GROUP BY DATE(posted_at)
ORDER BY date DESC;

-- View: Trending vs Manual Performance Comparison
CREATE VIEW trending_vs_manual_performance AS
SELECT 
  perplexity_source,
  CASE 
    WHEN perplexity_source THEN 'Perplexity AI'
    ELSE 'Manual Fallback'
  END as source_type,
  COUNT(*) as total_posts,
  COUNT(instagram_id) as instagram_success,
  COUNT(youtube_id) as youtube_success,
  COUNT(tiktok_id) as tiktok_success,
  COUNT(google_drive_id) as gdrive_success,
  ROUND(AVG(array_length(platforms_posted, 1)), 2) as avg_platforms_per_post,
  ROUND(AVG(CASE WHEN success THEN 1 ELSE 0 END) * 100, 2) as success_rate,
  SUM(estimated_cost) as total_cost,
  ROUND(AVG(estimated_cost), 4) as avg_cost_per_post,
  -- Engagement metrics (if available)
  ROUND(AVG(COALESCE(instagram_likes, 0)), 0) as avg_instagram_likes,
  ROUND(AVG(COALESCE(youtube_views, 0)), 0) as avg_youtube_views,
  ROUND(AVG(COALESCE(tiktok_views, 0)), 0) as avg_tiktok_views
FROM meme_videos_multiplatform_gdrive_perplexity
WHERE posted_at > NOW() - INTERVAL '30 days'
GROUP BY perplexity_source
ORDER BY total_posts DESC;

-- View: Platform Success Rates
CREATE VIEW perplexity_platform_success AS
SELECT 
  'Instagram' as platform,
  COUNT(instagram_id) as successful_posts,
  COUNT(*) as total_attempts,
  ROUND(COUNT(instagram_id)::DECIMAL / NULLIF(COUNT(*), 0) * 100, 2) as success_rate,
  SUM(CASE WHEN perplexity_source THEN 1 ELSE 0 END) as perplexity_powered,
  ROUND(AVG(COALESCE(instagram_likes, 0)), 0) as avg_likes,
  ROUND(AVG(COALESCE(instagram_comments, 0)), 0) as avg_comments
FROM meme_videos_multiplatform_gdrive_perplexity
WHERE posted_at > NOW() - INTERVAL '7 days'

UNION ALL

SELECT 
  'YouTube' as platform,
  COUNT(youtube_id) as successful_posts,
  COUNT(*) as total_attempts,
  ROUND(COUNT(youtube_id)::DECIMAL / NULLIF(COUNT(*), 0) * 100, 2) as success_rate,
  SUM(CASE WHEN perplexity_source THEN 1 ELSE 0 END) as perplexity_powered,
  ROUND(AVG(COALESCE(youtube_views, 0)), 0) as avg_views,
  ROUND(AVG(COALESCE(youtube_likes, 0)), 0) as avg_likes
FROM meme_videos_multiplatform_gdrive_perplexity
WHERE posted_at > NOW() - INTERVAL '7 days'

UNION ALL

SELECT 
  'TikTok' as platform,
  COUNT(tiktok_id) as successful_posts,
  COUNT(*) as total_attempts,
  ROUND(COUNT(tiktok_id)::DECIMAL / NULLIF(COUNT(*), 0) * 100, 2) as success_rate,
  SUM(CASE WHEN perplexity_source THEN 1 ELSE 0 END) as perplexity_powered,
  ROUND(AVG(COALESCE(tiktok_views, 0)), 0) as avg_views,
  ROUND(AVG(COALESCE(tiktok_likes, 0)), 0) as avg_likes
FROM meme_videos_multiplatform_gdrive_perplexity
WHERE posted_at > NOW() - INTERVAL '7 days'

UNION ALL

SELECT 
  'Google Drive' as platform,
  COUNT(google_drive_id) as successful_posts,
  COUNT(*) as total_attempts,
  ROUND(COUNT(google_drive_id)::DECIMAL / NULLIF(COUNT(*), 0) * 100, 2) as success_rate,
  SUM(CASE WHEN perplexity_source THEN 1 ELSE 0 END) as perplexity_powered,
  0 as metric1,
  0 as metric2
FROM meme_videos_multiplatform_gdrive_perplexity
WHERE posted_at > NOW() - INTERVAL '7 days'

ORDER BY successful_posts DESC;

-- View: Top Trending Topics
CREATE VIEW top_trending_topics AS
SELECT 
  topic,
  COUNT(*) as times_used,
  SUM(CASE WHEN perplexity_source THEN 1 ELSE 0 END) as perplexity_generated,
  SUM(CASE WHEN trending_topic THEN 1 ELSE 0 END) as was_trending,
  COUNT(instagram_id) as instagram_posts,
  COUNT(youtube_id) as youtube_posts,
  COUNT(tiktok_id) as tiktok_posts,
  ROUND(AVG(array_length(platforms_posted, 1)), 2) as avg_platforms,
  DATE(MAX(posted_at)) as last_used,
  DATE(MIN(posted_at)) as first_used,
  -- Engagement if available
  ROUND(AVG(COALESCE(instagram_likes, 0) + COALESCE(youtube_likes, 0) + COALESCE(tiktok_likes, 0)), 0) as avg_total_likes,
  ROUND(AVG(COALESCE(youtube_views, 0) + COALESCE(tiktok_views, 0)), 0) as avg_total_views
FROM meme_videos_multiplatform_gdrive_perplexity
WHERE posted_at > NOW() - INTERVAL '14 days'
GROUP BY topic
ORDER BY times_used DESC, avg_total_views DESC
LIMIT 20;

-- View: Cost Analysis
CREATE VIEW perplexity_cost_analysis AS
SELECT 
  DATE_TRUNC('month', posted_at) as month,
  COUNT(*) as total_posts,
  SUM(CASE WHEN perplexity_source THEN 1 ELSE 0 END) as perplexity_posts,
  SUM(estimated_cost) as total_cost,
  ROUND(AVG(estimated_cost), 4) as avg_cost_per_post,
  -- Estimated API costs
  SUM(CASE WHEN perplexity_source THEN 0.005 ELSE 0 END) as perplexity_api_cost,
  SUM(CASE WHEN api_provider LIKE 'veo%' THEN 0.30 ELSE 0.08 END) as video_api_cost,
  SUM(CASE 
    WHEN perplexity_source THEN 0.005 + CASE WHEN api_provider LIKE 'veo%' THEN 0.30 ELSE 0.08 END
    ELSE CASE WHEN api_provider LIKE 'veo%' THEN 0.30 ELSE 0.08 END
  END) as estimated_monthly_cost
FROM meme_videos_multiplatform_gdrive_perplexity
GROUP BY DATE_TRUNC('month', posted_at)
ORDER BY month DESC;

-- Function: Get Perplexity Statistics for Last N Days
CREATE OR REPLACE FUNCTION get_perplexity_stats(days_back INTEGER DEFAULT 7)
RETURNS TABLE (
  metric VARCHAR,
  value NUMERIC,
  percentage NUMERIC
) AS $$
BEGIN
  RETURN QUERY
  WITH stats AS (
    SELECT 
      COUNT(*) as total,
      SUM(CASE WHEN perplexity_source THEN 1 ELSE 0 END) as perplexity,
      SUM(CASE WHEN NOT perplexity_source THEN 1 ELSE 0 END) as fallback,
      SUM(CASE WHEN trending_topic THEN 1 ELSE 0 END) as trending,
      SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful,
      COUNT(instagram_id) as instagram,
      COUNT(youtube_id) as youtube,
      COUNT(tiktok_id) as tiktok,
      COUNT(google_drive_id) as gdrive
    FROM meme_videos_multiplatform_gdrive_perplexity
    WHERE posted_at > NOW() - (days_back || ' days')::INTERVAL
  )
  SELECT 'Total Posts'::VARCHAR, total::NUMERIC, 100.0::NUMERIC FROM stats
  UNION ALL
  SELECT 'Perplexity AI Posts', perplexity::NUMERIC, ROUND((perplexity::DECIMAL / NULLIF(total, 0) * 100), 2) FROM stats
  UNION ALL
  SELECT 'Fallback Posts', fallback::NUMERIC, ROUND((fallback::DECIMAL / NULLIF(total, 0) * 100), 2) FROM stats
  UNION ALL
  SELECT 'Trending Topics', trending::NUMERIC, ROUND((trending::DECIMAL / NULLIF(total, 0) * 100), 2) FROM stats
  UNION ALL
  SELECT 'Successful Posts', successful::NUMERIC, ROUND((successful::DECIMAL / NULLIF(total, 0) * 100), 2) FROM stats
  UNION ALL
  SELECT 'Instagram Posts', instagram::NUMERIC, ROUND((instagram::DECIMAL / NULLIF(total, 0) * 100), 2) FROM stats
  UNION ALL
  SELECT 'YouTube Posts', youtube::NUMERIC, ROUND((youtube::DECIMAL / NULLIF(total, 0) * 100), 2) FROM stats
  UNION ALL
  SELECT 'TikTok Posts', tiktok::NUMERIC, ROUND((tiktok::DECIMAL / NULLIF(total, 0) * 100), 2) FROM stats
  UNION ALL
  SELECT 'Google Drive Backups', gdrive::NUMERIC, ROUND((gdrive::DECIMAL / NULLIF(total, 0) * 100), 2) FROM stats;
END;
$$ LANGUAGE plpgsql;

-- Function: Get Trending Topic Performance
CREATE OR REPLACE FUNCTION get_trending_topic_performance()
RETURNS TABLE (
  topic VARCHAR,
  total_uses BIGINT,
  perplexity_generated BIGINT,
  avg_instagram_likes NUMERIC,
  avg_youtube_views NUMERIC,
  avg_tiktok_views NUMERIC,
  last_used DATE
) AS $$
BEGIN
  RETURN QUERY
  SELECT 
    t.topic::VARCHAR,
    COUNT(*)::BIGINT as total_uses,
    SUM(CASE WHEN t.perplexity_source THEN 1 ELSE 0 END)::BIGINT as perplexity_generated,
    ROUND(AVG(COALESCE(t.instagram_likes, 0)), 0) as avg_instagram_likes,
    ROUND(AVG(COALESCE(t.youtube_views, 0)), 0) as avg_youtube_views,
    ROUND(AVG(COALESCE(t.tiktok_views, 0)), 0) as avg_tiktok_views,
    DATE(MAX(t.posted_at)) as last_used
  FROM meme_videos_multiplatform_gdrive_perplexity t
  WHERE t.posted_at > NOW() - INTERVAL '30 days'
    AND t.trending_topic = true
  GROUP BY t.topic
  ORDER BY total_uses DESC, avg_youtube_views DESC
  LIMIT 10;
END;
$$ LANGUAGE plpgsql;

-- Sample queries to test the setup

-- 1. View daily analytics
-- SELECT * FROM perplexity_analytics LIMIT 7;

-- 2. Compare Perplexity vs Manual performance
-- SELECT * FROM trending_vs_manual_performance;

-- 3. Check platform success rates
-- SELECT * FROM perplexity_platform_success;

-- 4. View top trending topics
-- SELECT * FROM top_trending_topics;

-- 5. Analyze costs
-- SELECT * FROM perplexity_cost_analysis;

-- 6. Get statistics for last 7 days
-- SELECT * FROM get_perplexity_stats(7);

-- 7. Get trending topic performance
-- SELECT * FROM get_trending_topic_performance();

-- Grant permissions (if needed for specific users)
-- GRANT SELECT, INSERT, UPDATE ON meme_videos_multiplatform_gdrive_perplexity TO your_user;
-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO your_user;
-- GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO your_user;

-- Success message
DO $$
BEGIN
  RAISE NOTICE 'Perplexity AI PostgreSQL setup completed successfully!';
  RAISE NOTICE 'Table created: meme_videos_multiplatform_gdrive_perplexity';
  RAISE NOTICE 'Views created: 5 analytics views';
  RAISE NOTICE 'Functions created: 2 helper functions';
  RAISE NOTICE 'Ready to track AI-generated trending content!';
END $$;
