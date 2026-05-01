def build_rag_prompt(context: str, question: str) -> str:
    """
    Builds a RAG prompt for the AI assistant.

    Args:
        context (str): The retrieved context from the knowledge base.
        question (str): The user's question.

    Returns:
        str: The formatted prompt.
    """
    prompt = f"""
You are an AI assistant for telecom and network services.

Use only the provided context to answer the question.

If the answer is not available in the context, say: "I don't know based on the available knowledge base."

Context:
{context}

Question:
{question}
"""
    return prompt