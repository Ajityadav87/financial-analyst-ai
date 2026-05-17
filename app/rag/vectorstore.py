import chromadb

client = chromadb.PersistentClient(
    path="app/data/chroma_db"
)

collection = client.get_or_create_collection(
    name="financial_documents"
)