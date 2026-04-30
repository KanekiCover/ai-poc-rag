import os
import pickle
from pathlib import Path

import faiss
from sentence_transformers import SentenceTransformer

KB_DIR = Path(__file__).resolve().parent.parent / "data" / "kb_docs"
INDEX_DIR = Path(__file__).resolve().parent.parent / "vectorstore" / "faiss_index"
INDEX_PATH = INDEX_DIR / "index.faiss"
DOCUMENTS_PATH = INDEX_DIR / "documents.pkl"


def load_txt_files(source_dir: Path):
    files = list(source_dir.glob("*.txt"))
    documents = []

    for file_path in files:
        with file_path.open("r", encoding="utf-8") as f:
            documents.append(f.read().strip())

    return files, documents


def split_text_into_chunks(text: str, chunk_size=400, overlap=50):
    words = text.split()
    chunks = []
    start = 0
    length = len(words)

    while start < length:
        end = min(start + chunk_size, length)
        chunk = " ".join(words[start:end]).strip()
        if chunk:
            chunks.append(chunk)
        start = end - overlap if end < length else end

    return chunks


def ingest_documents(texts, model):
    chunks = []
    for text in texts:
        chunks.extend(split_text_into_chunks(text))

    if not chunks:
        raise ValueError("No document chunks were created from the source files.")

    embeddings = model.encode(chunks, show_progress_bar=True)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index, chunks


def main():
    os.makedirs(INDEX_DIR, exist_ok=True)

    files, documents = load_txt_files(KB_DIR)
    print(f"Loaded {len(files)} text file(s) from {KB_DIR}")

    if not documents:
        print("No .txt files found in the knowledge base directory.")
        return

    print("Creating embeddings using SentenceTransformer('all-MiniLM-L6-v2')...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    index, chunks = ingest_documents(documents, model)
    print(f"Created {len(chunks)} document chunk(s)")

    faiss.write_index(index, str(INDEX_PATH))
    with DOCUMENTS_PATH.open("wb") as f:
        pickle.dump(chunks, f)

    print(f"Saved FAISS index to: {INDEX_PATH}")
    print(f"Saved document chunks to: {DOCUMENTS_PATH}")


if __name__ == "__main__":
    main()
