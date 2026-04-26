import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class GeminiProvider:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate_response(self, prompt: str):
        response = self.model.generate_content(prompt)
        return response.text