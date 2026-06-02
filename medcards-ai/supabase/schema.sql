-- ============================================================================
-- MEDCARDS.AI - Database Schema
-- Supabase PostgreSQL Schema
-- ============================================================================

-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ============================================================================
-- USERS TABLE
-- Stores user profiles and complete progress metadata
-- ============================================================================
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email TEXT UNIQUE NOT NULL,
    full_name TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Progress metadata stored as JSONB for flexibility
    progress JSONB DEFAULT '{
        "specialties": {},
        "overall_stats": {
            "total_cases_attempted": 0,
            "total_cases_correct": 0,
            "total_time_spent_seconds": 0,
            "current_streak": 0,
            "longest_streak": 0,
            "last_activity_date": null
        },
        "badges_earned": [],
        "level": 1,
        "experience_points": 0
    }'::jsonb,

    -- User preferences
    preferences JSONB DEFAULT '{
        "daily_goal_cases": 10,
        "preferred_specialties": [],
        "notification_enabled": true,
        "theme": "dark"
    }'::jsonb,

    -- Subscription status (for future monetization)
    subscription_status TEXT DEFAULT 'free' CHECK (subscription_status IN ('free', 'trial', 'paid', 'cancelled')),
    subscription_ends_at TIMESTAMP WITH TIME ZONE,

    CONSTRAINT email_format CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- ============================================================================
-- CLINICAL_CASES TABLE
-- Repository of all medical cases for training
-- ============================================================================
CREATE TABLE clinical_cases (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Case identification
    case_code TEXT UNIQUE NOT NULL, -- e.g., "CARDIO-001", "NEURO-045"
    title TEXT NOT NULL,

    -- Case content
    clinical_presentation TEXT NOT NULL, -- The case description presented to student
    patient_data JSONB, -- Structured patient info: age, sex, vitals, labs, imaging

    -- Question and answers
    question TEXT NOT NULL,
    options JSONB NOT NULL, -- Array of objects: [{"id": "A", "text": "...", "is_correct": false}, ...]
    correct_answer_id TEXT NOT NULL,

    -- Educational content
    explanation TEXT NOT NULL, -- Why the answer is correct
    clinical_reasoning TEXT NOT NULL, -- The thought process residents should follow
    key_concepts TEXT[], -- Array of key medical concepts
    differential_diagnosis TEXT[], -- List of possible diagnoses to consider

    -- Classification
    specialty TEXT NOT NULL, -- cardiologia, neurologia, pneumologia, etc.
    subspecialty TEXT, -- e.g., "arritmias" within "cardiologia"
    difficulty_level INTEGER CHECK (difficulty_level BETWEEN 1 AND 5), -- 1=basic, 5=expert
    clinical_algorithm TEXT, -- The clinical decision-making algorithm involved

    -- Analytics
    times_presented INTEGER DEFAULT 0,
    times_answered_correctly INTEGER DEFAULT 0,
    average_time_to_answer_seconds NUMERIC(10, 2),

    -- Metadata
    source TEXT, -- e.g., "REVALIDA 2023", "Internal"
    tags TEXT[], -- Additional categorization
    is_active BOOLEAN DEFAULT true,

    -- Performance tracking
    global_success_rate NUMERIC(5, 2) GENERATED ALWAYS AS
        (CASE
            WHEN times_presented > 0
            THEN ROUND((times_answered_correctly::NUMERIC / times_presented * 100), 2)
            ELSE 0
        END) STORED
);

-- ============================================================================
-- INTERACTIONS TABLE
-- Records every student interaction with cases
-- ============================================================================
CREATE TABLE interactions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Foreign keys
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    case_id UUID NOT NULL REFERENCES clinical_cases(id) ON DELETE CASCADE,

    -- Interaction details
    selected_answer_id TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL,
    time_to_answer_seconds INTEGER NOT NULL,

    -- Student reasoning capture
    student_reasoning TEXT, -- Optional: student can explain their thinking
    confidence_level INTEGER CHECK (confidence_level BETWEEN 1 AND 5), -- 1=guessing, 5=certain

    -- AI assistance used
    hints_used JSONB DEFAULT '[]'::jsonb, -- Array of hints requested
    hint_count INTEGER DEFAULT 0,
    ai_coach_consulted BOOLEAN DEFAULT false,

    -- AI-generated feedback
    ai_feedback JSONB, -- Structured feedback from Claude
    /*
    Example structure:
    {
        "analysis": "Student correctly identified...",
        "clinical_pattern": "Acute Coronary Syndrome presentation",
        "reasoning_gaps": ["Did not consider atypical presentations"],
        "next_steps": ["Review ACS STEMI vs NSTEMI differentiation"],
        "strength_demonstrated": ["Quick ECG interpretation"]
    }
    */

    -- Context
    session_id UUID, -- Groups interactions in same study session
    was_adaptive_selection BOOLEAN DEFAULT false, -- Was this case selected by AI?
    adaptive_reason TEXT, -- Why AI selected this case

    -- Performance metrics
    points_earned INTEGER DEFAULT 0,

    CONSTRAINT valid_answer_time CHECK (time_to_answer_seconds > 0 AND time_to_answer_seconds < 7200)
);

-- ============================================================================
-- CHAT_HISTORY TABLE
-- Stores AI Coach conversations for context and memory
-- ============================================================================
CREATE TABLE chat_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    -- Conversation
    role TEXT NOT NULL CHECK (role IN ('user', 'assistant')),
    content TEXT NOT NULL,

    -- Context
    session_id UUID, -- Groups messages in same chat session
    related_case_id UUID REFERENCES clinical_cases(id), -- If discussing specific case

    -- Metadata
    token_count INTEGER,
    model_used TEXT DEFAULT 'claude-sonnet-4'
);

-- ============================================================================
-- BADGES TABLE
-- Gamification achievements
-- ============================================================================
CREATE TABLE badges (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    icon_emoji TEXT, -- e.g., "🏆", "⚡", "🎯"

    -- Unlock criteria (evaluated by application logic)
    criteria JSONB NOT NULL,
    /*
    Example:
    {
        "type": "streak",
        "target": 5,
        "description": "Answer 5 cases correctly in a row"
    }
    */

    category TEXT CHECK (category IN ('achievement', 'streak', 'mastery', 'speed', 'special')),
    rarity TEXT CHECK (rarity IN ('common', 'rare', 'epic', 'legendary')),
    points_value INTEGER DEFAULT 0
);

-- ============================================================================
-- USER_BADGES TABLE
-- Tracks which badges each user has earned
-- ============================================================================
CREATE TABLE user_badges (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    earned_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    badge_id UUID NOT NULL REFERENCES badges(id) ON DELETE CASCADE,

    -- Context of earning
    earned_by_interaction_id UUID REFERENCES interactions(id),

    UNIQUE(user_id, badge_id) -- User can only earn each badge once
);

-- ============================================================================
-- INDEXES
-- Optimized for common query patterns
-- ============================================================================

-- Users indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_subscription ON users(subscription_status) WHERE subscription_status = 'paid';

-- Clinical cases indexes
CREATE INDEX idx_cases_specialty ON clinical_cases(specialty);
CREATE INDEX idx_cases_difficulty ON clinical_cases(difficulty_level);
CREATE INDEX idx_cases_active ON clinical_cases(is_active) WHERE is_active = true;
CREATE INDEX idx_cases_specialty_difficulty ON clinical_cases(specialty, difficulty_level) WHERE is_active = true;
CREATE INDEX idx_cases_success_rate ON clinical_cases(global_success_rate);

-- Interactions indexes
CREATE INDEX idx_interactions_user ON interactions(user_id);
CREATE INDEX idx_interactions_case ON interactions(case_id);
CREATE INDEX idx_interactions_user_created ON interactions(user_id, created_at DESC);
CREATE INDEX idx_interactions_session ON interactions(session_id) WHERE session_id IS NOT NULL;
CREATE INDEX idx_interactions_user_case ON interactions(user_id, case_id);

-- Chat history indexes
CREATE INDEX idx_chat_user ON chat_history(user_id);
CREATE INDEX idx_chat_session ON chat_history(session_id) WHERE session_id IS NOT NULL;
CREATE INDEX idx_chat_user_created ON chat_history(user_id, created_at DESC);

-- User badges indexes
CREATE INDEX idx_user_badges_user ON user_badges(user_id);
CREATE INDEX idx_user_badges_badge ON user_badges(badge_id);

-- ============================================================================
-- ROW LEVEL SECURITY (RLS)
-- Users can only access their own data
-- ============================================================================

ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE interactions ENABLE ROW LEVEL SECURITY;
ALTER TABLE chat_history ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_badges ENABLE ROW LEVEL SECURITY;

-- Users can read/update their own profile
CREATE POLICY "Users can view own profile" ON users
    FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update own profile" ON users
    FOR UPDATE USING (auth.uid() = id);

-- Users can access their own interactions
CREATE POLICY "Users can view own interactions" ON interactions
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own interactions" ON interactions
    FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Users can access their own chat history
CREATE POLICY "Users can view own chat history" ON chat_history
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own chat messages" ON chat_history
    FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Users can view their own badges
CREATE POLICY "Users can view own badges" ON user_badges
    FOR SELECT USING (auth.uid() = user_id);

-- Clinical cases are readable by all authenticated users
CREATE POLICY "Authenticated users can view active cases" ON clinical_cases
    FOR SELECT USING (auth.role() = 'authenticated' AND is_active = true);

-- Badges are readable by all authenticated users
CREATE POLICY "Authenticated users can view badges" ON badges
    FOR SELECT USING (auth.role() = 'authenticated');

-- ============================================================================
-- FUNCTIONS
-- Business logic helpers
-- ============================================================================

