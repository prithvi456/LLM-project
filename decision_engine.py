from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

# Access the API key
API_KEY = os.getenv("API_KEY")
client = Groq(api_key=API_KEY)

def evaluate_decision(query_info, retrieved_clauses):
    prompt = f"""
Query Info:
{query_info}

Relevant Clauses:
{retrieved_clauses}

Answer in this JSON format:
{{
  "decision": "Approved/Rejected",
  "amount": "Amount in INR if applicable",
  "justification": "Reason for decision with referenced clause"
}}
"""
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0  # Ensures consistent response
    )
    return response.choices[0].message.content
