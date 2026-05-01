from app.llm.client import LLMClient
from app.llm.prompt_manager import build_rag_prompt
from app.orchestrator.intent_router import IntentRouter
from app.services.metrics.metrics_service import MetricsService
from app.services.rag.retriever import Retriever


class ChatService:
    def __init__(self):
        self.llm = LLMClient()
        self.retriever = Retriever()
        self.metrics_service = MetricsService()

    def generate_response(self, message: str, user_id: str):
        intent = IntentRouter.classify_intent(message)

        if intent == "metrics":
            return self.metrics_service.generate_metrics_response(message, user_id)

        context_docs = self.retriever.retrieve(message)
        context = "\n".join(context_docs)

        prompt = build_rag_prompt(context, message)

        return self.llm.generate(prompt)
