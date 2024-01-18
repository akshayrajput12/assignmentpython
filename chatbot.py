'''1.	Chatbot:
Develop a simple chatbot using natural language processing libraries. The chatbot should be able to answer basic questions and engage in a conversation.
'''
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('My Chatbot')

# Train the chatbot with pre-defined conversational data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

def main():
    print("Hello! I am My Chatbot. How can I help you?")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print(f"My Chatbot: {response}")

if __name__ == "__main__":
    main()
