import streamlit as st
from transformers import pipeline
from llm import load_llm
from vector_store import search_text

st.set_page_config(page_title="JARVIS AI")

st.title("🤖 JARVIS – Personal AI Assistant")

tokenizer, model = load_llm()
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

query = st.text_input("Ask something")

if query:
    context = search_text(query)
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    response = generator(prompt, max_length=120)
    st.write(response[0]["generated_text"])
