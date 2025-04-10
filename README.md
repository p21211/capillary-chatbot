# 🤖 CapillaryTech Documentation Chatbot

A powerful chatbot built to interact with [CapillaryTech Docs](https://docs.capillarytech.com/) using semantic search and a large language model. Ask questions and get context-aware answers directly from the documentation.

---

## 📌 Features

- 🧼 Cleans and preprocesses raw documentation
- 🕸️ Scrapes CapillaryTech docs into `.txt` files
- 🔍 Splits, deduplicates, and embeds text with HuggingFace models
- ⚡ Stores vector embeddings using FAISS for fast retrieval
- 🧠 Answers your questions with LLaMA 3 (Meta-Llama-3-8B-Instruct)
- 🖥️ Runs a sleek chatbot UI using Streamlit

---

## 🗂️ Project Structure



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
