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
        border-radius: 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        margin-bottom: 0;
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

# Custom header
st.markdown("""
<div class="header-bar">
    <div class="header-title">🍞 Overconfident Toaster</div>
    <div class="header-subtitle">Life Advice as if Everything is Bread | Mapping Problems to Toast Settings Since 2025</div>
</div>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

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
    for message in st.session_state.messages:
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
