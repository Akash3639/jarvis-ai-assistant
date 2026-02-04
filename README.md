# 🤖 JARVIS – Personal AI Assistant

A self-hosted AI assistant built using a local Large Language Model (LLM) and a vector database for contextual question answering.

## 🚀 Features
- Self-hosted LLM (Phi-2)
- Vector-based semantic search using Pinecone
- Retrieval-Augmented Generation (RAG)
- Interactive chatbot UI using Streamlit

## 🛠 Tech Stack
- Python 3.10
- HuggingFace Transformers
- Pinecone Vector Database
- Sentence Transformers
- Streamlit

## ⚙️ Setup Instructions

1. Clone the repository

git clone https://github.com/your-username/jarvis-ai-assistant.git
cd jarvis-ai-assistant

2. Install dependencies
   pip install -r requirements.txt
   
3. Configure environment variables
   PINECONE_API_KEY=your_key
   PINECONE_ENV=your_env
   PINECONE_INDEX=jarvis-index
   
4. Index data
   python ingest.py
   
5. Run the application
   streamlit run app.py

