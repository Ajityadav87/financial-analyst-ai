from app.rag.chunker import chunk_text

sample_text = """
Infosys revenue increased strongly in Q2.
Operating margin improved significantly.
Net profit also showed healthy growth.
""" * 100

chunks = chunk_text(sample_text)

print("Total Chunks:", len(chunks))

print("\nFirst Chunk:\n")

print(chunks[0])