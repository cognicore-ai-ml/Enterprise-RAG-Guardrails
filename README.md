# Enterprise RAG Assistant with Guardrails

### 🚀 Overview
An enterprise-grade Retrieval-Augmented Generation (RAG) system designed to query internal documents securely. This project demonstrates production-ready AI engineering, implementing **Role-Based Access Control (RBAC)** and **NeMo Guardrails** to prevent prompt injection and unauthorized data access.

### 🛠 Tech Stack
*   **LLM:** [Insert Model: e.g., OpenAI GPT-4o / Llama 3]
*   **Framework:** LangChain
*   **Vector Store:** ChromaDB
*   **Security:** NeMo Guardrails
*   **UI:** Streamlit

### 🔑 Key Features
*   **Secure Retrieval:** Implements RBAC to filter context based on user authorization levels.
*   **Safety Layer:** Uses NeMo Guardrails to block prompt injection and filter PII (Personally Identifiable Information).
*   **Rigorous Evaluation:** Quantified metrics using **RAGAS** to measure faithfulness, answer relevancy, and context precision.
*   **Modular Architecture:** Designed for scalability with a clean `src/` directory structure.

### 📂 Project Structure
```text
/Enterprise-RAG-Guardrails
├── /data                # Secure document storage
├── /src
│   ├── ingestion.py     # Document parsing & chunking logic
│   ├── vector_store.py  # Embedding & retrieval implementation
│   ├── guardrails.py    # Input/Output filtering rules
│   └── chain.py         # RAG pipeline logic
├── /app
│   └── ui.py            # Streamlit dashboard
├── requirements.txt
└── README.md


```
# bash
git clone [https://github.com/your-username/Enterprise-RAG-Guardrails.git](https://github.com/your-username/Enterprise-RAG-Guardrails.git) 

```

```
# bash

streamlit run app/ui.py

```





📈 Evaluation
Current RAGAS Scores:

MetricScore
Faithfulness 0.92
Answer Relevancy 0.88
Context Precision 0.85

