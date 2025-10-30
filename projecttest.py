import streamlit as st
import numpy as np
import sys

with st.chat_message("user"):
    st.write("I am DataBot. What part of data analysis can I help you with?")
    usertask = st.chat_input("...")