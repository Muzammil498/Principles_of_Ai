import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot using dictionaries
patterns_responses = {
    'admission': ['For admission inquiries, you can visit our website or contact the admission office.'],
    'program': ['Our institution offers a variety of programs. Which program are you interested in?'],
    'deadline': ['The admission deadline varies depending on the program. Please check our website for specific deadlines.'],
    'financial aid': ['Information about financial aid options is available on our website or you can contact the financial aid office for assistance.'],
    'contact': ['You can contact our admission office at admission@example.com or call +123456789.'],
    'help': ['How can I assist you further?'],
    'AIML': ['We have 180 students in AIML branch'],
    'deadline':['The last date for admission is 21-12-24'],
    'faculty': ['We have best faculties in our college. They will morally guide you and support you in academics and also in life'],
    'canteen': ['We have best canteen with delicious food and with vast seating arrangement']
}

# Create patterns from keys of patterns_responses dictionary
patterns = [(r'(.*)' + pattern + r'(.*)', responses) for pattern, responses in patterns_responses.items()]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Define a function to interact with the chatbot
def admission_chat():
    print("Welcome to the Admission Chatbot. How can I assist you today?")
    print("Type 'quit' to exit.")

    # Start chatting
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)


nltk.download('punkt')
admission_chat()
