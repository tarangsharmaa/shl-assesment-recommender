class ConversationManager:

    def __init__(self):
        self.history = []
        self.last_recommendations=[]
        
    def set_last_recommendations(self, recommendations):
        self.last_recommendations = recommendations

    def get_last_recommendations(self):
        return self.last_recommendations

    def add_message(self, role, message):
        
        self.history.append({
            "role": role,
            "message": message
        })
        
    def add_recommendations(self, assessments):

        summary = "Recommended: "
        summary += ", ".join(assessments)
        self.history.append({
            "role": "Assistant",
            "message": summary
    })
        self.set_last_recommendations(assessments)

    def get_history(self):
        return self.history

    def get_context(self):

        context = ""

        for chat in self.history:
            context += f"{chat['role']}: {chat['message']}\n"

        return context

    def clear(self):
        self.history = []
        self.last_recommendations=[]