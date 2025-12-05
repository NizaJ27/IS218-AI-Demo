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
        // Fallback for non-HTTPS contexts where crypto.subtle is unavailable
        if (!crypto.subtle) {
            // Simple string hash fallback (NOT secure, just for demo on HTTP)
            let hash = 0;
            for (let i = 0; i < password.length; i++) {
                const char = password.charCodeAt(i);
                hash = ((hash << 5) - hash) + char;
                hash = hash & hash;
            }
            return Math.abs(hash).toString(16);
        }
        
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
        // For now, return intelligent simulated response based on context
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        const therapist = THERAPISTS[this.appState.currentTherapist];
        const messageLower = userMessage.toLowerCase();
        
        // Analyze user message for context and sentiment
        const context = this.analyzeMessage(messageLower);
        
        // Generate contextual response based on therapist type and user's message
        return this.generateTherapeuticResponse(therapist, userMessage, context);
    }

    analyzeMessage(messageLower) {
        const context = {
            isGreeting: /^(hi|hello|hey|good morning|good evening)/.test(messageLower),
            hasAnxiety: /(anxious|anxiety|worried|worry|nervous|panic|stress|overwhelm)/.test(messageLower),
            hasDepression: /(depressed|depression|sad|hopeless|empty|numb|down)/.test(messageLower),
            hasAnger: /(angry|anger|mad|frustrated|irritated|rage)/.test(messageLower),
            hasRelationship: /(relationship|partner|spouse|family|friend|people)/.test(messageLower),
            hasPast: /(past|childhood|before|used to|history|remember)/.test(messageLower),
            hasThoughts: /(think|thought|believe|mind|racing thoughts)/.test(messageLower),
            hasFeelings: /(feel|feeling|emotion|emotional)/.test(messageLower),
            hasQuestion: /\?/.test(messageLower),
            isShort: messageLower.split(' ').length < 5,
            mentionsChange: /(change|different|better|improve|help)/.test(messageLower),
            mentionsGoals: /(goal|want|wish|hope|need)/.test(messageLower)
        };
        return context;
    }

    generateTherapeuticResponse(therapist, userMessage, context) {
        // Handle greetings
        if (context.isGreeting) {
            return `Hello! I'm ${therapist.name}. I'm here to support you through ${therapist.approach}. What brings you to therapy today?`;
        }

        // Generate therapy-specific contextual responses
        const responses = {
            sourdough: this.generateCBTResponse(userMessage, context),
            brioche: this.generatePsychodynamicResponse(userMessage, context),
            wholewheat: this.generateACTResponse(userMessage, context),
            pumpernickel: this.generateDBTResponse(userMessage, context),
            ciabatta: this.generatePersonCenteredResponse(userMessage, context),
            focaccia: this.generateSolutionFocusedResponse(userMessage, context),
            rye: this.generateExistentialResponse(userMessage, context),
            naan: this.generateMindfulnessResponse(userMessage, context)
        };

        return responses[therapist.id] || this.generateGenericResponse(userMessage, context);
    }

    generateCBTResponse(userMessage, context) {
        if (context.hasThoughts && context.hasAnxiety) {
            return "I hear that you're experiencing anxious thoughts. In CBT, we explore how our thoughts influence our feelings. What specific thoughts are going through your mind when you feel this anxiety? Are there patterns you notice?";
        }
        if (context.hasAnxiety) {
            return "Anxiety can be challenging. Let's look at this through a CBT lens. When you notice these anxious feelings, what situation triggers them? And what thoughts come up for you in those moments?";
        }
        if (context.hasDepression && context.hasThoughts) {
            return "Thank you for sharing that with me. Depression often involves negative thought patterns. Can you help me understand the thoughts that accompany these feelings? What are you telling yourself?";
        }
        if (context.hasAnger) {
            return "Anger is a valid emotion, and it often signals something important. In CBT, we look at the thoughts behind the anger. What goes through your mind in these situations? What meaning are you giving to what happened?";
        }
        if (context.mentionsChange || context.mentionsGoals) {
            return "I appreciate you wanting to make changes. In CBT, we work on identifying and challenging unhelpful thought patterns. What would be most helpful to work on first? What thoughts or behaviors would you like to change?";
        }
        return "I'm listening carefully to what you're sharing. In CBT, we focus on the connection between thoughts, feelings, and behaviors. Can you tell me more about what thoughts arise in this situation?";
    }

    generatePsychodynamicResponse(userMessage, context) {
        if (context.hasPast) {
            return "You're touching on something from your past. These earlier experiences often shape how we relate to situations today. What feelings come up as you reflect on this? How might this be connected to what you're experiencing now?";
        }
        if (context.hasRelationship) {
            return "Relationships are a window into our inner world. As we explore this, I'm curious about the patterns you notice. How does this relationship remind you of earlier relationships in your life?";
        }
        if (context.hasAnxiety || context.hasDepression) {
            return "These feelings you're describing—they're significant. Sometimes our current emotions are connected to unresolved experiences. What comes to mind when you sit with these feelings? Are there memories or earlier experiences that surface?";
        }
        return "I'm noticing what you're sharing, and I wonder about the deeper meaning here. What associations come to mind? Sometimes our unconscious guides us toward understanding—what might your feelings be trying to tell you?";
    }

    generateACTResponse(userMessage, context) {
        if (context.hasAnxiety || context.hasFeelings) {
            return "Thank you for sharing these difficult feelings. In ACT, we don't try to eliminate uncomfortable emotions—we learn to make room for them. What would it be like to simply observe this feeling without trying to change it? What values matter to you in this situation?";
        }
        if (context.mentionsChange) {
            return "Change is about moving toward what matters to you. Instead of focusing on eliminating discomfort, let's explore your values. When you imagine a meaningful life, what does that look like? What actions align with those values?";
        }
        if (context.hasThoughts) {
            return "I hear you getting caught up in these thoughts. In ACT, we practice defusion—observing thoughts without getting tangled in them. Can you notice these thoughts as mental events, rather than absolute truths? What happens if you hold them more lightly?";
        }
        return "What I'm hearing is important. In ACT, we ask: even with these difficult experiences, what matters to you? What would you do if this feeling weren't an obstacle? How can you move toward your values, even in small ways?";
    }

    generateDBTResponse(userMessage, context) {
        if (context.hasAnger || (context.hasFeelings && context.hasRelationship)) {
            return "I hear the intensity in what you're sharing. DBT teaches us that all emotions are valid, even the difficult ones. Let's practice dialectics—both validating your feelings AND looking at skills that might help. What emotion are you experiencing most strongly right now?";
        }
        if (context.hasAnxiety) {
            return "Anxiety in the moment can be overwhelming. Let's use some DBT skills. First, I want to validate—this is genuinely difficult. Now, what might help you tolerate this distress? Have you tried any grounding techniques like the 5-4-3-2-1 method?";
        }
        if (context.hasRelationship) {
            return "Relationships can bring up intense emotions. DBT's interpersonal effectiveness skills can help here. What do you need from this relationship? How can we balance asking for what you need with maintaining the relationship and your self-respect?";
        }
        return "Thank you for being open with me. DBT is about balancing acceptance and change. I want to validate what you're experiencing—it makes sense given your situation. At the same time, what skills might help you in this moment? Let's explore what would be most helpful.";
    }

    generatePersonCenteredResponse(userMessage, context) {
        if (context.isShort) {
            return "I sense there's more beneath the surface. I'm here, fully present with you. Take your time—what would you like to explore?";
        }
        if (context.hasFeelings) {
            return "I hear the emotion in what you're sharing, and I want you to know it's safe to feel this here. You know yourself best—what do these feelings mean to you? What are they telling you about what you need?";
        }
        if (context.mentionsChange) {
            return "Your desire for change is meaningful. I trust in your capacity to find your own answers. What feels right to you? What does your inner wisdom tell you about the direction you want to go?";
        }
        return "I'm here with you, hearing not just your words but what's beneath them. You're the expert on your own experience. What else would you like me to understand about this? What feels most important to explore?";
    }

    generateSolutionFocusedResponse(userMessage, context) {
        if (context.mentionsGoals) {
            return "I love that you're thinking about what you want. Let's get really specific—what would be different if this problem were solved? On a scale of 1-10, where are you now, and what would a 10 look like?";
        }
        if (context.mentionsChange) {
            return "Change is already happening just by you being here. Let's focus on what's working. When is this problem less intense or not present at all? What are you doing differently in those moments? Those are your resources!";
        }
        if (context.hasDepression || context.hasAnxiety) {
            return "I hear this is difficult. Let me ask you something—despite this challenge, what's still going okay in your life? Even small things count. When this feeling is less intense, even slightly, what's different? Let's build on that.";
        }
        return "Thank you for sharing that. I want to focus on solutions and strengths. Tell me about a time when you handled something similar successfully. What did you do? What strengths did you use? How can we apply that here?";
    }

    generateExistentialResponse(userMessage, context) {
        if (context.mentionsGoals || context.mentionsChange) {
            return "You're grappling with questions of meaning and purpose—that's deeply human. What gives your life meaning? When you imagine looking back on your life, what would make it feel worthwhile? These are the questions that guide authentic living.";
        }
        if (context.hasAnxiety) {
            return "Anxiety often arises when we confront our freedom and responsibility. You're facing the reality that you must choose, and with choice comes uncertainty. What are you anxious about choosing? What would it mean to take responsibility for this decision?";
        }
        if (context.hasDepression) {
            return "What you're experiencing touches on existential questions—questions of meaning, purpose, perhaps feelings of emptiness. These are profound concerns. What matters to you? When do you feel most alive, most authentic? Let's explore what gives your existence meaning.";
        }
        return "You're touching on something fundamental about the human experience. We all face questions of freedom, meaning, death, and isolation. How does this connect to your sense of purpose? What would it mean to live more authentically in relation to this concern?";
    }

    generateMindfulnessResponse(userMessage, context) {
        if (context.hasThoughts) {
            return "I hear your mind is quite active. Let's practice mindfulness together. Can you notice these thoughts without judgment—like clouds passing in the sky? What happens when you simply observe them, rather than getting caught up in their content?";
        }
        if (context.hasAnxiety) {
            return "Anxiety pulls us into the future. Let's practice coming back to this present moment. Right now, as you sit here, what do you notice? What physical sensations are present? Can you bring gentle awareness to your breath, just for a few moments?";
        }
        if (context.hasFeelings) {
            return "Thank you for noticing and naming this feeling. Mindfulness invites us to be with our emotions without pushing them away or getting overwhelmed. Can you locate this feeling in your body? What happens if you bring kind, curious attention to it?";
        }
        return "What you're sharing is important. Let's bring mindful awareness to this experience. Can you notice what's happening right now, in this moment, without judgment? What physical sensations are present? What thoughts? Let's practice being with what is.";
    }

    generateGenericResponse(userMessage, context) {
        if (context.hasQuestion) {
            return "That's an important question. Rather than me providing answers, I'm curious what you think. What feels true for you? What does your intuition tell you?";
        }
        return "Thank you for sharing that with me. I want to make sure I'm understanding fully. Can you tell me more about what this means for you? How does this affect you?";
    }

    showTypingIndicator() {
        const messagesContainer = document.getElementById('chatMessages');
        const therapist = THERAPISTS[this.appState.currentTherapist];
        
        const typingWrapper = document.createElement('div');
        typingWrapper.id = 'typingIndicator';
        typingWrapper.className = 'message-wrapper therapist-wrapper';
        
        const senderLabel = document.createElement('div');
        senderLabel.className = 'message-sender';
        senderLabel.innerHTML = `${therapist.emoji} ${therapist.name}`;
        typingWrapper.appendChild(senderLabel);
        
        const typing = document.createElement('div');
        typing.className = 'message-bubble therapist-message';
        typing.innerHTML = '<div class="typing-dots"><span></span><span></span><span></span></div>';
        typingWrapper.appendChild(typing);
        
        messagesContainer.appendChild(typingWrapper);
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
        
        // Create message wrapper
        const messageWrapper = document.createElement('div');
        messageWrapper.className = `message-wrapper ${role === 'user' ? 'user-wrapper' : 'therapist-wrapper'}`;
        
        if (animate) {
            messageWrapper.style.opacity = '0';
            messageWrapper.style.transform = 'translateY(10px)';
        }
        
        // Add sender label
        const senderLabel = document.createElement('div');
        senderLabel.className = 'message-sender';
        if (role === 'user') {
            senderLabel.textContent = this.appState.user.username;
        } else {
            const therapist = THERAPISTS[this.appState.currentTherapist];
            senderLabel.innerHTML = `${therapist.emoji} ${therapist.name}`;
        }
        messageWrapper.appendChild(senderLabel);
        
        // Create message bubble
        const messageDiv = document.createElement('div');
        messageDiv.className = `message-bubble ${role === 'user' ? 'user-message' : 'therapist-message'}`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.textContent = content;
        
        const timeDiv = document.createElement('div');
        timeDiv.className = 'message-time';
        timeDiv.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        
        messageDiv.appendChild(contentDiv);
        messageDiv.appendChild(timeDiv);
        messageWrapper.appendChild(messageDiv);
        
        container.appendChild(messageWrapper);
        
        if (animate) {
            setTimeout(() => {
                messageWrapper.style.opacity = '1';
                messageWrapper.style.transform = 'translateY(0)';
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
