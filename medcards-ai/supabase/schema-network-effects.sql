-- ============================================================================
-- MEDCARDS.AI - Network Effects & Social Features Schema Extension
-- This extends the base schema with community, marketplace, and social features
-- ============================================================================

-- ============================================================================
-- DATA NETWORK EFFECT: Learning from Collective Intelligence
-- ============================================================================

-- Track real-world difficulty vs predicted difficulty
CREATE TABLE case_difficulty_calibration (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    case_id UUID NOT NULL REFERENCES clinical_cases(id) ON DELETE CASCADE,

    -- Calibration metrics
    actual_difficulty_score NUMERIC(5, 2), -- Based on real user performance
    predicted_difficulty_score NUMERIC(5, 2), -- What we thought it would be
    difficulty_delta NUMERIC(5, 2), -- How off were we?

    sample_size INTEGER NOT NULL, -- Number of interactions used for calculation
    confidence_level NUMERIC(3, 2), -- Statistical confidence (0.00-1.00)

    -- Performance breakdown
    performance_by_level JSONB, -- {"beginner": 0.3, "intermediate": 0.6, "advanced": 0.8}
    time_distribution JSONB, -- {"p50": 180, "p75": 240, "p90": 320}

    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    CONSTRAINT valid_confidence CHECK (confidence_level >= 0 AND confidence_level <= 1)
);

CREATE INDEX idx_calibration_case ON case_difficulty_calibration(case_id);
CREATE INDEX idx_calibration_updated ON case_difficulty_calibration(updated_at DESC);

-- Track AI model versions and performance
CREATE TABLE prediction_model_versions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    version TEXT UNIQUE NOT NULL,
    deployed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Training data
    training_data_size INTEGER NOT NULL,
    training_period_start TIMESTAMP WITH TIME ZONE,
    training_period_end TIMESTAMP WITH TIME ZONE,

    -- Performance metrics
    accuracy_metrics JSONB NOT NULL,
    /*
    {
        "case_selection_accuracy": 0.85,
        "difficulty_prediction_mae": 0.3,
        "time_prediction_mape": 15.2,
        "student_success_prediction_auc": 0.78
    }
    */

    performance_improvement_vs_previous NUMERIC(5, 2), -- Percentage improvement

    -- Model metadata
    model_architecture TEXT,
    hyperparameters JSONB,
    notes TEXT,

    is_active BOOLEAN DEFAULT false
);

CREATE INDEX idx_model_active ON prediction_model_versions(is_active) WHERE is_active = true;

-- ============================================================================
-- CONTENT NETWORK EFFECT: Community-Contributed Cases
-- ============================================================================

CREATE TABLE community_cases (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Creator
    created_by_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    -- Case content (same structure as clinical_cases)
    case_code TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    clinical_presentation TEXT NOT NULL,
    patient_data JSONB,
    question TEXT NOT NULL,
    options JSONB NOT NULL,
    correct_answer_id TEXT NOT NULL,
    explanation TEXT NOT NULL,
    clinical_reasoning TEXT NOT NULL,
    key_concepts TEXT[],
    differential_diagnosis TEXT[],

    -- Classification
    specialty TEXT NOT NULL,
    subspecialty TEXT,
    difficulty_level INTEGER CHECK (difficulty_level BETWEEN 1 AND 5),
    clinical_algorithm TEXT,

    -- Review status
    status TEXT NOT NULL DEFAULT 'draft' CHECK (status IN ('draft', 'submitted', 'under_review', 'approved', 'rejected', 'needs_revision')),
    submitted_at TIMESTAMP WITH TIME ZONE,
    reviewed_at TIMESTAMP WITH TIME ZONE,
    approved_by_user_id UUID REFERENCES users(id),

    -- Community feedback
    community_rating NUMERIC(3, 2), -- 0.00 to 5.00
    rating_count INTEGER DEFAULT 0,
    times_used INTEGER DEFAULT 0,
    success_rate NUMERIC(5, 2),

    -- Moderation
    curator_notes TEXT,
    revision_requests TEXT[],

    -- Monetization
    is_premium BOOLEAN DEFAULT false,
    price_credits INTEGER DEFAULT 0,
    earnings_generated NUMERIC(10, 2) DEFAULT 0,

    -- Quality signals
    expert_verified BOOLEAN DEFAULT false,
    flagged_count INTEGER DEFAULT 0,

    tags TEXT[]
);

