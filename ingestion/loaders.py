from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)
from pathlib import Path

def load_documents(data_dir: str):
    docs = []
    for file in Path(data_dir).glob("*"):
        if file.suffix == ".pdf":
            docs.extend(PyPDFLoader(str(file)).load())
        elif file.suffix == ".txt":
            docs.extend(TextLoader(str(file)).load())
        elif file.suffix == ".docx":
            docs.extend(Docx2txtLoader(str(file)).load())
    return docs
