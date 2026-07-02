from app.core.retriever import Retriever

retriever = Retriever()

results = retriever.search(
    "Java Backend Developer",
    k=5
)

print("=" * 60)

for document, score in results:

    print(document.metadata["name"])
    print("Score:", score)
    print(document.metadata["link"])
    print("-" * 60)