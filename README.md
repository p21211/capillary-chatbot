# 🧠 FAISS-based Vector Store Builder

This project provides a streamlined Python script to create a vector store using [FAISS](https://github.com/facebookresearch/faiss) and HuggingFace sentence-transformers. It processes raw text documents, splits them into chunks, deduplicates, embeds them, and saves the resulting FAISS index locally.

---

## 📂 File Overview

### `vectorstore.py`
- **Main script** to process input documents and build a vector store.
- Uses:
  - `CharacterTextSplitter` for chunking
  - `HuggingFaceEmbeddings` for vector embeddings
  - `FAISS` for indexing and similarity search
  - `InMemoryDocstore` to temporarily store the documents

---

## 🔧 Requirements

Install dependencies with:

```bash
pip install faiss-cpu langchain sentence-transformers numpy
