# 🍞 The Bread Therapist Collective

> **Professional AI Therapy Through the Lens of Bread** — An innovative mental health support application featuring 8 specialized therapist personas, each representing a different therapeutic approach and named after a unique type of bread.

## 🌟 Features

### 🔐 Personalized Therapy Experience

- **User Authentication** - Secure login system with password hashing
- **Intake Assessment** - Smart 5-question questionnaire that recommends the best therapist for your needs
- **Session Logging** - Automatic session saves every 2 message exchanges
- **Progress Tracking** - Set therapy goals and track your journey over time
- **Session History** - Review past conversations and see your growth
- **User Dashboard** - Sidebar with your profile, progress metrics, and goals

### 8 Specialized Therapist Personas

Choose from evidence-based therapeutic approaches, each with a unique bread-themed personality:

- **🥖 Dr. Sourdough** - Cognitive Behavioral Therapy (CBT)
- **🥐 Dr. Brioche** - Psychodynamic Therapy
- **🍞 Dr. Whole Wheat** - Acceptance and Commitment Therapy (ACT)
- **🍞 Dr. Pumpernickel** - Dialectical Behavior Therapy (DBT)
- **🥖 Dr. Ciabatta** - Person-Centered Therapy
- **🫓 Dr. Focaccia** - Solution-Focused Brief Therapy
- **🍞 Dr. Rye** - Existential Therapy
- **🫓 Dr. Naan** - Mindfulness-Based Therapy

### Beautiful UI/UX
- Light, warm toast-inspired color scheme with radial gradient background
- Interactive therapist selection cards with hover effects
- Responsive chat interface with streaming responses
- Clean, modern design optimized for therapy sessions

### Smart Features
- OpenAI GPT-4 powered conversations with therapeutic expertise
- Model selection (GPT-4o, GPT-4o-mini, GPT-4-turbo, etc.)
- Session persistence with message history
- Easy therapist switching mid-session
- Personalized recommendations based on intake assessment

---

## 🚀 Quick Start

Run the Bread Therapist Collective from the **project root**:

```bash
# From enterprise_ai_demo1_websearch/ directory
make run

# Or directly
streamlit run therapy_app/streamlit_app.py
```

---

## 📋 Prerequisites

- Python 3.13+
- OpenAI API key
- Virtual environment (recommended)

---

## 🛠️ Setup

1. **Navigate to project root**
```bash
cd enterprise_ai_demo1_websearch
```

2. **Set up environment** (if not already done)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies** (from project root)
```bash
pip install -r requirements.txt
```

4. **Configure OpenAI API key** (from project root)
```bash
# Create .env file in project root
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

5. **Run the application**
```bash
make run
```

---

## 🧪 Testing

Run tests from the **project root**:

```bash
# Run all tests
make test

