import os
from dotenv import load_dotenv
load_dotenv()

import openai
import argparse
import re

def main():

    #get input from user
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    user_input_list = user_input.split()
    level_input = user_input_list[0]
    role_input = user_input_list[1]
    language_input = user_input_list[2]
    
    # programming_language = ["Python","PHP","JavaScript",""]
    # level = ["Easy","Intermediate","Difficult"]
    # roles = ["Backend","Frontend","Fullstack","ML Engineer","Data Engineer","Security Engineer","DevOps Engineer"]
    
    print(f'User input: {user_input}')
    project_ideas = [generate_project_ideas(level_input, role_input) for _ in range(0,3)]
    tutorial_links = [generate_tutorial_link(idea, language_input) for idea in project_ideas]
    print(f"Ideas:{project_ideas}")
    print(f"Useful Links:{tutorial_links}")

def generate_project_ideas(level_input: str, role_input: str) -> str :
    
    openai.api_key = os.environ.get("API_Key")
 
    prompt = f"Suggest one {level_input} portfolio project to be a {role_input} engineer(only project name)"
    #Generate response
    response = openai.Completion.create(model="text-davinci-003", 
                                        prompt=prompt, 
                                        temperature=1,
                                        max_tokens=256,
                                        top_p=1,
                                        best_of=3,
                                        frequency_penalty=0,
                                        presence_penalty=0)
    
    portfolio_idea: str = response["choices"][0]["text"]
    portfolio_idea = portfolio_idea.strip()
    portfolio_idea = portfolio_idea.replace("1.","")
    portfolio_idea = portfolio_idea.lower()
    
    return portfolio_idea

def generate_tutorial_link(project_example: str, language_input: str) -> str :
    
    openai.api_key = os.environ.get("API_Key")
    
    #Generate response
    enriched_prompt = f"Suggest one best resource to learn how to build a {project_example} using {language_input}(link only)"
    print(enriched_prompt)
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=enriched_prompt,
                                        temperature=1,
                                        max_tokens=256,
                                        top_p=1,
                                        frequency_penalty=0,
                                        presence_penalty=0)

    tutorial_link: str = response["choices"][0]["text"]
    tutorial_link = tutorial_link.strip()

    return tutorial_link

if __name__ == "__main__" :
    main()
