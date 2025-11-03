# AI Chatbot

An intelligent, conversational chatbot powered by Google Gemini 2.5 Flash. Upgraded from a simple rule-based system to a fully AI-driven experience with natural language understanding, conversation history tracking, and persistent storage.

## Features

- ✨ **AI-Powered Responses** - Uses Google Gemini 2.5 Flash for intelligent, context-aware conversations
- 💾 **Conversation Management** - Maintains session history, tracks interactions with timestamps
- 📝 **Persistent Storage** - Save/load conversations to JSON, comprehensive interaction logging
- 🎯 **Easy Integration** - Simple CLI interface, FastAPI backend for web deployment
- 🔧 **Modular Architecture** - Clean, extensible codebase with separate config and utility modules
- 🚀 **Production-Ready** - Error handling, logging, and comprehensive documentation

## File Structure

```
AI_ChatBot/
├── chat_bot/
│ ├── init.py # Package initialization
│ ├── bot.py # Main GeminiBot class
│ ├── config.py # Configuration settings
│ └── utils.py # Utility functions
├── chatbot.py # CLI chatbot interface
├── requirements.txt # Python dependencies
├── .env # place your api key here
├── .gitignore # Git ignore rules
└── README.md # This file         
```

## Installation

1️⃣ Clone Repository
```bash
git clone https://github.com/Abdul-Saboor1612/gemini-chatbot.git
cd gemini-chatbot
```
2️⃣ Create & Activate Virtual Environment
```bash
python3 -m venv .venv

# Activate (Mac/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Setup API Key
- Create .env file in the root directory
- Get your API key from: [link](https://aistudio.google.com/app/apikey)
- Go to .env file and write:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

5️⃣ Test Installation
```bash
python test_api.py
```

6️⃣ Run Script
```bash
python chatbot.py
```

## Author

Built as a simple demonstration of AI chatbot CLI implementation.
