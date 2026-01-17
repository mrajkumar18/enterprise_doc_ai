from langchain_community.vectorstores import FAISS
from config.llm_config import get_embeddings

VECTORSTORE_PATH = "vectorstore"

def get_retriever(k: int = 5):
    embeddings = get_embeddings()
    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": k, "fetch_k": 15}
    )


