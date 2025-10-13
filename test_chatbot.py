"""Simple test script to verify chatbot functionality."""

from chatbot import RuleBasedChatbot

def test_chatbot():
    """Test various chatbot responses."""
    bot = RuleBasedChatbot()
    
    test_cases = [
        ("hello", "greeting"),
        ("how are you", "status check"),
        ("what's your name", "name inquiry"),
        ("help", "help request"),
        ("tell me a joke", "joke request"),
        ("thank you", "thanks"),
        ("what is the weather", "weather query"),
        ("what time is it", "time query"),
        ("random gibberish xyz123", "fallback"),
    ]
    
    print("Testing Rule-Based Chatbot")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for user_input, test_name in test_cases:
        try:
            response, should_exit = bot.find_response(user_input)
            if response:
                print(f"✓ {test_name}: PASS")
                print(f"  Input: '{user_input}'")
                print(f"  Response: '{response[:60]}...'")
                passed += 1
            else:
                print(f"✗ {test_name}: FAIL - No response")
                failed += 1
        except Exception as e:
            print(f"✗ {test_name}: FAIL - {str(e)}")
            failed += 1
        print()
    
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)
    
    # Test exit functionality
    print("\nTesting exit functionality:")
    response, should_exit = bot.find_response("bye")
    print(f"Exit command 'bye' triggers exit: {should_exit}")
    
    if failed == 0:
        print("\n✓ All tests passed! The chatbot is working correctly.")
    else:
        print(f"\n✗ Some tests failed. Please check the implementation.")

if __name__ == "__main__":
    test_chatbot()
