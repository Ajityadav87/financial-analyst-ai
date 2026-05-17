from app.rag.retriever import retrieve_documents

results = retrieve_documents(
    "What was Infosys revenue growth?"
)

documents = results["documents"][0]

for i, doc in enumerate(documents):

    print(f"\nResult {i+1}:\n")

    print(doc[:1000])