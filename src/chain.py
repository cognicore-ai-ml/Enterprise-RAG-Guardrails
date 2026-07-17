from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.vector_store import load_vector_store

def get_rag_chain():
    # 1. Load your vector store (memory)
    vector_db = load_vector_store()
    retriever = vector_db.as_retriever()

    # 2. Setup the LLM
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    # 3. Define the Prompt (The "Enterprise" personality)
    prompt = ChatPromptTemplate.from_template("""
    You are a secure Enterprise Assistant. Answer the user's question based ONLY on the following context.
    If the information is not in the context, say you don't know. 
    
    Context: {context}
    Question: {input}
    """)

    # 4. Create the chain
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, combine_docs_chain)

# Usage in your app/ui.py would look like:
# chain = get_rag_chain()
# response = chain.invoke({"input": user_query})
