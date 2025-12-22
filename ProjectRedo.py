import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import os
from openai import OpenAI

client = OpenAI(api_key='KeyHere')

st.title('Plan Your Dream European Vacation')

ctry =  st.selectbox('Select A Country:', ['Albania','Andorra','Austria','Belarus',
    'Belgium','Bosnia and Herzegovina','Bulgaria','Croatia','Czechia','Denmark',
    'Estonia','Finland','France','Germany','Greece','Hungary','Iceland','Ireland',
    'Italy','Kosovo','Latvia','Liechtenstein','Lithuania','Luxembourg','Malta',
    'Moldova','Monaco','Montenegro','Netherlands','North Macedonia','Norway',
    'Poland','Portugal','Romania','Russia','San Marino','Serbia','Slovakia',
    'Slovenia','Spain','Sweden','Switzerland','Turkey','Ukraine','United Kingdom'])

if ctry == 'Albania':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])

st.write('\n')
st.subheader('What Kind Of Activity Are You Looking For?')
st.write('Select Up To Three Types Of Activities')
advtr = st.checkbox('Adventure Tours')
boattr = st.checkbox('Boat Tours')
fdr = st.checkbox('Food and Drink')
lndm = st.checkbox('Landmarks')
nat = st.checkbox('Nature')
boo = st.checkbox('Paranormal')
vehtr = st.checkbox('Vehicle Tours')
wlktr = st.checkbox('Walking Tours')
tagtotal = advtr + boattr + fdr + lndm + nat + boo + vehtr + wlktr
tags = []

st.write("\n")
st.subheader('Click The button Below To Find Activities')
Confirm = st.button('Make My List')
if Confirm == True and tagtotal < 4 and tagtotal > 0:
    def vacayitems(ctry, citty):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} and a link to where I can book them.
                    Format the list like this:
                
                    Attraction Name
                    Booking link
                    """
                }
            ],
            temperature=0.8,
            max_tokens=1000
        )
        vacaylist = response.choices[0].message.content
        return vacaylist
    vacay = vacayitems(ctry, citty)
    st.write(vacay)
    
if Confirm == True and tagtotal > 3:
    st.write('You Selected Too Many Tags')
if Confirm == True and tagtotal == 0:
    st.write('You Need To Select At Least One Tag')
   
# sources:
# https://simple.wikipedia.org/wiki/List_of_European_countries
# https://worldpopulationreview.com/cities/albania
