import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
print(f"API Key loaded: {api_key[:10]}..." if api_key else "No API key found")

genai.configure(api_key=api_key)

# List available models
print("\nAvailable models:")
for model in genai.list_models():
    print(f"  - {model.name}")
