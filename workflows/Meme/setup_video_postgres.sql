-- PostgreSQL Setup for Video Meme Automation
-- Extends existing meme automation with video support

-- ==============================================
-- 1. Create Video Posts Table
-- ==============================================

CREATE TABLE IF NOT EXISTS meme_videos (
  id SERIAL PRIMARY KEY,
  topic VARCHAR(100) NOT NULL,
  video_prompt TEXT NOT NULL,
  video_url TEXT,
  instagram_id VARCHAR(100),
  posted_at TIMESTAMP DEFAULT NOW(),
  success BOOLEAN DEFAULT TRUE,
  generation_time_seconds INTEGER,
  api_provider VARCHAR(50) DEFAULT 'replicate',
  video_duration_seconds INTEGER DEFAULT 15,
  replicate_prediction_id VARCHAR(255)
);

COMMENT ON TABLE meme_videos IS 'Stores history of AI-generated video meme posts';
COMMENT ON COLUMN meme_videos.topic IS 'Meme topic/theme (e.g., ai, coffee, coding)';
COMMENT ON COLUMN meme_videos.video_prompt IS 'Full prompt used for video generation';
COMMENT ON COLUMN meme_videos.video_url IS 'URL of generated video (hosted by API provider)';
COMMENT ON COLUMN meme_videos.instagram_id IS 'Instagram Reel ID after publishing';
COMMENT ON COLUMN meme_videos.generation_time_seconds IS 'Time taken for API to generate video';
COMMENT ON COLUMN meme_videos.api_provider IS 'API used (replicate, runway, veo, etc)';
COMMENT ON COLUMN meme_videos.replicate_prediction_id IS 'Replicate prediction ID for tracking';

-- ==============================================
-- 2. Create Indexes for Performance
-- ==============================================

CREATE INDEX IF NOT EXISTS idx_meme_videos_posted_at 
ON meme_videos(posted_at DESC);

CREATE INDEX IF NOT EXISTS idx_meme_videos_topic 
ON meme_videos(topic);

CREATE INDEX IF NOT EXISTS idx_meme_videos_success 
ON meme_videos(success);

CREATE INDEX IF NOT EXISTS idx_meme_videos_provider 
ON meme_videos(api_provider);

-- ==============================================
-- 3. Create Analytics View for Videos
-- ==============================================

CREATE OR REPLACE VIEW meme_videos_analytics AS
SELECT 
  DATE(posted_at) as date,
  COUNT(*) as total_videos,
  SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful_videos,
  SUM(CASE WHEN NOT success THEN 1 ELSE 0 END) as failed_videos,
  ROUND(100.0 * SUM(CASE WHEN success THEN 1 ELSE 0 END) / COUNT(*), 2) as success_rate,
  COUNT(DISTINCT topic) as unique_topics,
  AVG(generation_time_seconds) as avg_generation_time,
  api_provider
FROM meme_videos
GROUP BY DATE(posted_at), api_provider
ORDER BY date DESC;

COMMENT ON VIEW meme_videos_analytics IS 'Daily analytics for video meme generation and posting';

-- ==============================================
-- 4. Create Topic Performance View
-- ==============================================

CREATE OR REPLACE VIEW video_topic_stats AS
SELECT 
  topic,
  COUNT(*) as video_count,
  SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful,
  MAX(posted_at) as last_posted,
  AVG(generation_time_seconds) as avg_generation_time
FROM meme_videos
WHERE posted_at > NOW() - INTERVAL '30 days'
GROUP BY topic
ORDER BY video_count DESC;

COMMENT ON VIEW video_topic_stats IS 'Performance statistics by video topic for last 30 days';

-- ==============================================
-- 5. Create API Provider Stats View
-- ==============================================

CREATE OR REPLACE VIEW api_provider_stats AS
SELECT 
  api_provider,
  COUNT(*) as total_generations,
  SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful,
  ROUND(100.0 * SUM(CASE WHEN success THEN 1 ELSE 0 END) / COUNT(*), 2) as success_rate,
  AVG(generation_time_seconds) as avg_time_seconds,
  MIN(generation_time_seconds) as min_time,
  MAX(generation_time_seconds) as max_time
FROM meme_videos
WHERE posted_at > NOW() - INTERVAL '30 days'
GROUP BY api_provider
ORDER BY total_generations DESC;

COMMENT ON VIEW api_provider_stats IS 'Performance comparison of different video API providers';

-- ==============================================
-- 6. Create Cleanup Function for Old Videos
-- ==============================================

CREATE OR REPLACE FUNCTION cleanup_old_videos() 
RETURNS INTEGER AS $$
DECLARE
  deleted_count INTEGER;
