from dotenv import load_dotenv
from openai import OpenAI
import os
from ai_common import *

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
if api_key:
    print(f"OpenAI API Key exists and begins {api_key[:8]}")
else:
    print("OpenAI API Key not set")

openai = OpenAI()

def chat(model, messages):
    response = openai.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content

def test_prompt():
    messages = add_user_message("Hello, GPT! This is a test prompt to check that you're working!", [])
    messages = add_system_message("You are a very kind LLM", messages)
    response = chat("gpt-4o-mini", messages)
    print(response)
