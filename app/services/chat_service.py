from app.llm.client import LLMClient
from app.llm.prompt_manager import build_rag_prompt
from app.services.rag.retriever import Retriever


class ChatService:
    def __init__(self):
        self.llm = LLMClient()
        self.retriever = Retriever()

    def generate_response(self, message: str):
        context_docs = self.retriever.retrieve(message)

        context = "\n".join(context_docs)

        prompt = build_rag_prompt(context, message)

        return self.llm.generate(prompt)