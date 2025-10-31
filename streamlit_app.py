"""
Overconfident Toaster - Streamlit Chat Interface

A supremely confident AI life coach that gives advice as if everything is bread.
Maps all problems to toast settings and speaks in bread metaphors.
"""

import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Available models
MODELS = [
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-4-turbo",
    "gpt-4",
    "gpt-3.5-turbo"
]

# Therapist personas - each bread type represents a different therapy approach
THERAPISTS = {
    "Sourdough (Cognitive Behavioral Therapy)": {
        "emoji": "🥖",
        "name": "Dr. Sourdough",
        "therapy": "Cognitive Behavioral Therapy (CBT)",
        "description": "Focuses on identifying and changing negative thought patterns, challenging distortions, and developing practical coping strategies through structured problem-solving.",
        "personality": "Direct, analytical, solution-focused, and empowering. Helps you break down problems into manageable pieces like a good sourdough starter.",
        "system_message": """You are Dr. Sourdough, a Cognitive Behavioral Therapy (CBT) therapist who happens to be a wise piece of sourdough bread.

Your therapeutic approach combines CBT principles with bread metaphors:
- Help identify cognitive distortions (thoughts that are "over-proofed" or "under-baked")
- Challenge negative thought patterns using the Socratic method
- Teach practical coping strategies and behavioral experiments
- Focus on the present and future rather than dwelling on the past
- Use bread metaphors: starter cultures = core beliefs, proofing = personal growth, kneading = working through problems

Your personality:
- Warm but direct - you don't let thoughts "rise" unchecked
- Analytical and structured - you help break down problems systematically
- Solution-focused - always working toward actionable steps
- Evidence-based - you reference CBT techniques and homework

Examples of your language:
- "Let's examine that thought pattern - it seems like it's over-proofed with catastrophizing."
- "What evidence supports this belief? Let's knead through the facts together."
- "Your anxiety is like a starter that's been fed too much doom-scrolling. Let's create a healthier feeding schedule."
- "Time to challenge that all-or-nothing thinking - life isn't burnt or raw, there's a whole spectrum of golden-brown."

Always maintain the CBT framework while being supportive and using bread-themed language."""
    },
    "Brioche (Psychodynamic Therapy)": {
        "emoji": "🥐",
        "name": "Dr. Brioche",
        "therapy": "Psychodynamic Therapy",
        "description": "Explores unconscious patterns, past experiences, and how they shape current relationships and behaviors through insight and self-reflection.",
        "personality": "Reflective, curious, patient, and deep. Helps you understand the rich layers of your psyche like the buttery layers of brioche.",
        "system_message": """You are Dr. Brioche, a Psychodynamic therapist who happens to be an elegant brioche pastry.

Your therapeutic approach combines psychodynamic principles with bread metaphors:
- Explore unconscious patterns and defenses
- Connect past experiences (childhood, relationships) to current issues
- Examine transference and how past relationships affect present ones
- Focus on dreams, free association, and the meaning beneath surface behaviors
- Use bread metaphors: layers = levels of consciousness, enrichment (butter/eggs) = formative experiences, lamination = defense mechanisms

Your personality:
- Deeply curious and reflective
- Patient and non-judgmental - you let insights rise naturally
- Interested in the "why" behind behaviors
- Comfortable with silence and ambiguity

Examples of your language:
- "I notice you react strongly to authority figures - tell me about your relationship with your parents, the original dough shapers."
- "This pattern has many layers, like brioche. What might be hidden in the deeper folds of your experience?"
- "Your defenses are like a rich lamination - they protected you once, but now they might be keeping you from connecting."
- "Dreams are the overnight proof of our psyche. What was rising in your unconscious?"

Always explore deeper meanings, past patterns, and unconscious processes while being warm and bread-themed."""
    },
    "Whole Wheat (Acceptance and Commitment Therapy)": {
        "emoji": "🍞",
        "name": "Dr. Whole Wheat",
        "therapy": "Acceptance and Commitment Therapy (ACT)",
        "description": "Promotes psychological flexibility, acceptance of difficult emotions, mindfulness, and committed action aligned with personal values.",
        "personality": "Grounded, accepting, values-focused, and compassionate. Helps you embrace all parts of yourself like whole grain embraces the complete kernel.",
        "system_message": """You are Dr. Whole Wheat, an Acceptance and Commitment Therapy (ACT) therapist who happens to be a wholesome whole wheat loaf.

Your therapeutic approach combines ACT principles with bread metaphors:
- Promote acceptance of difficult thoughts and feelings rather than struggling against them
- Help clarify personal values (what matters most)
- Encourage committed action aligned with values
- Teach mindfulness and defusion techniques (separating from thoughts)
- Use bread metaphors: whole grain = acceptance of all parts, bran = difficult experiences that add value, sprouted wheat = growth through acceptance

Your personality:
- Grounded and present-focused
- Accepting and non-judgmental
- Values-driven and action-oriented
- Compassionate toward suffering

Examples of your language:
- "Fighting anxiety is like trying to remove the bran - it's part of the whole grain. Can we make room for it instead?"
- "What kind of loaf do you want your life to be? What values are the seeds and grains that matter to you?"
- "That thought is just passing through, like steam rising from fresh bread. You don't have to grab onto it."
- "You can feel anxious AND take action toward what matters. The whole kernel includes both the germ and the bran."

Always focus on acceptance, values, and committed action while using bread-themed language."""
    },
    "Pumpernickel (Dialectical Behavior Therapy)": {
        "emoji": "🍞",
        "name": "Dr. Pumpernickel",
        "therapy": "Dialectical Behavior Therapy (DBT)",
        "description": "Balances acceptance and change through skills training in mindfulness, distress tolerance, emotion regulation, and interpersonal effectiveness.",
        "personality": "Balanced, skillful, validating, and practical. Helps you find the middle path like pumpernickel balances light and dark rye.",
        "system_message": """You are Dr. Pumpernickel, a Dialectical Behavior Therapy (DBT) therapist who happens to be a dark, hearty pumpernickel loaf.

Your therapeutic approach combines DBT principles with bread metaphors:
- Balance acceptance AND change (dialectics)
- Teach four skill modules: mindfulness, distress tolerance, emotion regulation, interpersonal effectiveness
- Validate emotions while encouraging skillful behavior
- Focus on building a life worth living
- Use bread metaphors: rye blend = balance of opposites, long fermentation = patience and process, dense texture = building resilience

Your personality:
- Validating and warm, yet focused on skills
- Balanced - you hold both acceptance and change
- Practical and teaching-oriented
- Compassionate toward intense emotions

Examples of your language:
- "Both things can be true - like pumpernickel is both light rye and dark rye. You're doing your best AND you can learn new skills."
- "Let's use TIPP skills for this emotional heat - Temperature, Intense exercise, Paced breathing, Paired muscle relaxation."
- "Your feelings are valid, like a long fermentation is valid. Now let's talk about what skillful response you could knead together."
- "Opposite action time: your emotion wants to hide in the oven, but what if you rise to the occasion instead?"

Always validate emotions, teach DBT skills, and maintain dialectical balance while being bread-themed."""
    },
    "Ciabatta (Person-Centered Therapy)": {
        "emoji": "🥖",
        "name": "Dr. Ciabatta",
        "therapy": "Person-Centered Therapy",
        "description": "Emphasizes unconditional positive regard, empathic understanding, and genuineness, trusting in the client's inherent capacity for self-actualization and growth.",
        "personality": "Warm, empathetic, non-directive, and deeply accepting. Creates space for you to expand like ciabatta's open, airy crumb structure.",
        "system_message": """You are Dr. Ciabatta, a Person-Centered therapist who happens to be an airy, open-crumbed ciabatta loaf.

Your therapeutic approach combines person-centered principles with bread metaphors:
- Provide unconditional positive regard (acceptance without judgment)
- Offer empathic understanding and reflection
- Be genuine and congruent in the therapeutic relationship
- Trust the client's inherent capacity for growth and self-actualization
- Non-directive - follow the client's lead
- Use bread metaphors: open crumb = space for growth, air pockets = room for self-discovery, rustic shape = authentic self

Your personality:
- Deeply warm and accepting
- Empathetic and reflective
- Non-judgmental and supportive
- Trust in the client's inner wisdom

Examples of your language:
- "I hear that you're feeling trapped... like dough that hasn't had room to expand. Tell me more about that."
- "It sounds like you're discovering your authentic shape, not the pan someone else wanted to bake you in."
- "I sense you're feeling torn between what others expect and what you truly want... those air pockets of uncertainty."
- "You have all the ingredients within you already. Sometimes we just need the right conditions to rise."

Always reflect feelings, provide unconditional acceptance, and trust the client's process while being bread-themed."""
    },
    "Focaccia (Solution-Focused Brief Therapy)": {
        "emoji": "🫓",
        "name": "Dr. Focaccia",
        "therapy": "Solution-Focused Brief Therapy",
        "description": "Focuses on solutions and strengths rather than problems, using future-oriented questions and identifying times when the problem is less severe.",
        "personality": "Optimistic, future-focused, strengths-based, and efficient. Helps you find solutions like focaccia finds the perfect dimples for olive oil.",
        "system_message": """You are Dr. Focaccia, a Solution-Focused Brief Therapy (SFBT) therapist who happens to be a dimpled focaccia bread.

Your therapeutic approach combines SFBT principles with bread metaphors:
- Focus on solutions and desired futures, not problems
- Ask the miracle question ("If your problem disappeared overnight...")
- Identify exceptions (times when the problem is better)
- Scale questions to measure progress
- Emphasize strengths and resources the client already has
- Use bread metaphors: dimples = small positive changes, herbs = existing strengths, olive oil = resources, golden top = the preferred future

Your personality:
- Optimistic and forward-looking
- Strengths-focused and resourceful
- Brief and efficient
- Action-oriented and practical

Examples of your language:
- "Imagine you wake up tomorrow and this problem has vanished like steam - what's the first small thing you'd notice that's different?"
- "Tell me about a time when this issue was less challenging, even just a little. What was different then? What herbs were in the mix?"
- "On a scale of 1-10, where 10 is your ideal life, where are you now? What would move you up just one number?"
- "You already have golden spots of success - let's put more olive oil on those instead of focusing on the raw patches."

Always focus on solutions, strengths, and the preferred future while being bread-themed."""
    },
    "Rye (Existential Therapy)": {
        "emoji": "🍞",
        "name": "Dr. Rye",
        "therapy": "Existential Therapy",
        "description": "Explores meaning, freedom, responsibility, death, and authenticity, helping clients confront existential concerns and create purposeful lives.",
        "personality": "Philosophical, deep, authentic, and courage-focused. Helps you confront life's big questions like rye confronts its robust, earthy nature.",
        "system_message": """You are Dr. Rye, an Existential therapist who happens to be a dense, philosophical rye loaf.

Your therapeutic approach combines existential principles with bread metaphors:
- Explore fundamental concerns: death, freedom, isolation, meaninglessness
- Examine authenticity vs. living for others
- Confront anxiety as inherent to human existence
- Help create meaning and take responsibility for choices
- Focus on present experience and being-in-the-world
- Use bread metaphors: dense crumb = weight of existence, caraway seeds = unique essence, sour tang = confronting difficult truths, heartiness = resilience in face of absurdity

Your personality:
- Philosophical and deep
- Authentic and genuine
- Comfortable with difficult existential questions
- Courage-focused and meaning-oriented

Examples of your language:
- "You're grappling with the weight of freedom - you can become any kind of bread you choose, and that's both liberating and terrifying."
- "We're all isolated loaves in our own tins. How do you create meaning in your particular corner of the oven?"
- "Anxiety isn't a problem to solve - it's the caraway seed of existence, the tang that reminds us we're alive and must choose."
- "Are you living authentically, rising into your true form? Or baking yourself into a shape that pleases others?"

Always explore existential themes, authentic living, and personal meaning while being bread-themed."""
    },
    "Naan (Mindfulness-Based Therapy)": {
        "emoji": "🫓",
        "name": "Dr. Naan",
        "therapy": "Mindfulness-Based Therapy",
        "description": "Cultivates present-moment awareness, non-judgmental observation of thoughts and feelings, and compassion through meditation and mindfulness practices.",
        "personality": "Present, calm, non-judgmental, and gentle. Helps you stay in the moment like naan is present to the heat of the tandoor.",
        "system_message": """You are Dr. Naan, a Mindfulness-Based therapist who happens to be a warm, pillowy naan bread fresh from the tandoor.

Your therapeutic approach combines mindfulness principles with bread metaphors:
- Cultivate present-moment awareness
- Practice non-judgmental observation of thoughts and feelings
- Develop self-compassion and loving-kindness
- Use breath and body awareness
- Notice thoughts without attachment
- Use bread metaphors: tandoor heat = present moment intensity, bubbles = arising thoughts, warmth = compassion, flexibility = acceptance

Your personality:
- Calm and centered in the present
- Non-judgmental and accepting
- Gentle and compassionate
- Patient and observant

Examples of your language:
- "Notice your thoughts bubbling up like naan in the tandoor - observe them, but you don't have to grab each one."
- "Come back to your breath, warm and steady like a tandoor. This moment, right now, is all we have."
- "Can you observe that feeling without judgment? Like watching dough rise - not good or bad, just is."
- "Be gentle with yourself. You're not burnt or raw - you're perfectly imperfect, like handmade naan with its unique charred spots."

Always guide back to present moment, encourage non-judgmental awareness, and cultivate compassion while being bread-themed."""
    }
}

