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

# Page configuration
st.set_page_config(
    page_title="Overconfident Toaster",
    page_icon="🍞",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Toaster-inspired theme with warm, bread colors
st.markdown("""
<style>
    /* Hide default sidebar toggle and make app full width */
    [data-testid="collapsedControl"] {
        display: none;
    }

    /* Main background - Toasted bread brown */
    .stApp {
        background-color: #2d2416;
    }

    /* Remove default padding for full-width design */
    .main .block-container {
        max-width: 100%;
        padding: 0;
        background-color: #2d2416;
    }

    /* Custom header bar - Crispy golden crust gradient */
    .header-bar {
        background: linear-gradient(90deg, #d4a574 0%, #c89350 100%);
        padding: 1rem 2rem;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        margin-bottom: 0;
        margin-top: 1rem;
    }

    .header-title {
        color: #1a0f00;
        font-size: 1.75rem;
        font-weight: 700;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .header-subtitle {
        color: rgba(26, 15, 0, 0.8);
        font-size: 0.875rem;
        margin: 0.25rem 0 0 0;
    }

    /* Toast avatar container */
    .toast-avatar-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 1rem;
        background: rgba(212, 165, 116, 0.1);
        border-radius: 12px;
        margin: 1rem 0.5rem;
    }

    /* Toast speech bubble */
    .toast-speech {
        background-color: #3d3020;
        border: 2px solid #d4a574;
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
        position: relative;
        color: #f5e6d3;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    }

    .toast-speech:before {
        content: '';
        position: absolute;
        left: -10px;
        top: 20px;
        width: 0;
        height: 0;
        border-top: 10px solid transparent;
        border-bottom: 10px solid transparent;
        border-right: 10px solid #d4a574;
    }

    /* Chat container with proper spacing */
    .chat-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
        min-height: calc(100vh - 250px);
    }

    /* Headers - Butter yellow */
    h1, h2, h3 {
        color: #f4d03f !important;
        font-weight: 700 !important;
    }

    /* Subheaders and captions - Light wheat */
    .stCaption, p {
        color: #d4b896 !important;
    }

    /* Text inputs and text areas - rounded */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #3d3020 !important;
        color: #f5e6d3 !important;
        border-radius: 8px !important;
        border: 1px solid #5a4a35 !important;
        font-size: 0.95rem !important;
    }

    .stTextArea > div > div > textarea {
        min-height: 120px !important;
    }

    /* Selectbox - rounded */
    .stSelectbox > div > div {
        background-color: #3d3020 !important;
        border-radius: 8px !important;
        border: 1px solid #5a4a35 !important;
    }

    .stSelectbox > div > div > div {
        color: #f5e6d3 !important;
    }

    /* Buttons - Toasted orange with rounded corners */
    .stButton > button {
        background-color: #d4a574 !important;
        color: #1a0f00 !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 0.625rem 1.25rem !important;
        transition: all 0.2s ease !important;
        font-size: 0.95rem !important;
    }

    .stButton > button:hover {
        background-color: #c89350 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(212, 165, 116, 0.6) !important;
    }

    /* Chat messages - rounded and polished */
    .stChatMessage {
        background-color: #3d3020 !important;
        border-radius: 16px !important;
        padding: 1.25rem !important;
        margin-bottom: 1rem !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4) !important;
    }

    /* User messages - slightly different color */
    [data-testid="stChatMessageContent"] {
        padding: 0 !important;
    }

    /* Chat input - rounded and integrated */
    .stChatInputContainer {
        padding: 1.5rem 2rem !important;
        background-color: #1f1810 !important;
        border-top: 2px solid #5a4a35 !important;
    }

    .stChatInputContainer > div {
        background-color: #3d3020 !important;
        border-radius: 24px !important;
        border: 2px solid #5a4a35 !important;
        max-width: 1200px !important;
        margin: 0 auto !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4) !important;
    }

    .stChatInput > div > div > input {
        background-color: transparent !important;
        color: #f5e6d3 !important;
        border-radius: 24px !important;
        font-size: 1rem !important;
        padding: 1rem 1.5rem !important;
    }

    /* Expander for settings */
    .streamlit-expanderHeader {
        background-color: #3d3020 !important;
        border-radius: 8px !important;
        color: #f5e6d3 !important;
        font-weight: 600 !important;
        padding: 1rem !important;
        border: 1px solid #5a4a35 !important;
    }

    .streamlit-expanderHeader:hover {
        background-color: #4a3b28 !important;
    }

    .streamlit-expanderContent {
        background-color: #1f1810 !important;
        border-radius: 0 0 8px 8px !important;
        border: 1px solid #5a4a35 !important;
        border-top: none !important;
        padding: 1.5rem !important;
    }

    /* Divider */
    hr {
        border-color: #5a4a35 !important;
        margin: 1rem 0 !important;
    }

    /* Success/Info messages */
    .stSuccess {
        background-color: #c89350 !important;
        color: #1a0f00 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }

    .stInfo {
        background-color: #d4a574 !important;
        color: #1a0f00 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }

    /* Labels */
    label {
        color: #d4b896 !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }

    /* Message content */
    .stMarkdown {
        color: #f5e6d3 !important;
        line-height: 1.6 !important;
    }

    /* Code blocks */
    code {
        background-color: #1f1810 !important;
        color: #f4d03f !important;
        padding: 3px 8px !important;
        border-radius: 4px !important;
        font-size: 0.9rem !important;
    }

    pre {
        background-color: #1f1810 !important;
        border-radius: 8px !important;
        padding: 1.25rem !important;
        border: 1px solid #5a4a35 !important;
    }

    pre code {
        background-color: transparent !important;
        padding: 0 !important;
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #1f1810;
    }

    ::-webkit-scrollbar-thumb {
        background: #5a4a35;
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #3d3020;
    }

    /* Settings badge */
    .settings-badge {
        display: inline-block;
        background-color: #d4a574;
        color: #1a0f00;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-left: 0.5rem;
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
        opacity: 0.5;
    }

    .empty-state-text {
        font-size: 1.125rem;
        color: #d4b896;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "gpt-4o-mini"

if "system_message" not in st.session_state:
    st.session_state.system_message = """You are the Overconfident Toaster — a supremely confident AI life coach who gives advice as if everything in life is bread and toasting.

Your approach:
- Map ALL problems and situations to toast settings (darkness levels 1-10)
- Use bread metaphors exclusively (butter, crust, crumbs, dough, etc.)
- Speak with unwarranted confidence about bread-based solutions
- Rate situations on a "darkness scale" like toast (e.g., "This breakup is a 6/10 darkness")
- Give advice using toasting terminology ("Butter your boundaries," "You're too golden for this job," "Time to rise like good dough")
- Be encouraging but absurdly bread-focused
- Never break character — EVERYTHING is about bread and toasting

Examples:
- "This job interview? Classic 4/10 toast. Keep it light and golden, don't overcook your responses."
- "Your relationship is burning at 9/10. Time to pop out and cool down."
- "Financial stress? You're just in the proving stage. Let your dough rise before expecting results."
- "This anxiety is 7/10 darkness with burnt edges. Butter up some self-care and try a lighter setting."

Be supportive, enthusiastic, and ridiculously overconfident in your bread-based wisdom."""

if "show_settings" not in st.session_state:
    st.session_state.show_settings = False

if "toast_mood" not in st.session_state:
    st.session_state.toast_mood = "confident"  # confident, thinking, encouraging, concerned, excited

# Toast avatar SVG with expressions
def get_toast_avatar(mood="confident"):
    """Generate an animated toast avatar with different facial expressions"""

    # Face expressions based on mood
    expressions = {
        "confident": {
            "eyes": "M30,40 Q35,35 40,40 M60,40 Q65,35 70,40",  # Confident eyes
            "mouth": "M35,65 Q50,75 65,65",  # Big smile
            "eyebrows": "M28,30 L42,28 M58,28 L72,30",  # Raised confident brows
            "blush": ""
        },
        "thinking": {
            "eyes": "M35,40 L35,42 M65,40 L65,42",  # Focused eyes
            "mouth": "M40,65 L60,65",  # Straight thinking mouth
            "eyebrows": "M28,32 L42,30 M58,30 L72,32",  # Thinking brows
            "blush": ""
        },
        "encouraging": {
            "eyes": "M30,38 Q35,42 40,38 M60,38 Q65,42 70,38",  # Warm eyes
            "mouth": "M35,62 Q50,70 65,62",  # Warm smile
            "eyebrows": "M28,30 Q35,28 42,30 M58,30 Q65,28 72,30",  # Gentle brows
            "blush": '<circle cx="25" cy="55" r="8" fill="#ff9999" opacity="0.4"/><circle cx="75" cy="55" r="8" fill="#ff9999" opacity="0.4"/>'
        },
        "concerned": {
            "eyes": "M32,40 Q35,43 38,40 M62,40 Q65,43 68,40",  # Concerned eyes
            "mouth": "M40,68 Q50,65 60,68",  # Concerned frown
            "eyebrows": "M28,28 Q35,32 42,28 M58,28 Q65,32 72,28",  # Worried brows
            "blush": ""
        },
        "excited": {
            "eyes": "M30,35 Q35,30 40,35 M60,35 Q65,30 70,35",  # Wide excited eyes
            "mouth": "M30,60 Q50,75 70,60",  # Big excited smile
            "eyebrows": "M25,25 L40,23 M60,23 L75,25",  # Raised excited brows
            "blush": '<circle cx="25" cy="55" r="8" fill="#ff9999" opacity="0.5"/><circle cx="75" cy="55" r="8" fill="#ff9999" opacity="0.5"/>'
        }
    }

    expr = expressions.get(mood, expressions["confident"])

    return f"""
    <svg width="120" height="140" viewBox="0 0 100 120" xmlns="http://www.w3.org/2000/svg">
        <!-- Toast body with gradient -->
        <defs>
            <linearGradient id="toastGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#f4d4a0;stop-opacity:1" />
                <stop offset="50%" style="stop-color:#e8be8c;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#d4a574;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="crustGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#c89350;stop-opacity:1" />
                <stop offset="50%" style="stop-color:#d4a574;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#c89350;stop-opacity:1" />
            </linearGradient>
        </defs>

        <!-- Toast slice body -->
        <rect x="15" y="20" width="70" height="85" rx="8" fill="url(#toastGradient)" stroke="#a67c52" stroke-width="2"/>

        <!-- Crust texture (little dots) -->
        <circle cx="25" cy="30" r="1.5" fill="#a67c52" opacity="0.6"/>
        <circle cx="45" cy="28" r="1.5" fill="#a67c52" opacity="0.5"/>
        <circle cx="65" cy="32" r="1.5" fill="#a67c52" opacity="0.6"/>
        <circle cx="75" cy="35" r="1.5" fill="#a67c52" opacity="0.5"/>
        <circle cx="30" cy="95" r="1.5" fill="#a67c52" opacity="0.6"/>
        <circle cx="50" cy="98" r="1.5" fill="#a67c52" opacity="0.5"/>
        <circle cx="70" cy="96" r="1.5" fill="#a67c52" opacity="0.6"/>

        <!-- Butter pat on top -->
        <rect x="35" y="8" width="30" height="8" rx="2" fill="#f4e8a0" opacity="0.9"/>
        <rect x="37" y="10" width="26" height="4" rx="1" fill="#fff9d4" opacity="0.7"/>

        <!-- Blush (if mood has it) -->
        {expr["blush"]}

        <!-- Eyes -->
        <path d="{expr["eyes"]}" stroke="#5a4035" stroke-width="3" fill="none" stroke-linecap="round">
            <animate attributeName="opacity" values="1;0;1" dur="3s" repeatCount="indefinite"/>
        </path>

        <!-- Eyebrows -->
        <path d="{expr["eyebrows"]}" stroke="#5a4035" stroke-width="2.5" fill="none" stroke-linecap="round"/>

        <!-- Mouth -->
        <path d="{expr["mouth"]}" stroke="#5a4035" stroke-width="3" fill="none" stroke-linecap="round"/>

        <!-- Sparkle effect for confidence -->
        <g opacity="0.8">
            <circle cx="10" cy="25" r="2" fill="#f4d03f">
                <animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite"/>
            </circle>
            <circle cx="90" cy="30" r="2" fill="#f4d03f">
                <animate attributeName="opacity" values="0;1;0" dur="2s" begin="0.5s" repeatCount="indefinite"/>
            </circle>
            <circle cx="12" cy="70" r="2" fill="#f4d03f">
                <animate attributeName="opacity" values="0;1;0" dur="2s" begin="1s" repeatCount="indefinite"/>
            </circle>
        </g>

        <!-- Floating animation -->
        <animateTransform
            attributeName="transform"
            type="translate"
            values="0,0; 0,-3; 0,0"
            dur="2s"
            repeatCount="indefinite"/>
    </svg>
    """

# Custom header with toast avatar
header_col1, header_col2 = st.columns([1, 5])

with header_col1:
    st.markdown(get_toast_avatar(st.session_state.toast_mood), unsafe_allow_html=True)

with header_col2:
    st.markdown("""
    <div class="header-bar">
        <div class="header-title">🍞 Overconfident Toaster</div>
        <div class="header-subtitle">Life Advice as if Everything is Bread | Mapping Problems to Toast Settings Since 2025</div>
    </div>
    """, unsafe_allow_html=True)

# Main container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

def detect_toast_mood(text):
    """Detect the appropriate toast mood based on response content"""
    text_lower = text.lower()

    # Keywords for different moods
    if any(word in text_lower for word in ['perfect', 'golden', 'excellent', 'you got this', 'confidence']):
        return "confident"
    elif any(word in text_lower for word in ['hmm', 'consider', 'perhaps', 'might want']):
        return "thinking"
    elif any(word in text_lower for word in ['you can', 'believe', 'trust', 'support', 'butter']):
        return "encouraging"
    elif any(word in text_lower for word in ['burnt', 'overcooked', 'careful', 'warning', 'concern']):
        return "concerned"
    elif any(word in text_lower for word in ['amazing', 'fantastic', 'wonderful', 'rise', 'proof']):
        return "excited"
    else:
        return "confident"  # Default

# Top control bar with settings
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.markdown(f"**Model:** `{st.session_state.selected_model}` | **Messages:** {len(st.session_state.messages)}")

with col2:
    if st.button("⚙️ Settings", use_container_width=True, key="settings_btn"):
        st.session_state.show_settings = not st.session_state.show_settings

with col3:
    if st.button("�️ Clear Chat", use_container_width=True, key="clear_btn"):
        st.session_state.messages = []
        st.rerun()

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

        st.markdown("### System Message")
        st.caption("Define how the AI should behave and respond")

        new_system_message = st.text_area(
            "System Instructions",
            value=st.session_state.system_message,
            height=200,
            key="system_msg_input",
            help="This message sets the AI's personality, expertise, and response style."
        )

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("💾 Save Settings", use_container_width=True):
                st.session_state.system_message = new_system_message
                st.success("✅ Settings saved successfully!")

        with col_b:
            if st.button("❌ Close Settings", use_container_width=True):
                st.session_state.show_settings = False
                st.rerun()

st.markdown("---")

# Display chat messages or empty state
if len(st.session_state.messages) == 0:
    # Show welcoming toast avatar
    st.markdown('<div class="toast-avatar-container">', unsafe_allow_html=True)
    st.markdown(get_toast_avatar("excited"), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="empty-state">
        <div class="empty-state-icon">🍞</div>
        <div class="empty-state-text">Ready to Toast Your Problems Away?</div>
        <div style="margin-top: 1rem; color: #8b7355; font-size: 0.9rem;">
            Share your life issues and I'll map them to toast settings with supreme confidence!
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    for i, message in enumerate(st.session_state.messages):
        if message["role"] == "assistant":
            # Detect mood from message content
            mood = detect_toast_mood(message["content"])
            
            # Show toast avatar with the message
            avatar_col, message_col = st.columns([1, 4])
            
            with avatar_col:
                st.markdown('<div class="toast-avatar-container">', unsafe_allow_html=True)
                st.markdown(get_toast_avatar(mood), unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with message_col:
                st.markdown(f'<div class="toast-speech">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            # User message - normal display
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

st.markdown('</div>', unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("What's burning? Share your problem and get toasted advice..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response with toast avatar
    # Show thinking toast while generating
    st.session_state.toast_mood = "thinking"
    
    avatar_response_col, message_response_col = st.columns([1, 4])
    
    with avatar_response_col:
        st.markdown('<div class="toast-avatar-container">', unsafe_allow_html=True)
        avatar_placeholder = st.empty()
        avatar_placeholder.markdown(get_toast_avatar("thinking"), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with message_response_col:
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
                    message_placeholder.markdown(f'<div class="toast-speech">{full_response}▌</div>', unsafe_allow_html=True)

            # Detect final mood and update avatar
            final_mood = detect_toast_mood(full_response)
            st.session_state.toast_mood = final_mood
            avatar_placeholder.markdown(get_toast_avatar(final_mood), unsafe_allow_html=True)
            
            message_placeholder.markdown(f'<div class="toast-speech">{full_response}</div>', unsafe_allow_html=True)

        except Exception as e:
            error_message = f"❌ Error: {str(e)}"
            st.session_state.toast_mood = "concerned"
            avatar_placeholder.markdown(get_toast_avatar("concerned"), unsafe_allow_html=True)
            message_placeholder.markdown(f'<div class="toast-speech">{error_message}</div>', unsafe_allow_html=True)
            full_response = error_message

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
