#!/bin/bash
# Run the Bread Therapist Collective Streamlit Application

echo "🍞 Starting The Bread Therapist Collective..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found!"
    echo "Please create a .env file with your OPENAI_API_KEY"
    exit 1
fi

# Check if OpenAI API key is set
if ! grep -q "OPENAI_API_KEY" .env; then
    echo "❌ Error: OPENAI_API_KEY not found in .env file!"
    echo "Please add your OpenAI API key to the .env file"
    exit 1
fi

echo "✅ Configuration validated"
echo ""
echo "🚀 Launching application..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Run streamlit
streamlit run therapy_app/streamlit_app.py
