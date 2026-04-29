# AI POC – RAG-based Chat Assistant

## 🚀 Overview

This project is a Proof of Concept (POC) for an AI-powered assistant that can:

- Answer knowledge base (KB) queries
- Demonstrate a scalable AI backend architecture

The system uses a Retrieval-Augmented Generation (RAG) approach.

---

## 🧠 Architecture

User → API → Service → Retriever → LLM → Response

---

## 🧱 Project Structure

ai-poc/

- app/
  - main.py                # FastAPI entry point
  - api/
    - chat.py             # API endpoints
  - services/
    - chat_service.py     # Business logic
    - rag/
      - retriever.py      # RAG retrieval logic
  - llm/
    - client.py           # LLM abstraction (mock)
  - core/                 # future
  - data/                 # future
  - orchestrator/         # future

- venv/
- requirements.txt
- README.md

---

## ⚙️ Technologies Used

### Backend
- FastAPI
- Uvicorn

### AI / ML
- sentence-transformers
- FAISS

---

## 🧠 Current Features

- FastAPI backend with Swagger UI
- Chat API (/chat)
- Modular architecture
- RAG pipeline with:
  - embeddings
  - FAISS vector search
  - context retrieval
- Mock LLM (no API key required)

---

## 🧪 How to Run

### Activate environment
- venv\Scripts\activate

### Start server
- uvicorn app.main:app --reload


### Open Swagger UI

http://localhost:8000/docs

---

## 🧪 Example Request

POST /chat

### Open Swagger UI

http://localhost:8000/docs

---

## 🧪 Example Request

POST /chat
{
"user_id": "1",
"message": "What is Cloud Connect?"
}


---

## 📌 Current Limitations

- Uses mock LLM (no real generation)
- Static knowledge base
- No persistence of vector store
- No authentication

---

## 🚧 Planned Enhancements

### Short Term
- Add real LLM (OpenAI / local model)
- Load KB from files (PDF/TXT)
- Persist FAISS index

### Medium Term
- Intent routing (KB vs metrics)
- Database integration

### Long Term
- Multi-agent system
- Cloud deployment

---

## 🧠 Design Principles

- Separation of concerns
- Modular architecture
- Pluggable LLM layer
- Avoid unnecessary complexity

---

## 📊 Scope of This POC

### Included
- RAG-based knowledge retrieval
- Backend architecture

### Not Included
- Full production system
- UI/frontend
- Advanced orchestration

---

## 🧭 Future Direction

This POC will evolve into:

- AI assistant for domain-specific queries
- Multi-source retrieval system
- Scalable AI backend

---