CREATE INDEX idx_community_cases_creator ON community_cases(created_by_user_id);
CREATE INDEX idx_community_cases_status ON community_cases(status);
CREATE INDEX idx_community_cases_specialty ON community_cases(specialty) WHERE status = 'approved';
CREATE INDEX idx_community_cases_rating ON community_cases(community_rating DESC) WHERE status = 'approved';

-- Reviews for community cases
CREATE TABLE case_reviews (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    case_id UUID NOT NULL REFERENCES community_cases(id) ON DELETE CASCADE,
    reviewer_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    -- Review scores
    clinical_accuracy_score INTEGER CHECK (clinical_accuracy_score BETWEEN 1 AND 5),
    educational_value_score INTEGER CHECK (educational_value_score BETWEEN 1 AND 5),
    clarity_score INTEGER CHECK (clarity_score BETWEEN 1 AND 5),
    overall_score NUMERIC(3, 2), -- Calculated average

    -- Feedback
    review_text TEXT NOT NULL,
    strengths TEXT[],
    areas_for_improvement TEXT[],

    -- Reviewer credibility
    is_expert_review BOOLEAN DEFAULT false, -- Verified doctors/professors
    reviewer_specialty TEXT,

    -- Helpfulness
    helpful_count INTEGER DEFAULT 0,

    UNIQUE(case_id, reviewer_user_id) -- One review per user per case
);

CREATE INDEX idx_reviews_case ON case_reviews(case_id);
CREATE INDEX idx_reviews_expert ON case_reviews(is_expert_review) WHERE is_expert_review = true;

-- Case quality flags (for moderation)
CREATE TABLE case_flags (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    case_id UUID NOT NULL REFERENCES community_cases(id) ON DELETE CASCADE,
    flagged_by_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    flag_reason TEXT NOT NULL CHECK (flag_reason IN (
        'clinical_inaccuracy',
        'misleading_information',
        'inappropriate_content',
        'duplicate',
        'poor_quality',
        'other'
    )),

    description TEXT NOT NULL,
    status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'reviewed', 'resolved', 'dismissed')),
    resolution_notes TEXT,
    resolved_by_user_id UUID REFERENCES users(id),
    resolved_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_flags_case ON case_flags(case_id);
CREATE INDEX idx_flags_status ON case_flags(status) WHERE status = 'pending';

-- ============================================================================
-- SOCIAL NETWORK EFFECT: Study Groups & Peer Learning
-- ============================================================================

CREATE TABLE study_groups (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Group identity
    name TEXT NOT NULL,
    description TEXT,
    created_by_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    -- Access control
    is_public BOOLEAN DEFAULT false,
    requires_approval BOOLEAN DEFAULT false,
    invite_code TEXT UNIQUE, -- For private groups
    member_limit INTEGER DEFAULT 50,

    -- Configuration
    focus_specialties TEXT[],
    target_exam TEXT, -- "REVALIDA 2025", "USP Clínica Médica 2025"
    exam_date DATE,
    study_schedule JSONB, -- {"monday": ["19:00-21:00"], "saturday": ["09:00-12:00"]}

    -- Group stats
    total_cases_solved INTEGER DEFAULT 0,
    avg_group_success_rate NUMERIC(5, 2),
    active_members_count INTEGER DEFAULT 0,
    total_study_hours NUMERIC(10, 2) DEFAULT 0,

    -- Visibility
    is_archived BOOLEAN DEFAULT false,

    -- Group culture
    group_image_url TEXT,
    tags TEXT[]
);

CREATE INDEX idx_groups_public ON study_groups(is_public) WHERE is_public = true AND is_archived = false;
CREATE INDEX idx_groups_creator ON study_groups(created_by_user_id);
CREATE INDEX idx_groups_exam ON study_groups(target_exam) WHERE is_archived = false;

