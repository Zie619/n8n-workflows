-- PostgreSQL Setup Script for Meme Automation Workflow
-- Run this script to set up your database tables and indexes

-- ==============================================
-- 1. Create Main Table
-- ==============================================

CREATE TABLE IF NOT EXISTS meme_posts (
  id SERIAL PRIMARY KEY,
  template_id VARCHAR(50) NOT NULL,
  topic VARCHAR(100) NOT NULL,
  text0 VARCHAR(255) NOT NULL,
  text1 VARCHAR(255) NOT NULL,
  meme_url TEXT,
  instagram_id VARCHAR(100),
  posted_at TIMESTAMP DEFAULT NOW(),
  success BOOLEAN DEFAULT TRUE
);

COMMENT ON TABLE meme_posts IS 'Stores history of meme posts for tracking and deduplication';
COMMENT ON COLUMN meme_posts.template_id IS 'ImgFlip template ID used for the meme';
COMMENT ON COLUMN meme_posts.topic IS 'Meme topic/category (e.g., coding, coffee, remote)';
COMMENT ON COLUMN meme_posts.text0 IS 'Top text of the meme';
COMMENT ON COLUMN meme_posts.text1 IS 'Bottom text of the meme';
COMMENT ON COLUMN meme_posts.meme_url IS 'URL of the generated meme image (hosted by ImgFlip)';
COMMENT ON COLUMN meme_posts.instagram_id IS 'Instagram post ID after successful publishing';
COMMENT ON COLUMN meme_posts.posted_at IS 'Timestamp when meme was posted';
COMMENT ON COLUMN meme_posts.success IS 'Whether the post was successful or failed';

-- ==============================================
-- 2. Create Indexes for Performance
-- ==============================================

-- Index for recent posts lookup (used for deduplication)
CREATE INDEX IF NOT EXISTS idx_meme_posts_posted_at 
ON meme_posts(posted_at DESC);

-- Index for topic filtering
CREATE INDEX IF NOT EXISTS idx_meme_posts_topic 
ON meme_posts(topic);

-- Index for success rate queries
CREATE INDEX IF NOT EXISTS idx_meme_posts_success 
ON meme_posts(success);

-- Composite index for deduplication queries
CREATE INDEX IF NOT EXISTS idx_meme_posts_dedup 
ON meme_posts(template_id, topic, posted_at DESC);

-- ==============================================
-- 3. Create Analytics View
-- ==============================================

CREATE OR REPLACE VIEW meme_analytics AS
SELECT 
  DATE(posted_at) as date,
  COUNT(*) as total_posts,
  SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful_posts,
  SUM(CASE WHEN NOT success THEN 1 ELSE 0 END) as failed_posts,
  ROUND(100.0 * SUM(CASE WHEN success THEN 1 ELSE 0 END) / COUNT(*), 2) as success_rate,
  COUNT(DISTINCT topic) as unique_topics,
  COUNT(DISTINCT template_id) as unique_templates
FROM meme_posts
GROUP BY DATE(posted_at)
ORDER BY date DESC;

COMMENT ON VIEW meme_analytics IS 'Daily analytics for meme posting performance';

-- ==============================================
-- 4. Create Topic Stats View
-- ==============================================

CREATE OR REPLACE VIEW topic_stats AS
SELECT 
  topic,
  COUNT(*) as post_count,
  SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful,
  MAX(posted_at) as last_posted,
  COUNT(DISTINCT template_id) as templates_used
FROM meme_posts
WHERE posted_at > NOW() - INTERVAL '30 days'
GROUP BY topic
ORDER BY post_count DESC;

COMMENT ON VIEW topic_stats IS 'Statistics by topic for the last 30 days';

-- ==============================================
-- 5. Create Cleanup Function (Optional)
-- ==============================================

-- This function automatically deletes posts older than 90 days
-- Keeps database small and fast

CREATE OR REPLACE FUNCTION cleanup_old_posts() 
RETURNS INTEGER AS $$
DECLARE
  deleted_count INTEGER;
BEGIN
  DELETE FROM meme_posts 
  WHERE posted_at < NOW() - INTERVAL '90 days';
  
  GET DIAGNOSTICS deleted_count = ROW_COUNT;
  
  RETURN deleted_count;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION cleanup_old_posts() IS 'Deletes meme posts older than 90 days. Returns count of deleted rows.';

-- ==============================================
-- 6. Create Scheduled Cleanup (Optional)
-- ==============================================

