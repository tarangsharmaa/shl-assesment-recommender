from app.core.analyzer import Analyzer
from app.core.retriever import Retriever
from app.core.recommendation_engine import RecommendationEngine


def main():

    query = "Java Backend Developer"

    print("=" * 80)
    print("USER QUERY")
    print("=" * 80)
    print(query)

    # Step 1: Analyze the query
    analyzer = Analyzer()

    decision = analyzer.analyze(query)

    print("\nAnalyzer Decision:", decision)

    if decision != "recommendation":
        print("\nThe analyzer decided that this query should not go to the recommendation engine.")
        return

    # Step 2: Retrieve relevant assessments
    retriever = Retriever()

    retrieved_documents = retriever.search(query)

    print("\n" + "=" * 80)
    print("RETRIEVED ASSESSMENTS")
    print("=" * 80)

    for i, (document, score) in enumerate(retrieved_documents, start=1):

        print(f"\n{i}. {document.metadata['name']}")
        

    # Step 3: Generate recommendation
    recommendation_engine = RecommendationEngine()

    response = recommendation_engine.recommend(
        query,
        retrieved_documents
    )

    print("\n" + "=" * 80)
    print("FINAL RECOMMENDATION")
    print("=" * 80)
    print(response)


if __name__ == "__main__":
    main()