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
