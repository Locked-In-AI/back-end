import textwrap
import os

import google.generativeai as genai

INITIAL_PROMPT = """
"""

genai.configure(api_key=os.getenv("GEMINAI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')


def generatePrompt(description: str) -> str:
    pass


def getOptimizedDescription(prompt: str) -> str:
    pass
    # response = model.generate_content("What is the meaning of life?")
