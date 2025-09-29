from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_openai_response(prompt: str) -> str:
    """
    Get response from OpenAI API for a given prompt
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
"""from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_openai_response(prompt: str) -> str:
    Get response from OpenAI for a given prompt
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

from fastapi import APIRouter, Query
from openai_client.client import generate_text

router = APIRouter()

@router.get("/summarize")
def summarize_text(
    prompt: str = Query(..., description="Enter text to summarize using OpenAI")
):
    
    Endpoint to summarize a given text prompt.
    
    response = generate_text(prompt)
    return {
        "task": "summarization",
        "input_prompt": prompt,
        "openai_response": response
    }"""
