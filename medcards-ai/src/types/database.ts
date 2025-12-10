/**
 * MEDCARDS.AI - Database Types
 * TypeScript interfaces matching Supabase schema
 */

// ============================================================================
// Core Database Tables
// ============================================================================

export interface User {
  id: string;
  email: string;
  full_name: string | null;
  created_at: string;
  updated_at: string;
  progress: UserProgress;
  preferences: UserPreferences;
  subscription_status: 'free' | 'trial' | 'paid' | 'cancelled';
  subscription_ends_at: string | null;
}

export interface UserProgress {
  specialties: Record<string, SpecialtyProgress>;
  overall_stats: {
    total_cases_attempted: number;
    total_cases_correct: number;
    total_time_spent_seconds: number;
    current_streak: number;
    longest_streak: number;
    last_activity_date: string | null;
  };
  badges_earned: string[]; // Array of badge IDs
  level: number;
  experience_points: number;
}

export interface SpecialtyProgress {
  attempts: number;
  correct: number;
  success_rate: number;
  avg_time_seconds: number;
  last_attempt: string;
  trend: 'improving' | 'stable' | 'declining' | 'new';
}

export interface UserPreferences {
  daily_goal_cases: number;
  preferred_specialties: string[];
  notification_enabled: boolean;
  theme: 'light' | 'dark';
}

export interface ClinicalCase {
  id: string;
  created_at: string;
  updated_at: string;
  case_code: string;
  title: string;
  clinical_presentation: string;
  patient_data: PatientData;
  question: string;
  options: CaseOption[];
  correct_answer_id: string;
  explanation: string;
  clinical_reasoning: string;
  key_concepts: string[];
  differential_diagnosis: string[];
  specialty: string;
  subspecialty: string | null;
  difficulty_level: 1 | 2 | 3 | 4 | 5;
  clinical_algorithm: string;
  times_presented: number;
  times_answered_correctly: number;
  average_time_to_answer_seconds: number | null;
  global_success_rate: number;
  source: string;
  tags: string[];
  is_active: boolean;
}

export interface PatientData {
  age: number;
  sex: 'masculino' | 'feminino';
  vitals?: {
    blood_pressure?: string;
    heart_rate?: number;
    respiratory_rate?: number;
    temperature?: number;
    spo2?: number;
    glasgow?: number;
  };
  labs?: Record<string, any>;
  imaging?: Record<string, string>;
  ecg?: string;
  comorbidities?: string[];
  medications?: string[];
  [key: string]: any; // Allow additional custom fields
}

export interface CaseOption {
  id: string; // "A", "B", "C", "D", etc.
  text: string;
  is_correct: boolean;
}

export interface Interaction {
  id: string;
  created_at: string;
  user_id: string;
  case_id: string;
  selected_answer_id: string;
  is_correct: boolean;
  time_to_answer_seconds: number;
  student_reasoning: string | null;
  confidence_level: 1 | 2 | 3 | 4 | 5 | null;
  hints_used: Hint[];
  hint_count: number;
  ai_coach_consulted: boolean;
  ai_feedback: AIFeedback | null;
  session_id: string | null;
  was_adaptive_selection: boolean;
  adaptive_reason: string | null;
  points_earned: number;
}

export interface Hint {
  hint_level: number;
  hint_text: string;
  points_cost: number;
  timestamp: string;
}

export interface AIFeedback {
  verdict: 'correct' | 'incorrect';
  correct_answer_id: string;
  immediate_feedback: string;
  clinical_pattern: {
    name: string;
    key_features: string[];
    pathophysiology_brief: string;
  };
  reasoning_analysis: {
    what_student_got_right: string[];
    critical_mistake: string;
    information_missed: string[];
    cognitive_error_type: string;
  };
  correct_reasoning_path: Record<string, string>;
  key_takeaways: string[];
  common_exam_traps: string[];
  next_steps: {
    immediate_practice: string[];
    concept_to_review: string;
    similar_patterns: string[];
  };
  encouragement: {
    positive_reinforcement: string;
    growth_mindset: string;
    progress_note: string;
  };
  difficulty_rating: {
    case_difficulty: number;
    why_challenging: string;
    student_should_have_known: boolean;
    acceptable_mistake_for_level: boolean;
  };
  metadata: {
    feedback_generated_at: string;
    model_used: string;
    tokens_used: number;
  };
}

export interface ChatMessage {
  id: string;
  created_at: string;
  user_id: string;
  role: 'user' | 'assistant';
  content: string;
  session_id: string | null;
  related_case_id: string | null;
  token_count: number | null;
  model_used: string;
}

export interface Badge {
  id: string;
  created_at: string;
  code: string;
  name: string;
  description: string;
  icon_emoji: string | null;
  criteria: BadgeCriteria;
  category: 'achievement' | 'streak' | 'mastery' | 'speed' | 'special';
  rarity: 'common' | 'rare' | 'epic' | 'legendary';
  points_value: number;
}

export interface BadgeCriteria {
  type: string;
  target?: number;
  max_seconds?: number;
  must_be_correct?: boolean;
  specialty?: string;
  min_cases?: number;
  min_rate?: number;
  start_hour?: number;
  end_hour?: number;
  description?: string;
}

export interface UserBadge {
  id: string;
  earned_at: string;
  user_id: string;
  badge_id: string;
  earned_by_interaction_id: string | null;
}

// ============================================================================
// API Response Types
// ============================================================================

export interface NextCaseResponse {
  case: ClinicalCase;
  selection_reasoning: {
    primary_goal: 'address_weakness' | 'reinforce_strength' | 'explore_new';
    specialty_targeted: string;
    specific_gap: string;
    expected_outcome: string;
    confidence_this_helps: number;
  };
  coaching_message: string;
  hints_prepared: {
    hint_level: number;
    hint_text: string;
    points_cost: number;
  }[];
  success_criteria: {
    target_time_seconds: number;
    key_reasoning_steps: string[];
  };
}

export interface SubmitAnswerResponse {
  is_correct: boolean;
  feedback: AIFeedback;
  points_earned: number;
  new_badges_unlocked: Badge[];
  updated_progress: UserProgress;
}

export interface DashboardStats {
  overall_stats: {
    total_cases: number;
    success_rate: number;
    current_streak: number;
    avg_time_per_case: number;
  };
  specialty_performance: {
    specialty: string;
    attempts: number;
    success_rate: number;
    trend: 'improving' | 'stable' | 'declining';
  }[];
  recent_activity: {
    date: string;
    cases_completed: number;
    success_rate: number;
  }[];
  weak_areas: {
    clinical_algorithm: string;
    specialty: string;
    success_rate: number;
    attempts: number;
  }[];
  badges_progress: {
    total_earned: number;
    total_available: number;
    recently_earned: Badge[];
  };
}

// ============================================================================
// Utility Types
// ============================================================================

export type SubscriptionStatus = User['subscription_status'];
export type Specialty = string; // Could be union type of all specialties
export type DifficultyLevel = ClinicalCase['difficulty_level'];
export type BadgeCategory = Badge['category'];
export type BadgeRarity = Badge['rarity'];

// ============================================================================
// Query Filter Types
// ============================================================================

export interface CaseFilter {
  specialty?: string;
  subspecialty?: string;
  difficulty_level?: DifficultyLevel;
  clinical_algorithm?: string;
  tags?: string[];
  exclude_case_ids?: string[];
}

export interface InteractionFilter {
  user_id: string;
  specialty?: string;
  start_date?: string;
  end_date?: string;
  is_correct?: boolean;
  limit?: number;
}
