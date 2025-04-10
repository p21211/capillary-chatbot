import os
import re
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from secretkey import HUGGINGFACEHUB_API_TOKEN

DATA_DIR = "data/docs_raw/"


def clean_text(text):
    """Clean text by removing URLs, special characters, and extra whitespace."""
    text = re.sub(r"http\S+", "", text)         # Remove URLs
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)   # Remove special characters
    text = re.sub(r"\s+", " ", text)             # Collapse multiple spaces
    return text.strip().lower()


def load_documents():
    documents = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".txt"):
            with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as file:
                content = file.read()
                cleaned = clean_text(content)  # Use the clean_text function here
                documents.append(Document(page_content=cleaned, metadata={"source": filename}))
    return documents


def process_and_vectorize():
    print("⚙️ Processing documents...")
    docs = load_documents()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        cache_folder=".cache"
    )

    vectorstore = FAISS.from_documents(texts, embeddings)
    vectorstore.save_local("capillary_faiss_index")
    print("✅ Vector index saved.")

if __name__ == "__main__":
    process_and_vectorize()
