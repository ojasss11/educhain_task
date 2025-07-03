"""
generate_detailed_responses.py

This script tests the EduChain MCP server endpoints by making HTTP requests,
saving the requests and responses to a text file for documentation.
"""

import requests
import json
import os

# Base URL of the running FastAPI server
BASE_URL = "http://127.0.0.1:8000"

# Output file to store detailed test requests and responses
OUTPUT_FILE = "Detailed_Responses.txt"


def write_output(line: str) -> None:
    """
    Append a line of text to the output file.

    Args:
        line (str): The line to write.
    """
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n\n")


def reset_output_file() -> None:
    """
    Remove the previous output file if it exists.
    """
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    print(f"Previous {OUTPUT_FILE} removed.\n")


def test_generate_quiz(topic: str, num_questions: int) -> None:
    """
    Test the /tools/quiz endpoint.

    Args:
        topic (str): The topic for the quiz.
        num_questions (int): Number of quiz questions.
    """
    payload = {"topic": topic, "num_questions": num_questions}
    write_output(f"==> TEST: Generate Quiz\nTopic: {topic} | Num: {num_questions}")
    try:
        res = requests.post(f"{BASE_URL}/tools/quiz", json=payload)
        res.raise_for_status()
        result = res.json()
        write_output(f"POST {BASE_URL}/tools/quiz\nPayload:\n{json.dumps(payload, indent=2)}")
        write_output(f"Response:\n{json.dumps(result, indent=2)}")
        print(f"Quiz for '{topic}' done.")
    except Exception as e:
        write_output(f"Error: {e}")
        print(f"Error: {e}")


def test_generate_flashcards(topic: str, num_cards: int) -> None:
    """
    Test the /tools/flashcards endpoint.

    Args:
        topic (str): The topic for the flashcards.
        num_cards (int): Number of flashcards.
    """
    payload = {"topic": topic, "num_cards": num_cards}
    write_output(f"==> TEST: Generate Flashcards\nTopic: {topic} | Num: {num_cards}")
    try:
        res = requests.post(f"{BASE_URL}/tools/flashcards", json=payload)
        res.raise_for_status()
        result = res.json()
        write_output(f"POST {BASE_URL}/tools/flashcards\nPayload:\n{json.dumps(payload, indent=2)}")
        write_output(f"Response:\n{json.dumps(result, indent=2)}")
        print(f"Flashcards for '{topic}' done.")
    except Exception as e:
        write_output(f"Error: {e}")
        print(f"Error: {e}")


def test_study_plan(topic: str) -> None:
    """
    Test the /tools/study_plan endpoint.

    Args:
        topic (str): The topic for the study plan.
    """
    write_output(f"==> TEST: Generate Study Plan\nTopic: {topic}")
    try:
        res = requests.get(f"{BASE_URL}/tools/study_plan", params={"topic": topic})
        res.raise_for_status()
        result = res.json()
        write_output(f"GET {BASE_URL}/tools/study_plan?topic={topic}")
        write_output(f"Response:\n{json.dumps(result, indent=2)}")
        print(f"Study plan for '{topic}' done.")
    except Exception as e:
        write_output(f"Error: {e}")
        print(f"Error: {e}")


def test_generate_worksheet(topic: str) -> None:
    """
    Test the /tools/worksheet endpoint.

    Args:
        topic (str): The topic for the worksheet.
    """
    write_output(f"==> TEST: Generate Worksheet\nTopic: {topic}")
    try:
        res = requests.get(f"{BASE_URL}/tools/worksheet", params={"topic": topic})
        res.raise_for_status()
        result = res.json()
        write_output(f"GET {BASE_URL}/tools/worksheet?topic={topic}")
        write_output(f"Response:\n{json.dumps(result, indent=2)}")
        print(f"Worksheet for '{topic}' done.")
    except Exception as e:
        write_output(f"Error: {e}")
        print(f"Error: {e}")


def test_generate_vocabulary(text: str) -> None:
    """
    Test the /tools/vocabulary endpoint.

    Args:
        text (str): The text to generate vocabulary from.
    """
    write_output(f"==> TEST: Generate Vocabulary List\nText: {text}")
    try:
        res = requests.get(f"{BASE_URL}/tools/vocabulary", params={"text": text})
        res.raise_for_status()
        result = res.json()
        write_output(f"GET {BASE_URL}/tools/vocabulary?text={text}")
        write_output(f"Response:\n{json.dumps(result, indent=2)}")
        print(f"Vocabulary list for '{text[:20]}...' done.")
    except Exception as e:
        write_output(f"Error: {e}")
        print(f"Error: {e}")


def test_generate_projects(topic: str) -> None:
    """
    Test the /tools/projects endpoint.

    Args:
        topic (str): The topic for project ideas.
    """
    write_output(f"==> TEST: Generate Projects\nTopic: {topic}")
    try:
        res = requests.get(f"{BASE_URL}/tools/projects", params={"topic": topic})
        res.raise_for_status()
        result = res.json()
        write_output(f"GET {BASE_URL}/tools/projects?topic={topic}")
        write_output(f"Response:\n{json.dumps(result, indent=2)}")
        print(f"Projects for '{topic}' done.")
    except Exception as e:
        write_output(f"Error: {e}")
        print(f"Error: {e}")


def test_generate_assignment(topic: str) -> None:
    """
    Test the /tools/assignment endpoint.

    Args:
        topic (str): The topic for the assignment.
    """
    write_output(f"==> TEST: Generate Assignment\nTopic: {topic}")
    try:
        res = requests.get(f"{BASE_URL}/tools/assignment", params={"topic": topic})
        res.raise_for_status()
        result = res.json()
        write_output(f"GET {BASE_URL}/tools/assignment?topic={topic}")
        write_output(f"Response:\n{json.dumps(result, indent=2)}")
        print(f"Assignment for '{topic}' done.")
    except Exception as e:
        write_output(f"Error: {e}")
        print(f"Error: {e}")


def test_generate_exam(topic: str) -> None:
    """
    Test the /tools/exam endpoint.

    Args:
        topic (str): The topic for the exam.
    """
    write_output(f"==> TEST: Generate Exam\nTopic: {topic}")
    try:
        res = requests.get(f"{BASE_URL}/tools/exam", params={"topic": topic})
        res.raise_for_status()
        result = res.json()
        write_output(f"GET {BASE_URL}/tools/exam?topic={topic}")
        write_output(f"Response:\n{json.dumps(result, indent=2)}")
        print(f"Exam for '{topic}' done.")
    except Exception as e:
        write_output(f"Error: {e}")
        print(f"Error: {e}")


def run_tests() -> None:
    """
    Run all test cases and save their results to the output file.
    """
    reset_output_file()
    write_output("# EduChain MCP - Detailed Test Runs\n")

    test_generate_quiz("Data Structures", 4)
    test_study_plan("Chemistry")
    test_generate_flashcards("Trigonometry", 2)
    test_generate_quiz("World History", 3)
    test_generate_flashcards("Computer Networks", 5)

    test_generate_worksheet("Physics")
    test_generate_vocabulary("Photosynthesis is the process by which plants make food using sunlight.")
    test_generate_projects("AI")
    test_generate_assignment("Climate Change")
    test_generate_exam("Calculus")

    print(f"\nAll tests completed. Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    run_tests()
