"""from fastapi import FastAPI
from api.routes import router as api_router

#app = FastAPI(title="OpenAI FastAPI Example")
app = FastAPI()
# Include API routes
app.include_router(api_router, prefix="/api")

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI + OpenAI project!"}"""    
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}