CREATE TABLE study_group_members (
    group_id UUID NOT NULL REFERENCES study_groups(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    joined_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Role
    role TEXT NOT NULL DEFAULT 'member' CHECK (role IN ('owner', 'admin', 'member')),

    -- Member stats
    contribution_score INTEGER DEFAULT 0, -- Based on activity and helpfulness
    cases_solved_in_group INTEGER DEFAULT 0,
    last_active_at TIMESTAMP WITH TIME ZONE,

    -- Preferences
    notifications_enabled BOOLEAN DEFAULT true,

    PRIMARY KEY (group_id, user_id)
);

CREATE INDEX idx_group_members_user ON study_group_members(user_id);
CREATE INDEX idx_group_members_active ON study_group_members(last_active_at DESC);

-- Group activity feed
CREATE TABLE group_activities (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    group_id UUID NOT NULL REFERENCES study_groups(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,

    activity_type TEXT NOT NULL CHECK (activity_type IN (
        'member_joined',
        'member_left',
        'challenge_created',
        'challenge_completed',
        'milestone_reached',
        'case_recommended',
        'discussion_started'
    )),

    activity_data JSONB, -- Context-specific data
    visibility TEXT DEFAULT 'group' CHECK (visibility IN ('group', 'members_only', 'public'))
);

CREATE INDEX idx_activities_group ON group_activities(group_id, created_at DESC);

-- ============================================================================
-- COMPETITIVE FEATURES: Challenges & Leaderboards
-- ============================================================================

CREATE TABLE group_challenges (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    group_id UUID NOT NULL REFERENCES study_groups(id) ON DELETE CASCADE,
    created_by_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    -- Challenge details
    title TEXT NOT NULL,
    description TEXT,
    challenge_type TEXT NOT NULL CHECK (challenge_type IN (
        'speed_run',         -- Solve X cases as fast as possible
        'accuracy_battle',   -- Highest success rate wins
        'specialty_mastery', -- Focus on specific specialty
        'daily_streak',      -- Longest streak wins
        'total_cases'        -- Most cases solved
    )),

    -- Rules
    case_pool UUID[], -- Specific cases OR null for any cases
    specialty_filter TEXT,
    difficulty_filter INTEGER,

    -- Timing
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,

    -- Rewards
    prize_type TEXT CHECK (prize_type IN ('badges', 'credits', 'bragging_rights', 'real_prize')),
    prize_details JSONB, -- {"credits": 500, "badge_id": "uuid"}

    -- Status
    status TEXT DEFAULT 'upcoming' CHECK (status IN ('upcoming', 'active', 'completed', 'cancelled')),

    -- Stats
    participant_count INTEGER DEFAULT 0,
    total_cases_solved INTEGER DEFAULT 0
);

CREATE INDEX idx_challenges_group ON group_challenges(group_id);
CREATE INDEX idx_challenges_status ON group_challenges(status, start_time);

CREATE TABLE challenge_participants (
    challenge_id UUID NOT NULL REFERENCES group_challenges(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    joined_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Performance
    score INTEGER DEFAULT 0,
    cases_solved INTEGER DEFAULT 0,
    success_rate NUMERIC(5, 2),
    time_spent_seconds INTEGER DEFAULT 0,
    rank INTEGER,

    -- Completion
    completed_at TIMESTAMP WITH TIME ZONE,

    PRIMARY KEY (challenge_id, user_id)
);

CREATE INDEX idx_participants_challenge ON challenge_participants(challenge_id, score DESC);
CREATE INDEX idx_participants_user ON challenge_participants(user_id);

-- Global leaderboards
CREATE TABLE leaderboards (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    leaderboard_type TEXT NOT NULL CHECK (leaderboard_type IN (
        'global_weekly',
        'global_monthly',
        'global_all_time',
        'specialty_weekly',
        'university_weekly',
        'study_group'
    )),

    -- Filters
    specialty TEXT, -- For specialty leaderboards
    university TEXT, -- For university leaderboards
    study_group_id UUID REFERENCES study_groups(id),

    -- Period
    period_start TIMESTAMP WITH TIME ZONE NOT NULL,
    period_end TIMESTAMP WITH TIME ZONE NOT NULL,

    -- Rankings (denormalized for performance)
    rankings JSONB NOT NULL,
    /*
    [
        {"user_id": "uuid", "username": "João", "score": 9500, "cases_solved": 150, "success_rate": 0.85},
        {"user_id": "uuid", "username": "Maria", "score": 9200, "cases_solved": 145, "success_rate": 0.87},
        ...top 100
    ]
    */

    last_updated TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    UNIQUE(leaderboard_type, specialty, university, study_group_id, period_start)
);

CREATE INDEX idx_leaderboards_type ON leaderboards(leaderboard_type, period_end DESC);

-- ============================================================================
-- PEER INTERACTIONS: Direct User Connections
-- ============================================================================

CREATE TABLE peer_interactions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    from_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    to_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    interaction_type TEXT NOT NULL CHECK (interaction_type IN (
        'study_together_request',
        'case_recommendation',
        'explanation_request',
        'kudos', -- "Nice job on that case!"
        'challenge_invite',
        'mentor_request'
    )),

    context JSONB, -- Additional data depending on type
    status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'accepted', 'declined', 'expired')),

    response_at TIMESTAMP WITH TIME ZONE,
    expires_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_interactions_to_user ON peer_interactions(to_user_id, status);
CREATE INDEX idx_interactions_from_user ON peer_interactions(from_user_id);

-- Study buddy matching preferences
CREATE TABLE study_preferences (
    user_id UUID PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Exam goals
    target_exam TEXT,
    exam_date DATE,
    target_specialty TEXT, -- For residency

    -- Learning profile
    weak_specialties TEXT[],
    strong_specialties TEXT[],
    preferred_study_times TEXT[], -- "weekday_mornings", "weekend_afternoons", etc.
    study_hours_per_week INTEGER,

    -- Personality
    study_style TEXT CHECK (study_style IN ('competitive', 'collaborative', 'independent_with_accountability', 'mentor', 'mentee')),
    communication_preference TEXT CHECK (communication_preference IN ('chat', 'video', 'async')),

    -- Matching
    looking_for_buddy BOOLEAN DEFAULT false,
    open_to_group_invites BOOLEAN DEFAULT true,
    university TEXT,
    current_year INTEGER, -- Year of medical school

    -- Bio
    bio TEXT,
    interests TEXT[]
);

CREATE INDEX idx_preferences_looking ON study_preferences(looking_for_buddy) WHERE looking_for_buddy = true;
CREATE INDEX idx_preferences_exam ON study_preferences(target_exam, exam_date);

CREATE TABLE study_buddy_matches (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    user1_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    user2_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    -- Match quality
    match_score NUMERIC(3, 2) NOT NULL, -- 0.00 to 1.00
    match_reason JSONB NOT NULL,
    /*
    {
        "compatibility_factors": [
            "Both preparing for REVALIDA 2025",
            "Complementary strengths: You're strong in cardio, they're strong in neuro",
            "Similar study schedule preferences"
        ],
        "suggested_first_activity": "Try a cardiology challenge together"
    }
    */

    -- Status
    status TEXT DEFAULT 'suggested' CHECK (status IN ('suggested', 'accepted', 'declined', 'active', 'ended')),
    accepted_at TIMESTAMP WITH TIME ZONE,
    ended_at TIMESTAMP WITH TIME ZONE,

    -- Activity tracking
    study_sessions_together INTEGER DEFAULT 0,
    cases_solved_together INTEGER DEFAULT 0,

    CONSTRAINT different_users CHECK (user1_id != user2_id),
    UNIQUE(user1_id, user2_id)
);

CREATE INDEX idx_matches_user1 ON study_buddy_matches(user1_id, status);
CREATE INDEX idx_matches_user2 ON study_buddy_matches(user2_id, status);

-- ============================================================================
-- MARKETPLACE: Two-Sided Market for Content
-- ============================================================================

CREATE TABLE premium_content (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    creator_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    -- Content details
    content_type TEXT NOT NULL CHECK (content_type IN (
        'case_pack',          -- Bundle of cases
        'specialty_course',   -- Complete specialty review
        'exam_simulation',    -- Full mock exam
        'video_explanations', -- Video content
        'study_guide',        -- PDF/written guide
        'flashcard_deck',     -- Spaced repetition cards
        'ai_tutor_session'    -- 1-on-1 AI tutoring (premium)
    )),

    title TEXT NOT NULL,
    description TEXT NOT NULL,
    detailed_description TEXT,

    -- Pricing
    price_credits INTEGER NOT NULL,
    price_reais NUMERIC(10, 2), -- For direct purchase
    is_subscription BOOLEAN DEFAULT false, -- Monthly access vs one-time

    -- Content metadata
    content_metadata JSONB NOT NULL,
    /*
    {
        "case_count": 50,
        "specialty": "cardiologia",
        "difficulty_range": [3, 5],
        "includes_video": true,
        "estimated_hours": 10,
        "prerequisites": ["Basic cardiology knowledge"],
        "learning_objectives": ["Master ECG interpretation", "..."]
    }
    */

    -- Files/content
    content_files JSONB, -- URLs to files in Supabase storage
    preview_content JSONB, -- Free preview

    -- Performance metrics
    purchases_count INTEGER DEFAULT 0,
    view_count INTEGER DEFAULT 0,
    avg_rating NUMERIC(3, 2),
    review_count INTEGER DEFAULT 0,
    revenue_generated NUMERIC(10, 2) DEFAULT 0,

    -- Quality control
    is_verified BOOLEAN DEFAULT false, -- Verified by MedCards team
    is_featured BOOLEAN DEFAULT false,
    quality_score NUMERIC(3, 2), -- Internal quality metric

    -- Status
    status TEXT DEFAULT 'draft' CHECK (status IN ('draft', 'pending_review', 'published', 'unpublished')),
    published_at TIMESTAMP WITH TIME ZONE,

    -- SEO
    tags TEXT[],
    category TEXT
);

CREATE INDEX idx_premium_content_creator ON premium_content(creator_user_id);
CREATE INDEX idx_premium_content_published ON premium_content(status, published_at DESC) WHERE status = 'published';
CREATE INDEX idx_premium_content_featured ON premium_content(is_featured, avg_rating DESC) WHERE is_featured = true;
CREATE INDEX idx_premium_content_category ON premium_content(category, avg_rating DESC) WHERE status = 'published';

CREATE TABLE content_purchases (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    purchased_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    content_id UUID NOT NULL REFERENCES premium_content(id) ON DELETE CASCADE,

    -- Transaction
    price_paid_credits INTEGER,
    price_paid_reais NUMERIC(10, 2),
    payment_method TEXT, -- 'credits', 'card', 'pix'

    -- Access
    access_expires_at TIMESTAMP WITH TIME ZONE, -- For subscriptions

    -- Engagement
    last_accessed_at TIMESTAMP WITH TIME ZONE,
    completion_percentage NUMERIC(5, 2) DEFAULT 0,

    -- Satisfaction
    rated BOOLEAN DEFAULT false,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,

    UNIQUE(user_id, content_id) -- One purchase per user per content
);

CREATE INDEX idx_purchases_user ON content_purchases(user_id);
CREATE INDEX idx_purchases_content ON content_purchases(content_id);
CREATE INDEX idx_purchases_recent ON content_purchases(purchased_at DESC);

-- Creator profiles
CREATE TABLE creator_profiles (
    user_id UUID PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Verification
    is_verified_educator BOOLEAN DEFAULT false,
    verified_at TIMESTAMP WITH TIME ZONE,
    credentials TEXT, -- "Médico Residente R3 Cardiologia HC-USP"
    credentials_verified BOOLEAN DEFAULT false,

    -- Profile
    display_name TEXT NOT NULL,
    bio TEXT,
    profile_image_url TEXT,
    specialty TEXT,
    institution TEXT,

    -- Social
    website_url TEXT,
    twitter_handle TEXT,
    linkedin_url TEXT,

    -- Creator stats
    total_content_created INTEGER DEFAULT 0,
    total_revenue_earned NUMERIC(10, 2) DEFAULT 0,
    total_students_reached INTEGER DEFAULT 0,
    follower_count INTEGER DEFAULT 0,
    avg_content_rating NUMERIC(3, 2),

    -- Payout
    payout_method TEXT CHECK (payout_method IN ('bank_transfer', 'pix', 'paypal')),
    payout_details JSONB, -- Encrypted sensitive data
    minimum_payout_threshold NUMERIC(10, 2) DEFAULT 100.00,

    -- Status
    is_active BOOLEAN DEFAULT true,
    terms_accepted_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_creators_verified ON creator_profiles(is_verified_educator) WHERE is_verified_educator = true;
CREATE INDEX idx_creators_revenue ON creator_profiles(total_revenue_earned DESC);

CREATE TABLE creator_followers (
    follower_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    creator_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    followed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    notifications_enabled BOOLEAN DEFAULT true,

    PRIMARY KEY (follower_user_id, creator_user_id)
);

CREATE INDEX idx_followers_creator ON creator_followers(creator_user_id);
CREATE INDEX idx_followers_user ON creator_followers(follower_user_id);

-- Payout tracking
CREATE TABLE creator_payouts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    creator_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    -- Payout details
    amount NUMERIC(10, 2) NOT NULL,
    currency TEXT DEFAULT 'BRL',

    period_start TIMESTAMP WITH TIME ZONE NOT NULL,
    period_end TIMESTAMP WITH TIME ZONE NOT NULL,

    -- Transaction
    status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'processing', 'completed', 'failed')),
    payout_method TEXT NOT NULL,
    transaction_id TEXT,

    processed_at TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,

    -- Breakdown
    revenue_breakdown JSONB -- Details of what generated this revenue
);

