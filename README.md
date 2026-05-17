# Financial Analyst AI Assistant

## Overview

Financial Analyst AI Assistant is an AI-powered financial document analysis system built using:

- Gemini AI
- RAG (Retrieval-Augmented Generation)
- ChromaDB
- Sentence Transformers
- Streamlit

The system can analyze:

- Annual reports
- Quarterly earnings reports
- Investor spreadsheets
- Stock market CSV data

The assistant provides:
- intelligent financial analysis
- semantic document search
- conversational memory
- PDF report generation
- Excel spreadsheet exports

---

# Features

## AI-Powered Financial Analysis
- Uses Gemini AI for intelligent reasoning
- Answers financial questions using uploaded documents

## Semantic Search
- Uses vector embeddings for semantic retrieval
- Retrieves contextually relevant financial information

## Conversational Memory
- Handles follow-up questions
- Maintains chat history context

## PDF Report Generation
- Automatically generates downloadable PDF reports

## Excel Export Generation
- Creates downloadable Excel spreadsheets

## Intelligent Output Routing
- Automatically decides:
  - chat response
  - PDF output
  - Excel output

## Source Citations
- Shows document sources used for answers

## Streamlit Frontend
- Interactive web UI
- User-friendly financial assistant interface

---

# Tech Stack

| Component | Technology |
|---|---|
| LLM | Gemini 2.5 Flash |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Frontend | Streamlit |
| Backend | Python |
| PDF Parsing | PyMuPDF |
| Excel Processing | Pandas |
| PDF Export | ReportLab |

---

# Project Architecture

## 1. Document Ingestion
- Reads PDFs
- Reads Excel files
- Reads CSV files

## 2. Text Chunking
- Splits large documents into chunks

## 3. Embedding Generation
- Converts chunks into vector embeddings

## 4. Vector Storage
- Stores embeddings inside ChromaDB

## 5. Semantic Retrieval
- Retrieves relevant chunks based on user query

## 6. Gemini Reasoning
- Gemini generates financial analysis using retrieved context

## 7. Output Generation
- Generates:
  - chatbot responses
  - PDF reports
  - Excel spreadsheets

---

# Folder Structure

```text
financial-assistant/
│
├── app/
├── frontend/
├── tests/
├── assets/
├── README.md
├── REFLECTION.md
└── requirements.txt
```

---

# Setup Instructions

## Step 1 — Create Virtual Environment

```bash
python -m venv venv
```

## Step 2 — Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4 — Add Gemini API Key

Create `.env`

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Step 5 — Run Document Ingestion

```bash
python -m app.rag.ingest
```

---

## Step 6 — Start Streamlit App

```bash
streamlit run frontend/streamlit_app.py
```

---

# Sample Questions

## Chat Queries

- What was Infosys Q1 revenue growth?
- Summarize quarterly performance
- Compare operating margins across quarters

## PDF Queries

- Generate a financial analysis report for Q1

## Excel Queries

- Create a quarterly comparison spreadsheet

---

# Screenshots

## Main UI

(Add screenshot here)

## PDF Generation

(Add screenshot here)

## Excel Export

(Add screenshot here)

---

# Future Improvements

- Better financial forecasting
- Real-time stock APIs
- Advanced table extraction
- Multi-company analysis
- Cloud deployment

---

# Author
Ajit Yadav