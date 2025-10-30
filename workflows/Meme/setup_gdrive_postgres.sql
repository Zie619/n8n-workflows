-- PostgreSQL setup for Multi-Platform Meme Videos with Google Drive Backup
-- Run this script after deploying to Heroku with PostgreSQL addon

-- Drop existing table if you're updating from multiplatform setup
-- DROP TABLE IF EXISTS meme_videos_multiplatform_gdrive CASCADE;

-- Create main table for tracking multi-platform posts with Google Drive backup
CREATE TABLE IF NOT EXISTS meme_videos_multiplatform_gdrive (
  id SERIAL PRIMARY KEY,
  topic VARCHAR(100) NOT NULL,
  video_prompt TEXT NOT NULL,
  video_url TEXT NOT NULL,
  
  -- Platform IDs
  instagram_id VARCHAR(100),
  youtube_id VARCHAR(100),
  tiktok_id VARCHAR(100),
  
  -- Google Drive backup info
  google_drive_id VARCHAR(255),
  google_drive_url TEXT,
  drive_folder VARCHAR(100),
  
  -- Array of successfully posted platforms
  platforms_posted TEXT[] DEFAULT '{}',
  
  -- Metadata
  api_provider VARCHAR(50),
  posted_at TIMESTAMP DEFAULT NOW(),
  success BOOLEAN DEFAULT true,
  error_message TEXT,
  
  -- Indexes for faster queries
  CONSTRAINT unique_video_post UNIQUE(topic, posted_at)
);

-- Create indexes for common queries
CREATE INDEX IF NOT EXISTS idx_topic_date ON meme_videos_multiplatform_gdrive(topic, posted_at DESC);
CREATE INDEX IF NOT EXISTS idx_posted_at ON meme_videos_multiplatform_gdrive(posted_at DESC);
CREATE INDEX IF NOT EXISTS idx_platforms ON meme_videos_multiplatform_gdrive USING gin(platforms_posted);
CREATE INDEX IF NOT EXISTS idx_drive_folder ON meme_videos_multiplatform_gdrive(drive_folder);
CREATE INDEX IF NOT EXISTS idx_success ON meme_videos_multiplatform_gdrive(success, posted_at DESC);

-- View: Multi-platform analytics with Google Drive stats
CREATE OR REPLACE VIEW multiplatform_gdrive_analytics AS
SELECT 
  DATE(posted_at) as date,
  COUNT(*) as total_posts,
  COUNT(CASE WHEN success THEN 1 END) as successful_posts,
  COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) THEN 1 END) as instagram_posts,
  COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) THEN 1 END) as youtube_posts,
  COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) THEN 1 END) as tiktok_posts,
  COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END) as drive_backups,
  ROUND(AVG(CASE WHEN success THEN 100.0 ELSE 0 END), 2) as success_rate,
  api_provider,
  ROUND(AVG(array_length(platforms_posted, 1)), 2) as avg_platforms_per_post
FROM meme_videos_multiplatform_gdrive
WHERE posted_at >= NOW() - INTERVAL '30 days'
GROUP BY DATE(posted_at), api_provider
ORDER BY date DESC, api_provider;

-- View: Platform comparison with Google Drive backup rate
CREATE OR REPLACE VIEW platform_gdrive_comparison AS
SELECT 
  'Instagram' as platform,
  COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) THEN 1 END) as successful_posts,
  COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) AND google_drive_id IS NOT NULL THEN 1 END) as backed_up_posts,
  ROUND(100.0 * COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) THEN 1 END) / NULLIF(COUNT(*), 0), 2) as success_rate
FROM meme_videos_multiplatform_gdrive
WHERE posted_at >= NOW() - INTERVAL '7 days'
UNION ALL
SELECT 
  'YouTube' as platform,
  COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) THEN 1 END),
  COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) AND google_drive_id IS NOT NULL THEN 1 END),
  ROUND(100.0 * COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) THEN 1 END) / NULLIF(COUNT(*), 0), 2)
FROM meme_videos_multiplatform_gdrive
WHERE posted_at >= NOW() - INTERVAL '7 days'
UNION ALL
SELECT 
  'TikTok' as platform,
  COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) THEN 1 END),
  COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) AND google_drive_id IS NOT NULL THEN 1 END),
  ROUND(100.0 * COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) THEN 1 END) / NULLIF(COUNT(*), 0), 2)
