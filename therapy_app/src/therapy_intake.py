"""
Therapy Intake Assessment System

Analyzes user responses to recommend the most appropriate therapist.
"""

from typing import Dict, Tuple


class TherapyIntake:
    """Handles intake assessment and therapist recommendation."""
    
    # Intake questions with scoring weights for each therapist
    QUESTIONS = [
        {
            "id": "primary_concern",
            "question": "What brings you to therapy today?",
            "type": "multiple_choice",
            "options": [
                {"text": "Anxiety, worry, or racing thoughts", "weights": {"Sourdough (Cognitive Behavioral Therapy)": 3, "Naan (Mindfulness-Based Therapy)": 2}},
                {"text": "Depression or feeling stuck", "weights": {"Brioche (Psychodynamic Therapy)": 2, "Ciabatta (Person-Centered Therapy)": 2}},
                {"text": "Relationship or communication issues", "weights": {"Pumpernickel (Dialectical Behavior Therapy)": 3, "Ciabatta (Person-Centered Therapy)": 2}},
                {"text": "Life transitions or finding purpose", "weights": {"Rye (Existential Therapy)": 3, "Focaccia (Solution-Focused Brief Therapy)": 2}},
                {"text": "Emotional regulation difficulties", "weights": {"Pumpernickel (Dialectical Behavior Therapy)": 3, "Whole Wheat (Acceptance and Commitment Therapy)": 2}},
                {"text": "Trauma or past experiences affecting me", "weights": {"Brioche (Psychodynamic Therapy)": 3}},
                {"text": "Stress management and mindfulness", "weights": {"Naan (Mindfulness-Based Therapy)": 3, "Whole Wheat (Acceptance and Commitment Therapy)": 2}},
                {"text": "Specific problem I want to solve quickly", "weights": {"Focaccia (Solution-Focused Brief Therapy)": 3, "Sourdough (Cognitive Behavioral Therapy)": 2}}
            ]
        },
        {
            "id": "therapy_preference",
            "question": "What approach appeals to you most?",
            "type": "multiple_choice",
            "options": [
                {"text": "Practical tools and strategies", "weights": {"Sourdough (Cognitive Behavioral Therapy)": 3, "Pumpernickel (Dialectical Behavior Therapy)": 2}},
                {"text": "Understanding my past and unconscious patterns", "weights": {"Brioche (Psychodynamic Therapy)": 3}},
                {"text": "Accepting myself and living according to my values", "weights": {"Whole Wheat (Acceptance and Commitment Therapy)": 3}},
                {"text": "Being heard and understood without judgment", "weights": {"Ciabatta (Person-Centered Therapy)": 3}},
                {"text": "Finding solutions and focusing on the future", "weights": {"Focaccia (Solution-Focused Brief Therapy)": 3}},
                {"text": "Exploring meaning and authenticity", "weights": {"Rye (Existential Therapy)": 3}},
                {"text": "Mindfulness and present-moment awareness", "weights": {"Naan (Mindfulness-Based Therapy)": 3}}
            ]
        },
        {
            "id": "emotional_style",
            "question": "How would you describe your emotional experience?",
            "type": "multiple_choice",
            "options": [
                {"text": "Intense emotions that feel overwhelming", "weights": {"Pumpernickel (Dialectical Behavior Therapy)": 3, "Naan (Mindfulness-Based Therapy)": 2}},
                {"text": "Stuck in negative thought patterns", "weights": {"Sourdough (Cognitive Behavioral Therapy)": 3}},
                {"text": "Disconnected from my feelings", "weights": {"Brioche (Psychodynamic Therapy)": 2, "Naan (Mindfulness-Based Therapy)": 2}},
                {"text": "Avoiding difficult emotions", "weights": {"Whole Wheat (Acceptance and Commitment Therapy)": 3}},
                {"text": "Generally balanced, just need direction", "weights": {"Focaccia (Solution-Focused Brief Therapy)": 2, "Ciabatta (Person-Centered Therapy)": 2}}
            ]
        },
        {
            "id": "timeline",
            "question": "What's your therapy timeline preference?",
            "type": "multiple_choice",
            "options": [
                {"text": "Short-term, focused on specific goals", "weights": {"Focaccia (Solution-Focused Brief Therapy)": 3, "Sourdough (Cognitive Behavioral Therapy)": 2}},
                {"text": "Medium-term, learning new skills", "weights": {"Pumpernickel (Dialectical Behavior Therapy)": 2, "Whole Wheat (Acceptance and Commitment Therapy)": 2}},
                {"text": "Long-term, deep exploration", "weights": {"Brioche (Psychodynamic Therapy)": 3, "Rye (Existential Therapy)": 2}},
                {"text": "Flexible, whatever it takes", "weights": {"Ciabatta (Person-Centered Therapy)": 2, "Naan (Mindfulness-Based Therapy)": 2}}
            ]
        },
        {
            "id": "goals",
            "question": "What are you hoping to achieve?",
            "type": "text",
            "instruction": "Describe your therapy goals in 1-2 sentences"
        }
    ]
    
    @staticmethod
    def get_questions() -> list:
        """Return all intake questions."""
        return TherapyIntake.QUESTIONS
    
    @staticmethod
    def analyze_responses(responses: Dict) -> Tuple[str, Dict[str, int]]:
        """
        Analyze intake responses and recommend a therapist.
        
        Args:
            responses: Dictionary of question_id -> selected option index
            
        Returns:
            Tuple of (recommended_therapist_key, scores_dict)
        """
        scores = {}
        
        # Process multiple choice questions
        for question in TherapyIntake.QUESTIONS:
            if question["type"] == "multiple_choice":
                question_id = question["id"]
                if question_id in responses:
                    selected_index = responses[question_id]
                    if 0 <= selected_index < len(question["options"]):
                        weights = question["options"][selected_index]["weights"]
                        for therapist, weight in weights.items():
                            scores[therapist] = scores.get(therapist, 0) + weight
        
        # Find therapist with highest score
        if not scores:
            # Default to Person-Centered if no clear preference
            return "Ciabatta (Person-Centered Therapy)", scores
        
        recommended_therapist = max(scores, key=scores.get)
        return recommended_therapist, scores
    
    @staticmethod
    def get_recommendation_explanation(therapist_key: str, scores: Dict[str, int]) -> str:
        """
        Generate explanation for therapist recommendation.
        
        Args:
            therapist_key: Recommended therapist key
            scores: Therapist scores dictionary
            
        Returns:
            Explanation text
        """
        therapist_explanations = {
            "Sourdough (Cognitive Behavioral Therapy)": 
                "Dr. Sourdough specializes in CBT, which is excellent for addressing thought patterns, "
                "anxiety, and developing practical coping strategies. This structured approach helps you "
                "identify and challenge unhelpful thoughts.",
            
            "Brioche (Psychodynamic Therapy)":
                "Dr. Brioche offers psychodynamic therapy to help you explore how past experiences and "
                "unconscious patterns influence your present. This deeper exploration can provide lasting insight.",
            
            "Whole Wheat (Acceptance and Commitment Therapy)":
                "Dr. Whole Wheat practices ACT, helping you accept difficult emotions while committing to "
                "actions aligned with your values. This approach promotes psychological flexibility.",
            
            "Pumpernickel (Dialectical Behavior Therapy)":
                "Dr. Pumpernickel specializes in DBT, offering skills training in mindfulness, distress tolerance, "
                "and emotion regulation. This is particularly helpful for intense emotions and relationship challenges.",
            
            "Ciabatta (Person-Centered Therapy)":
                "Dr. Ciabatta provides person-centered therapy with unconditional positive regard, creating a "
                "safe space for self-discovery and growth. You lead the session direction.",
            
            "Focaccia (Solution-Focused Brief Therapy)":
                "Dr. Focaccia uses solution-focused therapy to help you identify what's already working and "
                "build on your strengths. This forward-looking approach is efficient and goal-oriented.",
            
            "Rye (Existential Therapy)":
                "Dr. Rye offers existential therapy to explore questions of meaning, freedom, and authenticity. "
                "This philosophical approach helps you confront life's fundamental concerns.",
            
            "Naan (Mindfulness-Based Therapy)":
                "Dr. Naan teaches mindfulness-based therapy, cultivating present-moment awareness and "
                "self-compassion. This approach reduces reactivity and promotes inner peace."
        }
        
        explanation = f"Based on your responses, we recommend **{therapist_key}**.\n\n"
        explanation += therapist_explanations.get(therapist_key, "")
        
        # Show top 3 matches
        if len(scores) > 1:
            sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            explanation += "\n\n**Your top matches:**\n"
            for i, (therapist, score) in enumerate(sorted_scores[:3], 1):
                explanation += f"{i}. {therapist} (Match score: {score})\n"
        
        return explanation
