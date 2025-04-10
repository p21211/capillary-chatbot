import streamlit as st
from langchain_community.llms import HuggingFaceHub
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from secretkey import HUGGINGFACEHUB_API_TOKEN


st.set_page_config(page_title="CapillaryTech Chatbot", layout="wide")
st.title("📘 CapillaryTech Documentation Chatbot ")
st.markdown("Ask me anything from the CapillaryTech docs! - Priyankaa Sarkar")


@st.cache_resource
def load_chain():
    try:
        
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

        
        vectorstore = FAISS.load_local(
            "capillary_faiss_index",
            embeddings,
            allow_dangerous_deserialization=True
        )

        
        retriever = vectorstore.as_retriever(
            search_type="similarity", search_kwargs={"k": 4}
        )

        
        llm = HuggingFaceHub(
            repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
            model_kwargs={"temperature": 0.6, "max_new_tokens": 1000},
            huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
        )

        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True
        )

        return qa_chain

    except Exception as e:
        st.error(f"🚨 Error loading chain: {e}")
        return None


qa = load_chain()


query = st.text_input("🔍 Enter your question:")
if query and qa:
    with st.spinner("🤖 Generating response..."):
        result = qa.invoke(query)

        st.markdown("### ✅ Answer:")
        st.write(result["result"])

        
        with st.expander("📄 Source Documents"):
            for i, doc in enumerate(result["source_documents"], 1):
                source = doc.metadata.get("source", "Unknown Source")
                st.markdown(f"**Source {i}: {source}**")
                st.write(doc.page_content[:500] + "...")
