import fitz
import os

from app.rag.chunker import chunk_text
from app.rag.embeddings import create_embedding
from app.rag.vectorstore import collection


def extract_pdf_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:

        text += page.get_text()

    return text


def process_pdfs():

    folder_path = "app/data/raw"

    document_id = 0

    for file_name in os.listdir(folder_path):

        if file_name.endswith(".pdf"):

            print(f"\nProcessing: {file_name}")

            full_path = os.path.join(
                folder_path,
                file_name
            )

            extracted_text = extract_pdf_text(
                full_path
            )

            chunks = chunk_text(
                extracted_text
            )

            for chunk in chunks:

                embedding = create_embedding(
                    chunk
                )

                collection.add(
                    documents=[chunk],
                    embeddings=[embedding],
                    ids=[str(document_id)],
                    metadatas=[
                        {
                            "source": file_name
                        }
                    ]
                )

                document_id += 1

    print("\nAll PDFs processed successfully.")


if __name__ == "__main__":

    process_pdfs()