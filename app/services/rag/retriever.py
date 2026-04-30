import pickle
from pathlib import Path

import faiss
from sentence_transformers import SentenceTransformer


class Retriever:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        repo_root = Path(__file__).resolve().parent.parent.parent.parent
        index_dir = repo_root / "vectorstore" / "faiss_index"
        self.index_path = index_dir / "index.faiss"
        self.documents_path = index_dir / "documents.pkl"

        if not self.index_path.exists() or not self.documents_path.exists():
            raise FileNotFoundError(
                "FAISS index or documents file not found. "
                "Please run: python scripts/ingest_kb.py"
            )

        self.index = faiss.read_index(str(self.index_path))
        with self.documents_path.open("rb") as f:
            self.documents = pickle.load(f)

    def retrieve(self, query: str, top_k=2):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            if idx >= 0 and idx < len(self.documents):
                results.append(self.documents[idx])

        return results