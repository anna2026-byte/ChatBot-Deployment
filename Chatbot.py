import os

import streamlit as st
from dotenv import load_dotenv
from langchain_classic.chains.sql_database import query
from langchain_core import chat_history
from langchain_groq import ChatGroq
from urllib3 import response

load_dotenv()

#stramlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)
st.title("🗪 Generative AI Chatbot")

#initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

#display chat history using the for loop
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#llm initiate
llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)

#input box
user_prompt=st.chat_input("ask Chatbot")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content":user_prompt})

    response=llm.invoke(
        input=[{"role":"system","content":"you area helpful assistant"},*st.session_state.chat_history]
    )

    assistant_response=response.content
    st.session_state.chat_history.append({"role":"assistant","content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)