-- Function to update case statistics after interaction
CREATE OR REPLACE FUNCTION update_case_statistics()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE clinical_cases
    SET
        times_presented = times_presented + 1,
        times_answered_correctly = times_answered_correctly + (CASE WHEN NEW.is_correct THEN 1 ELSE 0 END),
        average_time_to_answer_seconds = (
            COALESCE(average_time_to_answer_seconds * times_presented, 0) + NEW.time_to_answer_seconds
        ) / (times_presented + 1),
        updated_at = NOW()
    WHERE id = NEW.case_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to automatically update case statistics
CREATE TRIGGER trigger_update_case_statistics
    AFTER INSERT ON interactions
    FOR EACH ROW
    EXECUTE FUNCTION update_case_statistics();

-- Function to update user updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for updated_at
CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_cases_updated_at BEFORE UPDATE ON clinical_cases
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- SEED DATA - Initial Badges
-- ============================================================================

INSERT INTO badges (code, name, description, icon_emoji, criteria, category, rarity, points_value) VALUES
('FIRST_WIN', 'Primeira Vitória', 'Acertou seu primeiro caso clínico', '🎯', '{"type": "first_correct", "target": 1}'::jsonb, 'achievement', 'common', 10),
('STREAK_5', 'Sequência de 5', 'Acertou 5 casos seguidos', '🔥', '{"type": "streak", "target": 5}'::jsonb, 'streak', 'common', 50),
('STREAK_10', 'Sequência de 10', 'Acertou 10 casos seguidos', '⚡', '{"type": "streak", "target": 10}'::jsonb, 'streak', 'rare', 100),
('STREAK_25', 'Imparável', 'Acertou 25 casos seguidos', '💫', '{"type": "streak", "target": 25}'::jsonb, 'streak', 'epic', 250),
('SPEED_MASTER', 'Velocidade Cirúrgica', 'Respondeu corretamente em menos de 2 minutos', '⚡', '{"type": "speed", "max_seconds": 120, "must_be_correct": true}'::jsonb, 'speed', 'rare', 75),
('CARDIO_MASTERY', 'Mestre em Cardiologia', 'Acertou 50 casos de cardiologia com >80% de acertos', '❤️', '{"type": "specialty_mastery", "specialty": "cardiologia", "min_cases": 50, "min_rate": 0.8}'::jsonb, 'mastery', 'epic', 200),
('NEURO_MASTERY', 'Mestre em Neurologia', 'Acertou 50 casos de neurologia com >80% de acertos', '🧠', '{"type": "specialty_mastery", "specialty": "neurologia", "min_cases": 50, "min_rate": 0.8}'::jsonb, 'mastery', 'epic', 200),
('NIGHT_OWL', 'Coruja da Madrugada', 'Estudou entre 00h e 06h', '🦉', '{"type": "time_of_day", "start_hour": 0, "end_hour": 6}'::jsonb, 'special', 'common', 25),
('MARATHON', 'Maratona de Estudos', 'Resolveu 30+ casos em um único dia', '🏃', '{"type": "daily_count", "target": 30}'::jsonb, 'achievement', 'rare', 150),
('PERFECT_DAY', 'Dia Perfeito', 'Acertou todos os casos do dia (mínimo 10)', '💯', '{"type": "perfect_day", "min_cases": 10}'::jsonb, 'achievement', 'epic', 300);

-- ============================================================================
-- HELPFUL QUERIES
-- Common queries for application development
-- ============================================================================

-- Get user competency by specialty
COMMENT ON TABLE users IS 'Query user specialty competency:
SELECT
    specialty,
    COUNT(*) as total_attempts,
    SUM(CASE WHEN is_correct THEN 1 ELSE 0 END) as correct_count,
    ROUND(AVG(CASE WHEN is_correct THEN 1 ELSE 0 END) * 100, 2) as success_rate,
    AVG(time_to_answer_seconds) as avg_time
FROM interactions i
JOIN clinical_cases c ON i.case_id = c.id
WHERE user_id = $1
  AND created_at > NOW() - INTERVAL ''30 days''
GROUP BY specialty
ORDER BY success_rate DESC;';

-- Get next adaptive case for user
COMMENT ON TABLE clinical_cases IS 'Query for adaptive case selection:
WITH user_specialty_stats AS (
    SELECT
        c.specialty,
        COUNT(*) as attempts,
        AVG(CASE WHEN i.is_correct THEN 1 ELSE 0 END) as success_rate
    FROM interactions i
    JOIN clinical_cases c ON i.case_id = c.id
    WHERE i.user_id = $1
      AND i.created_at > NOW() - INTERVAL ''7 days''
    GROUP BY c.specialty
),
weak_specialties AS (
    SELECT specialty
    FROM user_specialty_stats
    WHERE success_rate < 0.7
    ORDER BY success_rate ASC
    LIMIT 3
)
SELECT c.*
FROM clinical_cases c
WHERE c.specialty IN (SELECT specialty FROM weak_specialties)
  AND c.is_active = true
  AND c.id NOT IN (
      SELECT case_id
      FROM interactions
      WHERE user_id = $1
        AND created_at > NOW() - INTERVAL ''7 days''
  )
ORDER BY RANDOM()
LIMIT 1;';
