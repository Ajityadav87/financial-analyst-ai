from app.exporters.pdf_exporter import (
    generate_pdf_report
)

sample_text = """
Infosys showed strong Q1 growth.

Revenue increased significantly.

Margins improved due to operational efficiency.
"""

generate_pdf_report(
    sample_text,
    "sample_report.pdf"
)