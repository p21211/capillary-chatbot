


import faiss  
from processor import clean_text

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
import numpy as np
import faiss

def build_vectorstore(documents):
    
    chunks = []
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    for doc in documents:
        text = doc["content"]
        if text.strip():  
            chunks.extend(splitter.split_text(text))

    
    unique_chunks = list(set(chunk.strip() for chunk in chunks if chunk.strip()))

    print(f"🧹 Total chunks before deduplication: {len(chunks)}")
    print(f"✅ Unique chunks after deduplication: {len(unique_chunks)}")

    
    model_name = "sentence-transformers/all-mpnet-base-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)

    
    test_vector = embeddings.embed_query("test")
    vector_np = np.array([test_vector], dtype='float32')
    dim = vector_np.shape[1]
    print(f"✅ Embedding dimension: {dim}")

    
    index = faiss.IndexFlatL2(dim)

    
    store = FAISS(
        embedding_function=embeddings,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={}
    )

    
    store.add_texts(unique_chunks)
    store.save_local("capillary_faiss_index")

    print("✅ Vector store saved to 'capillary_faiss_index/'")
    return store
