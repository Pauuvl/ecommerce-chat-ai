import google.generativeai as genai
import os


class GeminiProvider:

    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    def generate(self, prompt: str):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text