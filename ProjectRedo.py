# put the following into the terminal:
# python -m pip install streamlit
# python -m streamlit run .\ProjectRedo.py

# Local URL: http://localhost:8501
# Network URL: http://10.0.0.33:8501

# Idea: top destinations for each country with tags

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.write('Select A Country:')
CtryATrue = st.button('A')
if CtryATrue:
    CtryAfghTrue = st.button('Afghanistan')


# sources
# https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations
