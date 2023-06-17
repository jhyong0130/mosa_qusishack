import os
from dotenv import load_dotenv
load_dotenv()

import openai
import argparse
import re

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    
    print(f'User input: {user_input}')
    branding_snippet = generate_branding_snippet(user_input)
    branding_keyword = generate_keyword(user_input)
    print(branding_snippet)
    print(branding_keyword)

def generate_branding_snippet(user_input: str):
    
    openai.api_key = os.environ.get("API_Key")
 
    prompt = f"Generate upbeat branding snippet for {user_input}"

    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1.5, max_tokens=32)

    branding_text: str = response["choices"][0]["text"]
    
    branding_text = branding_text.strip()
    
    last_char =  branding_text[-1]
    if last_char not in {"!",".","?"}:
        branding_text += "..."

    return branding_text

def generate_keyword(user_input: str):
    
    openai.api_key = os.environ.get("API_Key")
 
    enriched_prompt = f"Generate related branding keywords for {user_input}:"

    response = openai.Completion.create(model="text-davinci-003", prompt=enriched_prompt, temperature=1.5, max_tokens=32)

    keywords_text: str = response["choices"][0]["text"]
    
    keywords_text = keywords_text.strip()

    return keywords_text

if __name__ == "__main__" :
    main()
