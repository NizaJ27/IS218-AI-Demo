# 🍞 The Bread Therapist Collective

> **Professional AI Therapy Through the Lens of Bread** — An innovative mental health support application featuring 8 specialized therapist personas, each representing a different therapeutic approach and named after a unique type of bread.

## 🌟 Features

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

---

## 🚀 Quick Start

Run the Bread Therapist Collective web interface:

```bash
# Easy way - using Make
make run

# Or directly with the script
./run.sh

# Or manually
streamlit run streamlit_app.py
```

**Available Commands:**
```bash
make help      # Show all available commands
make run       # Run the Streamlit application
make test      # Run all tests
make coverage  # Run tests with coverage report
make install   # Install dependencies
make clean     # Clean up generated files
make dev       # Run in development mode with auto-reload
```

---

## � Prerequisites

- Python 3.13+
- OpenAI API key
- Virtual environment (recommended)

---

## 🛠️ Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd enterprise_ai_demo1_websearch
```

2. **Set up environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
make install
# or
pip install -r requirements.txt
```

4. **Configure OpenAI API key**
```bash
# Create .env file
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

5. **Run the application**
```bash
make run
```

---

## 🧪 Testing

This project follows **Test-Driven Development** practices with 100% code coverage:

```bash
# Run all tests
make test

# Run with coverage report
make coverage

# Open HTML coverage report
open htmlcov/index.html
```

**Test Statistics:**
- ✅ 69 tests passing
- 📊 100% code coverage
- 🎯 TDD methodology

---

## 🏗️ Architecture

### Clean Layered Design

```
src/
├── models.py          # Data models (SearchRequest, SearchResult)
├── client.py          # OpenAI API client
├── parser.py          # Response parsing logic
├── search_service.py  # Business logic layer
├── main.py           # Application entry point
└── logging_config.py  # Centralized logging

streamlit_app.py      # Web interface with therapist personas
tests/                # Comprehensive test suite
```

### Key Design Principles
- **Separation of Concerns**: Each module has a single responsibility
- **Dependency Injection**: Testable, flexible components
- **Type Safety**: Pydantic models with validation
- **Error Handling**: Graceful degradation with informative messages
- **Logging**: Structured logging for debugging and monitoring

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

## 📚 What You'll Learn

This codebase demonstrates professional software development practices:

**Test-Driven Development** • **Clean Architecture** • **Enterprise Logging** • **Professional Git** • **CI/CD**

**The Twist:** This codebase is designed as a **living textbook**. Every file teaches you concepts through narrative comments and real examples.

````

---

## 🎯 Three Ways to Start

<table>
<tr>
<td width="33%" align="center">
<h3>🏃‍♂️ Just Get It Running</h3>
<p><strong>5-minute setup</strong></p>
<a href="docs/GETTING_STARTED.md">Quick Start Guide →</a>
<br><br>
<em>Setup, run tests, see it work</em>
</td>
<td width="33%" align="center">
<h3>📚 Teach Me Properly</h3>
<p><strong>Full learning path</strong></p>
<a href="docs/LEARNING_PATH.md">Learning Path Map →</a>
<br><br>
<em>Follow the guided journey</em>
</td>
<td width="33%" align="center">
<h3>🎯 I Know What I'm Doing</h3>
<p><strong>Jump to the code</strong></p>
<a href="src/">Browse Source →</a>
<br><br>
<em>See patterns, apply them</em>
</td>
</tr>
</table>

---

## 📖 Your Learning Resources

---

## 💻 Technology Stack

- **Frontend**: Streamlit (interactive web interface)
- **AI Engine**: OpenAI GPT-4 (GPT-4o, GPT-4o-mini, GPT-4-turbo)
- **Backend**: Python 3.13+
- **Testing**: pytest with 100% coverage
- **Styling**: Custom CSS with toast-inspired color palette
- **Development**: TDD methodology, clean architecture

---

## 📖 Documentation

### 🎓 Course Materials
- **[Learning Path Map](docs/LEARNING_PATH.md)** - Master roadmap
- **[Getting Started](docs/GETTING_STARTED.md)** - Setup and first steps
- **[Course Structure](docs/COURSE_STRUCTURE.md)** - 2-week session plan
- **[Code as Textbook](docs/CODE_AS_TEXTBOOK.md)** - How to read this code
- **[Student Guide](docs/STUDENT_GUIDE.md)** - Day-by-day checklist
- **[Grading Rubric](docs/GRADING.md)** - What you'll be evaluated on

### 🛠️ Development Guides
- **[TDD Workflow](docs/TDD_WORKFLOW.md)** - Write tests first (15 min read)
- **[AI Collaboration](docs/AI_COLLABORATION.md)** - Work with Claude (10 min read)
- **[Git Workflow](docs/GIT_WORKFLOW.md)** - Professional commits (10 min read)
- **[Logging Guide](docs/LOGGING.md)** - Enterprise logging (5 min read)
- **[Labs (Guided Practice)](docs/LEARNING_PATH.md#2-narrative-reading-days-12)** - Hands-on exercises per chapter

### 💡 Project Resources
- **[Project Launch Kit](docs/PROJECT_LAUNCH_KIT.md)** - Scope and planning template
- **[Project Ideas](docs/PROJECT_IDEAS.md)** - 60+ ideas with difficulty ratings
- **[OpenAI APIs](docs/openai_tools_research_oct2025.md)** - Complete API reference (1,300 lines)
- **[Demo Playbook](docs/DEMO_PLAYBOOK.md)** - Prepare your final presentation

### 📚 Reference Library
- **[Architecture Overview](docs/architecture.md)** - System diagrams and design decisions
- **[OpenAI Web Search Notes](docs/web_search_openai.md)** - Tool behavior, payloads, and examples

---

## 🏗️ What This Repository Demonstrates

**A production-quality AI web search application** that shows you:

```
📂 Architecture                      What You'll Learn
├── src/models.py                   → Dataclasses, type hints, exceptions
├── src/client.py                   → API clients, error handling, secrets
├── src/parser.py                   → Data transformation, defensive parsing
├── src/search_service.py           → Service layer, validation, orchestration
├── src/main.py                     → CLI design, user experience
└── src/logging_config.py           → Enterprise logging, rotation

