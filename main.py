from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from my_educhain_utils import CustomEduChainGenerator

app = FastAPI(title="Custom EduChain MCP")
generator = CustomEduChainGenerator()

class QuizRequest(BaseModel):
    """
    Request model for generating a quiz.

    Attributes:
        topic (str): The topic to generate quiz questions for.
        num_questions (int): Number of questions to generate (default is 5).
    """
    topic: str
    num_questions: int = 5

class SummaryRequest(BaseModel):
    """
    Request model for generating a summary.

    Attributes:
        text (str): The text to summarize.
    """
    text: str

class FlashcardsRequest(BaseModel):
    """
    Request model for generating flashcards.

    Attributes:
        topic (str): The topic to generate flashcards for.
        num_cards (int): Number of flashcards to generate (default is 5).
    """
    topic: str
    num_cards: int = 5

@app.get("/")
async def root():
    """
    Redirect to the API docs.
    """
    return RedirectResponse(url="/docs")

@app.get("/.well-known/mcp/tools")
async def get_tools():
    """
    Return available MCP tools.
    """
    return {
        "tools": [
            {"name": "quiz", "description": "Generate a quiz on a specific topic"},
            {"name": "summary", "description": "Generate a summary of text"},
            {"name": "flashcards", "description": "Generate flashcards for studying"},
            {"name": "study_plan", "description": "Generate a study plan"},
            {"name": "worksheet", "description": "Generate a worksheet"},
            {"name": "vocabulary", "description": "Generate a vocabulary list"},
            {"name": "projects", "description": "Generate project ideas"},
            {"name": "assignment", "description": "Generate an assignment"},
            {"name": "exam", "description": "Generate an exam"}
        ]
    }

@app.get("/.well-known/mcp/resources")
async def get_resources():
    """
    Return available MCP resources.
    """
    return {"resources": []}

@app.post("/tools/quiz")
async def create_quiz(request: QuizRequest):
    """
    Generate a quiz using the given topic and number of questions.
    """
    return generator.generate_quiz(request.topic, request.num_questions)

@app.post("/tools/summary")
async def create_summary(request: SummaryRequest):
    """
    Generate a summary of the provided text.
    """
    return generator.generate_summary(request.text)

@app.post("/tools/flashcards")
async def create_flashcards(request: FlashcardsRequest):
    """
    Generate flashcards for the given topic.
    """
    return generator.generate_flashcards(request.topic, request.num_cards)

@app.get("/tools/study_plan")
async def create_study_plan(topic: str):
    """
    Generate a study plan for the given topic.
    """
    return generator.generate_study_plan(topic)

@app.get("/tools/worksheet")
async def create_worksheet(topic: str):
    """
    Generate a worksheet for the given topic.
    """
    return generator.generate_worksheet(topic)

@app.get("/tools/vocabulary")
async def create_vocabulary(text: str):
    """
    Generate a vocabulary list from the given text.
    """
    return generator.generate_vocabulary_list(text)

@app.get("/tools/projects")
async def create_projects(topic: str):
    """
    Generate project ideas for the given topic.
    """
    return generator.generate_projects(topic)

@app.get("/tools/assignment")
async def create_assignment(topic: str):
    """
    Generate an assignment for the given topic.
    """
    return generator.generate_assignment(topic)

@app.get("/tools/exam")
async def create_exam(topic: str):
    """
    Generate an exam for the given topic.
    """
    return generator.generate_exam(topic)
