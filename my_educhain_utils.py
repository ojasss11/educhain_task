"""
my_educhain_utils.py

This module defines the CustomEduChainGenerator class that mocks various
education-related content generation tools (quiz, summary, flashcards, etc.).
"""

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class CustomEduChainGenerator:
    """
    CustomEduChainGenerator is a mock implementation of an EduChain content generator.
    It provides methods to simulate quiz creation, summaries, flashcards,
    study plans, worksheets, vocabulary lists, project ideas, assignments, and exams.
    """

    def __init__(self):
        """
        Initialize the generator.
        Checks for an OPENAI_API_KEY in environment but always runs in mock mode.
        """
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("[INFO] No OPENAI_API_KEY set — using mock data only.")
        else:
            print("[INFO] Key found but MOCK mode is active.")

    def generate_quiz(self, topic: str, num_questions: int = 5) -> dict:
        """
        Generate a mock quiz for a given topic.

        Args:
            topic (str): The topic of the quiz.
            num_questions (int): Number of questions to generate.

        Returns:
            dict: Mock quiz data.
        """
        return {
            "quiz": [
                {"question": f"Sample question {i + 1} about {topic}"}
                for i in range(num_questions)
            ]
        }

    def generate_summary(self, text: str) -> dict:
        """
        Generate a mock summary for given text.

        Args:
            text (str): The text to summarize.

        Returns:
            dict: Mock summary.
        """
        return {
            "summary": f"This is a mock summary for: {text[:50]}..."
        }

    def generate_flashcards(self, topic: str, num_cards: int = 5) -> dict:
        """
        Generate mock flashcards for a given topic.

        Args:
            topic (str): The topic of the flashcards.
            num_cards (int): Number of flashcards.

        Returns:
            dict: Mock flashcards.
        """
        return {
            "flashcards": [
                {
                    "term": f"{topic} Term {i + 1}",
                    "definition": f"Definition for {topic} Term {i + 1}"
                }
                for i in range(num_cards)
            ]
        }

    def generate_study_plan(self, topic: str) -> dict:
        """
        Generate a mock study plan for a given topic.

        Args:
            topic (str): The topic for the study plan.

        Returns:
            dict: Mock study plan.
        """
        return {
            "study_plan": [
                f"Step {i + 1}: Study {topic} concept {i + 1}"
                for i in range(5)
            ]
        }

    def generate_worksheet(self, topic: str) -> dict:
        """
        Generate a mock worksheet for a given topic.

        Args:
            topic (str): The topic for the worksheet.

        Returns:
            dict: Mock worksheet.
        """
        return {
            "worksheet": [
                {"question": f"Worksheet question {i + 1} about {topic}"}
                for i in range(5)
            ]
        }

    def generate_vocabulary_list(self, text: str) -> dict:
        """
        Generate a mock vocabulary list from input text.

        Args:
            text (str): The input text to extract words from.

        Returns:
            dict: Mock vocabulary list.
        """
        words = text.split()[:5]
        return {
            "vocabulary": [
                {"word": w, "definition": f"Definition of {w}"}
                for w in words
            ]
        }

    def generate_projects(self, topic: str) -> dict:
        """
        Generate mock project ideas for a given topic.

        Args:
            topic (str): The topic for the projects.

        Returns:
            dict: Mock project ideas.
        """
        return {
            "projects": [
                f"Project Idea {i + 1} for {topic}"
                for i in range(3)
            ]
        }

    def generate_assignment(self, topic: str) -> dict:
        """
        Generate a mock assignment for a given topic.

        Args:
            topic (str): The topic for the assignment.

        Returns:
            dict: Mock assignment.
        """
        return {
            "assignment": f"Write an essay about {topic} covering key aspects."
        }

    def generate_exam(self, topic: str) -> dict:
        """
        Generate a mock exam for a given topic.

        Args:
            topic (str): The topic for the exam.

        Returns:
            dict: Mock exam.
        """
        return {
            "exam": [
                {"question": f"Exam question {i + 1} about {topic}"}
                for i in range(5)
            ]
        }
