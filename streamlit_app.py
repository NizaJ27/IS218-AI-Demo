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
    layout="wide"
)

# Custom CSS for Discord-inspired theme
st.markdown("""
<style>
    /* Main background - Discord dark grey */
    .stApp {
        background-color: #36393f;
    }
    
    /* Sidebar styling - Discord darker grey */
    [data-testid="stSidebar"] {
        background-color: #2f3136;
    }
    
    /* Main content area */
    .main .block-container {
        background-color: #36393f;
        padding: 2rem 1rem;
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
        font-weight: 500 !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #4752c4 !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(88, 101, 242, 0.4) !important;
    }
    
    /* Chat messages - rounded */
    .stChatMessage {
        background-color: #40444b !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Chat input - rounded */
    .stChatInputContainer > div {
        background-color: #40444b !important;
        border-radius: 12px !important;
        border: 1px solid #202225 !important;
    }
    
    .stChatInput > div > div > input {
        background-color: #40444b !important;
        color: #dcddde !important;
        border-radius: 12px !important;
    }
    
    /* Divider */
    hr {
        border-color: #4f545c !important;
    }
    
    /* Success message */
    .stSuccess {
        background-color: #3ba55d !important;
        color: white !important;
        border-radius: 8px !important;
    }
    
    /* Labels */
    label {
        color: #b9bbbe !important;
        font-weight: 500 !important;
    }
    
    /* Sidebar title */
    [data-testid="stSidebar"] h1 {
        color: #ffffff !important;
    }
    
    /* Message content */
    .stMarkdown {
        color: #dcddde !important;
    }
    
    /* Code blocks */
    code {
        background-color: #2f3136 !important;
        color: #f26522 !important;
        padding: 2px 6px !important;
        border-radius: 4px !important;
    }
    
    pre {
        background-color: #2f3136 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #2f3136;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #202225;
        border-radius: 6px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #40444b;
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

if "show_config" not in st.session_state:
    st.session_state.show_config = False

# Sidebar for configuration
with st.sidebar:
    st.title("⚙️ Configuration")

    # Model selection
    st.session_state.selected_model = st.selectbox(
        "Select Model",
        MODELS,
        index=MODELS.index(st.session_state.selected_model)
    )

    st.divider()

    # Configure button
    if st.button("🔧 Configure System Message", use_container_width=True):
        st.session_state.show_config = not st.session_state.show_config

    # System message configuration
    if st.session_state.show_config:
        st.subheader("System Message")
        st.session_state.system_message = st.text_area(
            "Set the AI's behavior and personality:",
            value=st.session_state.system_message,
            height=150,
            help="The system message controls how the AI responds. For example: 'You are a helpful assistant that speaks like a pirate.'"
        )

        if st.button("Apply Changes", use_container_width=True):
            st.success("System message updated!")
            st.session_state.show_config = False
            st.rerun()

    st.divider()

    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    # Display info
    st.divider()
    st.caption(f"**Current Model:** {st.session_state.selected_model}")
    st.caption(f"**Messages:** {len(st.session_state.messages)}")

# Main chat interface
st.title("🤖 Discord Ops Copilot")
st.caption("Professional Discord Community Setup & Workflow Assistant")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

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
