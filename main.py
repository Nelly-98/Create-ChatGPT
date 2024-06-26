import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

def init():
    load_dotenv()
    # Load the OpenAI API Key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(
        page_title="My own ChatGPT",
        page_icon="🤖"
    )

def main():
    init()

    # Sidebar with radio buttons for menu
    st.sidebar.header("Menu")
    page = st.sidebar.radio("Navigate to:", ["Chat", "About"])

    if page == "Chat":
        # Chat interface
        chat_interface()
    elif page == "About":
        # About page content
        st.write("This is a simple ChatGPT application using Streamlit Made by Nelly GUEPNANG. Enjoy it !!!")

def chat_interface():
    chat = ChatOpenAI(temperature=0)

    if "messages" not in st.session_state:
        st.session_state.messages = [SystemMessage(content="You are a helpful assistant.")]

    st.header("My own ChatGPT 🤖")

    user_input = st.text_input("Your message:", key="user_input")

    if user_input:
        message(user_input, is_user=True)
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("Thinking..."):
            response = chat(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
        message(response.content, is_user=False)

    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')

if __name__ == '__main__':
    main()
