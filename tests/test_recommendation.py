from app.core.retriever import Retriever
from app.core.recommendation_engine import RecommendationEngine

query = "I need an assessment for a Java Backend Developer."

# Retrieve relevant assessments
retriever = Retriever()
results = retriever.retrieve(query)

print("\nRetrieved Assessments:\n")

for doc, score in results:
    print(doc.metadata["name"])
    print("Score:", score)
    print("-" * 50)

# Generate recommendation
engine = RecommendationEngine()

response = engine.recommend(
    query,
    results
)

print("\n" + "=" * 80)
print("FINAL RESPONSE")
print("=" * 80)
print(response)