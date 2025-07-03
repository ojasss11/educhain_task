# EduChain MCP (Model Context Protocol)

A **FastAPI-based MCP server** that provides educational content generation capabilities using a **mock EduChain Generator**.  
This project demonstrates how to expose educational tools through a simple API — no real OpenAI key needed.

---

## ✅ Features

- Generate quizzes and assessments (mock)
- Create text summaries (mock)
- Generate flashcards for study (mock)
- Create customized study plans (mock)
- Generate worksheets (mock)
- Create vocabulary lists (mock)
- Generate project ideas (mock)
- Generate assignments (mock)
- Generate exams (mock)

---

## ✅ Prerequisites

- Python 3.8+
- `pip` (Python package installer)

---

## ✅ Installation

1️⃣ Clone this repository (or copy the files)

2️⃣ (Optional) If you have an educhain local module, install it in editable mode
pip install -e educhain

3️⃣ Install required dependencies
pip install fastapi uvicorn[standard] python-dotenv

4️⃣ Set up your environment variables:

Create a .env file in the root folder
Add this line inside .env:
OPENAI_API_KEY=your-api-key-here

✅ Running the MCP Server
1️⃣ Start the FastAPI server:
uvicorn main:app --reload --host 127.0.0.1 --port 8000

2️⃣ Open your browser and visit:
http://127.0.0.1:8000/docs
Here you can test all endpoints using Swagger UI.

✅ Available Endpoints

| Method | Endpoint                     | Description                |
| ------ | ---------------------------- | -------------------------- |
| `GET`  | `/`                          | Redirect to API docs       |
| `GET`  | `/.well-known/mcp/tools`     | List all available tools   |
| `GET`  | `/.well-known/mcp/resources` | List all resources (empty) |
| `POST` | `/tools/quiz`                | Generate a quiz            |
| `POST` | `/tools/summary`             | Generate a summary         |
| `POST` | `/tools/flashcards`          | Generate flashcards        |
| `GET`  | `/tools/study_plan`          | Create a study plan        |
| `GET`  | `/tools/worksheet`           | Create a worksheet         |
| `GET`  | `/tools/vocabulary`          | Create a vocabulary list   |
| `GET`  | `/tools/projects`            | Generate project ideas     |
| `GET`  | `/tools/assignment`          | Generate an assignment     |
| `GET`  | `/tools/exam`                | Generate an exam           |

✅ How It Works

The server is defined in main.py — it exposes all the endpoints.

The mock logic is handled in my_educhain_utils.py — it returns fake data.

The .env and dotenv allow you to plug in an OpenAI API key later if needed.

The generate_detailed_responses.py script sends test requests to your MCP server and saves sample responses in Detailed_Responses.txt.
