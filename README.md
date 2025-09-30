
A FastAPI application for text summarization.
Setup Instructions
Create Folder Structure
pip install -r requirements.txt
uvicorn main:app --reload
How to test the endpoint(example request/response)
test the root endpoint http://localhost:8000/
steps 
Find the GET /api/summarize endpoint
Enter your prompt in the prompt field
Click "Execute" through terminal
See the response at Terminal and  http://localhost:8000/
Using Web Interface
Go to: http://localhost:8000/docs
Find the POST /api/summarize endpoint
Enter your prompt in the request body
Click "Execute"
View the response
