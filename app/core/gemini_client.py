import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

class GeminiClient:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

        self.model = "gemini-2.5-flash"

    def generate_response(self, prompt):

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text