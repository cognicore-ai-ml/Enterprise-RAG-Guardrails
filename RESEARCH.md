# Project Report: Enterprise-RAG-Guardrails

# Abstract

This project implements a Retrieval-Augmented Generation (RAG) pipeline designed for secure, enterprise-grade information retrieval. The core objective was to construct a robust system that balances effective document retrieval with necessary output guardrails while maintaining stability in a modular Python development environment.

# Technical Stack

Language: Python 3.12
Frameworks: LangChain, Streamlit
Environment: GitHub Codespaces, Virtual Environment (venv)
Dependency Management: pip, requirements.txt


# Engineering Challenges & Solutions


# 1. Dependency Modernization
Challenge: Navigating breaking changes in modern LangChain versions, specifically the modularization of legacy functionality (langchain_classic).
Solution: Conducted a comprehensive audit of the codebase. Instead of manual refactoring, utilized automated CLI tooling (find combined with sed) to perform project-wide updates of import statements from langchain.chains to langchain_classic.chains. This ensured consistency and resolved pervasive ModuleNotFoundError exceptions.

# 2. Environment Stability

Challenge: The project suffered from significant dependency corruption within the GitHub Codespaces environment.
Solution: Performed a clean re-installation of all dependencies. Verified environment integrity using isolated import testing (python -c) before launching the application. This established a stable, reproducible base for the RAG pipeline.

# 3. Path Management

Challenge: Issues with module resolution in the src directory when executing the application from the app root.
Solution: Implemented dynamic sys.path modification in ui.py to ensure the parent directory was correctly included in the path, allowing for reliable imports of local modules.

# Conclusion & Future Work

The project successfully achieves a functional, containerized RAG deployment. Future iterations will focus on:
Integrating specific evaluation metrics for the RAG guardrails.
Expanding the document ingestion pipeline.
Optimizing retrieval latency.
