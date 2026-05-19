import google.generativeai as genai
import os
import time

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def ask_gemini(prompt):

    retries = 3

    for attempt in range(retries):

        try:

            response = model.generate_content(
                prompt
            )

            return response.text

        except Exception as e:

            print(
                f"Retry {attempt+1} due to: {e}"
            )

            time.sleep(5)

    return (
        "Gemini API is temporarily busy. "
        "Please try again later."
    )