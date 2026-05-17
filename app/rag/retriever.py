from app.rag.vectorstore import collection
from app.rag.embeddings import create_embedding


def retrieve_documents(
    query,
    top_k=5
):

    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results