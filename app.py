from qa.rag_chain import get_rag_chain

def main():
    qa_chain = get_rag_chain()

    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break

        result = qa_chain(query)

        print("\nAnswer:")
        print(result["result"])

        print("\nSources:")
        for doc in result["source_documents"]:
            print("-", doc.metadata.get("source", "Unknown"))

if __name__ == "__main__":
    main()

