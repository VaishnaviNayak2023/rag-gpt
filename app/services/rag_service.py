from app.services.embedding_service import EmbeddingService
from app.services.llm_service import LLMService
from app.vectorstore.faiss_store import FAISSStore
from app.core.config import settings

class RAGService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.llm_service = LLMService()
        self.vectorstore = FAISSStore()

    async def generate_answer(self, query: str) -> str:
        query_embedding = await self.embedding_service.embed(query)

        docs = self.vectorstore.search(query_embedding, settings.TOP_K)

        context = "\n\n".join([doc["text"] for doc in docs])

        prompt = f"""
You are a helpful AI assistant.
Answer strictly based on the context below.

Context:
{context}

Question:
{query}
"""

        return await self.llm_service.generate(prompt)