CREATE INDEX idx_payouts_creator ON creator_payouts(creator_user_id, created_at DESC);
CREATE INDEX idx_payouts_status ON creator_payouts(status) WHERE status IN ('pending', 'processing');

-- ============================================================================
-- COMMUNITY FORUM
-- ============================================================================

CREATE TABLE forum_categories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT UNIQUE NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    description TEXT,
    icon_emoji TEXT,
    sort_order INTEGER DEFAULT 0,
    post_count INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT true
);

INSERT INTO forum_categories (name, slug, description, icon_emoji, sort_order) VALUES
('Discussão de Casos', 'case-discussion', 'Discuta casos clínicos específicos', '🩺', 1),
('Dicas de Estudo', 'study-tips', 'Compartilhe estratégias e métodos de estudo', '📚', 2),
('Estratégias de Prova', 'exam-strategies', 'Táticas para diferentes provas de residência', '✍️', 3),
('Dúvidas Clínicas', 'clinical-questions', 'Tire dúvidas sobre medicina', '❓', 4),
('Motivação', 'motivation', 'Apoio e motivação durante a jornada', '💪', 5),
('Anúncios', 'announcements', 'Novidades da plataforma', '📢', 6);

CREATE TABLE forum_posts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    category_id UUID NOT NULL REFERENCES forum_categories(id),

    -- Content
    title TEXT NOT NULL,
    content TEXT NOT NULL,

    -- Context
    related_case_id UUID REFERENCES clinical_cases(id),
    related_specialty TEXT,
    tags TEXT[],

    -- Engagement
    view_count INTEGER DEFAULT 0,
    upvote_count INTEGER DEFAULT 0,
    comment_count INTEGER DEFAULT 0,

    -- Status
    is_pinned BOOLEAN DEFAULT false,
    is_locked BOOLEAN DEFAULT false,
    is_solved BOOLEAN DEFAULT false, -- For questions
    accepted_answer_id UUID, -- For questions

    -- Moderation
    is_flagged BOOLEAN DEFAULT false,
    flag_count INTEGER DEFAULT 0
);

