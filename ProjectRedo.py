# put the following into the terminal:
# python -m pip install streamlit
# python -m pip install streamlit-option-menu
# python -m streamlit run .\ProjectRedo.py


# Local URL: http://localhost:8501
# Network URL: http://10.0.0.33:8501

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

# find country
# tags
# list destinations/activities
# sort by popularity (# of ratings) or top rated (highest ratings)
st.title('Select A Country')

tabA, tabB, tabC, tabD, tabE, tabF, tabG, tabH, tabI, tabK, tabL, tabM, tabN, tabP, tabR, tabS, tabT, tabU, tabV = st.tabs(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V']
)
with tabA:
    st.write("Albania")
    st.write("Andorra")
    st.write("Austria")
with tabB:
    st.write("Belarus")
    st.write("Belgium")
    st.write("Bosnia and Herzegovina")
    st.write("Bulgaria")
with tabC:
    st.write("Croatia")
    st.write("Czechia")
with tabD:
    st.write("Denmark")
with tabE:
    st.write("Estonia")
with tabF:
    st.write("Finland")
    st.write("France")
with tabG:
    st.write("Germany")
    st.write("Greece")
with tabH:
    st.write("Hungary")
with tabI:
    st.write("Iceland")
    st.write("Ireland")
    st.write("Italy")
with tabK:
    st.write("Kosovo")
with tabL:
    st.write("Latvia")
    st.write("Liechtenstein")
    st.write("Lithuania")
    st.write("Luxembourg")
with tabM:
    st.write("Malta")
    st.write("Moldova")
    st.write("Monaco")
    st.write("Montenegro")
with tabN:
    st.write("Netherlands")
    st.write("North Macedonia")
    st.write("Norway")
with tabP:
    st.write("Poland")
    st.write("Portugal")
with tabR:
    st.write("Romania")
    st.write("Russia")
with tabS:
    st.write("San Marino")
    st.write("Serbia")
    st.write("Slovakia")
    st.write("Slovenia")
    st.write("Spain")
    st.write("Sweden")
    st.write("Switzerland")
with tabT:
    st.write("Turkey")
with tabU:
    st.write("Ukraine")
    st.write("United Kingdom")
with tabV:
    st.write("Vatican City")

