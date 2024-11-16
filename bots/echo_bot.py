# bots/mirror_bot.py
import streamlit as st

def show():
    st.header("Echo Bot")

    # Initialize chat history - saving the chat history to st.session_state.messages_mirror_bot so messages won't disappear 
    if "messages_mirror_bot" not in st.session_state:
        st.session_state.messages_mirror_bot = []

    # Display previous messages on app rerun
    for message in st.session_state.messages_mirror_bot:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Updating chat history - react to user input 
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages_mirror_bot.append({"role": "user", "content": prompt})

        response = f"Echo: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages_mirror_bot.append({"role": "assistant", "content": response})