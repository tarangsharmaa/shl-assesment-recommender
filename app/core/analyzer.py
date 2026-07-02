class Analyzer:

    def __init__(self):

        self.keywords = [
            "developer",
            "engineer",
            "manager",
            "java",
            "python",
            "sales",
            "leadership",
            "aptitude",
            "coding",
            "assessment"
        ]

    def analyze(self, query):

        query = query.lower()

        if "compare" in query or "vs" in query:
            return "comparison"

        for keyword in self.keywords:

            if keyword in query:
                return "recommendation"

        return "clarification"