FROM meme_videos_multiplatform_gdrive
WHERE posted_at >= NOW() - INTERVAL '7 days'
UNION ALL
SELECT 
  'Google Drive' as platform,
  COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END),
  COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END),
  ROUND(100.0 * COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END) / NULLIF(COUNT(*), 0), 2)
FROM meme_videos_multiplatform_gdrive
WHERE posted_at >= NOW() - INTERVAL '7 days';

-- View: Topic performance by platform with Drive folder organization
CREATE OR REPLACE VIEW topic_platform_gdrive_performance AS
SELECT 
  topic,
  drive_folder,
  COUNT(*) as total_posts,
  COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) THEN 1 END) as instagram_count,
  COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) THEN 1 END) as youtube_count,
  COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) THEN 1 END) as tiktok_count,
  COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END) as drive_backup_count,
  ROUND(AVG(array_length(platforms_posted, 1)), 2) as avg_platforms,
  MAX(posted_at) as last_posted
FROM meme_videos_multiplatform_gdrive
WHERE posted_at >= NOW() - INTERVAL '30 days'
GROUP BY topic, drive_folder
ORDER BY total_posts DESC, last_posted DESC;

-- View: Google Drive storage analytics
CREATE OR REPLACE VIEW gdrive_storage_analytics AS
SELECT 
  drive_folder,
  COUNT(*) as video_count,
  COUNT(DISTINCT topic) as unique_topics,
  MIN(posted_at) as oldest_video,
  MAX(posted_at) as newest_video,
  ROUND(AVG(array_length(platforms_posted, 1)), 2) as avg_platforms_per_video,
  COUNT(CASE WHEN success THEN 1 END) as successful_uploads,
  ROUND(100.0 * COUNT(CASE WHEN success THEN 1 END) / COUNT(*), 2) as success_rate
FROM meme_videos_multiplatform_gdrive
WHERE google_drive_id IS NOT NULL
GROUP BY drive_folder
ORDER BY video_count DESC;

-- View: Failed platform posts (for troubleshooting)
CREATE OR REPLACE VIEW failed_platform_gdrive_posts AS
SELECT 
  id,
  topic,
  posted_at,
  CASE 
    WHEN instagram_id IS NULL THEN 'Instagram'
    WHEN youtube_id IS NULL THEN 'YouTube'
    WHEN tiktok_id IS NULL THEN 'TikTok'
    WHEN google_drive_id IS NULL THEN 'Google Drive'
  END as failed_platform,
  platforms_posted,
  google_drive_id IS NOT NULL as has_backup,
  error_message,
  video_url
FROM meme_videos_multiplatform_gdrive
WHERE 
  NOT success 
  OR array_length(platforms_posted, 1) < 4  -- Should have all 4: instagram, youtube, tiktok, google_drive
  OR google_drive_id IS NULL  -- Missing Google Drive backup
ORDER BY posted_at DESC
LIMIT 50;

-- View: Daily backup completion rate
CREATE OR REPLACE VIEW daily_backup_completion AS
SELECT 
  DATE(posted_at) as date,
  COUNT(*) as total_videos,
  COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END) as backed_up,
  COUNT(CASE WHEN google_drive_id IS NULL THEN 1 END) as not_backed_up,
  ROUND(100.0 * COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END) / COUNT(*), 2) as backup_rate,
  ROUND(100.0 * COUNT(CASE WHEN array_length(platforms_posted, 1) >= 4 THEN 1 END) / COUNT(*), 2) as full_success_rate
FROM meme_videos_multiplatform_gdrive
WHERE posted_at >= NOW() - INTERVAL '30 days'
GROUP BY DATE(posted_at)
ORDER BY date DESC;

