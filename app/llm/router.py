def detect_output_type(question):

    question = question.lower()

    pdf_keywords = [
        "report",
        "summary",
        "pdf",
        "financial analysis"
    ]

    excel_keywords = [
        "spreadsheet",
        "excel",
        "table",
        "comparison",
        "data sheet"
    ]

    for word in pdf_keywords:

        if word in question:

            return "pdf"

    for word in excel_keywords:

        if word in question:

            return "excel"

    return "chat"