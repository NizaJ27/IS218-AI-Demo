# Enterprise AI Demo - Web Search & Therapy Applications# 🍞 The Bread Therapist Collective



> **A learning platform for building production-quality AI applications** — This repository contains both educational materials and a complete therapy application demonstrating professional software development practices.> **Professional AI Therapy Through the Lens of Bread** — An innovative mental health support application featuring 8 specialized therapist personas, each representing a different therapeutic approach and named after a unique type of bread.



---## 🌟 Features



## 📂 Repository Structure### 8 Specialized Therapist Personas



This repository is organized into two main sections:Choose from evidence-based therapeutic approaches, each with a unique bread-themed personality:



### 🍞 **`therapy_app/`** - The Bread Therapist Collective- **🥖 Dr. Sourdough** - Cognitive Behavioral Therapy (CBT)

A complete, production-ready mental health support application featuring:- **🥐 Dr. Brioche** - Psychodynamic Therapy  

- 8 specialized AI therapist personas (each named after bread!)- **🍞 Dr. Whole Wheat** - Acceptance and Commitment Therapy (ACT)

- User authentication and personalization- **🍞 Dr. Pumpernickel** - Dialectical Behavior Therapy (DBT)

- Intelligent intake assessment- **🥖 Dr. Ciabatta** - Person-Centered Therapy

- Session logging and progress tracking- **🫓 Dr. Focaccia** - Solution-Focused Brief Therapy

- Beautiful toast-themed UI- **🍞 Dr. Rye** - Existential Therapy

- **🫓 Dr. Naan** - Mindfulness-Based Therapy

**[→ View Therapy App Documentation](therapy_app/README.md)**

### Beautiful UI/UX

### 📚 **`docs/`** - Course Materials & Learning Resources- Light, warm toast-inspired color scheme with radial gradient background

Comprehensive guides for learning professional AI development:- Interactive therapist selection cards with hover effects

- TDD methodology and testing practices- Responsive chat interface with streaming responses

- Clean architecture patterns- Clean, modern design optimized for therapy sessions

- Git workflows and CI/CD

- AI collaboration techniques### Smart Features

- Project ideas and templates- OpenAI GPT-4 powered conversations with therapeutic expertise

- Lab exercises and tutorials- Model selection (GPT-4o, GPT-4o-mini, GPT-4-turbo, etc.)

- Session persistence with message history

**[→ Browse Course Materials](docs/)**- Easy therapist switching mid-session



------



## 🚀 Quick Start## 🚀 Quick Start



### Run The Bread Therapist CollectiveRun the Bread Therapist Collective web interface:



```bash```bash

# Easy way - using Make# Easy way - using Make

make runmake run



# Or directly with the script# Or directly with the script

./run.sh./run.sh



# Or manually# Or manually

streamlit run therapy_app/streamlit_app.pystreamlit run streamlit_app.py

``````



**To stop the application:****Available Commands:**

```bash```bash

# Press Ctrl+C in the terminal, or from another terminal:make help      # Show all available commands

make stopmake run       # Run the Streamlit application

```make test      # Run all tests

make coverage  # Run tests with coverage report

---make install   # Install dependencies

make clean     # Clean up generated files

## 📋 Prerequisitesmake dev       # Run in development mode with auto-reload

```

