from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import letter


def generate_pdf_report(
    text,
    output_path
):

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        "Financial Analysis Report",
        styles["Title"]
    )

    story.append(title)

    story.append(
        Spacer(1, 20)
    )

    body = Paragraph(
        text.replace("\n", "<br/>"),
        styles["BodyText"]
    )

    story.append(body)

    doc.build(story)

    print(
        f"\nPDF saved at: {output_path}"
    )