-- Function: Get platform statistics for recent period
CREATE OR REPLACE FUNCTION get_platform_gdrive_stats(days_back INTEGER DEFAULT 7)
RETURNS TABLE (
  platform TEXT,
  post_count BIGINT,
  success_rate NUMERIC,
  has_drive_backup BIGINT,
  backup_rate NUMERIC
) AS $$
BEGIN
  RETURN QUERY
  SELECT 
    'Instagram'::TEXT,
    COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) THEN 1 END),
    ROUND(100.0 * COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) THEN 1 END) / NULLIF(COUNT(*), 0), 2),
    COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) AND google_drive_id IS NOT NULL THEN 1 END),
    ROUND(100.0 * COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) AND google_drive_id IS NOT NULL THEN 1 END) / NULLIF(COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) THEN 1 END), 0), 2)
  FROM meme_videos_multiplatform_gdrive
  WHERE posted_at >= NOW() - (days_back || ' days')::INTERVAL
  
  UNION ALL
  
  SELECT 
    'YouTube'::TEXT,
    COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) THEN 1 END),
    ROUND(100.0 * COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) THEN 1 END) / NULLIF(COUNT(*), 0), 2),
    COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) AND google_drive_id IS NOT NULL THEN 1 END),
    ROUND(100.0 * COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) AND google_drive_id IS NOT NULL THEN 1 END) / NULLIF(COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) THEN 1 END), 0), 2)
  FROM meme_videos_multiplatform_gdrive
  WHERE posted_at >= NOW() - (days_back || ' days')::INTERVAL
  
  UNION ALL
  
  SELECT 
    'TikTok'::TEXT,
    COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) THEN 1 END),
    ROUND(100.0 * COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) THEN 1 END) / NULLIF(COUNT(*), 0), 2),
    COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) AND google_drive_id IS NOT NULL THEN 1 END),
    ROUND(100.0 * COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) AND google_drive_id IS NOT NULL THEN 1 END) / NULLIF(COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) THEN 1 END), 0), 2)
  FROM meme_videos_multiplatform_gdrive
  WHERE posted_at >= NOW() - (days_back || ' days')::INTERVAL
  
  UNION ALL
  
  SELECT 
    'Google Drive'::TEXT,
    COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END),
    ROUND(100.0 * COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END) / NULLIF(COUNT(*), 0), 2),
    COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END),
    100.00
  FROM meme_videos_multiplatform_gdrive
  WHERE posted_at >= NOW() - (days_back || ' days')::INTERVAL;
END;
$$ LANGUAGE plpgsql;

-- Function: Check platform health including Google Drive
CREATE OR REPLACE FUNCTION check_platform_gdrive_health()
RETURNS TABLE (
  platform TEXT,
  status TEXT,
  last_success TIMESTAMP,
  recent_failures BIGINT,
  health_score NUMERIC
) AS $$
BEGIN
  RETURN QUERY
  WITH recent_posts AS (
    SELECT * FROM meme_videos_multiplatform_gdrive
    WHERE posted_at >= NOW() - INTERVAL '24 hours'
  )
  SELECT 
    'Instagram'::TEXT,
    CASE 
      WHEN COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) THEN 1 END) >= 2 THEN 'Healthy'
      WHEN COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) THEN 1 END) >= 1 THEN 'Warning'
      ELSE 'Critical'
    END,
    MAX(CASE WHEN 'instagram' = ANY(platforms_posted) THEN posted_at END),
    COUNT(CASE WHEN 'instagram' != ALL(platforms_posted) THEN 1 END),
    ROUND(100.0 * COUNT(CASE WHEN 'instagram' = ANY(platforms_posted) THEN 1 END) / NULLIF(COUNT(*), 0), 2)
  FROM recent_posts
  
  UNION ALL
  
  SELECT 
    'YouTube'::TEXT,
    CASE 
      WHEN COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) THEN 1 END) >= 2 THEN 'Healthy'
      WHEN COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) THEN 1 END) >= 1 THEN 'Warning'
      ELSE 'Critical'
    END,
    MAX(CASE WHEN 'youtube' = ANY(platforms_posted) THEN posted_at END),
    COUNT(CASE WHEN 'youtube' != ALL(platforms_posted) THEN 1 END),
    ROUND(100.0 * COUNT(CASE WHEN 'youtube' = ANY(platforms_posted) THEN 1 END) / NULLIF(COUNT(*), 0), 2)
  FROM recent_posts
  
  UNION ALL
  
  SELECT 
    'TikTok'::TEXT,
    CASE 
      WHEN COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) THEN 1 END) >= 2 THEN 'Healthy'
      WHEN COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) THEN 1 END) >= 1 THEN 'Warning'
      ELSE 'Critical'
    END,
    MAX(CASE WHEN 'tiktok' = ANY(platforms_posted) THEN posted_at END),
    COUNT(CASE WHEN 'tiktok' != ALL(platforms_posted) THEN 1 END),
    ROUND(100.0 * COUNT(CASE WHEN 'tiktok' = ANY(platforms_posted) THEN 1 END) / NULLIF(COUNT(*), 0), 2)
  FROM recent_posts
  
  UNION ALL
  
  SELECT 
    'Google Drive'::TEXT,
    CASE 
      WHEN COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END) >= 2 THEN 'Healthy'
      WHEN COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END) >= 1 THEN 'Warning'
      ELSE 'Critical'
    END,
    MAX(CASE WHEN google_drive_id IS NOT NULL THEN posted_at END),
    COUNT(CASE WHEN google_drive_id IS NULL THEN 1 END),
    ROUND(100.0 * COUNT(CASE WHEN google_drive_id IS NOT NULL THEN 1 END) / NULLIF(COUNT(*), 0), 2)
  FROM recent_posts;
