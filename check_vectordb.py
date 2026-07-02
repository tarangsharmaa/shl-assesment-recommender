from app.core.embeddings import Embeddingmodel
from app.core.vector_store import VectorStore

embedding = Embeddingmodel()

vector_store = VectorStore()

db = vector_store.load(
    embedding.get_embeddings()
)

print(db.index.ntotal)