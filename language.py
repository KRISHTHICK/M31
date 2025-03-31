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
