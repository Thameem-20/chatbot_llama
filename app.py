import streamlit as st
import ollama
import time

def stream_data(text,delay:float=0.02):
    for word in text.split():
        yield word + " "
        time.sleep(delay)


prompt = st.chat_input("Ask anything")

if prompt:

    with st.chat_message("user"):
        st.write(prompt)




