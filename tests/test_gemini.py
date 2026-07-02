from app.core.gemini_client import GeminiClient

llm = GeminiClient()

response = llm.generate_response(
    "Reply with only: Hello World"
)

print(response)