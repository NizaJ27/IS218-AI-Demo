/**
 * The Bread Therapist Collective - PWA Application
 * Main application logic for therapy app
 */

// ============================================================================
// THERAPIST DATA
// ============================================================================

const THERAPISTS = {
    "sourdough": {
        id: "sourdough",
        emoji: "🥖",
        name: "Dr. Sourdough",
        fullName: "Sourdough (Cognitive Behavioral Therapy)",
        approach: "Cognitive Behavioral Therapy",
        description: "Specializes in CBT, excellent for addressing thought patterns, anxiety, and developing practical coping strategies.",
        systemMessage: "You are Dr. Sourdough, a warm and supportive Cognitive Behavioral Therapist who helps clients identify and challenge unhelpful thought patterns. You're practical, structured, and focus on teaching coping strategies. Always maintain professional therapeutic boundaries while being empathetic."
    },
    "brioche": {
        id: "brioche",
        emoji: "🥐",
        name: "Dr. Brioche",
        fullName: "Brioche (Psychodynamic Therapy)",
        approach: "Psychodynamic Therapy",
        description: "Offers psychodynamic therapy to explore how past experiences and unconscious patterns influence your present.",
        systemMessage: "You are Dr. Brioche, a compassionate Psychodynamic Therapist who helps clients explore their unconscious patterns and how past experiences shape the present. You're insightful, patient, and guide clients to deeper self-understanding."
    },
    "wholewheat": {
        id: "wholewheat",
        emoji: "🌾",
        name: "Dr. Whole Wheat",
        fullName: "Whole Wheat (Acceptance and Commitment Therapy)",
        approach: "Acceptance and Commitment Therapy",
        description: "Practices ACT, helping you accept difficult emotions while committing to actions aligned with your values.",
        systemMessage: "You are Dr. Whole Wheat, an empowering ACT therapist who helps clients accept difficult emotions and commit to value-driven actions. You focus on psychological flexibility, mindfulness, and living authentically."
    },
    "pumpernickel": {
        id: "pumpernickel",
        emoji: "🍞",
        name: "Dr. Pumpernickel",
        fullName: "Pumpernickel (Dialectical Behavior Therapy)",
        approach: "Dialectical Behavior Therapy",
        description: "Specializes in DBT, offering skills training in mindfulness, distress tolerance, and emotion regulation.",
        systemMessage: "You are Dr. Pumpernickel, a skillful DBT therapist who teaches mindfulness, distress tolerance, emotion regulation, and interpersonal effectiveness. You balance validation with change-oriented strategies."
    },
    "ciabatta": {
        id: "ciabatta",
        emoji: "🥖",
        name: "Dr. Ciabatta",
        fullName: "Ciabatta (Person-Centered Therapy)",
        approach: "Person-Centered Therapy",
        description: "Provides person-centered therapy with unconditional positive regard, creating a safe space for self-discovery.",
        systemMessage: "You are Dr. Ciabatta, a person-centered therapist who offers unconditional positive regard, empathy, and genuine presence. You believe clients have the capacity for growth and self-direction when provided a safe, non-judgmental space."
    },
    "focaccia": {
        id: "focaccia",
        emoji: "🫓",
        name: "Dr. Focaccia",
        fullName: "Focaccia (Solution-Focused Brief Therapy)",
        approach: "Solution-Focused Brief Therapy",
        description: "Uses solution-focused therapy to help you identify what's already working and build on your strengths.",
        systemMessage: "You are Dr. Focaccia, a solution-focused brief therapist who helps clients identify their strengths and what's already working. You're future-oriented, efficient, and focus on solutions rather than problems."
    },
    "rye": {
        id: "rye",
        emoji: "🍞",
        name: "Dr. Rye",
        fullName: "Rye (Existential Therapy)",
        approach: "Existential Therapy",
        description: "Offers existential therapy to explore questions of meaning, freedom, and authenticity.",
        systemMessage: "You are Dr. Rye, an existential therapist who helps clients explore questions of meaning, purpose, freedom, and authenticity. You engage with life's fundamental concerns and help clients take responsibility for their choices."
    },
    "naan": {
        id: "naan",
        emoji: "🫓",
        name: "Dr. Naan",
        fullName: "Naan (Mindfulness-Based Therapy)",
        approach: "Mindfulness-Based Therapy",
        description: "Teaches mindfulness-based therapy, cultivating present-moment awareness and self-compassion.",
        systemMessage: "You are Dr. Naan, a mindfulness-based therapist who teaches present-moment awareness, non-judgment, and self-compassion. You guide clients to observe their thoughts and feelings without getting caught up in them."
    }
};

