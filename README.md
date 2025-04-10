#  CapillaryTech Documentation Chatbot

A powerful chatbot built to interact with [CapillaryTech Docs](https://docs.capillarytech.com/) using semantic search and a large language model. Ask questions and get context-aware answers directly from the documentation.

---

## 📌 Features

-  Cleans and preprocesses raw documentation  
-  Scrapes CapillaryTech docs into `.txt` files  
-  Splits, deduplicates, and embeds text with HuggingFace models  
-  Stores vector embeddings using FAISS for fast retrieval  
-  Answers your questions with LLaMA 3 (Meta-Llama-3-8B-Instruct)  
-  Runs a sleek chatbot UI using Streamlit  

---

##  Overview

This project is an intelligent chatbot that allows you to query CapillaryTech's official documentation using natural language. It scrapes the documentation, preprocesses and indexes the content using embeddings, and lets you ask questions through a Streamlit-based interface.

---

##  Tech Stack

- Python   
- LangChain  
- FAISS  
- HuggingFace Transformers & Embeddings  
- Streamlit (UI)  
- BeautifulSoup (for web scraping)  

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/capillarytech-chatbot.git
cd capillarytech-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install core libraries:

```bash
pip install faiss-cpu langchain sentence-transformers numpy
```

---

## ⚙️ Run the Project

### 1. Scrape the Docs

```bash
python scraper.py
```

### 2. Preprocess and Build Vector Store

```bash
python preprocessor.py
```

### 3. Launch the Streamlit App

```bash
streamlit run app.py
```

---

## 🗂️ Project Structure

```
.
├── app.py                 # Main Streamlit UI
├── scraper.py             # Scraper for documentation
├── preprocessor.py        # Cleans and vectorizes docs
├── vectorstore.py         # FAISS vectorstore builder
├── secretkey.py           # HuggingFace API key 
├── data/
│   └── docs_raw/          # Raw scraped text files
├── capillary_faiss_index/ # Vector store directory
└── README.md              # This file
```

---

## 📂 File Overview

### `app.py`
- Streamlit app that:
  - Loads FAISS index  
  - Accepts user input  
  - Queries the vector store  
  - Uses Meta-Llama-3 via HuggingFaceHub to generate answers  

### `scraper.py`
- Scrapes CapillaryTech documentation pages  
- Saves clean HTML text to `data/docs_raw/`  

### `preprocessor.py`
- Loads raw `.txt` files  
- Cleans, chunks, and embeds them using HuggingFace transformers  
- Saves FAISS vector index to local directory  

### `vectorstore.py`
- Optional utility to build or update vector store  
- Uses:
  - `CharacterTextSplitter` for chunking  
  - `HuggingFaceEmbeddings` for embeddings  
  - `FAISS` for similarity search  
  - `InMemoryDocstore` to store metadata  


---



## 🧑‍💻 Author

Made by **Priyankaa Sarkar**

---



