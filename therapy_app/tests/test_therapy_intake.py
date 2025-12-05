"""
Unit tests for TherapyIntake class.

Tests intake assessment questions, response analysis, and therapist recommendations.
"""

import pytest

from src.therapy_intake import TherapyIntake


class TestTherapyIntakeInitialization:
    """Tests for TherapyIntake initialization."""

    def test_initialization(self):
        """Test TherapyIntake initializes correctly."""
        intake = TherapyIntake()
        
        assert intake is not None
        assert hasattr(intake, 'QUESTIONS')

    def test_questions_structure(self):
        """Test that QUESTIONS has correct structure."""
        assert len(TherapyIntake.QUESTIONS) == 5
        
        # Check first 4 are multiple choice
        for i in range(4):
            assert "question" in TherapyIntake.QUESTIONS[i]
            assert "options" in TherapyIntake.QUESTIONS[i]
            assert "type" in TherapyIntake.QUESTIONS[i]
            assert TherapyIntake.QUESTIONS[i]["type"] == "multiple_choice"
        
        # Check last one is text
        assert TherapyIntake.QUESTIONS[4]["type"] == "text"

    def test_questions_have_ids(self):
        """Test that all questions have unique IDs."""
        ids = [q["id"] for q in TherapyIntake.QUESTIONS]
        assert len(ids) == len(set(ids))  # All unique


class TestGetQuestions:
    """Tests for getting intake questions."""

    def test_get_questions_returns_all(self):
        """Test that get_questions returns all questions."""
        intake = TherapyIntake()
        questions = intake.get_questions()
        
        assert len(questions) == 5

    def test_get_questions_structure(self):
        """Test that returned questions have expected structure."""
        intake = TherapyIntake()
        questions = intake.get_questions()
        
        for question in questions[:4]:  # Multiple choice
            assert "id" in question
            assert "question" in question
            assert "type" in question
            assert "options" in question


class TestAnalyzeResponses:
    """Tests for analyzing intake responses."""

    def test_analyze_responses_returns_tuple(self):
        """Test that analyze_responses returns (therapist, scores) tuple."""
        responses = {
            "primary_concern": 0,
            "therapy_preference": 0,
            "emotional_style": 0,
            "timeline": 0,
            "goals": "Test goal"
        }
        
        result = TherapyIntake.analyze_responses(responses)
        
        assert isinstance(result, tuple)
        assert len(result) == 2
        
        recommended, scores = result
        assert isinstance(recommended, str)
        assert isinstance(scores, dict)

    def test_analyze_responses_with_anxiety_concern(self):
        """Test analysis with anxiety as primary concern."""
        responses = {
            "primary_concern": 0,  # Anxiety
            "therapy_preference": 0,  # Practical tools
            "emotional_style": 1,  # Stuck in thoughts
            "timeline": 0,  # Short-term
            "goals": "Manage anxiety"
        }
        
        recommended, scores = TherapyIntake.analyze_responses(responses)
        
        # Should recommend a therapist
        assert recommended is not None
        assert len(scores) > 0
        
        # Sourdough (CBT) should have points for anxiety and practical tools
        cbt_key = "Sourdough (Cognitive Behavioral Therapy)"
        assert cbt_key in scores
        assert scores[cbt_key] > 0

    def test_analyze_responses_with_relationship_issues(self):
        """Test analysis with relationship issues."""
        responses = {
            "primary_concern": 2,  # Relationships
            "therapy_preference": 3,  # Being heard
            "emotional_style": 0,  # Intense emotions
            "timeline": 1,  # Medium-term
            "goals": "Improve relationships"
        }
        
        recommended, scores = TherapyIntake.analyze_responses(responses)
        
        assert recommended is not None
        # Should recommend therapist good for relationships
        assert len(scores) > 0

    def test_analyze_responses_returns_highest_scorer(self):
        """Test that recommended therapist has highest or tied score."""
        responses = {
            "primary_concern": 0,
            "therapy_preference": 0,
            "emotional_style": 0,
            "timeline": 0,
            "goals": "Test"
        }
        
        recommended, scores = TherapyIntake.analyze_responses(responses)
        
        if scores:  # If any scores were assigned
            max_score = max(scores.values())
            assert scores[recommended] == max_score

    def test_analyze_responses_with_mindfulness_preference(self):
        """Test analysis with mindfulness preference."""
        responses = {
            "primary_concern": 6,  # Stress management
            "therapy_preference": 6,  # Mindfulness
            "emotional_style": 0,  # Intense emotions
            "timeline": 1,  # Medium
            "goals": "Be more present"
        }
        
        recommended, scores = TherapyIntake.analyze_responses(responses)
        
        # Naan (Mindfulness) should score well
        naan_key = "Naan (Mindfulness-Based Therapy)"
        assert naan_key in scores
        assert scores[naan_key] > 0

    def test_analyze_responses_handles_empty_scores(self):
        """Test analyze handles case where no scores match."""
        # Responses that might not match standard patterns
        responses = {
            "goals": "Just some text"
        }
        
        recommended, scores = TherapyIntake.analyze_responses(responses)
        
        # Should return default (Ciabatta)
        assert recommended is not None
        assert "Ciabatta" in recommended

    def test_analyze_responses_with_all_valid_responses(self):
        """Test with all questions answered."""
        responses = {
            "primary_concern": 0,
            "therapy_preference": 0,
            "emotional_style": 0,
            "timeline": 0,
            "goals": "Comprehensive goals text"
        }
        
        recommended, scores = TherapyIntake.analyze_responses(responses)
        
        assert recommended is not None
        assert isinstance(scores, dict)

    def test_analyze_responses_score_accumulation(self):
        """Test that scores accumulate across multiple questions."""
        # Choose CBT-favoring options
        responses = {
            "primary_concern": 0,  # Anxiety -> CBT gets points
            "therapy_preference": 0,  # Practical tools -> CBT gets points
            "emotional_style": 1,  # Stuck in thoughts -> CBT gets points
            "timeline": 0,
            "goals": "Test"
        }
        
        recommended, scores = TherapyIntake.analyze_responses(responses)
        
        cbt_key = "Sourdough (Cognitive Behavioral Therapy)"
        # CBT should have accumulated points from multiple questions
        if cbt_key in scores:
            assert scores[cbt_key] >= 3  # Should have at least 3 points