// ============================================================================
// INTAKE ASSESSMENT QUESTIONS
// ============================================================================

const INTAKE_QUESTIONS = [
    {
        id: "primary_concern",
        question: "What brings you to therapy today?",
        type: "multiple_choice",
        options: [
            {
                text: "Anxiety, worry, or racing thoughts",
                weights: { sourdough: 3, naan: 2 }
            },
            {
                text: "Depression or feeling stuck",
                weights: { brioche: 2, ciabatta: 2 }
            },
            {
                text: "Relationship or communication issues",
                weights: { pumpernickel: 3, ciabatta: 2 }
            },
            {
                text: "Life transitions or finding purpose",
                weights: { rye: 3, focaccia: 2 }
            },
            {
                text: "Emotional regulation difficulties",
                weights: { pumpernickel: 3, wholewheat: 2 }
            },
            {
                text: "Trauma or past experiences affecting me",
                weights: { brioche: 3 }
            },
            {
                text: "Stress management and mindfulness",
                weights: { naan: 3, wholewheat: 2 }
            },
            {
                text: "Specific problem I want to solve quickly",
                weights: { focaccia: 3, sourdough: 2 }
            }
        ]
    },
    {
        id: "therapy_preference",
        question: "What approach appeals to you most?",
        type: "multiple_choice",
        options: [
            {
                text: "Practical tools and strategies",
                weights: { sourdough: 3, pumpernickel: 2 }
            },
            {
                text: "Understanding my past and unconscious patterns",
                weights: { brioche: 3 }
            },
            {
                text: "Accepting myself and living according to my values",
                weights: { wholewheat: 3 }
            },
            {
                text: "Being heard and understood without judgment",
                weights: { ciabatta: 3 }
            },
            {
                text: "Finding solutions and focusing on the future",
                weights: { focaccia: 3 }
            },
            {
                text: "Exploring meaning and authenticity",
                weights: { rye: 3 }
            },
            {
                text: "Mindfulness and present-moment awareness",
                weights: { naan: 3 }
            }
        ]
    },
    {
        id: "emotional_style",
        question: "How would you describe your emotional experience?",
        type: "multiple_choice",
        options: [
            {
                text: "Intense emotions that feel overwhelming",
                weights: { pumpernickel: 3, naan: 2 }
            },
            {
                text: "Stuck in negative thought patterns",
                weights: { sourdough: 3 }
            },
            {
                text: "Disconnected from my feelings",
                weights: { brioche: 2, naan: 2 }
            },
            {
                text: "Avoiding difficult emotions",
                weights: { wholewheat: 3 }
            },
            {
                text: "Generally balanced, just need direction",
                weights: { focaccia: 2, ciabatta: 2 }
            }
        ]
    },
    {
        id: "timeline",
        question: "What's your therapy timeline preference?",
        type: "multiple_choice",
        options: [
            {
                text: "Short-term, focused on specific goals",
                weights: { focaccia: 3, sourdough: 2 }
            },
            {
                text: "Medium-term, learning new skills",
                weights: { pumpernickel: 2, wholewheat: 2 }
            },
            {
                text: "Long-term, deep exploration",
                weights: { brioche: 3, rye: 2 }
            },
            {
                text: "Flexible, whatever it takes",
                weights: { ciabatta: 2, naan: 2 }
            }
        ]
    },
    {
        id: "goals",
        question: "What are you hoping to achieve?",
        type: "text",
        placeholder: "Describe your therapy goals in 1-2 sentences..."
    }
];

// ============================================================================
// APPLICATION STATE
// ============================================================================

class AppState {
    constructor() {
        this.currentScreen = 'authScreen';
        this.user = null;
        this.currentTherapist = null;
        this.intakeResponses = {};
        this.recommendedTherapist = null;
        this.chatHistory = [];
        this.sessions = [];
        this.goals = [];
        this.progressNotes = [];
        this.selectedModel = 'gpt-4o';
        
        this.loadFromStorage();
    }

    loadFromStorage() {
        try {
            const stored = localStorage.getItem('therapyAppState');
            if (stored) {
                const data = JSON.parse(stored);
                Object.assign(this, data);
            }
        } catch (error) {
            console.error('Error loading state:', error);
        }
    }

    save() {
        try {
            localStorage.setItem('therapyAppState', JSON.stringify(this));
        } catch (error) {
            console.error('Error saving state:', error);
        }
    }

