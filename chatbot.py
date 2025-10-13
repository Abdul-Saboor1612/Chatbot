import re
import sys

class RuleBasedChatbot:
    """A simple rule-based chatbot using pattern matching."""
    
    def __init__(self):
        self.name = "RuleBot"
        self.rules = self._initialize_rules()
    
    def _initialize_rules(self):
        """Define chatbot rules with patterns and responses."""
        return [
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
                    f"I'm {self.name}, your friendly rule-based chatbot!",
                    f"My name is {self.name}. I'm here to chat with you!",
                    f"You can call me {self.name}!"
                ]
            },
            # Help
            {
                'patterns': [r'\bhelp\b', r'\bwhat can you do\b', r'\bcapabilities\b'],
                'responses': [
                    "I can chat with you about various topics! Try asking me about:\n"
                    "  - Greetings\n"
                    "  - How I'm doing\n"
                    "  - My name\n"
                    "  - The weather\n"
                    "  - Time\n"
                    "  - Jokes\n"
                    "  - Or just say goodbye when you're done!"
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
                    "Goodbye! Have a great day!",
                    "See you later! Come back anytime!",
                    "Take care! It was nice chatting with you!"
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
    
    def find_response(self, user_input):
        """Find and return appropriate response based on user input."""
        user_input = user_input.lower().strip()
        
        # Check each rule (except fallback)
        for rule in self.rules:
            if rule.get('fallback'):
                continue
                
            for pattern in rule['patterns']:
                if re.search(pattern, user_input, re.IGNORECASE):
                    import random
                    response = random.choice(rule['responses'])
                    should_exit = rule.get('exit', False)
                    return response, should_exit
        
        # If no match found, use fallback
        fallback_rule = [r for r in self.rules if r.get('fallback')][0]
        import random
        response = random.choice(fallback_rule['responses'])
        return response, False
    
    def chat(self):
        """Main chat loop."""
        print(f"\n{'='*60}")
        print(f"  Welcome to {self.name} - Your Rule-Based Chatbot!")
        print(f"{'='*60}")
        print("\nType 'help' to see what I can do, or 'quit' to exit.\n")
        
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                # Check for empty input
                if not user_input:
                    print(f"{self.name}: Please say something!\n")
                    continue
                
                # Get response
                response, should_exit = self.find_response(user_input)
                
                # Display response
                print(f"{self.name}: {response}\n")
                
                # Exit if needed
                if should_exit:
                    break
                    
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! (Interrupted by user)\n")
                sys.exit(0)
            except EOFError:
                print(f"\n\n{self.name}: Goodbye!\n")
                break
        
        print(f"{'='*60}\n")


def main():
    """Entry point for the chatbot."""
    chatbot = RuleBasedChatbot()
    chatbot.chat()


if __name__ == "__main__":
    main()
