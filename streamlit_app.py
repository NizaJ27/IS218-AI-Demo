"""
Discord Ops Copilot - Streamlit Chat Interface

A professional Discord community setup and workflow assistant that helps design
server layouts, roles, automation, onboarding flows, event schedules, and moderation policies.
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
    page_title="Discord Ops Copilot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Discord-inspired theme with professional layout
st.markdown("""
<style>
    /* Hide default sidebar toggle and make app full width */
    [data-testid="collapsedControl"] {
        display: none;
    }

    /* Main background - Discord dark grey */
    .stApp {
        background-color: #36393f;
    }

    /* Remove default padding for full-width design */
    .main .block-container {
        max-width: 100%;
        padding: 0;
        background-color: #36393f;
    }

    /* Custom header bar */
    .header-bar {
        background: linear-gradient(90deg, #5865f2 0%, #4752c4 100%);
        padding: 1rem 2rem;
        border-radius: 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        margin-bottom: 0;
    }

    .header-title {
        color: white;
        font-size: 1.75rem;
        font-weight: 700;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .header-subtitle {
        color: rgba(255, 255, 255, 0.8);
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

    /* Headers - Discord blurple */
    h1, h2, h3 {
        color: #5865f2 !important;
        font-weight: 700 !important;
    }

    /* Subheaders and captions */
    .stCaption, p {
        color: #b9bbbe !important;
    }

    /* Text inputs and text areas - rounded */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #40444b !important;
        color: #dcddde !important;
        border-radius: 8px !important;
        border: 1px solid #202225 !important;
        font-size: 0.95rem !important;
    }

    .stTextArea > div > div > textarea {
        min-height: 120px !important;
    }

    /* Selectbox - rounded */
    .stSelectbox > div > div {
        background-color: #40444b !important;
        border-radius: 8px !important;
        border: 1px solid #202225 !important;
    }

    .stSelectbox > div > div > div {
        color: #dcddde !important;
    }

    /* Buttons - Discord blurple with rounded corners */
    .stButton > button {
        background-color: #5865f2 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 0.625rem 1.25rem !important;
        transition: all 0.2s ease !important;
        font-size: 0.95rem !important;
    }

    .stButton > button:hover {
        background-color: #4752c4 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(88, 101, 242, 0.5) !important;
    }

    /* Chat messages - rounded and polished */
    .stChatMessage {
        background-color: #40444b !important;
        border-radius: 16px !important;
        padding: 1.25rem !important;
        margin-bottom: 1rem !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
    }

    /* User messages - slightly different color */
    [data-testid="stChatMessageContent"] {
        padding: 0 !important;
    }

    /* Chat input - rounded and integrated */
    .stChatInputContainer {
        padding: 1.5rem 2rem !important;
        background-color: #2f3136 !important;
        border-top: 2px solid #202225 !important;
    }

    .stChatInputContainer > div {
        background-color: #40444b !important;
        border-radius: 24px !important;
        border: 2px solid #202225 !important;
        max-width: 1200px !important;
        margin: 0 auto !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
    }

    .stChatInput > div > div > input {
        background-color: transparent !important;
        color: #dcddde !important;
        border-radius: 24px !important;
        font-size: 1rem !important;
        padding: 1rem 1.5rem !important;
    }

    /* Expander for settings */
    .streamlit-expanderHeader {
        background-color: #40444b !important;
        border-radius: 8px !important;
        color: #dcddde !important;
        font-weight: 600 !important;
        padding: 1rem !important;
        border: 1px solid #202225 !important;
    }

    .streamlit-expanderHeader:hover {
        background-color: #4f545c !important;
    }

    .streamlit-expanderContent {
        background-color: #2f3136 !important;
        border-radius: 0 0 8px 8px !important;
        border: 1px solid #202225 !important;
        border-top: none !important;
        padding: 1.5rem !important;
    }

    /* Divider */
    hr {
        border-color: #4f545c !important;
        margin: 1rem 0 !important;
    }

    /* Success/Info messages */
    .stSuccess {
        background-color: #3ba55d !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }

    .stInfo {
        background-color: #5865f2 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }

    /* Labels */
    label {
        color: #b9bbbe !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }

    /* Message content */
    .stMarkdown {
        color: #dcddde !important;
        line-height: 1.6 !important;
    }

    /* Code blocks */
    code {
        background-color: #2f3136 !important;
        color: #f26522 !important;
        padding: 3px 8px !important;
        border-radius: 4px !important;
        font-size: 0.9rem !important;
    }

    pre {
        background-color: #2f3136 !important;
        border-radius: 8px !important;
        padding: 1.25rem !important;
        border: 1px solid #202225 !important;
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
        background: #2f3136;
    }

    ::-webkit-scrollbar-thumb {
        background: #202225;
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #40444b;
    }

    /* Settings badge */
    .settings-badge {
        display: inline-block;
        background-color: #5865f2;
        color: white;
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
        color: #72767d;
    }

    .empty-state-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        opacity: 0.5;
    }

    .empty-state-text {
        font-size: 1.125rem;
        color: #b9bbbe;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "gpt-4o-mini"

if "system_message" not in st.session_state:
    st.session_state.system_message = """You are a professional Discord Ops Copilot — an expert community setup and workflow assistant specializing in Discord server architecture and management.

Your expertise includes:
- Designing comprehensive server layouts with optimal channel organization
- Creating role hierarchies and permission structures
- Developing automation workflows using Discord bots and integrations
- Crafting effective onboarding flows for new members
- Planning engaging event schedules and community activities
- Drafting moderation policies and community guidelines
- Recommending best practices for community growth and engagement
- Implementing security measures and anti-spam strategies

Provide detailed, actionable advice with specific examples. When designing server elements, present them in a clear, structured format that can be easily implemented. Consider community size, purpose, and culture in your recommendations."""

if "show_settings" not in st.session_state:
    st.session_state.show_settings = False

# Custom header
st.markdown("""
<div class="header-bar">
    <div class="header-title">🤖 Discord Ops Copilot</div>
    <div class="header-subtitle">Professional Discord Community Setup & Workflow Assistant</div>
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
        <div class="empty-state-icon">💬</div>
        <div class="empty-state-text">Start a conversation with your Discord Ops Copilot</div>
        <div style="margin-top: 1rem; color: #72767d; font-size: 0.9rem;">
            Ask about server setup, roles, moderation, automation, and more!
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

st.markdown('</div>', unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Type your message here..."):
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