    setUser(user) {
        this.user = user;
        this.save();
    }

    logout() {
        this.user = null;
        this.currentTherapist = null;
        this.intakeResponses = {};
        this.recommendedTherapist = null;
        this.chatHistory = [];
        this.save();
    }

    setTherapist(therapistId) {
        this.currentTherapist = therapistId;
        this.chatHistory = [];
        this.save();
    }

    addChatMessage(role, content) {
        this.chatHistory.push({
            role,
            content,
            timestamp: new Date().toISOString()
        });
        this.save();
    }

    saveSession() {
        if (this.chatHistory.length > 0) {
            this.sessions.push({
                id: Date.now(),
                therapist: this.currentTherapist,
                messages: [...this.chatHistory],
                date: new Date().toISOString(),
                messageCount: this.chatHistory.length
            });
            this.save();
        }
    }

    addGoal(goalText) {
        this.goals.push({
            id: Date.now(),
            text: goalText,
            created: new Date().toISOString(),
            completed: false
        });
        this.save();
    }

    addProgressNote(note) {
        this.progressNotes.push({
            id: Date.now(),
            text: note,
            date: new Date().toISOString()
        });
        this.save();
    }
}

// ============================================================================
// USER MANAGER (Authentication)
// ============================================================================

class UserManager {
    constructor() {
        this.users = this.loadUsers();
    }

    loadUsers() {
        try {
            const stored = localStorage.getItem('therapyUsers');
            return stored ? JSON.parse(stored) : {};
        } catch (error) {
            console.error('Error loading users:', error);
            return {};
        }
    }

    saveUsers() {
        try {
            localStorage.setItem('therapyUsers', JSON.stringify(this.users));
        } catch (error) {
            console.error('Error saving users:', error);
        }
    }

    async hashPassword(password) {
        // Simple hash for demo - in production use bcrypt or similar
        const encoder = new TextEncoder();
        const data = encoder.encode(password);
        const hashBuffer = await crypto.subtle.digest('SHA-256', data);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    }

    async register(username, password) {
        if (this.users[username]) {
            throw new Error('Username already exists');
        }

        const passwordHash = await this.hashPassword(password);
        this.users[username] = {
            username,
            passwordHash,
            createdAt: new Date().toISOString(),
            intakeCompleted: false
        };
        this.saveUsers();
        return { username, createdAt: this.users[username].createdAt };
    }

    async login(username, password) {
        const user = this.users[username];
        if (!user) {
            throw new Error('User not found');
        }

        const passwordHash = await this.hashPassword(password);
        if (passwordHash !== user.passwordHash) {
            throw new Error('Invalid password');
        }

        return {
            username: user.username,
            createdAt: user.createdAt,
            intakeCompleted: user.intakeCompleted
        };
    }

    completeIntake(username) {
        if (this.users[username]) {
            this.users[username].intakeCompleted = true;
            this.saveUsers();
        }
    }
}

// ============================================================================
// INTAKE ASSESSMENT
// ============================================================================

class IntakeAssessment {
    constructor() {
        this.currentQuestionIndex = 0;
        this.responses = {};
    }

    getCurrentQuestion() {
        return INTAKE_QUESTIONS[this.currentQuestionIndex];
    }

    getTotalQuestions() {
        return INTAKE_QUESTIONS.length;
    }

    saveResponse(questionId, response) {
        this.responses[questionId] = response;
    }

    nextQuestion() {
        if (this.currentQuestionIndex < INTAKE_QUESTIONS.length - 1) {
            this.currentQuestionIndex++;
            return true;
        }
        return false;
    }

    previousQuestion() {
        if (this.currentQuestionIndex > 0) {
            this.currentQuestionIndex--;
            return true;
        }
        return false;
    }

    analyzeResponses() {
        const scores = {};
        
        // Initialize scores
        Object.keys(THERAPISTS).forEach(id => {
            scores[id] = 0;
        });

        // Calculate scores from multiple choice questions
        INTAKE_QUESTIONS.forEach(question => {
            if (question.type === 'multiple_choice') {
                const response = this.responses[question.id];
                if (response !== undefined) {
                    const option = question.options[response];
                    if (option && option.weights) {
                        Object.entries(option.weights).forEach(([therapist, weight]) => {
                            scores[therapist] = (scores[therapist] || 0) + weight;
                        });
                    }
                }
            }
        });

        // Find highest scoring therapist
        let maxScore = 0;
        let recommendedId = 'ciabatta'; // default
        
        Object.entries(scores).forEach(([id, score]) => {
            if (score > maxScore) {
                maxScore = score;
                recommendedId = id;
            }
        });

        // Get top 3
        const sortedScores = Object.entries(scores)
            .sort(([, a], [, b]) => b - a)
            .slice(0, 3);

        return {
            recommended: recommendedId,
            scores: sortedScores,
            allScores: scores
        };
    }

