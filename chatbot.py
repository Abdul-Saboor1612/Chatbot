import re
import sys
import random


class RuleBasedChatbot:
    """A rule-based chatbot with mental health support."""
    
    def __init__(self):
        self.name = "RuleBot"
        self.rules = self._initialize_rules()
        self.crisis_resources = self._initialize_crisis_resources()
        self.conversation_history = []
        
    def _initialize_crisis_resources(self):
        """crisis hotline and resource information."""
        return {
            'international': {
                'info': "If you're in crisis, please reach out to these resources:",
                'hotlines': [
                    "🌍 International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/",
                    "🇺🇸 USA - 988 Suicide & Crisis Lifeline: Call/Text 988",
                    "🇺🇸 USA - Crisis Text Line: Text HOME to 741741",
                    "🇬🇧 UK - Samaritans: 116 123",
                    "🇮🇳 India - AASRA: 91-9820466726",
                    "🇦🇺 Australia - Lifeline: 13 11 14",
                    "🇨🇦 Canada - Crisis Services: 1-833-456-4566",
                ]
            }
        }
    
    def _initialize_rules(self):
        """Define chatbot rules with patterns and responses."""
        return [
            # === CRISIS DETECTION ===
            {
                'patterns': [
                    r'\b(suicid(e|al)|kill myself|end my life|want to die|no reason to live)\b',
                    r'\b(hurt myself|self[- ]?harm|cutting myself)\b',
                    r'\b(can\'?t go on|give up|no hope left)\b'
                ],
                'responses': [
                    "I'm really concerned about what you're sharing. Your life matters, and there are people who want to help. "
                    "Please reach out to a crisis helpline immediately - they have trained professionals available 24/7.\n\n"
                    "🆘 If you're in immediate danger, please call emergency services (911 in US, 999 in UK, 112 in EU).\n\n"
                    "Would you like me to share crisis support resources?"
                ],
                'crisis': True,
                'show_resources': True
            },
            
            
            # Depression and Sadness
            {
                'patterns': [
                    r'\b(depress(ed|ion)|feeling down|so sad|hopeless|empty inside)\b',
                    r'\b(lost interest|nothing matters|numb|can\'?t feel)\b'
                ],
                'responses': [
                    "I hear that you're going through a really difficult time. Depression is a serious but treatable condition. "
                    "You don't have to face this alone. Have you considered talking to a mental health professional? "
                    "They can provide proper support and treatment options.",
                    
                    "What you're feeling is valid, and it takes courage to acknowledge it. Depression affects many people, "
                    "and there are effective treatments available. Would it help to talk about what's been weighing on you? "
                    "I'm also here to share professional resources if you'd like.",
                    
                    "I'm sorry you're experiencing these feelings. Please know that depression is not a personal failing - "
                    "it's a medical condition that responds well to treatment. Consider reaching out to a counselor or therapist "
                    "who can provide specialized support."
                ]
            },
            
            # Anxiety and Stress
            {
                'patterns': [
                    r'\b(anxious|anxiety|panic|worried|stress(ed|ful)|overwhelmed)\b',
                    r'\b(can\'?t breathe|heart racing|panic attack)\b'
                ],
                'responses': [
                    "Anxiety can feel overwhelming, but there are ways to manage it. Have you tried deep breathing exercises? "
                    "Breathe in slowly for 4 counts, hold for 4, then exhale for 4. Would you like some more coping strategies, "
                    "or would you prefer information about professional support?",
                    
                    "I understand that stress and anxiety can be really difficult to handle. You're taking a positive step by "
                    "talking about it. Some people find relief through mindfulness, exercise, or speaking with a therapist. "
                    "What kind of support do you think might help you right now?",
                    
                    "What you're experiencing sounds challenging. Anxiety is very common, and there are evidence-based treatments "
                    "that can help. In the moment, try grounding techniques: Name 5 things you see, 4 you can touch, 3 you hear, "
                    "2 you smell, and 1 you taste. Would professional guidance be helpful for you?"
                ]
            },
            
            # Loneliness and Isolation
            {
                'patterns': [
                    r'\b(lonely|alone|isolated|no one cares|no friends)\b',
                    r'\b(feel invisible|nobody understands|so alone)\b'
                ],
                'responses': [
                    "Feeling lonely can be really painful, and I'm sorry you're experiencing this. You're not alone in feeling this way - "
                    "many people struggle with loneliness. Have you considered joining support groups or community activities? "
                    "Sometimes connecting with others who understand can help.",
                    
                    "I hear you, and your feelings matter. Loneliness is a common human experience, but that doesn't make it easier. "
                    "Would you like to talk about what's contributing to these feelings? Sometimes sharing can lighten the burden.",
                    
                    "What you're feeling is real and valid. Building connections takes time, but there are people and communities "
                    "that would value you. Consider reaching out to online support groups, local meetups, or a counselor who can "
                    "help you work through these feelings."
                ]
            },
            
            # Sleep Issues
            {
                'patterns': [
                    r'\b(can\'?t sleep|insomnia|trouble sleeping|nightmares)\b',
                    r'\b(sleep(ing)? (problems|issues|difficulties))\b'
                ],
                'responses': [
                    "Sleep difficulties can really impact your mental health. Some helpful practices include: keeping a consistent "
                    "sleep schedule, avoiding screens before bed, and creating a relaxing bedtime routine. If this continues, "
                    "a healthcare provider can help identify underlying causes.",
                    
                    "I understand sleep problems can be frustrating. They're often connected to stress, anxiety, or other factors. "
                    "Have you noticed any patterns with your sleep? A mental health professional or sleep specialist might be able "
                    "to provide personalized strategies."
                ]
            },
            
            # General Mental Health Inquiry
            {
                'patterns': [
                    r'\b(mental health|therapy|therapist|counselor|psychiatrist)\b',
                    r'\b(need help|get support|professional help)\b'
                ],
                'responses': [
                    "It's great that you're thinking about mental health support! Therapy can be really beneficial. "
                    "You might consider:\n"
                    "  • Speaking with your primary care doctor for referrals\n"
                    "  • Using online directories like Psychology Today\n"
                    "  • Checking if your workplace/school offers counseling services\n"
                    "  • Exploring teletherapy options for convenience\n"
                    "Would you like more specific guidance?",
                    
                    "Seeking professional help is a sign of strength, not weakness. Mental health professionals like therapists, "
                    "counselors, and psychiatrists are trained to help with various challenges. If cost is a concern, many offer "
                    "sliding scale fees, and some communities have free clinics."
                ]
            },
            
            # Self-Care and Coping
            {
                'patterns': [
                    r'\b(self[- ]?care|coping|how to feel better)\b',
                    r'\b(take care of myself|improve mood)\b'
                ],
                'responses': [
                    "Self-care is so important! Here are some evidence-based strategies:\n"
                    "  • Regular physical activity (even a short walk helps)\n"
                    "  • Maintaining social connections\n"
                    "  • Adequate sleep (7-9 hours)\n"
                    "  • Healthy nutrition and hydration\n"
                    "  • Mindfulness or meditation practices\n"
                    "  • Setting boundaries and saying no when needed\n"
                    "  • Engaging in activities you enjoy\n"
                    "What resonates most with you?",
                    
                    "Taking care of your mental health is just as important as physical health. Small steps matter: "
                    "spending time in nature, journaling, connecting with loved ones, or practicing gratitude. "
                    "Remember, self-care isn't selfish - it's necessary."
                ]
            },
            
            
            # Greetings
            {
                'patterns': [r'\b(hi|hello|hey|greetings)\b'],
                'responses': [
                    "Hello! How can I help you today?",
                    "Hi there! What can I do for you?",
                    "Hey! Nice to meet you!"
                ]
            },
            
            # How are you
            {
                'patterns': [r'\bhow are you\b', r'\bhow\'?s it going\b', r'\bhow do you do\b'],
                'responses': [
                    "I'm doing great, thank you for asking! How about you?",
                    "I'm functioning perfectly! How can I assist you?",
                    "All systems operational! What brings you here?"
                ]
            },
            
            # Name inquiry
            {
                'patterns': [r'\bwhat(?:\'?s| is) your name\b', r'\bwho are you\b'],
                'responses': [
                    f"I'm {self.name}, your friendly rule-based chatbot with mental health support!",
                    f"My name is {self.name}. I'm here to chat and provide support!",
                    f"You can call me {self.name}!"
                ]
            },
            
            # Help
            {
                'patterns': [r'\bhelp\b', r'\bwhat can you do\b', r'\bcapabilities\b'],
                'responses': [
                    "I can chat with you about various topics! Try asking me about:\n"
                    "  - Mental health support and resources\n"
                    "  - Coping strategies for anxiety and stress\n"
                    "  - Self-care tips\n"
                    "  - Crisis resources (if you need immediate help)\n"
                    "  - General conversation topics\n"
                    "  - Greetings and jokes\n"
                    "  - Or just say goodbye when you're done!\n\n"
                    "⚠️  Important: I'm a supportive bot, but not a replacement for professional mental health care."
                ]
            },
            
            # Weather
            {
                'patterns': [r'\bweather\b', r'\btemperature\b', r'\bforecast\b'],
                'responses': [
                    "I'm a simple chatbot and don't have access to weather data. Try checking weather.com!",
                    "I wish I could tell you about the weather, but I'm not connected to weather services.",
                    "For weather updates, I recommend checking your local weather service!"
                ]
            },
            
            # Time
            {
                'patterns': [r'\bwhat time\b', r'\bcurrent time\b', r'\bwhat\'?s the time\b'],
                'responses': [
                    "I don't have access to real-time data, but you can check your system clock!",
                    "Time flies when we're chatting! Check your device for the current time."
                ]
            },
            
            # Jokes
            {
                'patterns': [r'\bjoke\b', r'\bfunny\b', r'\bmake me laugh\b'],
                'responses': [
                    "Why don't programmers like nature? It has too many bugs! 🐛",
                    "Why do programmers prefer dark mode? Because light attracts bugs! 💡",
                    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
                    "Why did the chatbot go to therapy? It had too many unresolved issues! 😄"
                ]
            },
            
            # Thanks
            {
                'patterns': [r'\bthank(?:s| you)\b', r'\bappreciate\b'],
                'responses': [
                    "You're welcome! Happy to help!",
                    "No problem at all! Anything else I can do for you?",
                    "My pleasure! Feel free to ask more questions!"
                ]
            },
            
            # Goodbye
            {
                'patterns': [r'\b(bye|goodbye|exit|quit|see you)\b'],
                'responses': [
                    "Goodbye! Remember, you're not alone - help is always available. Take care!",
                    "See you later! Come back anytime you need support!",
                    "Take care! Wishing you all the best! 💙"
                ],
                'exit': True
            },
            
            # Yes/No
            {
                'patterns': [r'^\b(yes|yeah|yep|sure|ok|okay)\b$'],
                'responses': [
                    "Great! What else would you like to know?",
                    "Awesome! How can I help you further?"
                ]
            },
            {
                'patterns': [r'^\b(no|nope|nah)\b$'],
                'responses': [
                    "Alright! Let me know if you need anything.",
                    "No problem! What else can I do for you?"
                ]
            },
            
            # Default fallback
            {
                'patterns': [r'.*'],
                'responses': [
                    "I'm not sure I understand. Could you rephrase that?",
                    "Hmm, I don't have a response for that. Can you ask something else?",
                    "Sorry, I didn't quite get that. Try asking about help to see what I can do!",
                    "That's interesting! Though I'm not sure how to respond. Type 'help' to see what I can do."
                ],
                'fallback': True
            }
        ]
    
    def _show_crisis_resources(self):
        """Display crisis hotline information."""
        print(f"\n{'='*60}")
        print("🆘 CRISIS SUPPORT RESOURCES")
        print(f"{'='*60}")
        print(self.crisis_resources['international']['info'])
        print()
        for hotline in self.crisis_resources['international']['hotlines']:
            print(f"  {hotline}")
        print(f"\n{'='*60}\n")
    
    def find_response(self, user_input):
        """Find and return appropriate response based on user input."""
        user_input_lower = user_input.lower().strip()
        
        # Check each rule (except fallback)
        for rule in self.rules:
            if rule.get('fallback'):
                continue
                
            for pattern in rule['patterns']:
                if re.search(pattern, user_input_lower, re.IGNORECASE):
                    response = random.choice(rule['responses'])
                    should_exit = rule.get('exit', False)
                    is_crisis = rule.get('crisis', False)
                    show_resources = rule.get('show_resources', False)
                    
                    return response, should_exit, is_crisis, show_resources
        
        # If no match found, use fallback
        fallback_rule = [r for r in self.rules if r.get('fallback')][0]
        response = random.choice(fallback_rule['responses'])
        return response, False, False, False
    
    def chat(self):
        """Main chat loop."""
        print(f"\n{'='*60}")
        print(f"  Welcome to {self.name} - Mental Health Support Chatbot")
        print(f"{'='*60}")
        print("\n⚠️  IMPORTANT DISCLAIMER:")
        print("This chatbot provides supportive conversation and resources,")
        print("but is NOT a substitute for professional mental health care.")
        print("If you're in crisis, please contact emergency services or a")
        print("crisis helpline immediately.\n")
        print("Type 'help' to see what I can do, or 'quit' to exit.\n")
        
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                # Check for empty input
                if not user_input:
                    print(f"{self.name}: Please say something!\n")
                    continue
                
                # Store in conversation history
                self.conversation_history.append(user_input)
                
                # Get response
                response, should_exit, is_crisis, show_resources = self.find_response(user_input)
                
                # Display response
                print(f"{self.name}: {response}\n")
                
                # Show crisis resources if needed
                if show_resources or is_crisis:
                    self._show_crisis_resources()
                
                # Exit if needed
                if should_exit:
                    break
                    
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! Remember, support is always available. 💙\n")
                sys.exit(0)
            except EOFError:
                print(f"\n\n{self.name}: Goodbye! Take care of yourself! 💙\n")
                break
        
        print(f"{'='*60}\n")


def main():
    """Entry point for the chatbot."""
    chatbot = RuleBasedChatbot()
    chatbot.chat()


if __name__ == "__main__":
    main()
