from fastapi import FastAPI
from api.routes import router as api_router

#app = FastAPI(title="OpenAI FastAPI Example")
app = FastAPI()
# Include API routes
app.include_router(api_router, prefix="/api")

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI + OpenAI project!"}

    
