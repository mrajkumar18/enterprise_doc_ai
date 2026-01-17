from retrieval.retriever import get_retriever

retriever = get_retriever()
docs = retriever.get_relevant_documents("What is the incident reporting timeline?")

for d in docs:
    print(d.page_content)
    print("-----")