    getRecommendationText(therapistId) {
        const therapist = THERAPISTS[therapistId];
        return `Based on your responses, we recommend **${therapist.name}** (${therapist.approach}). ${therapist.description}`;
    }
}

// ============================================================================
// CHAT MANAGER
// ============================================================================

class ChatManager {
    constructor(appState) {
        this.appState = appState;
        this.isProcessing = false;
    }

    async sendMessage(userMessage) {
        if (this.isProcessing) return;
        
        this.isProcessing = true;
        this.appState.addChatMessage('user', userMessage);

        try {
            // Show typing indicator
            this.showTypingIndicator();

            // Simulate API call (replace with actual OpenAI API call)
            const response = await this.callOpenAI(userMessage);
            
            this.hideTypingIndicator();
            this.appState.addChatMessage('assistant', response);
            
            return response;
        } catch (error) {
            this.hideTypingIndicator();
            console.error('Error sending message:', error);
            throw error;
        } finally {
            this.isProcessing = false;
        }
    }

    async callOpenAI(userMessage) {
        // TODO: Replace with actual OpenAI API call
        // For now, return simulated response
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        const therapist = THERAPISTS[this.appState.currentTherapist];
        
        // Simulated therapeutic responses based on therapist type
        const responses = {
            sourdough: [
                "That's an interesting observation. Let's explore the thoughts that lead to these feelings. What goes through your mind when this happens?",
                "I hear you. In CBT, we often look at the connection between thoughts, feelings, and behaviors. Can you identify the automatic thoughts that arise in this situation?"
            ],
            brioche: [
                "I'm noticing patterns in what you're sharing. How do you think your past experiences might be influencing how you're feeling now?",
                "That resonates with something we discussed earlier. Let's explore what this might mean for your current relationships."
            ],
            // Add more responses for other therapists...
        };

        const therapistResponses = responses[therapist.id] || [
            "Thank you for sharing that with me. Tell me more about how this affects you.",
            "I'm here to support you. What would be most helpful to explore right now?"
        ];

        return therapistResponses[Math.floor(Math.random() * therapistResponses.length)];
    }

    showTypingIndicator() {
        const messagesContainer = document.getElementById('chatMessages');
        const typing = document.createElement('div');
        typing.id = 'typingIndicator';
        typing.className = 'message-bubble therapist-message';
        typing.innerHTML = '<div class="typing-dots"><span></span><span></span><span></span></div>';
        messagesContainer.appendChild(typing);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    hideTypingIndicator() {
        const typing = document.getElementById('typingIndicator');
        if (typing) typing.remove();
    }
}

// ============================================================================
// UI MANAGER
// ============================================================================

class UIManager {
    constructor(appState, userManager, chatManager) {
        this.appState = appState;
        this.userManager = userManager;
        this.chatManager = chatManager;
        this.intakeAssessment = null;
        
        this.initializeEventListeners();
        this.restoreState();
    }

