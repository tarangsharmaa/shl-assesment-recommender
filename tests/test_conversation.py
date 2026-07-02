from app.core.conversation_manager import ConversationManager

conversation = ConversationManager()

conversation.add_message(
    "User",
    "Need Java assessments."
)

conversation.add_message(
    "Assistant",
    "Recommended Java Advanced."
)

conversation.add_message(
    "User",
    "Only for freshers."
)

print(conversation.get_context())