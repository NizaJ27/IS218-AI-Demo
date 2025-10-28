# Streamlit Chat Interface Guide

## Overview

This Streamlit application provides a ChatGPT-like interface for interacting with OpenAI's language models. It features model selection, configurable system messages, and a clean chat interface.

## Features

- **Multiple Model Support**: Choose from various OpenAI models (GPT-4, GPT-3.5-turbo, etc.)
- **System Message Configuration**: Customize the AI's behavior and personality
- **Chat History**: Full conversation history maintained during the session
- **Streaming Responses**: Real-time streaming of AI responses
- **Clean UI**: Modern, user-friendly interface

## Installation

The required dependencies are already included in `requirements.txt`. If you need to install them separately:

```bash
pip install streamlit openai python-dotenv
```

## Configuration

1. Ensure your `.env` file contains your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

2. The application will automatically load the API key from the `.env` file.

## Running the Application

To start the Streamlit chat interface:

```bash
streamlit run streamlit_app.py
```

The application will open in your default web browser, typically at `http://localhost:8501`.

## Using the Chat Interface

### Basic Usage

1. **Select a Model**: Use the dropdown in the sidebar to choose your preferred OpenAI model
2. **Type Your Message**: Enter your message in the chat input at the bottom
3. **View Responses**: AI responses will stream in real-time
4. **Continue Conversation**: The chat maintains full context of your conversation

### Configuring the System Message

1. Click the **"🔧 Configure System Message"** button in the sidebar
2. Edit the system message to control the AI's behavior
3. Click **"Apply Changes"** to save your settings

**Example System Messages:**
- `"You are a helpful assistant."` (default)
- `"You are a Python programming expert who provides clear, concise code examples."`
- `"You are a creative writing assistant who helps with storytelling."`
- `"You are a technical documentation writer who explains complex concepts simply."`

### Managing Your Chat

- **Clear Chat**: Click the "🗑️ Clear Chat" button to start a new conversation
- **Message Count**: View the number of messages in the current session in the sidebar

## Features Breakdown

### Model Selection

Choose from the following models:
- **gpt-4o**: Latest GPT-4 Optimized model (faster, more efficient)
- **gpt-4o-mini**: Smaller, faster version of GPT-4o
- **gpt-4-turbo**: Enhanced GPT-4 with improved performance
- **gpt-4**: Standard GPT-4 model
- **gpt-3.5-turbo**: Fast and cost-effective model

### System Message

The system message is sent with every request and influences how the AI responds. It's useful for:
- Setting the AI's personality or tone
- Defining expertise areas
- Establishing output format preferences
- Creating role-based assistants

### Session State

The application maintains the following in session state:
- Full conversation history
- Selected model
- System message configuration
- UI state (configuration panel visibility)

## Architecture

The application follows a simple, clean architecture:

```
streamlit_app.py
├── Configuration (Sidebar)
│   ├── Model Selection
│   ├── System Message Editor
│   └── Chat Controls
└── Chat Interface (Main)
    ├── Message History Display
    └── Chat Input
```

## Tips for Best Results

1. **Choose the Right Model**: Use GPT-4o-mini for faster responses, GPT-4 for more complex tasks
2. **Craft Good System Messages**: Be specific about the AI's role and expected behavior
3. **Clear Context When Needed**: Use the Clear Chat button to start fresh conversations
4. **Experiment**: Try different system messages to see how they affect responses

## Troubleshooting

### "Error: Invalid API Key"
- Check that your `.env` file contains the correct `OPENAI_API_KEY`
- Ensure the `.env` file is in the same directory as `streamlit_app.py`

### "Model not found"
- Ensure you have access to the selected model in your OpenAI account
- Try selecting a different model from the dropdown

### Application not loading
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Ensure you're running the command from the project directory

## Extending the Application

This basic interface can be extended with additional features:
- Save/load conversation history
- Export chats to file
- Add temperature and other parameter controls
- Implement conversation branching
- Add image generation capabilities
- Multi-user support with authentication
