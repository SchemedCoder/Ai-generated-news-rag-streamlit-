import streamlit as st
from rag.query import ask_question

st.set_page_config(page_title="AI News RAG", layout="wide")

st.title("🧠 AI News Insight Generator")

question = st.text_input("Ask a question about AI news:")

if st.button("Generate Answer"):
    if question:
        with st.spinner("Thinking..."):
            answer = ask_question(question)
        st.success(answer)
    else:
        st.warning("Please enter a question")