- **Python 3.13+** ([Download](https://python.org))

- **OpenAI API key** ([Get one](https://platform.openai.com/api-keys))---

- **Git** ([Download](https://git-scm.com))

## � Prerequisites

---

- Python 3.13+

## 🛠️ Setup- OpenAI API key

- Virtual environment (recommended)

1. **Clone the repository**

```bash---

git clone <repository-url>

cd enterprise_ai_demo1_websearch## 🛠️ Setup

```

1. **Clone the repository**

2. **Set up virtual environment**```bash

```bashgit clone <repository-url>

python -m venv .venvcd enterprise_ai_demo1_websearch

source .venv/bin/activate  # On Windows: .venv\Scripts\activate```

```

2. **Set up environment**

3. **Install dependencies**```bash

```bashpython -m venv .venv

make installsource .venv/bin/activate  # On Windows: .venv\Scripts\activate

# or```

pip install -r requirements.txt

```3. **Install dependencies**

```bash

4. **Configure OpenAI API key**make install

```bash# or

# Create .env filepip install -r requirements.txt

echo "OPENAI_API_KEY=your-api-key-here" > .env```

```

4. **Configure OpenAI API key**

5. **Run the application**```bash

```bash# Create .env file

make runecho "OPENAI_API_KEY=your-api-key-here" > .env

``````



---5. **Run the application**

```bash

## 🧪 Testingmake run

```

```bash

# Run all tests---

make test

## 🧪 Testing

# Run with coverage report

make coverageThis project follows **Test-Driven Development** practices with 100% code coverage:



# Open HTML coverage report```bash

open htmlcov/index.html# Run all tests

```make test



---# Run with coverage report

make coverage

## 💡 Available Commands

# Open HTML coverage report

```bashopen htmlcov/index.html

make help      # Show all available commands```

make run       # Run The Bread Therapist Collective

make stop      # Stop the running application**Test Statistics:**

make test      # Run all tests- ✅ 69 tests passing

make coverage  # Run tests with coverage report- 📊 100% code coverage

make install   # Install dependencies- 🎯 TDD methodology

make clean     # Clean up generated files

make dev       # Run in development mode with auto-reload---

```

## 🏗️ Architecture

---

### Clean Layered Design

## 🎓 Learning Paths

```

### Option 1: Just Get the App Runningsrc/

1. Follow setup steps above├── models.py          # Data models (SearchRequest, SearchResult)

2. Run `make run`├── client.py          # OpenAI API client

3. Create an account and complete intake assessment├── parser.py          # Response parsing logic

4. Start your therapy session!├── search_service.py  # Business logic layer

├── main.py           # Application entry point

### Option 2: Learn the Development Concepts└── logging_config.py  # Centralized logging

1. Read [Getting Started Guide](docs/GETTING_STARTED.md)

2. Follow the [Learning Path](docs/LEARNING_PATH.md)streamlit_app.py      # Web interface with therapist personas

3. Complete the [Lab exercises](docs/labs/)tests/                # Comprehensive test suite

4. Build your own project using the patterns you learned```



### Option 3: Dive into the Code### Key Design Principles

1. Explore `therapy_app/src/` - see clean architecture in action- **Separation of Concerns**: Each module has a single responsibility

2. Read `therapy_app/tests/` - learn TDD methodology- **Dependency Injection**: Testable, flexible components

3. Study `therapy_app/streamlit_app.py` - understand UI/UX design- **Type Safety**: Pydantic models with validation

4. Review [Architecture docs](docs/architecture.md)- **Error Handling**: Graceful degradation with informative messages

- **Logging**: Structured logging for debugging and monitoring

---

---

## 📖 Key Documentation

## 🎨 Therapist Personas

### For App Users

- **[Therapy App README](therapy_app/README.md)** - How to use The Bread Therapist CollectiveEach therapist combines professional therapeutic techniques with bread-themed wisdom:

- **[Personalization System](therapy_app/PERSONALIZATION_SUMMARY.md)** - How the recommendation algorithm works

### Dr. Sourdough (CBT)

### For Developers/Students- Focuses on identifying and challenging negative thought patterns

- **[Getting Started](docs/GETTING_STARTED.md)** - Setup in 5-10 minutes- Helps break down problems systematically

- **[Learning Path](docs/LEARNING_PATH.md)** - Master roadmap- Teaches practical coping strategies

- **[TDD Workflow](docs/TDD_WORKFLOW.md)** - Test-driven development- "Let's examine that thought pattern - it seems like it's over-proofed with catastrophizing."

- **[Code as Textbook](docs/CODE_AS_TEXTBOOK.md)** - How to read this code

- **[AI Collaboration](docs/AI_COLLABORATION.md)** - Working with AI tools### Dr. Brioche (Psychodynamic)

- **[Git Workflow](docs/GIT_WORKFLOW.md)** - Professional version control- Explores unconscious patterns and past experiences

- **[Project Ideas](docs/PROJECT_IDEAS.md)** - 60+ project ideas- Examines how early relationships shape current behaviors

- Patient and deeply reflective approach

---- "This pattern has many layers, like brioche. What might be hidden in the deeper folds?"



## 🏗️ What This Repository Demonstrates### Dr. Whole Wheat (ACT)

- Promotes acceptance of difficult emotions

### Production-Quality Features- Helps clarify personal values

- ✅ Clean layered architecture- Encourages committed action aligned with values

- ✅ Comprehensive test coverage (100%)- "Fighting anxiety is like trying to remove the bran - it's part of the whole grain."

- ✅ Test-Driven Development (TDD)

- ✅ Enterprise-grade logging### Dr. Pumpernickel (DBT)

- ✅ Error handling and validation- Balances acceptance and change

- ✅ Type safety with Pydantic- Teaches mindfulness, distress tolerance, emotion regulation

- ✅ User authentication and security- Validates emotions while building skills

- ✅ Session management- "Both things can be true - you're doing your best AND you can learn new skills."

- ✅ Professional UI/UX design

### Dr. Ciabatta (Person-Centered)

### Educational Components- Provides unconditional positive regard

- 📚 Code written as narrative teaching material- Trusts in your inherent capacity for growth

- 🔬 Lab exercises for hands-on learning- Non-directive, empathetic listening

- 📖 Comprehensive documentation- "You have all the ingredients within you already."

- 🎯 Real-world project examples

- 🤖 AI collaboration best practices### Dr. Focaccia (Solution-Focused)

- 🌟 Professional development patterns- Focuses on solutions rather than problems

- Uses future-oriented questions

---- Identifies existing strengths and resources

- "What would be the first small thing you'd notice if this problem vanished?"

## 💻 Technology Stack

### Dr. Rye (Existential)

### The Bread Therapist Collective- Explores meaning, freedom, and authenticity

- **Frontend**: Streamlit with custom CSS- Helps confront existential concerns

- **AI Engine**: OpenAI GPT-4 (GPT-4o, GPT-4o-mini, GPT-4-turbo)- Philosophical and courage-focused

- **Backend**: Python 3.13+- "You're grappling with the weight of freedom - you can become any kind of bread you choose."

- **Authentication**: SHA-256 password hashing

- **Data Storage**: JSON (user profiles & sessions)### Dr. Naan (Mindfulness-Based)

- **Testing**: pytest with 100% coverage- Cultivates present-moment awareness

- Non-judgmental observation of thoughts

### Development Tools- Develops self-compassion

- **Version Control**: Git with professional workflows- "Notice your thoughts bubbling up - observe them, but you don't have to grab each one."

- **CI/CD**: GitHub Actions (configured)

- **Code Quality**: pylint, black (optional)---

- **Documentation**: Markdown with comprehensive guides

## 📚 What You'll Learn

---

This codebase demonstrates professional software development practices:

## 🎯 What You'll Learn

**Test-Driven Development** • **Clean Architecture** • **Enterprise Logging** • **Professional Git** • **CI/CD**

By exploring this repository, you'll master:

**The Twist:** This codebase is designed as a **living textbook**. Every file teaches you concepts through narrative comments and real examples.

✅ Building robust API clients with error handling  

✅ Writing comprehensive tests using TDD  ````

✅ Structuring applications with clean architecture  

✅ Implementing enterprise logging and monitoring  ---

✅ Using professional Git workflows  

✅ Collaborating effectively with AI tools  ## 🎯 Three Ways to Start

✅ Creating beautiful, functional UIs  

✅ Managing user authentication and data  <table>

✅ Presenting technical work professionally  <tr>

<td width="33%" align="center">

**Most importantly:** You'll shift from writing "scripts that work" to building "systems that last."<h3>🏃‍♂️ Just Get It Running</h3>

<p><strong>5-minute setup</strong></p>

---<a href="docs/GETTING_STARTED.md">Quick Start Guide →</a>

<br><br>

## 🗂️ Repository Contents<em>Setup, run tests, see it work</em>

</td>

```<td width="33%" align="center">

enterprise_ai_demo1_websearch/<h3>📚 Teach Me Properly</h3>

├── therapy_app/                    # The Bread Therapist Collective<p><strong>Full learning path</strong></p>

│   ├── streamlit_app.py            # Main application<a href="docs/LEARNING_PATH.md">Learning Path Map →</a>

│   ├── src/                        # Source code<br><br>

│   │   ├── user_manager.py         # Authentication & profiles<em>Follow the guided journey</em>

│   │   ├── therapy_intake.py       # Intake assessment</td>

│   │   ├── client.py               # OpenAI client<td width="33%" align="center">

│   │   ├── models.py               # Data models<h3>🎯 I Know What I'm Doing</h3>

│   │   └── ...                     # Other modules<p><strong>Jump to the code</strong></p>

│   ├── tests/                      # Test suite (100% coverage)<a href="src/">Browse Source →</a>

│   ├── user_data/                  # User profiles & sessions (gitignored)<br><br>

│   ├── logs/                       # Application logs<em>See patterns, apply them</em>

│   └── README.md                   # App documentation</td>

│</tr>

├── docs/                           # Course materials</table>

│   ├── GETTING_STARTED.md          # Setup guide

│   ├── LEARNING_PATH.md            # Learning roadmap---

│   ├── TDD_WORKFLOW.md             # Testing guide

│   ├── AI_COLLABORATION.md         # AI usage guide## 📖 Your Learning Resources

│   ├── labs/                       # Hands-on exercises

│   └── ...                         # More guides---

│

├── requirements.txt                # Python dependencies## 💻 Technology Stack

├── Makefile                        # Development commands

├── pytest.ini                      # Test configuration- **Frontend**: Streamlit (interactive web interface)

├── run.sh                          # Application launcher- **AI Engine**: OpenAI GPT-4 (GPT-4o, GPT-4o-mini, GPT-4-turbo)

├── .env.example                    # Environment template- **Backend**: Python 3.13+

└── README.md                       # This file- **Testing**: pytest with 100% coverage

```- **Styling**: Custom CSS with toast-inspired color palette

- **Development**: TDD methodology, clean architecture

---

---

## 🆘 Getting Help

## 📖 Documentation

**During Development:**

1. Check the relevant guide in `docs/`### 🎓 Course Materials

2. Review example code in `therapy_app/src/`- **[Learning Path Map](docs/LEARNING_PATH.md)** - Master roadmap

3. Read test examples in `therapy_app/tests/`- **[Getting Started](docs/GETTING_STARTED.md)** - Setup and first steps

4. Search the [OpenAI API docs](docs/openai_tools_research_oct2025.md)- **[Course Structure](docs/COURSE_STRUCTURE.md)** - 2-week session plan

- **[Code as Textbook](docs/CODE_AS_TEXTBOOK.md)** - How to read this code

**Common Commands:**- **[Student Guide](docs/STUDENT_GUIDE.md)** - Day-by-day checklist

```bash- **[Grading Rubric](docs/GRADING.md)** - What you'll be evaluated on

make help                          # Show all commands

pytest -v                          # See test details### 🛠️ Development Guides

make coverage                      # Check code coverage- **[TDD Workflow](docs/TDD_WORKFLOW.md)** - Write tests first (15 min read)

git status                         # Check git status- **[AI Collaboration](docs/AI_COLLABORATION.md)** - Work with Claude (10 min read)

make clean                         # Clean up files- **[Git Workflow](docs/GIT_WORKFLOW.md)** - Professional commits (10 min read)

```- **[Logging Guide](docs/LOGGING.md)** - Enterprise logging (5 min read)

- **[Labs (Guided Practice)](docs/LEARNING_PATH.md#2-narrative-reading-days-12)** - Hands-on exercises per chapter

---

### 💡 Project Resources

## 🌟 Project Highlights- **[Project Launch Kit](docs/PROJECT_LAUNCH_KIT.md)** - Scope and planning template

- **[Project Ideas](docs/PROJECT_IDEAS.md)** - 60+ ideas with difficulty ratings

### The Bread Therapist Collective- **[OpenAI APIs](docs/openai_tools_research_oct2025.md)** - Complete API reference (1,300 lines)

- 8 unique therapist personas with distinct therapeutic approaches- **[Demo Playbook](docs/DEMO_PLAYBOOK.md)** - Prepare your final presentation

- Intelligent intake assessment with weighted scoring algorithm

- Personalized user experience with session history### 📚 Reference Library

- Beautiful, accessible UI with toast-themed design- **[Architecture Overview](docs/architecture.md)** - System diagrams and design decisions

- Production-ready code with comprehensive testing- **[OpenAI Web Search Notes](docs/web_search_openai.md)** - Tool behavior, payloads, and examples



### Educational Value---

- Real-world application architecture

- Professional development practices## 🏗️ What This Repository Demonstrates

- Comprehensive documentation

- Hands-on learning opportunities**A production-quality AI web search application** that shows you:

- AI collaboration examples

```

---📂 Architecture                      What You'll Learn

├── src/models.py                   → Dataclasses, type hints, exceptions

## 📊 Project Stats├── src/client.py                   → API clients, error handling, secrets

├── src/parser.py                   → Data transformation, defensive parsing

- **Lines of Code**: ~2,000+ (application)├── src/search_service.py           → Service layer, validation, orchestration

- **Test Coverage**: 100%├── src/main.py                     → CLI design, user experience

- **Number of Tests**: 69└── src/logging_config.py           → Enterprise logging, rotation

- **Therapist Personas**: 8

- **Documentation Pages**: 20+📂 Tests (69 tests, 100% coverage)   How You'll Prove It Works

- **Lab Exercises**: 6├── tests/test_models.py            → Unit testing patterns

├── tests/test_client.py            → Mocking external APIs

---├── tests/test_parser.py            → Data validation testing

├── tests/test_search_service.py    → Integration testing

<div align="center">└── tests/test_main.py              → System testing

```

**Ready to begin?**

**Key Feature:** Each source file pairs with a test file. This is Test-Driven Development.

**[Run the App →](therapy_app/README.md)** | **[Learn to Build →](docs/GETTING_STARTED.md)** | **[Browse Code →](therapy_app/src/)**

---

---

## 🎯 Your Mission (Choose One API or Combination)

*Enterprise AI Demo - Where Professional Development Meets Practical Application*

**Available Tools:**

**Questions?** Check the [Getting Started Guide](docs/GETTING_STARTED.md) or explore the [documentation](docs/).- Chat Completion (conversations)

- Vision (image analysis)

</div>- DALL-E 3 (image generation)

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
