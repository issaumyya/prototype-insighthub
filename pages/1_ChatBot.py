import streamlit as st
from transformers import pipeline

chatbot_pipeline = pipeline("conversational")

st.title("Ask Anything!")

user_input = st.text_input("Startups...", "")

if user_input:
    response = chatbot_pipeline(user_input)[0]['generated_text']
    st.text_area("Chatbot:", value=response, height=200, max_chars=None, key=None)

