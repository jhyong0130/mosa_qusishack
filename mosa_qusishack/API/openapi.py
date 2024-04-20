import os
import openai
from openai import OpenAI
import argparse
import ast
from dotenv import load_dotenv

load_dotenv()

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
    client = OpenAI()
    #Generate response for ideas
    prompt = f"You will act as a advisor for students who wish to become a software enginner.\
        Suggest three portfolio projects based on level of difficulty, role and programming language.\
            Only provide project name an array like ['project1','project2','project3']."
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview", 
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": f"Level of difficulty:{level_input},\
                          role: {role_input},\
                          programming language: {language_input}"
            }],
        temperature=1,
        max_tokens=512,
        )
        
    #change output to list
    portfolio_idea: str = response.choices[0].message.content
    portfolio_idea = ast.literal_eval(portfolio_idea)
    # portfolio_idea_array = re.split(",|\n|;", portfolio_idea)
    # portfolio_idea_array = [k.strip() for k in portfolio_idea_array]
    # portfolio_idea_array = [k for k in portfolio_idea_array if len(k) > 0]
    
    return portfolio_idea

def generate_link(language_input :str) -> str :
    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()
    #Generate response
    link_prompt = f"Suggest three free online resources to learn {language_input}(link only). Provide response in an array like [link1, link2]."
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview", 
        messages=[
            {
                "role": "user",
                "content": link_prompt
            }],
            temperature=1,
            max_tokens=512,                            
            )
    
    
    #Change output to list
    tutorial_link: str = response.choices[0].message.content
    tutorial_link = ast.literal_eval(tutorial_link)
    # tutorial_link_array = re.split(",|\n|;", tutorial_link)
    # tutorial_link_array = [k.lower().strip() for k in tutorial_link_array]
    # tutorial_link_array = [k for k in tutorial_link_array if len(k) > 0]

    return tutorial_link

def generate_jobscope_and_skills(role_input: str):
    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()
    job_prompt = f"Job scope of {role_input} engineer and skills required to be a{role_input} engineer in 3 sentences"
    
    response = client.chat.completions.create(
    model="gpt-4-turbo-preview", 
    messages=[
        {
            "role": "user",
            "content": job_prompt
        }],
        temperature=1,
        max_tokens=512,                            
        )
     #Change output to list
    jobscope_and_skills: str = response.choices[0].message.content
    jobscope_and_skills = jobscope_and_skills.strip()
    
    return jobscope_and_skills

if __name__ == "__main__" :
    main()
