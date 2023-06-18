import os
import openai
import argparse
import re

def main():
    
    #get input from user
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    
    # programming_language = ["Python","PHP","JavaScript",""]
    # level = ["Easy","Intermediate","Difficult"]
    # roles = ["Backend","Frontend","Fullstack","ML Engineer","Data Engineer","Security Engineer","DevOps Engineer"]
    
    print(f'User input: {user_input}')

    ideas = generate_idea(user_input)
    tutorial_links = generate_link(user_input)
    print(f"Ideas:{ideas}")
    print(f"Useful Links:{tutorial_links}")

def generate_idea(level_input: str, role_input: str, language_input: str) -> str :
    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    #Generate response for ideas
    prompt = f"Suggest three {level_input} {language_input}portfolio projects to be a {role_input} engineer(only project name)"
    response = openai.Completion.create(model="text-davinci-003", 
                                        prompt=prompt, 
                                        temperature=1,
                                        max_tokens=256,
                                        best_of=3)
    
    #change output to list
    portfolio_idea: str = response["choices"][0]["text"]
    portfolio_idea = portfolio_idea.strip()
    portfolio_idea_array = re.split(",|\n|;", portfolio_idea)
    portfolio_idea_array = [k.lower().strip() for k in portfolio_idea_array]
    portfolio_idea_array = [k for k in portfolio_idea_array if len(k) > 0]
    
    return portfolio_idea_array

def generate_link(language_input :str) -> str :
    
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    
    #Generate response
    enriched_prompt = f"Suggest three free online course to learn {language_input}(link only)"
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=enriched_prompt,
                                        temperature=1,
                                        max_tokens=256,
                                        top_p=1,
                                        best_of=3,
                                        frequency_penalty=0,
                                        presence_penalty=0)
    
    #Change output to list
    tutorial_link: str = response["choices"][0]["text"]
    tutorial_link = tutorial_link.strip()
    tutorial_link_array = re.split(",|\n|;", tutorial_link)
    tutorial_link_array = [k.lower().strip() for k in tutorial_link_array]
    tutorial_link_array = [k for k in tutorial_link_array if len(k) > 0]

    return tutorial_link_array

def generate_jobscope_and_skills(role_input: str):
    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    prompt = f"Job scope of {role_input} and skillls required to be a{role_input} programmer in 3 sentences"
    
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0,
                                        max_tokens=256,
                                        top_p=1,
                                        best_of=3,
                                        frequency_penalty=0,
                                        presence_penalty=0)
     #Change output to list
    jobscope_and_skills: str = response["choices"][0]["text"]
    jobscope_and_skills = jobscope_and_skills.strip()
    
    return jobscope_and_skills

if __name__ == "__main__" :
    main()
