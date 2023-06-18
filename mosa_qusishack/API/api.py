from fastapi import FastAPI, HTTPException
from openapi import generate_idea, generate_link
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate_project_ideas")
async def get_project_ideas(level_input: str, role_input: str):    
    ideas_list = generate_idea(level_input, role_input)
    return {"portfolio_ideas": ideas_list}


@app.get("/generate_tutorial_links")
async def get_link(language_input: str):
    links_list = generate_link(language_input)
    return {"tutorial_links": links_list}

