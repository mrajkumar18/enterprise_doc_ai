from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from config.llm_config import get_llm
from retrieval.retriever import get_retriever

PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an enterprise knowledge assistant.
Answer the question strictly using the provided context.
If the answer is not present in the context, say:
"This information is not available in the approved documents. Please contact the administrator or compliance team."


Provide a clear, concise, professional answer.

Context:
{context}

Question:
{question}

Answer:
"""
)

def get_rag_chain():
    llm = get_llm()
    retriever = get_retriever(k=5)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )

    return qa_chain

