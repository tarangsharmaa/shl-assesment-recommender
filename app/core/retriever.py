from app.core.embeddings import Embeddingmodel
from app.core.vector_store import VectorStore


class Retriever:

    def __init__(self):

        embedding = Embeddingmodel()

        vector_store = VectorStore()

        self.db = vector_store.load(
            embedding.get_embeddings()
        )

    def search(self, query, k=5):

        results = self.db.similarity_search_with_score(
            query,
            k=k
        )

        return results