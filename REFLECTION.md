# REFLECTION

## 1. What makes this chatbot feel intelligent rather than just doing keyword search? What did you specifically do to get there?

This chatbot uses Retrieval-Augmented Generation (RAG) with semantic embeddings instead of traditional keyword search.

The system converts document chunks into vector embeddings using Sentence Transformers (`all-MiniLM-L6-v2`) and stores them inside ChromaDB. When a user asks a question, the system retrieves semantically similar chunks rather than matching exact keywords.

This allows the chatbot to:
- understand contextual meaning
- answer questions across multiple financial documents
- handle paraphrased questions
- support follow-up conversations

I also added conversational memory so the chatbot can understand references to earlier questions such as:
- "What about Q2?"
- "Compare both quarters"

To improve financial reasoning quality, I designed a structured prompt template that:
- grounds Gemini responses in retrieved context
- prevents hallucination
- encourages analytical answers
- includes document citations

The chatbot also intelligently routes outputs into:
- normal chat responses
- downloadable PDF reports
- Excel spreadsheets

depending on the type of user query.

---

## 2. Where does the system still fall short? What would a real analyst notice that the system gets wrong or misses?

Although the chatbot performs well for document-based financial analysis, it still has limitations.

A real financial analyst would notice that:
- the system does not deeply reason about macroeconomic context
- trend analysis is still relatively shallow
- financial ratios are not explicitly calculated
- the chatbot depends heavily on retrieved chunks
- table extraction from PDFs is imperfect
- numerical consistency checks are limited

The chatbot can also occasionally:
- retrieve partially relevant chunks
- miss subtle accounting nuances
- produce generic summaries for highly detailed financial questions

Another limitation is that conversational memory is session-based and not persistent across users or sessions.

Additionally, the current implementation uses free-tier Gemini API limits, which can occasionally cause temporary rate-limit issues.

If I had more time, I would improve:
- structured financial metric extraction
- financial ratio calculations
- advanced table parsing
- better long-document retrieval
- persistent memory
- real-time stock market integrations

---

## 3. Which AI tools did you use to build this, and what did you have to fix or override yourself?

I used several AI and open-source tools while building the system.

Main technologies used:
- Gemini API for reasoning and response generation
- Sentence Transformers for semantic embeddings
- ChromaDB as the vector database
- Streamlit for frontend UI
- PyMuPDF for PDF parsing
- Pandas for Excel and CSV processing
- ReportLab for PDF generation

During development, I initially attempted to use Gemini embeddings directly. However, I encountered API compatibility and quota issues with the embedding models.

To improve stability and retrieval quality, I replaced Gemini embeddings with local Sentence Transformer embeddings (`all-MiniLM-L6-v2`).

I also manually implemented:
- conversational memory handling
- retrieval confidence scoring
- intelligent output routing
- PDF and Excel export logic
- citation formatting
- Streamlit session history
- Gemini retry handling for rate limits

One major engineering challenge was balancing:
- retrieval quality
- response grounding
- API limits
- frontend responsiveness

Overall, the project helped me better understand:
- RAG system design
- semantic retrieval
- prompt engineering
- conversational AI architecture
- production-level AI application workflows
