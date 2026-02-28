# RAG GPT – Retrieval-Augmented Generation AI

A Retrieval-Augmented Generation (RAG) system built with **FastAPI**, **OpenAI embeddings & LLMs**, and **FAISS vector store**.  
This project allows you to ingest text or PDF documents, create a searchable vector database, and generate AI responses based on context.

---

## Features

- **Document Ingestion:** Supports plain text or PDF files.
- **Vector Store:** Uses FAISS for storing embeddings and searching relevant documents.
- **Embedding Service:** Generates embeddings for documents using OpenAI embedding models (mockable for offline use).
- **LLM Service:** Generates responses using OpenAI GPT models (supports mock mode for testing without API keys).
- **RAG Pipeline:** Combines embeddings, retrieval, and LLM generation.
- **FastAPI Backend:** REST API for querying your documents.

---

## Folder Structure

```

GPT/
├─ app/
│  ├─ core/config.py
│  ├─ services/
│  │   ├─ embedding_service.py
│  │   ├─ llm_service.py
│  │   └─ rag_service.py
│  ├─ api/routes/chat.py
│  └─ main.py
├─ scripts/
│  └─ ingest.py
├─ vectorstore/faiss_store.py
├─ data/documents/      # Add your text/PDF files here
├─ .env                 # Your local environment variables (do NOT push)
├─ .env.example         # Template for environment variables
├─ requirements.txt
├─ LICENSE
├─ README.md
└─ .gitignore

````

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/VaishnaviNayak2023/rag-gpt.git
cd rag-gpt
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

1. Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

2. Fill in your OpenAI API key and model settings:

```env
OPENAI_API_KEY=your_openai_key_here
MODEL_NAME=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-large
VECTOR_DIM=3072
TOP_K=5
MOCK_MODE=false  # set true to run locally without API keys
```

---

## Usage

### 1. Add documents

Place `.txt` or `.pdf` files in:

```
data/documents/
```

### 2. Ingest documents

```bash
python -m scripts.ingest
```

* Generates embeddings for all documents.
* Builds a FAISS vector store.
* Output files: `data/faiss.index` and `data/meta.pkl`.

### 3. Run API server

```bash
uvicorn app.main:app --reload
```

* API available at `http://127.0.0.1:8000`
* Health check: `GET /` → returns `{"status":"ok"}`
* Chat endpoint: `POST /chat` with JSON:

```json
{
  "query": "What is AI?"
}
```

Response:

```json
{
  "answer": "Artificial Intelligence (AI) is the simulation of human intelligence in machines..."
}
```

---

## Mock Mode

Set `MOCK_MODE=true` in `.env` to run without OpenAI API keys.

* Embeddings will be random vectors
* LLM responses will be mock text

Great for **testing FAISS and API pipeline locally**.

---

## Notes

* **Never push your `.env` file** — it contains secrets. Use `.env.example` for reference.
* FAISS index and metadata are stored in `data/faiss.index` and `data/meta.pkl` and should not be committed.
* Add new documents in `data/documents/` and re-run `ingest.py` to update the vector store.

---

## License

* **Code:** MIT License
* **Text datasets:** CC0 (public domain)

See LICENSE for details.

---

## References

* [OpenAI API](https://platform.openai.com/)
* [FAISS Vector Search](https://github.com/facebookresearch/faiss)
* [FastAPI](https://fastapi.tiangolo.com/)
