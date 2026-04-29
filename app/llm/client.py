class LLMClient:
    def generate(self, prompt: str) -> str:
        # simulate extraction-based answer
        if "Cloud Connect" in prompt.lower():
            return "Cloud Connect is a network solution that enables seamless connectivity."

        if "latency" in prompt.lower():
            return "Latency is the time delay in network communication."

        return "Based on the provided context, here is the answer."