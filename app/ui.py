``` python
from src.chain import run_secure_chain
```

import streamlit as st
import os
from dotenv import load_dotenv
from src.chain import run_secure_chain  # <--- Put this here




import streamlit as st
import os
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()

# 2. Page Configuration
st.set_page_config(page_title="Enterprise RAG Assistant", page_icon="🛡️")

st.title("🛡️ Enterprise RAG Assistant")
st.markdown("Secure, guarded Q&A for internal documents.")

# 3. Sidebar for Configuration
with st.sidebar:
    st.header("Settings")
    model_choice = st.selectbox("Select LLM", ["GPT-4o", "Llama 3 (Local)"])
    st.info("Guardrails: Active & Monitoring")

# 4. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Chat Input Logic
if prompt := st.chat_input("Ask a question about your documents..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

        # Display assistant response
    with st.chat_message("assistant"):
        # This calls your secure chain logic
        response = run_secure_chain(prompt)
        st.markdown(response)
        
    
    st.session_state.messages.append({"role": "assistant", "content": response})

#
from 
# app/ui.py

# ... (setup code) ...

# Chat Input Logic
if prompt := st.chat_input("Ask a question about your documents..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        # This replaces your previous placeholder
        response = run_secure_chain(prompt) 
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})


# ... [Imports and Setup Code Above] ...

# 4. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. CHAT INPUT LOGIC (Paste your code here)
if prompt := st.chat_input("Ask a question about your documents..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        # This calls your secure backend
        response = run_secure_chain(prompt) 
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    
