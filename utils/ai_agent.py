import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(question, dataframe):

    prompt = f"""
You are an AI Data Analyst.

Dataset:
{dataframe.to_string()}

Question:
{question}

Instructions:
- Return ONLY the final answer.
- Do not explain your reasoning.
- Do not show calculations.
- Keep the answer within 2-3 lines.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content