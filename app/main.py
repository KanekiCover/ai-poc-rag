from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(title="AI POC")

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/health")
def health():
    return {"status": "running"}

app.include_router(chat_router)