import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings # Or use HuggingFaceEmbeddings for local/free models

# Initialize your embedding model
# Note: Ensure your OPENAI_API_KEY is set in your environment variables
embeddings = OpenAIEmbeddings()

def create_vector_store(chunks, persist_directory="./data/chroma_db"):
    """
    Converts text chunks into embeddings and saves them to ChromaDB.
    """
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    print(f"Vector store created/updated at {persist_directory}")
    return vector_db

def load_vector_store(persist_directory="./data/chroma_db"):
    """
    Loads an existing vector store from disk.
    """
    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

if __name__ == "__main__":
    print("Vector store module ready.")
  