END;
$$ LANGUAGE plpgsql;

-- Function: Get Drive folder statistics
CREATE OR REPLACE FUNCTION get_drive_folder_stats()
RETURNS TABLE (
  folder_name TEXT,
  video_count BIGINT,
  total_size_estimate_mb NUMERIC,
  oldest_video TIMESTAMP,
  newest_video TIMESTAMP,
  avg_platforms_per_video NUMERIC
) AS $$
BEGIN
  RETURN QUERY
  SELECT 
    COALESCE(drive_folder, 'Uncategorized')::TEXT,
    COUNT(*),
    -- Estimate: ~10MB per 10-second video
    ROUND(COUNT(*) * 10.0, 2),
    MIN(posted_at),
    MAX(posted_at),
    ROUND(AVG(array_length(platforms_posted, 1)), 2)
  FROM meme_videos_multiplatform_gdrive
  WHERE google_drive_id IS NOT NULL
  GROUP BY drive_folder
  ORDER BY COUNT(*) DESC;
END;
$$ LANGUAGE plpgsql;

-- Maintenance: Delete old records (keep last 90 days)
CREATE OR REPLACE FUNCTION cleanup_old_gdrive_records()
RETURNS INTEGER AS $$
DECLARE
  deleted_count INTEGER;
BEGIN
  DELETE FROM meme_videos_multiplatform_gdrive
  WHERE posted_at < NOW() - INTERVAL '90 days'
  AND google_drive_id IS NOT NULL;  -- Only delete if backed up to Drive
  
  GET DIAGNOSTICS deleted_count = ROW_COUNT;
  RETURN deleted_count;
END;
$$ LANGUAGE plpgsql;

-- Grant permissions (adjust if needed)
-- GRANT SELECT, INSERT, UPDATE ON meme_videos_multiplatform_gdrive TO your_n8n_user;
-- GRANT USAGE, SELECT ON SEQUENCE meme_videos_multiplatform_gdrive_id_seq TO your_n8n_user;

-- Sample queries you can run:

-- Check recent posts with Drive backup status
-- SELECT topic, posted_at, platforms_posted, google_drive_id IS NOT NULL as has_backup
-- FROM meme_videos_multiplatform_gdrive
-- ORDER BY posted_at DESC LIMIT 10;

-- Get platform health report
-- SELECT * FROM check_platform_gdrive_health();

-- See Drive folder organization
-- SELECT * FROM gdrive_storage_analytics;

-- Get statistics for last 7 days
-- SELECT * FROM get_platform_gdrive_stats(7);

-- Check Drive folder stats
-- SELECT * FROM get_drive_folder_stats();

-- View backup completion rates
-- SELECT * FROM daily_backup_completion;

COMMENT ON TABLE meme_videos_multiplatform_gdrive IS 'Tracks meme videos posted to Instagram, YouTube, TikTok with Google Drive backup';
COMMENT ON COLUMN meme_videos_multiplatform_gdrive.google_drive_id IS 'Google Drive file ID for backup';
COMMENT ON COLUMN meme_videos_multiplatform_gdrive.google_drive_url IS 'Direct link to view video in Google Drive';
COMMENT ON COLUMN meme_videos_multiplatform_gdrive.drive_folder IS 'Category folder in Drive (AI & Technology, Comedy, Lifestyle, etc.)';
COMMENT ON COLUMN meme_videos_multiplatform_gdrive.platforms_posted IS 'Array of platforms where video was successfully posted';
