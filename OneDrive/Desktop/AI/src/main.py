import os
from dotenv import load_dotenv
from agent import chat_with_ai

# Load environment variables
load_dotenv()

# Set up OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')
if not api_key or api_key == 'your_openai_api_key_here':
    print("Please set a valid OPENAI_API_KEY in .env file.")
    exit(1)
# API key is set in agent.py

if __name__ == "__main__":
    print("AI Agent: Hello! Ask me anything.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("AI Agent: Goodbye!")
            break
        response = chat_with_ai(user_input)
        print(f"AI Agent: {response}")