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
# 📘 CapillaryTech Documentation Chatbot

This project is an intelligent chatbot that allows you to query CapillaryTech's official documentation using natural language. It scrapes the documentation, preprocesses and indexes the content using embeddings, and lets you ask questions through a Streamlit-based interface.

---


## 🧰 Tech Stack

- Python 🐍
- LangChain
- FAISS (Facebook AI Similarity Search)
- HuggingFace Transformers & Embeddings
- Streamlit (UI)
- BeautifulSoup (for web scraping)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/capillarytech-chatbot.git
cd capillarytech-chatbot

**### Install Dependencies**
pip install -r requirements.txt
```bash
pip install faiss-cpu langchain sentence-transformers numpy


### ⚙️ Run the Project
1. Scrape the Docs 
python scraper.py

2. Preprocess and Build Vector Store
python preprocessor.py

3. Launch the Streamlit App
streamlit run app.py


## 🗂️ Project Structure

.
├── app.py                # Main Streamlit UI
├── scraper.py            # Scraper for documentation
├── preprocessor.py       # Cleans and vectorizes docs
├── vectorstore.py        # FAISS vectorstore builder
├── secretkey.py          # HuggingFace API key (keep this secret)
├── data/
│   └── docs_raw/         # Raw scraped text files
├── capillary_faiss_index/ # Vector store directory
└── README.md             # This file



🧑‍💻 Author
Made with ❤️ by Priyankaa Sarkar

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




