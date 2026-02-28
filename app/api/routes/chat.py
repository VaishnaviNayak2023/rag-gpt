from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService

router = APIRouter(prefix="/chat", tags=["chat"])

rag_service = RAGService()

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = await rag_service.generate_answer(request.query)
    return ChatResponse(answer=response)
