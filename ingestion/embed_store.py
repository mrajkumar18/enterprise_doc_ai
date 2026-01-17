from langchain_community.vectorstores import FAISS
from config.llm_config import get_embeddings

def create_vector_store(chunks, persist_path="vectorstore"):
    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(persist_path)
    return vectorstore
