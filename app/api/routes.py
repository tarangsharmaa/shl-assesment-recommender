from fastapi import APIRouter

from app.models.chat_models import ChatRequest, ChatResponse

from app.core.analyzer import Analyzer
from app.core.retriever import Retriever
from app.core.recommendation_engine import RecommendationEngine
from app.core.conversation_manager import ConversationManager


router = APIRouter()

conversation = ConversationManager()
analyzer = Analyzer()
retriever = Retriever()
recommendation_engine = RecommendationEngine()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # Save user message
    conversation.add_message(
        "User",
        request.query
    )

    # Analyze user query
    decision = analyzer.analyze(request.query)

    if decision == "clarification":

        return ChatResponse(
            status="clarification",
            response="Could you please provide more details about the role or skills you want to assess?"
        )

    # Retrieve relevant assessments
    retrieved_documents = retriever.search(request.query)

    if not retrieved_documents:

        return ChatResponse(
            status="not_found",
            response="I couldn't find any suitable SHL assessments."
        )

    # Generate recommendation
    response = recommendation_engine.recommend(
        query=request.query,
        retrieved_documents=retrieved_documents,
        conversation_context=conversation.get_context()
    )
    
    assessment_names = [
        document.metadata["name"]
        for document, _ in retrieved_documents
    ]
    
    response = recommendation_engine.recommend(
        query=request.query,
        retrieved_documents=retrieved_documents,
        conversation_context=conversation.get_context()
    )

    # Save assistant response
    conversation.add_recommendations(
        assessment_names
    )

    return ChatResponse(
        status="success",
        response=response
    )