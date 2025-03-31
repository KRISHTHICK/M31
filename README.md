# M31
GenAi

Python implementation of a chatbot that asks the user for their mother tongue and then responds in that language. I'll use the googletrans library for translation. Ensure you have the library installed using pip install googletrans==4.0.0-rc1.

Python
from googletrans import Translator

def get_language_code(language):
    languages = {
        'tamil': 'ta',
        'telugu': 'te',
        'kannada': 'kn',
        'malayalam': 'ml',
        'hindi': 'hi'
    }
    return languages.get(language.lower())

def chatbot():
    translator = Translator()
    
    mother_tongue = input("What is your mother tongue? (Tamil, Telugu, Kannada, Malayalam, Hindi): ").strip().lower()
    language_code = get_language_code(mother_tongue)
    
    if not language_code:
        print("Sorry, I currently support only Tamil, Telugu, Kannada, Malayalam, and Hindi.")
        return
    
    while True:
        user_input = input("Ask me anything in English: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        translation = translator.translate(user_input, dest=language_code)
        print(f"Answer in {mother_tongue.capitalize()}: {translation.text}")

if __name__ == "__main__":
    chatbot()
This script first asks the user for their mother tongue and then uses the googletrans library to translate the responses into the selected language. If the user types "exit", the chatbot will end the conversation.
