from fastapi import FastAPI
from app.api.routes import chat

app = FastAPI(title="RAG GPT")

app.include_router(chat.router)

@app.get("/")
async def health():
    return {"status": "ok"}