BEGIN
  DELETE FROM meme_videos 
  WHERE posted_at < NOW() - INTERVAL '90 days';
  
  GET DIAGNOSTICS deleted_count = ROW_COUNT;
  
  RETURN deleted_count;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION cleanup_old_videos() IS 'Deletes video posts older than 90 days. Returns count of deleted rows.';

-- ==============================================
-- 7. Sample Queries
-- ==============================================

-- Check recent video posts
-- SELECT * FROM meme_videos ORDER BY posted_at DESC LIMIT 10;

-- View daily video analytics
-- SELECT * FROM meme_videos_analytics LIMIT 30;

-- Check topic performance
-- SELECT * FROM video_topic_stats;

-- Compare API providers
-- SELECT * FROM api_provider_stats;

-- Calculate total success rate
-- SELECT 
--   COUNT(*) as total,
--   SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful,
--   ROUND(100.0 * SUM(CASE WHEN success THEN 1 ELSE 0 END) / COUNT(*), 2) as success_rate,
--   AVG(generation_time_seconds) as avg_gen_time
-- FROM meme_videos
-- WHERE posted_at > NOW() - INTERVAL '30 days';

-- Find slowest generations
-- SELECT topic, video_prompt, generation_time_seconds, api_provider
-- FROM meme_videos 
-- WHERE generation_time_seconds IS NOT NULL
-- ORDER BY generation_time_seconds DESC 
-- LIMIT 10;

-- Check database size
-- SELECT pg_size_pretty(pg_table_size('meme_videos'));

-- ==============================================
-- 8. Combined View (Images + Videos)
-- ==============================================

-- If you have both meme_posts (images) and meme_videos tables:
CREATE OR REPLACE VIEW all_memes_combined AS
SELECT 
  'image' as media_type,
  id,
  topic,
  text0 || ' vs ' || text1 as description,
  meme_url as media_url,
  instagram_id,
  posted_at,
  success
FROM meme_posts
UNION ALL
SELECT 
  'video' as media_type,
  id,
  topic,
  video_prompt as description,
  video_url as media_url,
  instagram_id,
  posted_at,
  success
FROM meme_videos
ORDER BY posted_at DESC;

COMMENT ON VIEW all_memes_combined IS 'Combined view of both image and video memes';

-- ==============================================
-- Setup Complete!
-- ==============================================

-- Verify setup
SELECT 
  'meme_videos' as table_name,
  COUNT(*) as row_count,
  pg_size_pretty(pg_table_size('meme_videos')) as table_size
FROM meme_videos;

-- Show indexes
SELECT 
  indexname,
  indexdef
FROM pg_indexes
WHERE tablename = 'meme_videos';

-- Show views
SELECT 
  viewname
FROM pg_views
WHERE schemaname = 'public' 
  AND viewname LIKE '%video%';

-- ==============================================
-- Maintenance Commands
-- ==============================================

-- Vacuum table
-- VACUUM ANALYZE meme_videos;

-- Update statistics
-- ANALYZE meme_videos;

-- Reindex
-- REINDEX TABLE meme_videos;

-- Cleanup old data
-- SELECT cleanup_old_videos();

-- ==============================================
-- Monitoring Queries
-- ==============================================

-- Check generation performance trends
-- SELECT 
--   DATE(posted_at) as date,
--   AVG(generation_time_seconds) as avg_time,
--   MIN(generation_time_seconds) as min_time,
--   MAX(generation_time_seconds) as max_time,
--   api_provider
-- FROM meme_videos
-- WHERE posted_at > NOW() - INTERVAL '7 days'
-- GROUP BY DATE(posted_at), api_provider
-- ORDER BY date DESC;

-- Check hourly posting pattern
-- SELECT 
--   EXTRACT(HOUR FROM posted_at) as hour,
--   COUNT(*) as video_count
-- FROM meme_videos
-- WHERE posted_at > NOW() - INTERVAL '7 days'
-- GROUP BY EXTRACT(HOUR FROM posted_at)
-- ORDER BY hour;

-- Find most popular topics
-- SELECT 
--   topic,
--   COUNT(*) as count,
--   ROUND(AVG(generation_time_seconds), 2) as avg_gen_time
-- FROM meme_videos
-- WHERE posted_at > NOW() - INTERVAL '30 days'
-- GROUP BY topic
-- ORDER BY count DESC
-- LIMIT 10;

RAISE NOTICE 'Video meme automation database setup complete!';
RAISE NOTICE 'Table: meme_videos';
RAISE NOTICE 'Views: meme_videos_analytics, video_topic_stats, api_provider_stats';
RAISE NOTICE 'Function: cleanup_old_videos()';
RAISE NOTICE 'Ready to import video generation workflow!';
