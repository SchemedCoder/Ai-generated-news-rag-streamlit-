import requests
import psycopg2
from config import DB_CONFIG
from rag.embed import get_embedding

API_KEY = "YOUR_NEWSAPI_KEY"

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

url = f"https://newsapi.org/v2/everything?q=artificial intelligence&apiKey={API_KEY}"
data = requests.get(url).json()

for a in data['articles']:
    text = f"{a.get('title','')} {a.get('description','')}"
    embedding = get_embedding(text)

    cur.execute("""
        INSERT INTO news (title, description, content, embedding)
        VALUES (%s, %s, %s, %s)
    """, (
        a.get('title'),
        a.get('description'),
        text,
        embedding
    ))

conn.commit()
cur.close()
conn.close()

print("✅ Data inserted with embeddings")