📂 Tests (69 tests, 100% coverage)   How You'll Prove It Works
├── tests/test_models.py            → Unit testing patterns
├── tests/test_client.py            → Mocking external APIs
├── tests/test_parser.py            → Data validation testing
├── tests/test_search_service.py    → Integration testing
└── tests/test_main.py              → System testing
```

**Key Feature:** Each source file pairs with a test file. This is Test-Driven Development.

---

## 🎯 Your Mission (Choose One API or Combination)

**Available Tools:**
- Chat Completion (conversations)
- Vision (image analysis)
- DALL-E 3 (image generation)
- Whisper (speech-to-text)
- TTS (text-to-speech)
- Embeddings (semantic search)
- Assistants (persistent agents)
- Sora 2 (video generation)
- GPT-5 Pro (advanced reasoning)

**Examples:**
- 📸 Recipe from food photo (Vision + Chat)
- 🎙️ Meeting transcriber (Whisper + Summarization)
- 🎨 AI art studio (DALL-E 3 + Chat)
- 📚 Document Q&A (Embeddings + Chat)
- 🎬 Story to video (Chat + Sora 2)

**[Browse 10 detailed project ideas →](docs/PROJECT_IDEAS.md)**

---

## ⚡ Quick Start (5 Minutes)

**Prerequisites:** Python 3.11 or higher ([Download](https://python.org))

```bash
# Clone and setup
git clone https://github.com/kaw393939/enterprise_ai_demo1_websearch.git
cd enterprise_ai_demo1_websearch
python -m venv venv
source venv/bin/activate  # Mac/Linux (Windows: venv\Scripts\activate)

# Install dependencies
pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add: OPENAI_API_KEY=sk-your-key-here

# Verify it works
pytest
python -m src.main "latest AI developments"
```

✅ **Working?** Great! Next: **[Read Course Structure →](docs/COURSE_STRUCTURE.md)**

❌ **Issues?** Check **[Getting Started Guide →](docs/GETTING_STARTED.md)**

---

## 💡 What Makes This Course Unique

### 1. **Code IS the Textbook**
Every file has narrative comments explaining concepts, design decisions, and alternatives.

**Traditional code:**
```python
@dataclass
class SearchOptions:
    model: str = "gpt-4o-mini"
```

**Our teaching code:**
```python
@dataclass
class SearchOptions:
    """
    📚 CONCEPT: Dataclasses auto-generate __init__, __repr__, __eq__

    📝 DESIGN: We default to "gpt-4o-mini" (fastest, cheapest for learning)

    EXAMPLE:
    >>> options = SearchOptions()  # Uses defaults
    >>> options = SearchOptions(model="gpt-4o")  # Override for production
    """
    model: str = "gpt-4o-mini"
```

### 2. **TDD is Non-Negotiable**
You'll write tests FIRST, then code. This is how professionals prevent bugs.

### 3. **Production Standards**
Not tutorial code—real patterns you'll use in your career.

### 4. **AI as Learning Partner**
Learn to use Claude effectively while maintaining quality and understanding.

---

## 📊 Grading at a Glance

| Category | Points | Key Requirements |
|----------|--------|------------------|
| **Works & Uses APIs** | 30 | No crashes, correct API usage |
| **Tests & TDD** | 30 | 80%+ coverage, tests written first |
| **Code Quality** | 25 | Clean architecture, logging, errors |
| **Documentation & Demo** | 15 | Clear README, 5-min presentation |

**[View full rubric →](docs/GRADING.md)**

---

## 🆘 Getting Help

**During class:** Ask instructor, pair with classmates, use Claude

**Outside class:**
1. Read the relevant guide in `docs/`
2. Check example code in `src/` and `tests/`
3. Search the [OpenAI API reference](docs/openai_tools_research_oct2025.md)
4. Ask Claude with specific context (see [AI Collaboration guide](docs/AI_COLLABORATION.md))

**Common issues:**
```bash
pytest -v                                          # See test details
source venv/bin/activate                           # Activate environment
pytest --cov=src --cov-report=term-missing         # Check coverage
git status && git log --oneline                    # Git status
```

---

## 🎓 Learning Outcomes

After completing this course, you will confidently:

✅ Build robust API clients with error handling
✅ Write comprehensive tests using TDD methodology
✅ Structure applications with clean architecture
✅ Implement enterprise-grade logging and monitoring
✅ Use professional git workflows and CI/CD
✅ Collaborate effectively with AI tools
✅ Present technical work clearly

**Most importantly:** You'll shift from writing "scripts that work" to building "systems that last."

---

## 🚀 Ready to Start?

### Option 1: Dive Right In
**[Getting Started Guide →](docs/GETTING_STARTED.md)** - Get running in 5 minutes

### Option 2: Learn the Concepts First
**[Code as Textbook →](docs/CODE_AS_TEXTBOOK.md)** - Understand the philosophy

### Option 3: See the Full Plan
**[Course Structure →](docs/COURSE_STRUCTURE.md)** - 2-week breakdown

---

<div align="center">

**Questions?** Check the [Getting Started Guide](docs/GETTING_STARTED.md) or ask your instructor.

*The Bread Therapist Collective - Where Professional Therapy Meets Artisan Bread*

**Ready to begin your therapeutic journey? Choose your therapist and start healing! 🍞**

</div>