    initializeEventListeners() {
        // Auth form listeners
        document.getElementById('loginForm')?.addEventListener('submit', (e) => this.handleLogin(e));
        document.getElementById('signupForm')?.addEventListener('submit', (e) => this.handleSignup(e));
        
        // Auth tab switching
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.switchAuthTab(e));
        });

        // Navigation
        document.getElementById('homeBtn')?.addEventListener('click', () => this.navigateTo('therapistScreen'));
        document.getElementById('therapistsBtn')?.addEventListener('click', () => this.navigateTo('therapistScreen'));
        document.getElementById('historyBtn')?.addEventListener('click', () => this.navigateTo('historyScreen'));
        document.getElementById('profileBtn')?.addEventListener('click', () => this.navigateTo('profileScreen'));
        
        // Chat
        document.getElementById('chatForm')?.addEventListener('submit', (e) => this.handleChatSubmit(e));
        document.getElementById('backBtn')?.addEventListener('click', () => this.navigateTo('therapistScreen'));
        
        // Profile
        document.getElementById('logoutBtn')?.addEventListener('click', () => this.handleLogout());
        document.getElementById('addGoalBtn')?.addEventListener('click', () => this.handleAddGoal());
        document.getElementById('modelSelect')?.addEventListener('change', (e) => {
            this.appState.selectedModel = e.target.value;
            this.appState.save();
        });

        // Auto-resize textarea
        const chatInput = document.getElementById('chatInput');
        if (chatInput) {
            chatInput.addEventListener('input', (e) => {
                e.target.style.height = 'auto';
                e.target.style.height = Math.min(e.target.scrollHeight, 120) + 'px';
            });
        }
    }

    restoreState() {
        if (this.appState.user) {
            // User is logged in
            if (this.appState.user.intakeCompleted) {
                // Show therapist selection or current chat
                if (this.appState.currentTherapist) {
                    this.navigateTo('chatScreen');
                    this.renderChatHistory();
                } else {
                    this.navigateTo('therapistScreen');
                }
            } else {
                // Start intake
                this.navigateTo('intakeScreen');
                this.startIntakeAssessment();
            }
        } else {
            // Show auth screen
            this.navigateTo('authScreen');
        }
    }

    switchAuthTab(e) {
        const tab = e.target.dataset.tab;
        
        // Update tab buttons
        document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
        e.target.classList.add('active');
        
        // Update forms
        document.querySelectorAll('.auth-form').forEach(form => form.classList.remove('active'));
        document.getElementById(`${tab}Form`).classList.add('active');
    }

    async handleLogin(e) {
        e.preventDefault();
        
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;

        try {
            this.showLoading();
            const user = await this.userManager.login(username, password);
            this.appState.setUser(user);
            
            this.showToast('Welcome back, ' + username + '! 🍞', 'success');
            
            if (user.intakeCompleted) {
                this.navigateTo('therapistScreen');
            } else {
                this.navigateTo('intakeScreen');
                this.startIntakeAssessment();
            }
        } catch (error) {
            this.showToast(error.message, 'error');
        } finally {
            this.hideLoading();
        }
    }

    async handleSignup(e) {
        e.preventDefault();
        
        const username = document.getElementById('signupUsername').value;
        const password = document.getElementById('signupPassword').value;
        const confirm = document.getElementById('signupConfirm').value;

        if (password !== confirm) {
            this.showToast('Passwords do not match', 'error');
            return;
        }

        if (password.length < 6) {
            this.showToast('Password must be at least 6 characters', 'error');
            return;
        }

        try {
            this.showLoading();
            const user = await this.userManager.register(username, password);
            this.appState.setUser(user);
            
            this.showToast('Welcome to Bread Therapy, ' + username + '! 🍞', 'success');
            
            // Start intake assessment
            this.navigateTo('intakeScreen');
            this.startIntakeAssessment();
        } catch (error) {
            this.showToast(error.message, 'error');
        } finally {
            this.hideLoading();
        }
    }

    startIntakeAssessment() {
        this.intakeAssessment = new IntakeAssessment();
        this.renderIntakeQuestion();
    }

    renderIntakeQuestion() {
        const question = this.intakeAssessment.getCurrentQuestion();
        const totalQuestions = this.intakeAssessment.getTotalQuestions();
        const currentIndex = this.intakeAssessment.currentQuestionIndex;
        
        // Update progress
        document.getElementById('currentQuestion').textContent = currentIndex + 1;
        document.getElementById('totalQuestions').textContent = totalQuestions;
        
        const progress = ((currentIndex + 1) / totalQuestions) * 100;
        document.getElementById('intakeProgress').style.width = progress + '%';
        
        // Render question
        const form = document.getElementById('intakeForm');
        form.innerHTML = '';
        
        const questionDiv = document.createElement('div');
        questionDiv.className = 'intake-question';
        
        const questionTitle = document.createElement('h3');
        questionTitle.className = 'question-title';
        questionTitle.textContent = question.question;
        questionDiv.appendChild(questionTitle);
        
        if (question.type === 'multiple_choice') {
            const optionsDiv = document.createElement('div');
            optionsDiv.className = 'intake-options';
            
            question.options.forEach((option, index) => {
                const label = document.createElement('label');
                label.className = 'intake-option';
                
                const radio = document.createElement('input');
                radio.type = 'radio';
                radio.name = question.id;
                radio.value = index;
                radio.checked = this.intakeAssessment.responses[question.id] === index;
                
                const text = document.createElement('span');
                text.textContent = option.text;
                
                label.appendChild(radio);
                label.appendChild(text);
                optionsDiv.appendChild(label);
            });
            
            questionDiv.appendChild(optionsDiv);
        } else if (question.type === 'text') {
            const textarea = document.createElement('textarea');
            textarea.className = 'form-input';
            textarea.name = question.id;
            textarea.placeholder = question.placeholder || '';
            textarea.rows = 4;
            textarea.value = this.intakeAssessment.responses[question.id] || '';
            questionDiv.appendChild(textarea);
        }
        
        form.appendChild(questionDiv);
        
        // Add navigation buttons
        const buttonsDiv = document.createElement('div');
        buttonsDiv.className = 'intake-buttons';
        
        if (currentIndex > 0) {
            const backBtn = document.createElement('button');
            backBtn.type = 'button';
            backBtn.className = 'btn btn-secondary';
            backBtn.textContent = '← Previous';
            backBtn.onclick = () => this.handleIntakePrevious();
            buttonsDiv.appendChild(backBtn);
        }
        
        const nextBtn = document.createElement('button');
        nextBtn.type = 'button';
        nextBtn.className = 'btn btn-primary';
        nextBtn.textContent = currentIndex === totalQuestions - 1 ? 'Complete Assessment' : 'Next →';
        nextBtn.onclick = () => this.handleIntakeNext();
        buttonsDiv.appendChild(nextBtn);
        
        form.appendChild(buttonsDiv);
    }

    handleIntakePrevious() {
        if (this.intakeAssessment.previousQuestion()) {
            this.renderIntakeQuestion();
        }
    }

    handleIntakeNext() {
        const question = this.intakeAssessment.getCurrentQuestion();
        
        // Validate and save response
        if (question.type === 'multiple_choice') {
            const selected = document.querySelector(`input[name="${question.id}"]:checked`);
            if (!selected) {
                this.showToast('Please select an option', 'error');
                return;
            }
            this.intakeAssessment.saveResponse(question.id, parseInt(selected.value));
        } else if (question.type === 'text') {
            const value = document.querySelector(`textarea[name="${question.id}"]`).value.trim();
            if (!value) {
                this.showToast('Please provide an answer', 'error');
                return;
            }
            this.intakeAssessment.saveResponse(question.id, value);
        }
        
        // Move to next question or complete
        if (this.intakeAssessment.nextQuestion()) {
            this.renderIntakeQuestion();
        } else {
            this.completeIntakeAssessment();
        }
    }

    completeIntakeAssessment() {
        const results = this.intakeAssessment.analyzeResponses();
        this.appState.recommendedTherapist = results.recommended;
        this.appState.intakeResponses = this.intakeAssessment.responses;
        
        // Mark intake as complete
        this.userManager.completeIntake(this.appState.user.username);
        this.appState.user.intakeCompleted = true;
        this.appState.save();
        
        // Show therapist selection with recommendation
        this.navigateTo('therapistScreen');
        this.renderTherapistSelection(results.recommended);
        
        const therapist = THERAPISTS[results.recommended];
        this.showToast(`We recommend ${therapist.name} for you! 🎯`, 'success');
    }

    renderTherapistSelection(recommendedId = null) {
        const grid = document.getElementById('therapistGrid');
        grid.innerHTML = '';
        
        // Show recommended therapist if exists
        if (recommendedId) {
            const recommendedSection = document.getElementById('recommendedSection');
            const recommendedCard = document.getElementById('recommendedCard');
            recommendedSection.style.display = 'block';
            
            const therapist = THERAPISTS[recommendedId];
            recommendedCard.innerHTML = this.createTherapistCardHTML(therapist, true);
            
            // Add click handler
            recommendedCard.querySelector('.therapist-card').addEventListener('click', () => {
                this.selectTherapist(therapist.id);
            });
        }
        
        // Render all therapists
        Object.values(THERAPISTS).forEach(therapist => {
            const card = document.createElement('div');
            card.innerHTML = this.createTherapistCardHTML(therapist, false);
            card.querySelector('.therapist-card').addEventListener('click', () => {
                this.selectTherapist(therapist.id);
            });
            grid.appendChild(card);
        });
    }

    createTherapistCardHTML(therapist, isRecommended) {
        return `
            <div class="therapist-card ${isRecommended ? 'recommended' : ''}">
                <div class="therapist-emoji">${therapist.emoji}</div>
                <h3 class="therapist-card-name">${therapist.name}</h3>
                <p class="therapist-card-approach">${therapist.approach}</p>
                <p class="therapist-card-description">${therapist.description}</p>
                ${isRecommended ? '<span class="recommended-badge">✨ Recommended</span>' : ''}
            </div>
        `;
    }

    selectTherapist(therapistId) {
        this.appState.setTherapist(therapistId);
        const therapist = THERAPISTS[therapistId];
        
        // Update chat screen header
        document.getElementById('chatTherapistEmoji').textContent = therapist.emoji;
        document.getElementById('chatTherapistName').textContent = therapist.name;
        document.getElementById('chatTherapistApproach').textContent = therapist.approach;
        
        // Clear chat and navigate
        this.navigateTo('chatScreen');
        this.renderChatHistory();
        
        this.showToast(`Starting session with ${therapist.name}`, 'success');
    }

    renderChatHistory() {
        const container = document.getElementById('chatMessages');
        container.innerHTML = '';
        
        if (this.appState.chatHistory.length === 0) {
            const welcome = document.createElement('div');
            welcome.className = 'welcome-message';
            welcome.innerHTML = `
                <div class="welcome-icon">🍞</div>
                <p>Ready to begin your session?</p>
                <p class="welcome-subtitle">Share what's on your mind</p>
            `;
            container.appendChild(welcome);
        } else {
            this.appState.chatHistory.forEach(msg => {
                this.addMessageToChat(msg.role, msg.content, false);
            });
        }
        
        container.scrollTop = container.scrollHeight;
    }

    addMessageToChat(role, content, animate = true) {
        const container = document.getElementById('chatMessages');
        
        // Remove welcome message if exists
        const welcome = container.querySelector('.welcome-message');
        if (welcome) welcome.remove();
        
        const messageDiv = document.createElement('div');
        messageDiv.className = `message-bubble ${role === 'user' ? 'user-message' : 'therapist-message'}`;
        
        if (animate) {
            messageDiv.style.opacity = '0';
            messageDiv.style.transform = 'translateY(10px)';
        }
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.textContent = content;
        
        const timeDiv = document.createElement('div');
        timeDiv.className = 'message-time';
        timeDiv.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        
        messageDiv.appendChild(contentDiv);
        messageDiv.appendChild(timeDiv);
        container.appendChild(messageDiv);
        
        if (animate) {
            setTimeout(() => {
                messageDiv.style.opacity = '1';
                messageDiv.style.transform = 'translateY(0)';
            }, 10);
        }
        
        container.scrollTop = container.scrollHeight;
    }

    async handleChatSubmit(e) {
        e.preventDefault();
        
        const input = document.getElementById('chatInput');
        const message = input.value.trim();
        
        if (!message) return;
        
        // Clear input
        input.value = '';
        input.style.height = 'auto';
        
        // Add user message to chat
        this.addMessageToChat('user', message);
        
        try {
            // Send to therapist (OpenAI)
            const response = await this.chatManager.sendMessage(message);
            
            // Add therapist response
            this.addMessageToChat('assistant', response);
            
            // Auto-save every 4 messages
            if (this.appState.chatHistory.length % 4 === 0) {
                this.appState.saveSession();
                this.showToast('Session auto-saved', 'info');
            }
        } catch (error) {
            this.showToast('Error sending message. Please try again.', 'error');
        }
    }

    handleLogout() {
        if (confirm('Save current session before logging out?')) {
            this.appState.saveSession();
        }
        
        this.appState.logout();
        this.navigateTo('authScreen');
        this.showToast('Logged out successfully', 'info');
    }

    handleAddGoal() {
        const goalText = prompt('Enter your therapy goal:');
        if (goalText && goalText.trim()) {
            this.appState.addGoal(goalText.trim());
            this.renderProfile();
            this.showToast('Goal added!', 'success');
        }
    }

    renderProfile() {
        // Update profile info
        document.getElementById('profileUsername').textContent = this.appState.user.username;
        const memberDate = new Date(this.appState.user.createdAt);
        document.getElementById('memberSince').textContent = memberDate.toLocaleDateString();
        
        // Update model selection
        document.getElementById('modelSelect').value = this.appState.selectedModel;
        
        // Render goals
        const goalsContainer = document.getElementById('goalsContainer');
        if (this.appState.goals.length === 0) {
            goalsContainer.innerHTML = '<p class="empty-state-text">No goals set yet</p>';
        } else {
            goalsContainer.innerHTML = this.appState.goals.map(goal => `
                <div class="goal-item">
                    <input type="checkbox" ${goal.completed ? 'checked' : ''} 
                           onchange="app.toggleGoal(${goal.id})">
                    <span class="${goal.completed ? 'completed' : ''}">${goal.text}</span>
                </div>
            `).join('');
        }
        
        // Render progress notes
        const notesContainer = document.getElementById('notesContainer');
        if (this.appState.progressNotes.length === 0) {
            notesContainer.innerHTML = '<p class="empty-state-text">No progress notes yet</p>';
        } else {
            notesContainer.innerHTML = this.appState.progressNotes.map(note => `
                <div class="note-item">
                    <p class="note-date">${new Date(note.date).toLocaleDateString()}</p>
                    <p class="note-text">${note.text}</p>
                </div>
            `).join('');
        }
    }

    renderHistory() {
        // Update stats
        document.getElementById('totalSessions').textContent = this.appState.sessions.length;
        document.getElementById('goalsSet').textContent = this.appState.goals.length;
        document.getElementById('progressNotes').textContent = this.appState.progressNotes.length;
        
        // Render session list
        const historyList = document.getElementById('historyList');
        if (this.appState.sessions.length === 0) {
            historyList.innerHTML = '<p class="empty-state-text">No sessions yet</p>';
        } else {
            historyList.innerHTML = this.appState.sessions.map(session => {
                const therapist = THERAPISTS[session.therapist];
                const date = new Date(session.date);
                return `
                    <div class="session-card">
                        <div class="session-header">
                            <span class="therapist-emoji">${therapist.emoji}</span>
                            <div>
                                <h4>${therapist.name}</h4>
                                <p class="session-date">${date.toLocaleDateString()} at ${date.toLocaleTimeString()}</p>
                            </div>
                        </div>
                        <div class="session-stats">
                            <span>💬 ${session.messageCount} messages</span>
                        </div>
                    </div>
                `;
            }).join('');
        }
    }

    toggleGoal(goalId) {
        const goal = this.appState.goals.find(g => g.id === goalId);
        if (goal) {
            goal.completed = !goal.completed;
            this.appState.save();
            this.renderProfile();
        }
    }

    navigateTo(screenId) {
        // Hide all screens
        document.querySelectorAll('.screen').forEach(screen => {
            screen.classList.remove('active');
        });
        
        // Show target screen
        document.getElementById(screenId).classList.add('active');
        
        // Update nav buttons
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // Show/hide header based on screen
        const header = document.querySelector('.app-header');
        if (screenId === 'authScreen' || screenId === 'intakeScreen') {
            header.style.display = 'none';
        } else {
            header.style.display = 'block';
            
            // Update active nav button
            const navMap = {
                'therapistScreen': 'homeBtn',
                'chatScreen': 'therapistsBtn',
                'historyScreen': 'historyBtn',
                'profileScreen': 'profileBtn'
            };
            const activeBtn = document.getElementById(navMap[screenId]);
            if (activeBtn) activeBtn.classList.add('active');
        }
        
        // Render screen content
        if (screenId === 'therapistScreen') {
            this.renderTherapistSelection(this.appState.recommendedTherapist);
        } else if (screenId === 'historyScreen') {
            this.renderHistory();
        } else if (screenId === 'profileScreen') {
            this.renderProfile();
        }
        
        this.appState.currentScreen = screenId;
        this.appState.save();
    }

    showToast(message, type = 'info') {
        const container = document.getElementById('toastContainer');
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        
        const icon = {
            success: '✓',
            error: '✕',
            warning: '⚠',
            info: 'ℹ'
        }[type] || 'ℹ';
        
        toast.innerHTML = `<span class="toast-icon">${icon}</span><span>${message}</span>`;
        container.appendChild(toast);
        
        setTimeout(() => toast.classList.add('show'), 10);
        
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }

    showLoading() {
        document.getElementById('loadingOverlay').classList.add('active');
    }

    hideLoading() {
        document.getElementById('loadingOverlay').classList.remove('active');
    }
}

// ============================================================================
// INITIALIZE APPLICATION
// ============================================================================

let app;

document.addEventListener('DOMContentLoaded', () => {
    const appState = new AppState();
    const userManager = new UserManager();
    const chatManager = new ChatManager(appState);
    const uiManager = new UIManager(appState, userManager, chatManager);
    
    // Make app globally accessible for inline handlers
    window.app = uiManager;
    
    // Check online/offline status
    window.addEventListener('online', () => {
        document.getElementById('offlineIndicator').classList.remove('active');
    });
    
    window.addEventListener('offline', () => {
        document.getElementById('offlineIndicator').classList.add('active');
    });
    
    console.log('🍞 Bread Therapist Collective PWA initialized');
});
