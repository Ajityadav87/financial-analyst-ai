from app.rag.retriever import retrieve_documents

from app.llm.gemini_client import ask_gemini

from app.llm.prompts import (
    FINANCIAL_ANALYST_PROMPT
)
from app.memory.memory_manager import (
    add_to_memory,
    get_memory
)
from app.llm.router import (
    detect_output_type
)

from app.exporters.pdf_exporter import (
    generate_pdf_report
)

from app.exporters.excel_exporter import (
    generate_excel_report
)
def generate_answer(question):

    results = retrieve_documents(question)

    documents = results["documents"][0]

    metadatas = results["metadatas"][0]

    context = ""

    sources = []

    for doc, meta in zip(
        documents,
        metadatas
    ):

        context += doc + "\n\n"

        source = meta["source"]

        if source not in sources:

            sources.append(source)

    history = get_memory()

    prompt = FINANCIAL_ANALYST_PROMPT.format(
    history=history,
    context=context,
    question=question
)

    answer = ask_gemini(prompt)

    citation_text = "\n\nSources:\n"

    for source in sources:

        citation_text += f"- {source}\n"

    final_response = (
    answer + citation_text
)

    add_to_memory(
    question,
    final_response
)

    return final_response

if __name__ == "__main__":

    while True:

        question = input("\nAsk Question: ")

        if question.lower() == "exit":

            break

        response = generate_answer(
            question
        )

        output_type = detect_output_type(
            question
        )

        if output_type == "pdf":

            generate_pdf_report(
                response,
                "financial_report.pdf"
            )

            print(
                "\nPDF report generated."
            )

        elif output_type == "excel":

            sample_data = [
                {
                    "Response": response
                }
            ]

            generate_excel_report(
                sample_data,
                "financial_data.xlsx"
            )

            print(
                "\nExcel report generated."
            )

        else:

            print("\n")
            print(response)