import os
from dotenv import load_dotenv

load_dotenv()

# Gemini Configuration
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
MODEL_NAME = 'gemini-2.5-flash'

# System prompt for your chatbot
SYSTEM_PROMPT = """You are a helpful chatbot assistant. 
You help users by answering questions, providing information, and having meaningful conversations.
Be friendly, concise, and helpful in your responses."""

# Conversation settings
MAX_HISTORY = 10  # Keep last 10 messages
TEMPERATURE = 0.7