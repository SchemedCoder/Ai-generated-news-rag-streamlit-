# Ai-generated-news-rag-streamlit-

AI News Insight Generator (RAG + Streamlit)

 Overview
 
This project is a **Retrieval-Augmented Generation (RAG) pipeline** that ingests AI-related news, converts it into embeddings, and allows users to ask questions using a Streamlit app.

It combines:
- Data ingestion (API)
- Vector storage (PostgreSQL + pgvector)
- Semantic search
- LLM-based answer generation

---

 Architecture
News API → PostgreSQL → Embeddings → Vector Search → LLM → Streamlit 
---

 Setup Steps

#1️⃣ Install Dependencies
pip install -r requirements.txt

---

#2️⃣ Setup PostgreSQL

Create database:
createdb ai_news

Run schema:
psql -d ai_news -f db/schema.sql

---

# 3️⃣ Add API Keys

Update `config.py`:
- OpenAI API key  
- News API key (inside `fetch_news.py`)

---

# 4️⃣ Load Data (with embeddings)
python etl/fetch_news.py

---

# Run Streamlit App
streamlit run app/streamlit_app.py

---

 How It Works

1. News articles are fetched from API  
2. Each article is converted into embeddings  
3. Embeddings are stored in PostgreSQL (pgvector)  
4. User asks a question  
5. System retrieves similar articles  
6. LLM generates answer using that context  

---


 Common Issues

- pgvector extension not installed  
- Empty database → no results  
- Incorrect API keys  
- PostgreSQL not running  

---

 Future Improvements

- Kafka streaming integration  
- Airflow scheduling  
- Docker deployment  
- Advanced filtering (date/company)  
