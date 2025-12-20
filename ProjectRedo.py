import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import os
import openai

st.subheader('Select A Country')

ctry =  st.selectbox('Select A Country:', ['Albania','Andorra','Austria','Belarus',
    'Belgium','Bosnia and Herzegovina','Bulgaria','Croatia','Czechia','Denmark',
    'Estonia','Finland','France','Germany','Greece','Hungary','Iceland','Ireland',
    'Italy','Kosovo','Latvia','Liechtenstein','Lithuania','Luxembourg','Malta',
    'Moldova','Monaco','Montenegro','Netherlands','North Macedonia','Norway',
    'Poland','Portugal','Romania','Russia','San Marino','Serbia','Slovakia',
    'Slovenia','Spain','Sweden','Switzerland','Turkey','Ukraine','United Kingdom'])

st.write('\n')
st.subheader('What Kind Of Activity Are You Looking For?')
st.write('Select Up To Three Types Of Activities')
advtr = st.checkbox('Adventure Tours')
aq = st.checkbox('Aquatic')
boattr = st.checkbox('Boat Tours')
fdr = st.checkbox('Food and Drink')
hist = st.checkbox('Historical')
lndm = st.checkbox('Landmarks')
nat = st.checkbox('Nature')
boo = st.checkbox('Paranormal')
vehtr = st.checkbox('Vehicle Tours')
wlktr = st.checkbox('Walking Tours')
tagtotal = advtr + aq + boattr + fdr + hist + lndm + nat + boo + vehtr + wlktr

st.write("\n")
st.subheader('Click The button Below To Find Activities')
Confirm = st.button('Make My List')
if Confirm == True and tagtotal < 4:
    st.write('Making your list')
if Confirm == True and tagtotal > 3:
    st.write('You Selected Too Many Tags')
    openai.api_key = os.getenv('YOURKEYHERE')
