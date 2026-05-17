from app.llm.gemini_client import ask_gemini

response = ask_gemini(
    "Explain EBITDA in simple terms."
)

print(response)