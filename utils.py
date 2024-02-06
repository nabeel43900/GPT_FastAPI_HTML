# utils.py

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())  # read local .env file

# Create an OpenAI client
client = OpenAI()

def generate_description(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a personal assistant, skilled in technology."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content