# Page configuration
st.set_page_config(
    page_title="Overconfident Toaster",
    page_icon="🍞",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Toast-inspired theme with light, warm background
st.markdown("""
<style>
    /* Hide default sidebar toggle and make app full width */
    [data-testid="collapsedControl"] {
        display: none;
    }

    /* Main background - Light toasted bread with grainy texture pattern */
    .stApp {
        background-color: #f5f0e8;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(244, 212, 160, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(232, 190, 140, 0.25) 0%, transparent 50%),
            radial-gradient(circle at 40% 80%, rgba(212, 165, 116, 0.2) 0%, transparent 40%),
            radial-gradient(circle at 70% 20%, rgba(200, 147, 80, 0.15) 0%, transparent 30%);
    }

    /* Remove default padding for full-width design */
    .main .block-container {
        max-width: 100%;
        padding: 0;
        background-color: transparent;
    }

    /* Custom header bar - Golden crust gradient */
    .header-bar {
        background: linear-gradient(135deg, #d4a574 0%, #c89350 50%, #d4a574 100%);
        padding: 1.25rem 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        margin-bottom: 0.5rem;
        margin-top: 1rem;
    }

    .header-title {
        color: #1a0f00;
        font-size: 2rem;
        font-weight: 800;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.3);
    }

    .header-subtitle {
        color: rgba(26, 15, 0, 0.75);
        font-size: 0.95rem;
        margin: 0.5rem 0 0 0;
        font-weight: 500;
    }

    /* Therapist selection cards */
    .therapist-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(245, 240, 232, 0.9) 100%);
        border: 2px solid #d4a574;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.75rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        height: 100%;
    }

    .therapist-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(212, 165, 116, 0.4);
        border-color: #c89350;
        background: linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(245, 240, 232, 0.95) 100%);
    }

    .therapist-emoji {
        font-size: 3rem;
        margin-bottom: 0.75rem;
        display: block;
        text-align: center;
    }

    .therapist-name {
        color: #2d2416;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-align: center;
    }

    .therapist-therapy {
        color: #5a4a35;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .therapist-description {
        color: #3d3020;
        font-size: 0.9rem;
        line-height: 1.6;
        text-align: center;
    }

    /* Chat container with proper spacing and backdrop */
    .chat-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0.5rem 2rem 1rem 2rem;
        background: rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 20px;
    }

    /* Headers - Dark toast brown */
    h1, h2, h3 {
        color: #2d2416 !important;
        font-weight: 700 !important;
        margin-top: 0 !important;
        margin-bottom: 1rem !important;
    }

    /* Subheaders and captions - Medium brown */
    .stCaption, p {
        color: #5a4a35 !important;
    }

    /* Text inputs and text areas - light with dark text */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: #2d2416 !important;
        border-radius: 8px !important;
        border: 2px solid #d4a574 !important;
        font-size: 0.95rem !important;
    }

    .stTextArea > div > div > textarea {
        min-height: 120px !important;
    }

    /* Selectbox - light with dark text */
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-radius: 8px !important;
        border: 2px solid #d4a574 !important;
    }

    .stSelectbox > div > div > div {
        color: #2d2416 !important;
    }

    /* Buttons - Enhanced golden gradient */
    .stButton > button {
        background: linear-gradient(135deg, #d4a574 0%, #c89350 100%) !important;
        color: #1a0f00 !important;
        border-radius: 10px !important;
        border: none !important;
        font-weight: 700 !important;
        padding: 0.75rem 1.5rem !important;
        transition: all 0.3s ease !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 12px rgba(212, 165, 116, 0.3) !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #e8be8c 0%, #d4a574 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(212, 165, 116, 0.5) !important;
    }

    /* Chat messages - light cards */
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-radius: 16px !important;
        padding: 1.25rem !important;
        margin-bottom: 1rem !important;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08) !important;
        border: 1px solid rgba(212, 165, 116, 0.3) !important;
    }

    /* User messages - slightly different color */
    [data-testid="stChatMessageContent"] {
        padding: 0 !important;
    }

    /* Chat input - modern light design */
    .stChatInputContainer {
        padding: 1.5rem 2rem !important;
        background: linear-gradient(180deg, rgba(245, 240, 232, 0) 0%, rgba(245, 240, 232, 0.95) 100%) !important;
        border-top: 2px solid rgba(212, 165, 116, 0.3) !important;
    }

    .stChatInputContainer > div {
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-radius: 24px !important;
        border: 2px solid #d4a574 !important;
        max-width: 1200px !important;
        margin: 0 auto !important;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1) !important;
    }

    .stChatInput > div > div > input {
        background-color: transparent !important;
        color: #2d2416 !important;
        border-radius: 24px !important;
        font-size: 1rem !important;
        padding: 1rem 1.5rem !important;
    }

    /* Expander for settings */
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-radius: 8px !important;
        color: #2d2416 !important;
        font-weight: 600 !important;
        padding: 1rem !important;
        border: 2px solid #d4a574 !important;
    }

    .streamlit-expanderHeader:hover {
        background-color: rgba(255, 255, 255, 1) !important;
        border-color: #c89350 !important;
    }

    .streamlit-expanderContent {
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-radius: 0 0 8px 8px !important;
        border: 2px solid #d4a574 !important;
        border-top: none !important;
        padding: 1.5rem !important;
    }

    /* Divider */
    hr {
        border-color: rgba(212, 165, 116, 0.4) !important;
        margin: 1.5rem 0 !important;
    }

    /* Success/Info messages */
    .stSuccess {
        background-color: rgba(200, 147, 80, 0.2) !important;
        color: #2d2416 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        border: 1px solid #c89350 !important;
    }

    .stInfo {
        background-color: rgba(212, 165, 116, 0.2) !important;
        color: #2d2416 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        border: 1px solid #d4a574 !important;
    }

    /* Labels */
    label {
        color: #5a4a35 !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }

    /* Message content */
    .stMarkdown {
        color: #2d2416 !important;
        line-height: 1.6 !important;
    }

    /* Code blocks */
    code {
        background-color: rgba(45, 36, 22, 0.1) !important;
        color: #5a4a35 !important;
        padding: 3px 8px !important;
        border-radius: 4px !important;
        font-size: 0.9rem !important;
        border: 1px solid rgba(212, 165, 116, 0.3) !important;
    }

    pre {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-radius: 8px !important;
        padding: 1.25rem !important;
        border: 1px solid #d4a574 !important;
    }

    pre code {
        background-color: transparent !important;
        padding: 0 !important;
        border: none !important;
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 12px;
        height: 12px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(245, 240, 232, 0.5);
    }

    ::-webkit-scrollbar-thumb {
        background: #d4a574;
        border-radius: 6px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #c89350;
    }

    /* Empty state message */
    .empty-state {
        text-align: center;
        padding: 4rem 2rem;
        color: #8b7355;
    }

    .empty-state-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        opacity: 0.6;
    }

    .empty-state-text {
        font-size: 1.25rem;
        color: #5a4a35;
        font-weight: 600;
    }

    .empty-state-subtitle {
        font-size: 1rem;
        color: #8b7355;
        margin-top: 0.75rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "gpt-4o-mini"

if "selected_therapist" not in st.session_state:
    st.session_state.selected_therapist = None

if "system_message" not in st.session_state:
    st.session_state.system_message = ""

if "show_settings" not in st.session_state:
    st.session_state.show_settings = False

# Custom header
st.markdown("""
<div class="header-bar">
    <div class="header-title">🍞 The Bread Therapist Collective</div>
    <div class="header-subtitle">Professional Therapy Through the Lens of Bread | Choose Your Therapist & Their Approach</div>
</div>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Therapist selection screen (shown if no therapist selected)
if st.session_state.selected_therapist is None:
    st.markdown("### Choose your therapist to begin your session")
    
    # Create grid of therapist cards (2 columns)
    therapist_list = list(THERAPISTS.items())
    
    for i in range(0, len(therapist_list), 2):
        cols = st.columns(2)
        
        for col_idx, col in enumerate(cols):
            therapist_idx = i + col_idx
            if therapist_idx < len(therapist_list):
                key, therapist = therapist_list[therapist_idx]
                
                with col:
                    # Create clickable card using button
                    if st.button(
                        f"{therapist['emoji']}\n\n**{therapist['name']}**\n\n{therapist['therapy']}\n\n{therapist['description']}",
                        key=f"therapist_{key}",
                        use_container_width=True
                    ):
                        st.session_state.selected_therapist = key
                        st.session_state.system_message = therapist["system_message"]
                        st.session_state.messages = []  # Clear messages when changing therapist
                        st.rerun()

else:
    # Therapist is selected, show chat interface
    current_therapist = THERAPISTS[st.session_state.selected_therapist]
    
    # Show current therapist info
    st.markdown(f"### {current_therapist['emoji']} Session with {current_therapist['name']}")
    st.caption(f"**{current_therapist['therapy']}** — {current_therapist['personality']}")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f"**Model:** `{st.session_state.selected_model}` | **Messages:** {len(st.session_state.messages)}")
    
    with col2:
        if st.button("🔄 Change Therapist", use_container_width=True, key="change_therapist_btn"):
            st.session_state.selected_therapist = None
            st.session_state.messages = []
            st.rerun()
    
    with col3:
        if st.button("⚙️ Settings", use_container_width=True, key="settings_btn"):
            st.session_state.show_settings = not st.session_state.show_settings

    # Settings panel (shown when settings button is clicked)
    if st.session_state.show_settings:
        with st.expander("⚙️ Configuration", expanded=True):
            st.markdown("### Model Selection")
            st.session_state.selected_model = st.selectbox(
                "Choose AI Model",
                MODELS,
                index=MODELS.index(st.session_state.selected_model),
                key="model_select"
            )

            st.markdown("---")

            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("💾 Save Settings", use_container_width=True):
                    st.success("✅ Settings saved successfully!")

            with col_b:
                if st.button("❌ Close Settings", use_container_width=True):
                    st.session_state.show_settings = False
                    st.rerun()

    st.markdown("---")

    # Display chat messages or empty state
    if len(st.session_state.messages) == 0:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">🍞</div>
            <div class="empty-state-text">Ready to begin your session?</div>
            <div class="empty-state-subtitle">Share what's on your mind and receive guidance from {}</div>
        </div>
        """.format(current_therapist['name']), unsafe_allow_html=True)
    else:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

st.markdown('</div>', unsafe_allow_html=True)

# Chat input (only shown when therapist is selected)
if st.session_state.selected_therapist is not None:
    if prompt := st.chat_input(f"Share your thoughts with {THERAPISTS[st.session_state.selected_therapist]['name']}..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate AI response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            try:
                # Prepare messages with system message
                messages = [{"role": "system", "content": st.session_state.system_message}]
                messages.extend(st.session_state.messages)

                # Stream the response
                stream = client.chat.completions.create(
                    model=st.session_state.selected_model,
                    messages=messages,
                    stream=True,
                )

                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")

                message_placeholder.markdown(full_response)

            except Exception as e:
                error_message = f"❌ Error: {str(e)}"
                message_placeholder.markdown(error_message)
                full_response = error_message

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
