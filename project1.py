import datetime  # Time ke liye ye library chahiye

def chatbot():
    print("🤖 Bot: Hello! I'm your Rule-Based Chatbot. Type 'bye', 'exit', or 'quit' to leave.")
    
    # Continuous loop
    while True:
        user_input = input("You: ").lower().strip()  

        # 1. Exit Commands
        if user_input in ["bye", "exit", "quit", "goodbye"]:
            print("🤖 Bot: Goodbye! Have a great day 👋")
            break  
        
        # 2. Greetings
        elif user_input in ["hi", "hello", "hey", "salam"]:
            print("🤖 Bot: Hello there! How can I help you today?")

        # 3. How are you
        elif "how are you" in user_input:
            print("🤖 Bot: I'm doing great, thanks for asking! What about you?")

        # 4. Name puchna
        elif "your name" in user_input or "who are you" in user_input:
            print("🤖 Bot: I'm a simple Rule-Based Chatbot made in Python 😎")

        # 5. NEW RULE: Time batao
        elif "time" in user_input:
            now = datetime.datetime.now()
            print(f"🤖 Bot: Abhi time hai {now.strftime('%I:%M %p')}")
        # 6. Help
        elif "help" in user_input:
            print("🤖 Bot: Try saying 'hi', 'time', 'your name', or 'bye' to exit.")

        # 7. Default Rule
        else:
            print("🤖 Bot: Sorry, I didn't understand that. Try saying 'hi' or 'help'.")

# Function ko run karo
if __name__ == "__main__":
    chatbot()
