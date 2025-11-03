import google.generativeai as genai
from chat_bot.config import GOOGLE_API_KEY, MODEL_NAME, SYSTEM_PROMPT, MAX_HISTORY
import json
from datetime import datetime

class GeminiBot:
    
    def __init__(self, system_prompt=SYSTEM_PROMPT):
        
        if not GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(MODEL_NAME)
        self.system_prompt = system_prompt
        self.conversation_history = []
        self.chat_session = None
    
    def start_session(self):
        
        self.chat_session = self.model.start_chat(history=[])
        self.conversation_history = []
    
    def add_system_context(self, message):
        
        if not self.conversation_history:
            return f"{self.system_prompt}\n\nUser: {message}"
        return message
    
    def get_response(self, user_message: str) -> str:
       
        if not self.chat_session:
            self.start_session()
        
        try:
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "content": user_message,
                "timestamp": datetime.now().isoformat()
            })
            
            # Get response from Gemini
            response = self.chat_session.send_message(user_message)
            assistant_message = response.text
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message,
                "timestamp": datetime.now().isoformat()
            })
            
            # Keep only recent history
            if len(self.conversation_history) > MAX_HISTORY * 2:
                self.conversation_history = self.conversation_history[-MAX_HISTORY*2:]
            
            return assistant_message
        
        except Exception as e:
            error_message = f"Error getting response: {str(e)}"
            print(error_message)
            return error_message
    
    def get_history(self):
        
        return self.conversation_history
    
    def save_history(self, filename: str = "conversation_history.json"):
        
        with open(filename, 'w') as f:
            json.dump(self.conversation_history, f, indent=2)
    
    def load_history(self, filename: str = "conversation_history.json"):
        
        try:
            with open(filename, 'r') as f:
                self.conversation_history = json.load(f)
        except FileNotFoundError:
            print(f"History file {filename} not found")
    
    def clear_history(self):
        
        self.conversation_history = []
        self.start_session()
    
    def set_system_prompt(self, prompt: str):
        
        self.system_prompt = prompt
        self.clear_history()

