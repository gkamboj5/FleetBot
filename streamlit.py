import streamlit as st
from dotenv import load_dotenv

load_dotenv()

prompt: str = st.chat_input("Enter a prompt here")

USER = "user"
ASSISTANT = "assistant"

if prompt:
    st.chat_message(USER).write(prompt)
    st.chat_message(ASSISTANT).write(f"You wrote {prompt}")
