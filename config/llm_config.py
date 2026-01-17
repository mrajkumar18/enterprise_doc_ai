from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain_community.llms import Ollama
# from langchain_community.embeddings import OllamaEmbeddings

USE_OPENAI = True  # Set False to use Ollama

def get_llm():
    if USE_OPENAI:
        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )
    else:
        return Ollama(
            model="llama3"
        )

def get_embeddings():
    if USE_OPENAI:
        return OpenAIEmbeddings(
            model="text-embedding-3-large"
        )
    else:
        return OllamaEmbeddings(
            model="nomic-embed-text"
        )
