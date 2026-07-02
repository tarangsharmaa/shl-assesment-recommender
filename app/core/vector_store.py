from langchain_community.vectorstores import FAISS

class VectorStore:
    def create_vector_store(self, documents, embedding_model):

        vector_db = FAISS.from_documents(
            documents,
            embedding_model
        )
        return vector_db

    def save_vector_store(self, vector_db):
        vector_db.save_local("data/vector_db")
        
    def load(self, embeddings):

        return FAISS.load_local(
            "data/vector_db",
            embeddings,
            allow_dangerous_deserialization=True
        )