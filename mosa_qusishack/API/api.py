from fastapi import FastAPI, HTTPException
from openapi import generate_project_ideas, generate_tutorial_link
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
MAX_INPUT_LENGTH = 32

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate_project_ideas")
async def generate_project_ideas(level_input: str, role_input: str):
    ideas_list = generate_project_ideas(level_input, role_input)
    return {"portfolio_ideas": ideas_list}


@app.get("/generate_tutorial_links")
async def generate_tutorial_link(project_example: str, language_input: str):
    tutorial_links_list = generate_tutorial_link(project_example, language_input)
    return {"tutorial_links": tutorial_links_list}

