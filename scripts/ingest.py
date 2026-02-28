import os
import asyncio
from app.services.embedding_service import EmbeddingService
from app.vectorstore.faiss_store import FAISSStore
from app.utils.chunking import chunk_text

DATA_DIR = "data/documents"

async def ingest():
    embedder = EmbeddingService()
    store = FAISSStore()

    for file in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, file)
        if not os.path.isfile(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        chunks = chunk_text(text)

        embeddings = []
        docs = []

        for chunk in chunks:
            emb = await embedder.embed(chunk)
            embeddings.append(emb)
            docs.append({"text": chunk})

        store.add(embeddings, docs)

if __name__ == "__main__":
    asyncio.run(ingest())
