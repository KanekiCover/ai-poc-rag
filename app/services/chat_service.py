from app.llm.client import LLMClient
from app.services.rag.retriever import Retriever


class ChatService:
    def __init__(self):
        self.llm = LLMClient()
        self.retriever = Retriever()

    def generate_response(self, message: str):
        context_docs = self.retriever.retrieve(message)

        context = "\n".join(context_docs)

        prompt = f"""
You are an AI assistant.

Use the following context to answer the question.

Context:
{context}

Question:
{message}

Answer clearly based on context.
"""

        return self.llm.generate(prompt)