from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class Retriever:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # Sample knowledge base (replace later with real docs)
        self.documents = [
            "Cloud Connect is a network solution that enables seamless connectivity.",
            "Polarin NaaS helps manage network services efficiently.",
            "Latency is the time delay in network communication.",
        ]

        # Create embeddings
        self.embeddings = self.model.encode(self.documents)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))

    def retrieve(self, query: str, top_k=2):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, top_k)

        results = [self.documents[i] for i in indices[0]]
        return results