-- Note: Heroku PostgreSQL doesn't support pg_cron extension
-- Run cleanup manually or via a separate n8n workflow

-- Manual cleanup command:
-- SELECT cleanup_old_posts();

-- ==============================================
-- 7. Sample Queries
-- ==============================================

-- Check recent posts
-- SELECT * FROM meme_posts ORDER BY posted_at DESC LIMIT 10;

-- View daily analytics
-- SELECT * FROM meme_analytics LIMIT 30;

-- Check topic performance
-- SELECT * FROM topic_stats;

-- Calculate overall success rate
-- SELECT 
--   COUNT(*) as total,
--   SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful,
--   ROUND(100.0 * SUM(CASE WHEN success THEN 1 ELSE 0 END) / COUNT(*), 2) as success_rate
-- FROM meme_posts
-- WHERE posted_at > NOW() - INTERVAL '30 days';

-- Find most popular template
-- SELECT 
--   template_id, 
--   COUNT(*) as usage_count 
-- FROM meme_posts 
-- WHERE posted_at > NOW() - INTERVAL '30 days'
-- GROUP BY template_id 
-- ORDER BY usage_count DESC;

-- Check database size
-- SELECT pg_size_pretty(pg_table_size('meme_posts'));

-- ==============================================
-- 8. Grant Permissions (if needed)
-- ==============================================

-- Usually not needed on Heroku, but included for completeness
-- GRANT SELECT, INSERT ON meme_posts TO your_n8n_user;
-- GRANT SELECT ON meme_analytics TO your_n8n_user;
-- GRANT SELECT ON topic_stats TO your_n8n_user;

-- ==============================================
-- Setup Complete!
-- ==============================================

-- Verify setup
SELECT 
  'meme_posts' as table_name,
  COUNT(*) as row_count,
  pg_size_pretty(pg_table_size('meme_posts')) as table_size
FROM meme_posts;

-- Show indexes
SELECT 
  indexname,
  indexdef
FROM pg_indexes
WHERE tablename = 'meme_posts';

-- Test with sample data (optional, uncomment to run)
-- INSERT INTO meme_posts (template_id, topic, text0, text1, meme_url, instagram_id, success)
-- VALUES 
--   ('181913649', 'test', 'Test Top', 'Test Bottom', 'https://example.com/meme.jpg', '12345', TRUE);

-- Verify insert
-- SELECT * FROM meme_posts ORDER BY id DESC LIMIT 1;

-- Clean up test data (optional)
-- DELETE FROM meme_posts WHERE topic = 'test';

-- ==============================================
-- Maintenance Commands
-- ==============================================

-- Run these periodically for optimal performance:

-- 1. Vacuum (reclaim space)
-- VACUUM ANALYZE meme_posts;

-- 2. Update statistics
-- ANALYZE meme_posts;

-- 3. Reindex (if needed)
-- REINDEX TABLE meme_posts;

-- 4. Cleanup old data
-- SELECT cleanup_old_posts();

-- ==============================================
-- Monitoring Commands
-- ==============================================

-- Check active connections
-- SELECT count(*) FROM pg_stat_activity;

-- Check table statistics
-- SELECT 
--   schemaname,
--   relname,
--   n_live_tup as live_rows,
--   n_dead_tup as dead_rows,
--   last_vacuum,
--   last_autovacuum,
--   last_analyze,
--   last_autoanalyze
-- FROM pg_stat_user_tables
-- WHERE relname = 'meme_posts';

-- Check cache hit rate
-- SELECT 
--   sum(heap_blks_read) as heap_read,
--   sum(heap_blks_hit) as heap_hit,
--   sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) * 100 as cache_hit_ratio
-- FROM pg_statio_user_tables;

-- ==============================================
-- Backup Recommendations
-- ==============================================

-- Heroku automatically backs up your database
-- You can also create manual backups:
-- 
-- Via Heroku CLI:
-- heroku pg:backups:capture -a your-app-name
-- heroku pg:backups:download -a your-app-name
--
-- Or export data:
-- COPY meme_posts TO '/tmp/meme_posts_backup.csv' CSV HEADER;

RAISE NOTICE 'Meme automation database setup complete!';
RAISE NOTICE 'Table: meme_posts';
RAISE NOTICE 'Views: meme_analytics, topic_stats';
RAISE NOTICE 'Function: cleanup_old_posts()';
RAISE NOTICE 'Ready to import n8n workflow!';
