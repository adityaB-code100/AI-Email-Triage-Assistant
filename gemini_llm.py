import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

def call_llm(prompt: str) -> str:
    if not prompt or not prompt.strip():
        return "Unable to generate response (empty input)."

    response = model.generate_content(prompt)
    return response.text.strip()
