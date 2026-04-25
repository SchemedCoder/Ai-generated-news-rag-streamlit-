CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE news (
    id SERIAL PRIMARY KEY,
    title TEXT,
    description TEXT,
    content TEXT,
    embedding VECTOR(1536)
);
--to run

createdb ai_news
psql -d ai_news -f db/schema.sql
