import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from app.main import generate_answer

from app.llm.router import (
    detect_output_type
)

from app.exporters.pdf_exporter import (
    generate_pdf_report
)

from app.exporters.excel_exporter import (
    generate_excel_report
)


st.set_page_config(
    page_title="Financial Analyst AI",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align: center;'>
    📊 Financial Analyst AI Assistant
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='text-align: center;'>
    Analyze annual reports, quarterly earnings,
    stock performance, and financial trends.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
if "history" not in st.session_state:

    st.session_state.history = []

question = st.text_area(
    "Ask your financial question:",
    height=120
)

if st.button("Analyze"):

    if question:

        with st.spinner(
            "Analyzing financial documents..."
        ):

            response = generate_answer(
                question
            )

            output_type = detect_output_type(
                question
            )

        st.success(
            "Analysis Complete"
        )

        st.subheader(
            "AI Financial Analysis"
        )

        st.write(response)
        st.session_state.history.append(
    {
        "question": question,
        "answer": response
    }
)

        # PDF Generation
        if output_type == "pdf":

            pdf_path = "financial_report.pdf"

            generate_pdf_report(
                response,
                pdf_path
            )

            with open(
                pdf_path,
                "rb"
            ) as pdf_file:

                st.download_button(
                    label="Download PDF Report",
                    data=pdf_file,
                    file_name="financial_report.pdf",
                    mime="application/pdf"
                )

        # Excel Generation
        elif output_type == "excel":

            excel_path = "financial_data.xlsx"

            sample_data = [
                
                {
                    "Quarter": "Q1",
                    "Revenue Trend": "Positive",
                    "Performance Summary": response[:200]
                },
                {
                    "Quarter": "Q2",
                    "Revenue Trend": "Stable",
                    "Performance Summary": response[:200]
                }
]
            

            generate_excel_report(
                sample_data,
                excel_path
            )

            with open(
                excel_path,
                "rb"
            ) as excel_file:

                st.download_button(
                    label="Download Excel Report",
                    data=excel_file,
                    file_name="financial_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

if st.session_state.history:

    st.subheader("Conversation History")

    for item in reversed(
        st.session_state.history
    ):

        st.markdown(
            f"### Question:\n{item['question']}"
        )

        st.markdown(
            f"### Answer:\n{item['answer']}"
        )

        st.markdown("---")