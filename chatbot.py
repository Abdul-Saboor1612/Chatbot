from chat_bot.bot import GeminiBot
from chat_bot.utils import log_interaction, save_conversation
import json

class Chatbot:
    
    def __init__(self):
        self.bot = GeminiBot()
        self.bot.start_session()
    
    def chat(self, user_input: str) -> str:
        """chatbot response."""
        response = self.bot.get_response(user_input)
        log_interaction(user_input, response)
        return response
    
    def interactive_chat(self):
        print("🤖 Hello I'm Jarvis")
        print("Type 'quit' to exit, 'history' to see conversation, 'save' to save chat\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye! 👋")
                break
            elif user_input.lower() == 'history':
                history = self.bot.get_history()
                for msg in history:
                    print(f"\n[{msg['role'].upper()}]: {msg['content']}")
            elif user_input.lower() == 'save':
                self.bot.save_history()
                print("✅ Conversation saved!")
            elif user_input:
                response = self.chat(user_input)
                print(f"\nJarvis: {response}\n")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.interactive_chat()

