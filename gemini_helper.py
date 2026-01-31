import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_gemini_answer(query, language):
    prompt = f"""
You are an agriculture expert helping Indian farmers.
Answer in {language}.
Use simple bullet points.

Question: {query}
"""

    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return chat.choices[0].message.content
