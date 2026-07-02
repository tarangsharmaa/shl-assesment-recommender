from app.core.catalog_loader import CatalogLoader
from app.core.document_builder import DocumentBuilder
from app.core.embeddings import Embeddingmodel
from app.core.vector_store import VectorStore
from app.core.retriever import Retriever

print("Loading Catalog..")
loader = CatalogLoader("data/shl_product_catalog.json")
catalog = loader.load_catalog()

print("Building Documents..")
builder = DocumentBuilder()
documents = builder.build_documents(catalog)

print("Loading Embedding Model...")
embedding = Embeddingmodel()

print("Creating Vector Store...")
vector_store = VectorStore()

db = vector_store.create_vector_store(
    documents,
    embedding.get_embeddings()
)

print("Saving Vector Store...")
vector_store.save_vector_store(db)

print()
print("Vector Database Created Successfully!")
print(f"Indexed {len(documents)} assessments.")