class TestGetRecommendationExplanation:
    """Tests for getting recommendation explanation."""

    def test_get_explanation_returns_string(self):
        """Test that explanation returns a string."""
        scores = {
            "Sourdough (Cognitive Behavioral Therapy)": 10,
            "Brioche (Psychodynamic Therapy)": 5,
            "Whole Wheat (Acceptance and Commitment Therapy)": 3
        }
        
        explanation = TherapyIntake.get_recommendation_explanation(
            "Sourdough (Cognitive Behavioral Therapy)", scores
        )
        
        assert isinstance(explanation, str)
        assert len(explanation) > 0

    def test_explanation_includes_therapist_name(self):
        """Test that explanation includes the recommended therapist."""
        scores = {"Sourdough (Cognitive Behavioral Therapy)": 10}
        
        explanation = TherapyIntake.get_recommendation_explanation(
            "Sourdough (Cognitive Behavioral Therapy)", scores
        )
        
        assert "Sourdough" in explanation

    def test_explanation_includes_approach_description(self):
        """Test that explanation describes the therapeutic approach."""
        scores = {"Sourdough (Cognitive Behavioral Therapy)": 10}
        
        explanation = TherapyIntake.get_recommendation_explanation(
            "Sourdough (Cognitive Behavioral Therapy)", scores
        )
        
        # Should mention CBT
        assert "CBT" in explanation or "Cognitive Behavioral" in explanation

    def test_explanation_shows_top_matches(self):
        """Test that explanation shows top 3 matches when multiple exist."""
        scores = {
            "Sourdough (Cognitive Behavioral Therapy)": 10,
            "Brioche (Psychodynamic Therapy)": 9,
            "Whole Wheat (Acceptance and Commitment Therapy)": 8,
            "Pumpernickel (Dialectical Behavior Therapy)": 2
        }
        
        explanation = TherapyIntake.get_recommendation_explanation(
            "Sourdough (Cognitive Behavioral Therapy)", scores
        )
        
        # Should mention top matches
        assert "top matches" in explanation.lower() or "match score" in explanation.lower()

    def test_explanation_for_different_therapists(self):
        """Test that different therapists get appropriate explanations."""
        scores = {"Brioche (Psychodynamic Therapy)": 10}
        
        explanation = TherapyIntake.get_recommendation_explanation(
            "Brioche (Psychodynamic Therapy)", scores
        )
        
        # Should mention psychodynamic approach
        assert "psychodynamic" in explanation.lower() or "past" in explanation.lower()

    def test_explanation_handles_single_therapist(self):
        """Test explanation when only one therapist has scores."""
        scores = {"Naan (Mindfulness-Based Therapy)": 5}
        
        explanation = TherapyIntake.get_recommendation_explanation(
            "Naan (Mindfulness-Based Therapy)", scores
        )
        
        assert isinstance(explanation, str)
        assert len(explanation) > 0


class TestIntegration:
    """Integration tests for complete intake flow."""

    def test_complete_intake_flow(self):
        """Test complete intake assessment flow."""
        intake = TherapyIntake()
        
        # Get questions
        questions = intake.get_questions()
        assert len(questions) == 5
        
        # Create responses
        responses = {
            "primary_concern": 0,
            "therapy_preference": 0,
            "emotional_style": 0,
            "timeline": 0,
            "goals": "I want to manage my anxiety better"
        }
        
        # Analyze responses
        recommended, scores = TherapyIntake.analyze_responses(responses)
        assert recommended is not None
        assert len(scores) > 0
        
        # Get explanation
        explanation = TherapyIntake.get_recommendation_explanation(recommended, scores)
        assert isinstance(explanation, str)
        assert len(explanation) > 50

    def test_different_responses_lead_to_different_recommendations(self):
        """Test that varied responses can lead to different recommendations."""
        # Anxiety/CBT focused
        anxiety_responses = {
            "primary_concern": 0,
            "therapy_preference": 0,
            "emotional_style": 1,
            "timeline": 0,
            "goals": "Manage anxiety"
        }
        
        # Relationship/person-centered focused
        relationship_responses = {
            "primary_concern": 2,
            "therapy_preference": 3,
            "emotional_style": 2,
            "timeline": 1,
            "goals": "Improve relationships"
        }
        
        rec1, scores1 = TherapyIntake.analyze_responses(anxiety_responses)
        rec2, scores2 = TherapyIntake.analyze_responses(relationship_responses)
        
        # Both should return valid recommendations
        assert rec1 is not None
        assert rec2 is not None
        
        # Score distributions should be different
        assert scores1 != scores2

    def test_consistency_across_multiple_calls(self):
        """Test that same input produces same output consistently."""
        responses = {
            "primary_concern": 0,
            "therapy_preference": 0,
            "emotional_style": 0,
            "timeline": 0,
            "goals": "Test"
        }
        
        rec1, scores1 = TherapyIntake.analyze_responses(responses)
        rec2, scores2 = TherapyIntake.analyze_responses(responses)
        
        assert rec1 == rec2
        assert scores1 == scores2
