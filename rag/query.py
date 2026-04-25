import psycopg2
from config import DB_CONFIG, OPENAI_API_KEY
from openai import OpenAI
from rag.embed import get_embedding

client = OpenAI(api_key=OPENAI_API_KEY)

def search_similar(query):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    embedding = get_embedding(query)

    cur.execute("""
        SELECT content
        FROM news
        ORDER BY embedding <-> %s
        LIMIT 5
    """, (embedding,))

    results = [r[0] for r in cur.fetchall()]

    cur.close()
    conn.close()

    return "\n".join(results)


def ask_question(question):
    context = search_similar(question)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer using context only"},
            {"role": "user", "content": f"{context}\n\nQuestion: {question}"}
        ]
    )

    return response.choices[0].message.content
