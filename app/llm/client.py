class LLMClient:
    """
    Temporary mock LLM client.
    This simulates answer generation until a real LLM provider is connected.
    """

    def generate(self, prompt: str) -> str:
        question = self._extract_question(prompt)
        question_lower = question.lower()

        if "cloud connect" in question_lower:
            return "Cloud Connect is a managed connectivity solution that enables seamless connectivity."

        if "polarin" in question_lower or "naas" in question_lower:
            return "Polarin NaaS is a network-as-a-service offering that helps manage network services efficiently."

        if "traffic" in question_lower:
            return "Traffic refers to the flow of data across the network."

        if "packet" in question_lower or "packets" in question_lower:
            return "Packets are discrete units of data transmitted across a network."

        if "latency" in question_lower:
            return "Latency is the time delay in network communication."

        return "I found relevant context, but the mock LLM does not yet know how to generate a specific answer for this question."

    def _extract_question(self, prompt: str) -> str:
        """
        Extracts the user question from the prompt.
        Expected prompt contains:
        Question:
        <user question>
        """
        if "Question:" not in prompt:
            return prompt

        question_part = prompt.split("Question:", 1)[1]

        if "Answer" in question_part:
            question_part = question_part.split("Answer", 1)[0]

        return question_part.strip()