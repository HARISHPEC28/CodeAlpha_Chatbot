def chatbot():
    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you?")
        
        elif user in ["how are you", "how are you?"]:
            print("Bot: I'm doing great! Thanks for asking.")
        
        elif user in ["what is your name", "your name"]:
            print("Bot: I'm a simple Python chatbot!")
        
        
        elif user in ["thank you", "thanks"]:
            print("Bot: You're welcome!")
        
        elif user in ["bye", "goodbye", "exit"]:
            print("Bot: Goodbye! Have a nice day!")
            break
        
        else:
            print("Bot: Sorry, I didn't understand that.")

chatbot()
