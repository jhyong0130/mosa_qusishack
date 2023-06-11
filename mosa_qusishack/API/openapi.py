import os
import openai
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    
    print(f'User input: {user_input}')
    generate_answer(user_input)

def generate_answer(user_input: str):
    
    openai.api_key = os.getenv("OPENAI_API_KEY")
 
    prompt = f"Generate upbeat branding snippet for {user_input}"

    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=32)

    print(response)
    answer = response["choices"][0]["text"]

if __name__ == "__main__" :
    main()
