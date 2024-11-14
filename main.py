# https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps

import streamlit as st 
import home
from bots import mirror_bot, simple_bot_stream, chatgpt_bot

st.title('LLM chat app')

# Sidebar for navigation
tab = st.sidebar.selectbox(
    "Select a tab",
    ("Home", "Mirror BOT", "Mirror BOT with streaming", "ChatGPT BOT")
)

# Dictionary to map tab names to modules
tabs = {
    "Home": home,
    "Mirror BOT": mirror_bot,
    "Mirror BOT with streaming": simple_bot_stream,
    "ChatGPT BOT": chatgpt_bot
}

# Render the selected tab
if tab in tabs:
    tabs[tab].show()