import json
from datetime import datetime

def format_response(text: str, max_length: int = 1000) -> str:
    """Format response text."""
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

def save_conversation(messages: list, filename: str = "chats.json"):
    """Save conversations to file."""
    data = {
        "timestamp": datetime.now().isoformat(),
        "messages": messages
    }
    try:
        with open(filename, 'r') as f:
            chats = json.load(f)
    except FileNotFoundError:
        chats = []
    
    chats.append(data)
    with open(filename, 'w') as f:
        json.dump(chats, f, indent=2)

def log_interaction(user_msg: str, bot_response: str, filename: str = "interactions.log"):
    """Log user-bot interactions."""
    with open(filename, 'a') as f:
        timestamp = datetime.now().isoformat()
        f.write(f"\n[{timestamp}]\n")
        f.write(f"User: {user_msg}\n")
        f.write(f"Bot: {bot_response}\n")
        f.write("-" * 80 + "\n")