# Run with coverage
make coverage
```

---

## 🏗️ Architecture

### Directory Structure

```
therapy_app/
├── streamlit_app.py           # Main Streamlit web application
├── src/
│   ├── __init__.py
│   ├── user_manager.py        # User authentication & profile management
│   ├── therapy_intake.py      # Intake assessment & therapist matching
│   ├── models.py              # Data models (SearchRequest, SearchResult)
│   ├── client.py              # OpenAI API client
│   ├── parser.py              # Response parsing logic
│   ├── search_service.py      # Business logic layer
│   ├── main.py                # CLI entry point
│   └── logging_config.py      # Centralized logging
├── tests/                     # Comprehensive test suite
│   ├── test_*.py              # Test files
│   └── fixtures/              # Test data
├── user_data/                 # User profiles and session logs (gitignored)
│   ├── profiles/              # User profile JSON files
│   └── sessions/              # Session logs per user
├── logs/                      # Application logs
├── README.md                  # This file
└── PERSONALIZATION_SUMMARY.md # Detailed personalization system docs
```

### Key Components

**User Management (`user_manager.py`)**
- User registration and authentication
- Password hashing (SHA-256)
- Profile storage and updates
- Session logging and history
- Progress notes and goal tracking

**Therapy Intake (`therapy_intake.py`)**
- 5-question assessment (4 multiple-choice + 1 text)
- Weighted scoring algorithm
- Intelligent therapist recommendation
- Detailed explanation of recommendations

**Main Application (`streamlit_app.py`)**
- Three-screen flow: Authentication → Intake → Therapy
- 8 therapist personas with unique system messages
- Auto-save every 2 message exchanges
- Sidebar dashboard with user metrics
- Session management (save, logout, change therapist)

---

## 🎨 Therapist Personas

Each therapist combines professional therapeutic techniques with bread-themed wisdom:

### Dr. Sourdough (CBT)
- Focuses on identifying and challenging negative thought patterns
- Helps break down problems systematically
- Teaches practical coping strategies
- "Let's examine that thought pattern - it seems like it's over-proofed with catastrophizing."

### Dr. Brioche (Psychodynamic)
- Explores unconscious patterns and past experiences
- Examines how early relationships shape current behaviors
- Patient and deeply reflective approach
- "This pattern has many layers, like brioche. What might be hidden in the deeper folds?"

### Dr. Whole Wheat (ACT)
- Promotes acceptance of difficult emotions
- Helps clarify personal values
- Encourages committed action aligned with values
- "Fighting anxiety is like trying to remove the bran - it's part of the whole grain."

### Dr. Pumpernickel (DBT)
- Balances acceptance and change
- Teaches mindfulness, distress tolerance, emotion regulation
- Validates emotions while building skills
- "Both things can be true - you're doing your best AND you can learn new skills."

### Dr. Ciabatta (Person-Centered)
- Provides unconditional positive regard
- Trusts in your inherent capacity for growth
- Non-directive, empathetic listening
- "You have all the ingredients within you already."

### Dr. Focaccia (Solution-Focused)
- Focuses on solutions rather than problems
- Uses future-oriented questions
- Identifies existing strengths and resources
- "What would be the first small thing you'd notice if this problem vanished?"

### Dr. Rye (Existential)
- Explores meaning, freedom, and authenticity
- Helps confront existential concerns
- Philosophical and courage-focused
- "You're grappling with the weight of freedom - you can become any kind of bread you choose."

### Dr. Naan (Mindfulness-Based)
- Cultivates present-moment awareness
- Non-judgmental observation of thoughts
- Develops self-compassion
- "Notice your thoughts bubbling up - observe them, but you don't have to grab each one."

---

## 🔐 Personalization System

### User Flow

1. **First Visit**
   - Create account with username/password
   - Complete 5-question intake assessment
   - Receive therapist recommendation with detailed explanation
   - Begin therapy session

2. **Returning Visit**
   - Login with credentials
   - See assigned therapist and progress dashboard
   - Continue therapy where you left off
   - View session history and goals

3. **During Session**
   - Chat with your assigned therapist
   - Sessions auto-save every 2 message exchanges
   - Manually save anytime with "Save Session" button
   - Add therapy goals in sidebar
   - Change therapist if needed

4. **Logout**
   - Sessions automatically saved on logout
   - All progress preserved for next visit

### Recommendation Algorithm

The intake assessment uses weighted scoring to match you with the best therapist:

**Questions:**
1. Primary concern (anxiety, depression, relationships, etc.)
2. Therapy preference (practical tools, past exploration, acceptance, etc.)
3. Emotional style (overwhelming, stuck in thoughts, disconnected, etc.)
4. Timeline (short-term, medium, long-term, flexible)
5. Therapy goals (text input)

Each answer awards points to different therapists based on their therapeutic approach. The therapist with the highest score is recommended, along with explanations for the top 3 matches.

**Example:**
- "I want practical tools" → +3 points to Dr. Sourdough (CBT), +2 to Dr. Focaccia (Solution-Focused)
- "I feel stuck in repetitive thoughts" → +3 to Dr. Sourdough (CBT), +2 to Dr. Naan (Mindfulness)

### Data Storage

**User Profiles** (`user_data/profiles/[username].json`)
```json
{
  "username": "joshua",
  "password_hash": "sha256...",
  "created_at": "2025-10-31T14:30:00",
  "last_login": "2025-10-31T15:45:00",
  "assigned_therapist": "sourdough",
  "intake_responses": {...},
  "therapy_goals": ["Reduce anxiety", "Improve sleep"],
  "progress_notes": [...],
  "total_sessions": 5
}
```

**Session Logs** (`user_data/sessions/[username]/session_[timestamp].json`)
```json
{
  "session_id": "session_20251031_154500",
  "username": "joshua",
  "therapist": "sourdough",
  "start_time": "2025-10-31T15:45:00",
  "messages": [
    {"role": "user", "content": "I've been feeling anxious..."},
    {"role": "assistant", "content": "I hear you..."}
  ]
}
```

---

## 💻 Technology Stack

- **Frontend**: Streamlit (interactive web interface)
- **AI Engine**: OpenAI GPT-4 (GPT-4o, GPT-4o-mini, GPT-4-turbo)
- **Backend**: Python 3.13+
- **Authentication**: SHA-256 password hashing
- **Data Storage**: JSON files (user profiles & session logs)
- **Testing**: pytest with comprehensive coverage
- **Styling**: Custom CSS with toast-inspired color palette
- **Development**: TDD methodology, clean architecture

---

## 📖 Documentation

- **[PERSONALIZATION_SUMMARY.md](PERSONALIZATION_SUMMARY.md)** - Detailed documentation of the personalization system, algorithms, and data formats

---

## 🔒 Security Notes

- Passwords are hashed using SHA-256 (consider bcrypt for production)
- User data stored locally in `user_data/` (gitignored for privacy)
- No sensitive data transmitted except to OpenAI API (encrypted)
- Session state managed securely with Streamlit

---

## 🎯 Future Enhancements

- Progress visualization with charts
- Therapist notes system
- Goal completion tracking
- Session rating and feedback
- Export therapy data
- Multi-therapist session history
- OAuth authentication
- Database migration (PostgreSQL/MongoDB)
- Admin dashboard
- Email notifications

---

<div align="center">

*The Bread Therapist Collective - Where Professional Therapy Meets Artisan Bread*

**Ready to begin your therapeutic journey? Choose your therapist and start healing! 🍞**

</div>
