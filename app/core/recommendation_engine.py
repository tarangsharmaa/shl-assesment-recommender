from app.core.gemini_client import GeminiClient
from langchain_core.prompts import ChatPromptTemplate


class RecommendationEngine:

    def __init__(self):
        self.llm = GeminiClient()

        self.prompt = ChatPromptTemplate.from_template("""
You are an SHL Assessment Recommendation Assistant.

Conversation History:
{conversation_history}

Current User Query:
{query}

Below are the most relevant SHL assessments retrieved from the catalog.

{context}

Instructions:

1. Recommend the top 3 assessments from the retrieved assessments above.
2. Recommend ONLY from the retrieved assessments.
3. Do NOT invent assessment names.
4. Rank them from most suitable to least suitable.
5. Explain in 2-3 lines why each assessment is appropriate.
6. Include the assessment link for each recommendation.
7. If none of the retrieved assessments are suitable, clearly say so.

Format:

1. Assessment Name
Reason:
Assessment Link:

2. Assessment Name
Reason:
Assessment Link:

3. Assessment Name
Reason:
Assessment Link:
""")

    def recommend(self, query, retrieved_documents, conversation_context):

        contexts = []

        for document, _ in retrieved_documents:

            contexts.append(
                f"""
{document.page_content}

Assessment Link:
{document.metadata["link"]}

----------------------------------------
"""
            )

        context = "\n".join(contexts)

        prompt = self.prompt.format(
            conversation_history=conversation_context,
            query=query,
            context=context
        )

        response = self.llm.generate_response(prompt)

        return response