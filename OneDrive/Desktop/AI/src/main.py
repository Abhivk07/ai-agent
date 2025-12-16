import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Set up OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')
if not api_key or api_key == 'your_openai_api_key_here':
    print("Please set a valid OPENAI_API_KEY in .env file.")
    exit(1)
openai.api_key = api_key

def chat_with_ai(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except openai.AuthenticationError:
        return "Authentication failed. Please check your OpenAI API key."
    except openai.RateLimitError:
        return "Rate limit exceeded. Please try again later."
    except Exception as e:
        error_str = str(e)
        if "insufficient_quota" in error_str:
            return "Insufficient quota. Please check your OpenAI billing and add credits."
        return f"Error: {error_str}"

if __name__ == "__main__":
    print("AI Agent: Hello! Ask me anything.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("AI Agent: Goodbye!")
            break
        response = chat_with_ai(user_input)
        print(f"AI Agent: {response}")