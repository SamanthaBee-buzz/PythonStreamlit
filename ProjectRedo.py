import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import os
from openai import OpenAI

client = OpenAI(api_key='PutKeyHere')

st.title('Plan Your Dream European Vacation')

ctry =  st.selectbox('Select A Country:', ['Albania','Austria','Belarus','Belgium',
    'Bosnia and Herzegovina','Bulgaria','Croatia','Czechia','Denmark','Estonia',
    'Finland','France','Germany','Greece','Hungary','Ireland','Italy','Latvia',
    'Lithuania','Moldova','Netherlands','North Macedonia','Norway','Poland','Portugal',
    'Romania','Russia','Serbia','Slovakia','Slovenia','Spain','Sweden','Switzerland',
    'Turkey','Ukraine','United Kingdom'])

if ctry == 'Albania':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Andorra':
    citty =  st.selectbox('Select A City:', ['Andorra la Vella','les Escaldes','Encamp'])
if ctry == 'Austria':
    citty =  st.selectbox('Select A City:', ['Vienna','Graz','Favoriten','Linz','Donaustadt'])
if ctry == 'Belarus':
    citty =  st.selectbox('Select A City:', ['Minsk','Gomel','Vitebsk','Brest','Mahilyow'])
if ctry == 'Belgium':
    citty =  st.selectbox('Select A City:', ['Brussels','Antwerp','Liege','Gent','Charleroi'])
if ctry == 'Bosnia and Herzegovina':
    citty =  st.selectbox('Select A City:', ['Sarajevo','Banja Luka','Zenica','Tuzla','Mostar'])
if ctry == 'Bulgaria':
    citty =  st.selectbox('Select A City:', ['Sofia','Plovdiv','Varna','Burgas','Ruse'])
if ctry == 'Croatia':
    citty =  st.selectbox('Select A City:', ['Zagreb','Split','Rijeka','Osijek','Zadar'])
if ctry == 'Czechia':
    citty =  st.selectbox('Select A City:', ['Prague','Brno','Ostrava','Pilsen','Liberec'])
if ctry == 'Denmark':
    citty =  st.selectbox('Select A City:', ['Copenhagen','Arhus','Odense','Aalborg','Frederiksberg'])
if ctry == 'Estonia':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Finland':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'France':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Germany':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Greece':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Hungary':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Iceland':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Ireland':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Italy':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Kosovo':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Latvia':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Liechtenstein':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Lithuania':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Luxembourg':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Malta':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Moldova':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Monaco':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Montenegro':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Netherlands':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'North Macedonia':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Norway':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Poland':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Portugal':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Romania':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Russia':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'San Marino':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Serbia':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Slovakia':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Slovenia':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Spain':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Sweden':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Switzerland':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Turkey':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'Ukraine':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])
if ctry == 'United Kingdom':
    citty =  st.selectbox('Select A City:', ['Tirana','Durres','Elbasan','Vlore','Shkoder'])

st.write('\n')
st.subheader('What Kind Of Activities Are You Looking For?')
st.write('Select Up To Three Types Of Activities')
boattr = st.checkbox('Boat Tours')
fdr = st.checkbox('Food and Drink')
lndm = st.checkbox('Landmarks')
nat = st.checkbox('Nature')
vehtr = st.checkbox('Vehicle Tours')
wlktr = st.checkbox('Walking Tours')
tagtotal = boattr + fdr + lndm + nat + vehtr + wlktr
tags = []

st.write("\n")
st.subheader('Click The button Below To Find Activities')
Confirm = st.button('Make My List')
if Confirm == True and tagtotal < 4 and tagtotal > 0:
    if boattr == True:
        tags.append('boat tours')
    if fdr == True:
        tags.append('food and drink')
    if lndm == True:
        tags.append('landmarks')
    if nat == True:
        tags.append('nature')
    if vehtr == True:
        tags.append('vehicle tours')
    if wlktr == True:
        tags.append('walking tours')
    def vacayitems(ctry, citty):
        if len(tags) == 1:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                        Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} involving {tags[0]}. Include a one to two sentence description.
                        Format the list like this:
                
                        Attraction Name
                        One to two sentence description
                        """
                    }
                ],
                temperature=0.8,
                max_tokens=1000
            )
        if len(tags) == 2:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                        Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} involving {tags[0]} and/or {tags[1]}. Include a one to two sentence description..
                        Format the list like this:
                
                        Attraction Name
                        One to two sentence description
                        """
                    }
                ],
                temperature=0.8,
                max_tokens=1000
            )
        if len(tags) == 3:
            tagone == tags[0]
            tagtwo == tags[1]
            tagthree == tags[2]
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                        Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} involving {tags[0]}, {tags[1]}, and/or {tags[2]}. Include a one to two sentence description..
                        Format the list like this:
                
                        Attraction Name
                        One to two sentence description
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