CREATE INDEX idx_posts_category ON forum_posts(category_id, created_at DESC);
CREATE INDEX idx_posts_user ON forum_posts(user_id);
CREATE INDEX idx_posts_popular ON forum_posts(upvote_count DESC, created_at DESC);
CREATE INDEX idx_posts_case ON forum_posts(related_case_id) WHERE related_case_id IS NOT NULL;

CREATE TABLE forum_comments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    post_id UUID NOT NULL REFERENCES forum_posts(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    parent_comment_id UUID REFERENCES forum_comments(id), -- For threaded replies

    content TEXT NOT NULL,

    -- Engagement
    upvote_count INTEGER DEFAULT 0,
    is_accepted_answer BOOLEAN DEFAULT false,

    -- Quality signals
    is_expert_answer BOOLEAN DEFAULT false, -- From verified educator/doctor
    is_edited BOOLEAN DEFAULT false,
    edited_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_comments_post ON forum_comments(post_id, created_at);
CREATE INDEX idx_comments_user ON forum_comments(user_id);
CREATE INDEX idx_comments_parent ON forum_comments(parent_comment_id) WHERE parent_comment_id IS NOT NULL;

CREATE TABLE forum_votes (
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    -- Polymorphic: can vote on posts or comments
    votable_type TEXT NOT NULL CHECK (votable_type IN ('post', 'comment')),
    votable_id UUID NOT NULL,

    vote_value INTEGER NOT NULL CHECK (vote_value IN (-1, 1)), -- -1 downvote, 1 upvote
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    PRIMARY KEY (user_id, votable_type, votable_id)
);

CREATE INDEX idx_votes_votable ON forum_votes(votable_type, votable_id);

-- ============================================================================
-- FUNCTIONS & TRIGGERS FOR NETWORK EFFECTS
-- ============================================================================

-- Update group stats when member activity happens
CREATE OR REPLACE FUNCTION update_group_stats()
RETURNS TRIGGER AS $$
BEGIN
    -- Update active member count
    UPDATE study_groups
    SET active_members_count = (
        SELECT COUNT(*)
        FROM study_group_members
        WHERE group_id = NEW.group_id
          AND last_active_at > NOW() - INTERVAL '7 days'
    )
    WHERE id = NEW.group_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_group_stats
    AFTER INSERT OR UPDATE ON study_group_members
    FOR EACH ROW
    EXECUTE FUNCTION update_group_stats();

-- Update creator stats when content is purchased
CREATE OR REPLACE FUNCTION update_creator_stats()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE creator_profiles
    SET
        total_revenue_earned = total_revenue_earned + COALESCE(NEW.price_paid_reais, 0),
        total_students_reached = (
            SELECT COUNT(DISTINCT user_id)
            FROM content_purchases
            WHERE content_id IN (
                SELECT id FROM premium_content WHERE creator_user_id = (
                    SELECT creator_user_id FROM premium_content WHERE id = NEW.content_id
                )
            )
        )
    WHERE user_id = (
        SELECT creator_user_id FROM premium_content WHERE id = NEW.content_id
    );

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_creator_stats
    AFTER INSERT ON content_purchases
    FOR EACH ROW
    EXECUTE FUNCTION update_creator_stats();

-- Update forum post comment count
CREATE OR REPLACE FUNCTION update_post_comment_count()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        UPDATE forum_posts
        SET comment_count = comment_count + 1
        WHERE id = NEW.post_id;
    ELSIF TG_OP = 'DELETE' THEN
        UPDATE forum_posts
        SET comment_count = comment_count - 1
        WHERE id = OLD.post_id;
    END IF;

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_post_comment_count
    AFTER INSERT OR DELETE ON forum_comments
    FOR EACH ROW
    EXECUTE FUNCTION update_post_comment_count();

-- ============================================================================
-- ROW LEVEL SECURITY POLICIES
-- ============================================================================

-- Community cases: Anyone can read approved, only creator can edit draft
ALTER TABLE community_cases ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can view approved community cases" ON community_cases
    FOR SELECT USING (status = 'approved' OR created_by_user_id = auth.uid());

CREATE POLICY "Users can create own community cases" ON community_cases
    FOR INSERT WITH CHECK (created_by_user_id = auth.uid());

CREATE POLICY "Users can update own draft cases" ON community_cases
    FOR UPDATE USING (created_by_user_id = auth.uid() AND status IN ('draft', 'needs_revision'));

-- Study groups: Members can view, admins can edit
ALTER TABLE study_groups ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can view public groups" ON study_groups
    FOR SELECT USING (
        is_public = true
        OR id IN (
            SELECT group_id FROM study_group_members WHERE user_id = auth.uid()
        )
    );

CREATE POLICY "Members can view their groups" ON study_groups
    FOR SELECT USING (
        id IN (SELECT group_id FROM study_group_members WHERE user_id = auth.uid())
    );

-- Marketplace: Buyers can see purchased content
ALTER TABLE premium_content ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can view published premium content" ON premium_content
    FOR SELECT USING (status = 'published' OR creator_user_id = auth.uid());

ALTER TABLE content_purchases ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view own purchases" ON content_purchases
    FOR SELECT USING (user_id = auth.uid());

-- Forum: Public read, authenticated write
ALTER TABLE forum_posts ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can view forum posts" ON forum_posts
    FOR SELECT USING (true);

CREATE POLICY "Authenticated users can create posts" ON forum_posts
    FOR INSERT WITH CHECK (auth.role() = 'authenticated' AND user_id = auth.uid());

CREATE POLICY "Users can update own posts" ON forum_posts
    FOR UPDATE USING (user_id = auth.uid());

ALTER TABLE forum_comments ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can view comments" ON forum_comments
    FOR SELECT USING (true);

CREATE POLICY "Authenticated users can comment" ON forum_comments
    FOR INSERT WITH CHECK (auth.role() = 'authenticated' AND user_id = auth.uid());

-- ============================================================================
-- ANALYTICS VIEWS (Materialized for performance)
-- ============================================================================

-- Daily network effect metrics
CREATE MATERIALIZED VIEW network_metrics_daily AS
SELECT
    DATE(created_at) as date,
    COUNT(DISTINCT user_id) as daily_active_users,
    COUNT(*) as total_interactions,

    -- Social metrics
    (SELECT COUNT(*) FROM study_group_members WHERE DATE(joined_at) = DATE(i.created_at)) as new_group_joins,
    (SELECT COUNT(*) FROM peer_interactions WHERE DATE(created_at) = DATE(i.created_at)) as peer_interactions_count,

    -- Content metrics
    (SELECT COUNT(*) FROM community_cases WHERE DATE(submitted_at) = DATE(i.created_at)) as community_cases_submitted,
    (SELECT COUNT(*) FROM content_purchases WHERE DATE(purchased_at) = DATE(i.created_at)) as marketplace_purchases,

    -- Engagement depth
    AVG(time_to_answer_seconds) as avg_time_per_case,
    AVG(CASE WHEN is_correct THEN 1.0 ELSE 0.0 END) as platform_success_rate

FROM interactions i
GROUP BY DATE(created_at);

CREATE UNIQUE INDEX ON network_metrics_daily(date);

-- Refresh daily (run as cron job)
-- SELECT cron.schedule('refresh-network-metrics', '0 2 * * *', 'REFRESH MATERIALIZED VIEW CONCURRENTLY network_metrics_daily');

-- ============================================================================
-- SAMPLE QUERIES FOR PRODUCT ANALYTICS
-- ============================================================================

COMMENT ON TABLE network_metrics_daily IS 'Sample query: SELECT * FROM network_metrics_daily WHERE date > NOW() - INTERVAL ''30 days'' ORDER BY date;';

COMMENT ON TABLE study_groups IS '
-- Find most active study groups
SELECT
    sg.name,
    sg.active_members_count,
    sg.total_cases_solved,
    sg.avg_group_success_rate
FROM study_groups sg
WHERE sg.is_archived = false
ORDER BY sg.total_cases_solved DESC
LIMIT 10;
';

COMMENT ON TABLE premium_content IS '
-- Top selling marketplace content
SELECT
    pc.title,
    cp.display_name as creator,
    pc.purchases_count,
    pc.avg_rating,
    pc.revenue_generated
FROM premium_content pc
JOIN creator_profiles cp ON pc.creator_user_id = cp.user_id
WHERE pc.status = ''published''
ORDER BY pc.revenue_generated DESC
LIMIT 10;
';
