from fastapi import APIRouter, Query, HTTPException
from openai_client.client import get_openai_response  # Use your actual function

router = APIRouter()

@router.get("/summarize")
def summarize_text(
    prompt: str = Query(..., description="Enter text to summarize using OpenAI")
):
    """
    Endpoint to summarize a given text prompt.
    """
    try:
        response = get_openai_response(prompt)
        
        # Check if response contains error
        if "Error" in response:
            raise HTTPException(status_code=500, detail=response)
            
        return {
            "task": "summarization",
            "input_prompt": prompt,
            "openai_response": response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
