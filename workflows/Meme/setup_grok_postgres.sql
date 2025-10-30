-- PostgreSQL Setup for Grok AI + Multi-Platform Meme Automation
-- This script creates tables and views for tracking AI-powered (Grok + Perplexity) video memes

-- =============================================================================
-- TABLE: meme_videos_ai_powered
-- Unified table for all AI-powered meme videos (Grok + Perplexity)
-- =============================================================================

CREATE TABLE IF NOT EXISTS meme_videos_ai_powered (
    id SERIAL PRIMARY KEY,
    
    -- Content information
    topic VARCHAR(100) NOT NULL,
    video_prompt TEXT NOT NULL,
    video_url TEXT NOT NULL,
    
    -- Platform IDs
    instagram_id VARCHAR(100),
    youtube_id VARCHAR(100),
    tiktok_id VARCHAR(100),
    
    -- Google Drive backup
    google_drive_id VARCHAR(255),
    google_drive_url TEXT,
    drive_folder VARCHAR(100),
    
    -- AI Provider information (NEW)
    ai_provider VARCHAR(50) NOT NULL DEFAULT 'manual',
    -- Options: 'grok', 'perplexity', 'manual', 'manual_fallback'
    
    content_style VARCHAR(50),
    -- Options: 'safe', 'edgy', 'controversial', 'professional'
    
    viral_score INTEGER,
    -- 1-10 scale, higher = more viral potential
    -- Grok typically: 8-10
    -- Perplexity typically: 6-8
    -- Manual typically: 5-7
    
    -- Tracking
    platforms_posted TEXT[],
    -- Array of successful platforms: ['instagram', 'youtube', 'tiktok', 'google_drive']
    
    api_provider VARCHAR(50),
    -- Video generation API: 'veo2', 'veo3', 'replicate', 'runway'
    
    -- Cost tracking
    estimated_cost DECIMAL(10,4),
    -- Estimated API cost for this post (video + AI)
    
    -- Metadata
    posted_at TIMESTAMP DEFAULT NOW(),
    success BOOLEAN DEFAULT TRUE,
    error_message TEXT,
    
    -- Indexes for performance
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_ai_provider ON meme_videos_ai_powered(ai_provider);
CREATE INDEX IF NOT EXISTS idx_content_style ON meme_videos_ai_powered(content_style);
CREATE INDEX IF NOT EXISTS idx_viral_score ON meme_videos_ai_powered(viral_score);
CREATE INDEX IF NOT EXISTS idx_posted_at ON meme_videos_ai_powered(posted_at);
CREATE INDEX IF NOT EXISTS idx_success ON meme_videos_ai_powered(success);

-- =============================================================================
-- VIEW: ai_provider_analytics
-- Daily analytics by AI provider
-- =============================================================================

CREATE OR REPLACE VIEW ai_provider_analytics AS
SELECT 
    DATE(posted_at) as day,
    ai_provider,
    COUNT(*) as total_posts,
    SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful_posts,
    ROUND(SUM(CASE WHEN success THEN 1 ELSE 0 END)::NUMERIC / COUNT(*) * 100, 2) as success_rate,
    AVG(viral_score) as avg_viral_score,
    SUM(estimated_cost) as total_cost,
    ROUND(SUM(estimated_cost) / COUNT(*), 4) as avg_cost_per_post,
    ARRAY_AGG(DISTINCT topic) as topics_used
FROM meme_videos_ai_powered
GROUP BY DATE(posted_at), ai_provider
ORDER BY day DESC, ai_provider;

-- =============================================================================
-- VIEW: grok_vs_perplexity_performance
-- Direct comparison of Grok vs Perplexity performance
-- =============================================================================

CREATE OR REPLACE VIEW grok_vs_perplexity_performance AS
WITH grok_stats AS (
    SELECT 
        COUNT(*) as grok_total_posts,
        AVG(viral_score) as grok_avg_viral_score,
        SUM(CASE WHEN success THEN 1 ELSE 0 END)::FLOAT / COUNT(*) * 100 as grok_success_rate,
        SUM(estimated_cost) as grok_total_cost,
        SUM(estimated_cost) / COUNT(*) as grok_avg_cost,
        COUNT(DISTINCT topic) as grok_unique_topics
    FROM meme_videos_ai_powered
    WHERE ai_provider = 'grok'
),
perplexity_stats AS (
    SELECT 
        COUNT(*) as perplexity_total_posts,
        AVG(viral_score) as perplexity_avg_viral_score,
        SUM(CASE WHEN success THEN 1 ELSE 0 END)::FLOAT / COUNT(*) * 100 as perplexity_success_rate,
        SUM(estimated_cost) as perplexity_total_cost,
        SUM(estimated_cost) / COUNT(*) as perplexity_avg_cost,
        COUNT(DISTINCT topic) as perplexity_unique_topics
    FROM meme_videos_ai_powered
    WHERE ai_provider = 'perplexity'
)
SELECT 
    g.*,
    p.*,
    CASE 
        WHEN g.grok_avg_viral_score > p.perplexity_avg_viral_score THEN 'Grok'
        WHEN g.grok_avg_viral_score < p.perplexity_avg_viral_score THEN 'Perplexity'
        ELSE 'Tie'
    END as higher_viral_potential,
    CASE
        WHEN g.grok_success_rate > p.perplexity_success_rate THEN 'Grok'
        WHEN g.grok_success_rate < p.perplexity_success_rate THEN 'Perplexity'
        ELSE 'Tie'
    END as higher_success_rate,
    CASE
        WHEN g.grok_avg_cost < p.perplexity_avg_cost THEN 'Grok'
        WHEN g.grok_avg_cost > p.perplexity_avg_cost THEN 'Perplexity'
        ELSE 'Tie'
    END as lower_cost_per_post
FROM grok_stats g, perplexity_stats p;

-- =============================================================================
-- VIEW: ai_platform_success
-- Success rates by AI provider and platform
-- =============================================================================

CREATE OR REPLACE VIEW ai_platform_success AS
SELECT 
    ai_provider,
    CASE 
        WHEN 'instagram' = ANY(platforms_posted) THEN 'Instagram'
        ELSE NULL
    END as platform,
    COUNT(*) FILTER (WHERE 'instagram' = ANY(platforms_posted)) as instagram_posts,
    COUNT(*) FILTER (WHERE 'youtube' = ANY(platforms_posted)) as youtube_posts,
    COUNT(*) FILTER (WHERE 'tiktok' = ANY(platforms_posted)) as tiktok_posts,
    COUNT(*) FILTER (WHERE 'google_drive' = ANY(platforms_posted)) as drive_backups,
    ROUND(
        COUNT(*) FILTER (WHERE 'instagram' = ANY(platforms_posted))::NUMERIC / 
        NULLIF(COUNT(*), 0) * 100, 
        2
    ) as instagram_success_rate,
    ROUND(
        COUNT(*) FILTER (WHERE 'youtube' = ANY(platforms_posted))::NUMERIC / 
        NULLIF(COUNT(*), 0) * 100, 
        2
    ) as youtube_success_rate,
    ROUND(
        COUNT(*) FILTER (WHERE 'tiktok' = ANY(platforms_posted))::NUMERIC / 
        NULLIF(COUNT(*), 0) * 100, 
        2
    ) as tiktok_success_rate
FROM meme_videos_ai_powered
GROUP BY ai_provider
ORDER BY ai_provider;

-- =============================================================================
-- VIEW: top_trending_by_ai_provider
-- Most used topics by each AI provider
-- =============================================================================

CREATE OR REPLACE VIEW top_trending_by_ai_provider AS
SELECT 
    ai_provider,
    topic,
    COUNT(*) as times_used,
    AVG(viral_score) as avg_viral_score,
    SUM(CASE WHEN success THEN 1 ELSE 0 END)::FLOAT / COUNT(*) * 100 as success_rate,
    content_style,
    MAX(posted_at) as last_used
FROM meme_videos_ai_powered
GROUP BY ai_provider, topic, content_style
ORDER BY ai_provider, times_used DESC, avg_viral_score DESC;

-- =============================================================================
-- VIEW: content_style_analysis
-- Performance by content style
-- =============================================================================

CREATE OR REPLACE VIEW content_style_analysis AS
SELECT 
    content_style,
    ai_provider,
    COUNT(*) as total_posts,
    AVG(viral_score) as avg_viral_score,
    SUM(CASE WHEN success THEN 1 ELSE 0 END)::FLOAT / COUNT(*) * 100 as success_rate,
    COUNT(*) FILTER (WHERE 'instagram' = ANY(platforms_posted))::FLOAT / COUNT(*) * 100 as instagram_rate,
    COUNT(*) FILTER (WHERE 'youtube' = ANY(platforms_posted))::FLOAT / COUNT(*) * 100 as youtube_rate,
    COUNT(*) FILTER (WHERE 'tiktok' = ANY(platforms_posted))::FLOAT / COUNT(*) * 100 as tiktok_rate
FROM meme_videos_ai_powered
GROUP BY content_style, ai_provider
ORDER BY ai_provider, avg_viral_score DESC;

-- =============================================================================
-- VIEW: ai_cost_comparison
-- Monthly cost comparison by AI provider
-- =============================================================================

CREATE OR REPLACE VIEW ai_cost_comparison AS
SELECT 
    DATE_TRUNC('month', posted_at) as month,
    ai_provider,
    COUNT(*) as total_posts,
    SUM(estimated_cost) as total_cost,
    ROUND(SUM(estimated_cost) / COUNT(*), 4) as avg_cost_per_post,
    ROUND(SUM(estimated_cost) / EXTRACT(DAY FROM DATE_TRUNC('month', posted_at) + INTERVAL '1 month' - INTERVAL '1 day'), 2) as estimated_monthly_cost
FROM meme_videos_ai_powered
GROUP BY DATE_TRUNC('month', posted_at), ai_provider
ORDER BY month DESC, ai_provider;

-- =============================================================================
-- VIEW: viral_potential_tracking
-- Track which concepts have highest viral potential
-- =============================================================================

CREATE OR REPLACE VIEW viral_potential_tracking AS
SELECT 
    topic,
    content_style,
    ai_provider,
    AVG(viral_score) as avg_viral_score,
    COUNT(*) as times_used,
    SUM(CASE WHEN success THEN 1 ELSE 0 END)::FLOAT / COUNT(*) * 100 as success_rate,
    MAX(posted_at) as last_used,
    CASE 
        WHEN AVG(viral_score) >= 9 THEN 'Very High'
        WHEN AVG(viral_score) >= 7 THEN 'High'
        WHEN AVG(viral_score) >= 5 THEN 'Medium'
        ELSE 'Low'
    END as viral_category
FROM meme_videos_ai_powered
GROUP BY topic, content_style, ai_provider
HAVING COUNT(*) >= 1
ORDER BY avg_viral_score DESC, success_rate DESC;

-- =============================================================================
-- FUNCTION: get_ai_stats
-- Get comprehensive statistics for specific AI provider over N days
-- =============================================================================

CREATE OR REPLACE FUNCTION get_ai_stats(
    provider VARCHAR(50),
    days_back INTEGER DEFAULT 7
)
RETURNS TABLE (
    total_posts BIGINT,
    successful_posts BIGINT,
    success_rate NUMERIC,
    avg_viral_score NUMERIC,
    total_cost NUMERIC,
    avg_cost_per_post NUMERIC,
    unique_topics BIGINT,
    most_common_style VARCHAR(50),
    instagram_posts BIGINT,
    youtube_posts BIGINT,
    tiktok_posts BIGINT,
    drive_backups BIGINT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        COUNT(*)::BIGINT as total_posts,
        SUM(CASE WHEN success THEN 1 ELSE 0 END)::BIGINT as successful_posts,
        ROUND(SUM(CASE WHEN success THEN 1 ELSE 0 END)::NUMERIC / COUNT(*) * 100, 2) as success_rate,
        ROUND(AVG(m.viral_score)::NUMERIC, 2) as avg_viral_score,
        ROUND(SUM(m.estimated_cost)::NUMERIC, 2) as total_cost,
        ROUND(SUM(m.estimated_cost)::NUMERIC / COUNT(*), 4) as avg_cost_per_post,
        COUNT(DISTINCT m.topic)::BIGINT as unique_topics,
        MODE() WITHIN GROUP (ORDER BY m.content_style) as most_common_style,
        COUNT(*) FILTER (WHERE 'instagram' = ANY(m.platforms_posted))::BIGINT as instagram_posts,
        COUNT(*) FILTER (WHERE 'youtube' = ANY(m.platforms_posted))::BIGINT as youtube_posts,
        COUNT(*) FILTER (WHERE 'tiktok' = ANY(m.platforms_posted))::BIGINT as tiktok_posts,
        COUNT(*) FILTER (WHERE 'google_drive' = ANY(m.platforms_posted))::BIGINT as drive_backups
    FROM meme_videos_ai_powered m
    WHERE m.ai_provider = provider
      AND m.posted_at >= CURRENT_DATE - days_back;
END;
$$ LANGUAGE plpgsql;

-- =============================================================================
-- FUNCTION: compare_ai_providers
-- Compare performance of two AI providers
-- =============================================================================

CREATE OR REPLACE FUNCTION compare_ai_providers(
    provider1 VARCHAR(50),
    provider2 VARCHAR(50),
    days_back INTEGER DEFAULT 30
)
RETURNS TABLE (
    metric VARCHAR(100),
    provider1_value NUMERIC,
    provider2_value NUMERIC,
    winner VARCHAR(50)
) AS $$
BEGIN
    RETURN QUERY
    WITH provider1_stats AS (
        SELECT * FROM get_ai_stats(provider1, days_back)
    ),
    provider2_stats AS (
        SELECT * FROM get_ai_stats(provider2, days_back)
    )
    SELECT 
        'Total Posts'::VARCHAR(100),
        p1.total_posts::NUMERIC,
        p2.total_posts::NUMERIC,
        CASE WHEN p1.total_posts > p2.total_posts THEN provider1 ELSE provider2 END
    FROM provider1_stats p1, provider2_stats p2
    UNION ALL
    SELECT 
        'Success Rate (%)'::VARCHAR(100),
        p1.success_rate::NUMERIC,
        p2.success_rate::NUMERIC,
        CASE WHEN p1.success_rate > p2.success_rate THEN provider1 ELSE provider2 END
    FROM provider1_stats p1, provider2_stats p2
    UNION ALL
    SELECT 
        'Avg Viral Score'::VARCHAR(100),
        p1.avg_viral_score::NUMERIC,
        p2.avg_viral_score::NUMERIC,
        CASE WHEN p1.avg_viral_score > p2.avg_viral_score THEN provider1 ELSE provider2 END
    FROM provider1_stats p1, provider2_stats p2
    UNION ALL
    SELECT 
        'Total Cost ($)'::VARCHAR(100),
        p1.total_cost::NUMERIC,
        p2.total_cost::NUMERIC,
        CASE WHEN p1.total_cost < p2.total_cost THEN provider1 ELSE provider2 END
    FROM provider1_stats p1, provider2_stats p2
    UNION ALL
    SELECT 
        'Unique Topics'::VARCHAR(100),
        p1.unique_topics::NUMERIC,
        p2.unique_topics::NUMERIC,
        CASE WHEN p1.unique_topics > p2.unique_topics THEN provider1 ELSE provider2 END
    FROM provider1_stats p1, provider2_stats p2;
END;
$$ LANGUAGE plpgsql;

-- =============================================================================
-- FUNCTION: get_trending_topics
-- Get current trending topics by AI provider
-- =============================================================================

CREATE OR REPLACE FUNCTION get_trending_topics(
    provider VARCHAR(50),
    days_back INTEGER DEFAULT 7,
    limit_count INTEGER DEFAULT 10
)
RETURNS TABLE (
    topic VARCHAR(100),
    times_used BIGINT,
    avg_viral_score NUMERIC,
    success_rate NUMERIC,
    last_used TIMESTAMP
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        m.topic,
        COUNT(*)::BIGINT as times_used,
        ROUND(AVG(m.viral_score)::NUMERIC, 2) as avg_viral_score,
        ROUND(SUM(CASE WHEN m.success THEN 1 ELSE 0 END)::NUMERIC / COUNT(*) * 100, 2) as success_rate,
        MAX(m.posted_at) as last_used
    FROM meme_videos_ai_powered m
    WHERE m.ai_provider = provider
      AND m.posted_at >= CURRENT_DATE - days_back
    GROUP BY m.topic
    ORDER BY times_used DESC, avg_viral_score DESC
    LIMIT limit_count;
END;
$$ LANGUAGE plpgsql;

-- =============================================================================
-- Example Queries
-- =============================================================================

-- Get Grok stats for last 7 days
-- SELECT * FROM get_ai_stats('grok', 7);

-- Get Perplexity stats for last 7 days
-- SELECT * FROM get_ai_stats('perplexity', 7);

-- Compare Grok vs Perplexity
-- SELECT * FROM compare_ai_providers('grok', 'perplexity', 30);

-- Get Grok trending topics
-- SELECT * FROM get_trending_topics('grok', 7, 10);

-- View all analytics
-- SELECT * FROM ai_provider_analytics WHERE day >= CURRENT_DATE - 7;

-- View Grok vs Perplexity comparison
-- SELECT * FROM grok_vs_perplexity_performance;

-- View content style performance
-- SELECT * FROM content_style_analysis WHERE ai_provider = 'grok';

-- View cost comparison
-- SELECT * FROM ai_cost_comparison WHERE month >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '3 months');

-- =============================================================================
-- Maintenance
-- =============================================================================

-- Clean up old records (keep last 90 days of AI content)
CREATE OR REPLACE FUNCTION cleanup_old_ai_records()
RETURNS INTEGER AS $$
DECLARE
    deleted_count INTEGER;
BEGIN
    DELETE FROM meme_videos_ai_powered
    WHERE posted_at < CURRENT_DATE - INTERVAL '90 days'
      AND ai_provider IN ('grok', 'perplexity');
    
    GET DIAGNOSTICS deleted_count = ROW_COUNT;
    RETURN deleted_count;
END;
$$ LANGUAGE plpgsql;

-- Schedule cleanup (run monthly)
-- SELECT cleanup_old_ai_records();

-- =============================================================================
-- Setup Complete
-- =============================================================================

-- Verify tables and views created
SELECT 
    'Tables' as object_type,
    COUNT(*) as count
FROM information_schema.tables 
WHERE table_schema = 'public' 
  AND table_name LIKE '%ai%'
UNION ALL
SELECT 
    'Views' as object_type,
    COUNT(*) as count
FROM information_schema.views
WHERE table_schema = 'public'
  AND table_name LIKE '%ai%'
UNION ALL
SELECT 
    'Functions' as object_type,
    COUNT(*) as count
FROM information_schema.routines
WHERE routine_schema = 'public'
  AND routine_name LIKE '%ai%';

COMMENT ON TABLE meme_videos_ai_powered IS 'Unified table for AI-powered (Grok + Perplexity) meme videos with multi-platform tracking';
COMMENT ON VIEW ai_provider_analytics IS 'Daily analytics comparing AI providers (Grok vs Perplexity)';
COMMENT ON VIEW grok_vs_perplexity_performance IS 'Direct performance comparison between Grok and Perplexity AI';
COMMENT ON FUNCTION get_ai_stats IS 'Get comprehensive statistics for specific AI provider';
COMMENT ON FUNCTION compare_ai_providers IS 'Compare performance metrics between two AI providers';
COMMENT ON FUNCTION get_trending_topics IS 'Get trending topics for specific AI provider';
