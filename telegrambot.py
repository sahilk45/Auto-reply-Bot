import pyautogui
import time
import pyperclip
import hashlib
import random

def auto_reply_telegram():
    # Store the last processed message hash to detect new messages
    last_message_hash = ""
    
    response_templates = [
        "Thanks for your message! I'll get back to you soon.",
        "I've received your message and will respond shortly.",
        "Hello! Thanks for reaching out. I'll reply as soon as possible.",
        "Got your message! I'll check and respond soon.",
        "Thanks for contacting me. I'll review this and get back to you."
    ]
    # Keyword-based
    keyword_responses = {
        "hello": ["Hi there!", "Hello! How can I help?", "Greetings! How are you?"],
        "help": ["I'd be happy to help. What do you need?", "How can I assist you?"],
        "thanks": ["You're welcome!", "Happy to help!", "No problem at all."],
        "bye": ["Goodbye!", "Talk to you later!", "Have a great day!"]
    }
    
    print("Starting Telegram Auto-Reply Bot...")
    print("Press Ctrl+C to stop")
    
    try:
        pyautogui.click(1430,1053)
        time.sleep(1)
        while True:
            pyautogui.moveTo(486, 451)
            pyautogui.dragTo(562, 944, duration=1, button="left")
            
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            
            message_text = pyperclip.paste()
            
            pyautogui.click(1842, 79)
            
            # Check if this is a new message
            if message_text:
                current_hash = hashlib.md5(message_text.encode()).hexdigest()
                
                # Check if we've already replied to this message
                if current_hash != last_message_hash:
                    last_message_hash = current_hash
                    print(f"\nNew message: {message_text}")
                    
                    # Generate a response based on keywords
                    response = generate_response(message_text, keyword_responses, response_templates)
                    print(f"Responding with: {response}")
                    
                    # Click on message input field (using YOUR coordinate)
                    pyautogui.click(559, 984)
                    time.sleep(1)
                    
                    # Type and send response
                    pyperclip.copy(response)
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                     
                    print("Response sent!")
                else:
                    print(".", end="", flush=True)
            else:
                print("No message detected")
                
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nBot stopped by user.")

def generate_response(message, keyword_responses, generic_responses):
    """Generate a simple response based on keywords in the message"""
    message_lower = message.lower()
    
    # Check keywords
    for keyword, responses in keyword_responses.items():
        if keyword in message_lower:
            return random.choice(responses)
    
    return random.choice(generic_responses)

if __name__ == "__main__":
    print("Preparing to start...")
    print("Please switch to the Telegram window within 5 seconds")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)

    auto_reply_telegram()