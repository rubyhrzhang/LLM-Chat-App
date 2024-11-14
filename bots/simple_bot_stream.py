# bots/mirror_bot_streaming.py
import streamlit as st
import random
import time

def show():
    st.title("Simple BOT with streaming")

    # the assistant’s reply appear incrementally rather than all at once
    # Streamed response emulator
    def response_generator():
        response = random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )
        for word in response.split():
            yield word + " "
            time.sleep(0.05)

    # Initialize chat history
    if "simple_bot_stream" not in st.session_state:
        st.session_state.simple_bot_stream = []

    # Display chat messages from history on app rerun
    for message in st.session_state.simple_bot_stream:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.simple_bot_stream.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.simple_bot_stream.append({"role": "assistant", "content": response})