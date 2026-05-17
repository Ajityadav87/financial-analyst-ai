from app.exporters.excel_exporter import (
    generate_excel_report
)

sample_data = [
    {
        "Quarter": "Q1",
        "Revenue Growth": "8%"
    },
    {
        "Quarter": "Q2",
        "Revenue Growth": "10%"
    }
]

generate_excel_report(
    sample_data,
    "financial_data.xlsx"
)