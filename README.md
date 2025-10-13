# Rule-Based Chatbot

A simple CLI-based chatbot that responds to user inputs using predefined rules and pattern matching.

## Features

- **Pattern Matching**: Uses regular expressions to identify user queries
- **Rule-Based Responses**: Predefined rules with multiple response variations
- **Simple & Lightweight**: No external dependencies required (uses Python standard library)
- **Easy to Extend**: Add new rules by modifying the `_initialize_rules()` method

## File Structure

```
rule_based_bot/
├── chatbot.py          # Main chatbot implementation
└── README.md           # This file
```

## How It Works

The chatbot uses a rule-based approach:

1. **Pattern Matching**: Each rule contains regex patterns that match user input
2. **Response Selection**: When a pattern matches, a random response is selected from that rule
3. **Fallback**: If no pattern matches, a default response is provided

## Installation

No installation required! Just ensure you have Python 3.6+ installed.

```bash
python --version  # Check your Python version
```

## Usage

Run the chatbot from the command line:

```bash
python chatbot.py
```

### Example Conversation

```
You: hello
RuleBot: Hi there! What can I do for you?

You: what can you do?
RuleBot: I can chat with you about various topics! Try asking me about:
  - Greetings
  - How I'm doing
  - My name
  - The weather
  - Time
  - Jokes
  - Or just say goodbye when you're done!

You: tell me a joke
RuleBot: Why don't programmers like nature? It has too many bugs! 🐛

You: thanks
RuleBot: You're welcome! Happy to help!

You: bye
RuleBot: Goodbye! Have a great day!
```

## Supported Queries

The chatbot can respond to:

- **Greetings**: hi, hello, hey
- **Status**: how are you, how's it going
- **Identity**: what's your name, who are you
- **Help**: help, what can you do
- **Weather**: questions about weather (with limitations notice)
- **Time**: questions about current time (with limitations notice)
- **Jokes**: tell me a joke, make me laugh
- **Thanks**: thank you, thanks
- **Goodbye**: bye, exit, quit

## Customization

To add new rules, modify the `_initialize_rules()` method in `chatbot.py`:

```python
{
    'patterns': [r'\byour_pattern\b', r'\balternative_pattern\b'],
    'responses': [
        "First possible response",
        "Second possible response"
    ]
}
```

### Example: Adding a Rule for "Favorite Color"

```python
{
    'patterns': [r'\bfavorite color\b', r'\bfavou?rite colou?r\b'],
    'responses': [
        "I like all colors, but blue is quite nice!",
        "As a chatbot, I appreciate the color of code editors - usually dark!",
    ]
}
```

## Exit Options

- Type `bye`, `goodbye`, `exit`, or `quit`
- Press `Ctrl+C` (keyboard interrupt)
- Press `Ctrl+D` (EOF)

## Technical Details

- **Language**: Python 3.6+
- **Libraries**: Only standard library (`re`, `sys`, `random`)
- **Architecture**: Object-oriented with `RuleBasedChatbot` class
- **Pattern Matching**: Case-insensitive regex matching

## Code Structure

```python
RuleBasedChatbot
├── __init__()               # Initialize chatbot
├── _initialize_rules()      # Define all rules and patterns
├── find_response()          # Match input to rules and get response
└── chat()                   # Main conversation loop
```

## Limitations

- No machine learning or natural language understanding
- Cannot learn from conversations
- Limited to predefined rules
- No persistent memory between sessions
- No external API integrations

## Future Enhancements

Possible improvements:

- Add more rules and patterns
- Include sentiment analysis
- Add conversation history
- Integrate with external APIs
- Add logging functionality
- Support multiple languages

## License

Free to use and modify for any purpose.

## Author

Built as a simple demonstration of rule-based chatbot implementation.
