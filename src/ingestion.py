import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_docs(file_path):
    # Load PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    # Chunking: Crucial for RAG performance
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200
    )
    return text_splitter.split_documents(documents)

# Example usage (you'll call this from your main chain)
if __name__ == "__main__":
    print("Ingestion module ready.")
  
