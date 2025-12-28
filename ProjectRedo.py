import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import os
from openai import OpenAI
import datetime

client = OpenAI(api_key=KeyHere)
st.markdown("<h1 style='text-align: center; color: white;'>Plan Your European Vacation</h1>", unsafe_allow_html=True)


def vacayitems(ctry, citty, fday):
        if len(tags) == 1:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                        Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} available on {fday} involving {tags[0]}. Include a one to two sentence description.
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
                        Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} available on {fday} involving {tags[0]} and/or {tags[1]}. Include a one to two sentence description.
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
                        Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} available on {fday} involving {tags[0]}, {tags[1]}, and/or {tags[2]}. Include a one to two sentence description.
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
def actchoice(vchoice):
    if vchoice == '1':
        start = vacay.find("1. ") + 3
        end = vacay.find("\n")
        vv = vacay[start:end]
        st.write(vv)
    if vchoice == '2':
        start = vacay.find("2. ") + 3
        end = vacay.find("\n")
        vv = vacay[start:end]
        st.write(vv)
    if vchoice == '3':
        start = vacay.find("3. ") + 3
        end = vacay.find("\n")
        vv = vacay[start:end]
        st.write(vv)
    if vchoice == '4':
        start = vacay.find("4. ") + 3
        end = vacay.find("\n")
        vv = vacay[start:end]
        st.write(vv)
    if vchoice == '5':
        start = vacay.find("5. ") + 3
        end = vacay.find("\n")
        vv = vacay[start:end]
        st.write(vv)


ctry =  st.selectbox('Select a country:', ['Albania','Austria','Belarus','Belgium',
    'Bosnia and Herzegovina','Bulgaria','Croatia','Czechia','Denmark','Estonia',
    'Finland','France','Germany','Greece','Hungary','Ireland','Italy','Latvia',
    'Lithuania','Moldova','Netherlands','North Macedonia','Norway','Poland','Portugal',
    'Romania','Russia','Serbia','Slovakia','Slovenia','Spain','Sweden','Switzerland',
    'Turkey','Ukraine','United Kingdom'])

if ctry == 'Albania':
    citty =  st.selectbox('Select a city:', ['Tirana','Durrës','Elbasan','Vlorë','Shkodër'])
if ctry == 'Austria':
    citty =  st.selectbox('Select a city:', ['Vienna','Graz','Favoriten','Linz','Donaustadt'])
if ctry == 'Belarus':
    citty =  st.selectbox('Select a city:', ['Minsk','Homyel','Vitsyebsk','Brest','Mahilyow'])
if ctry == 'Belgium':
    citty =  st.selectbox('Select a city:', ['Brussels','Antwerp','Liège','Ghent','Charleroi'])
if ctry == 'Bosnia and Herzegovina':
    citty =  st.selectbox('Select a city:', ['Sarajevo','Banja Luka','Zenica','Tuzla','Mostar'])
if ctry == 'Bulgaria':
    citty =  st.selectbox('Select a city:', ['Sofia','Plovdiv','Varna','Burgas','Ruse'])
if ctry == 'Croatia':
    citty =  st.selectbox('Select a city:', ['Zagreb','Split','Rijeka','Osijek','Zadar'])
if ctry == 'Czechia':
    citty =  st.selectbox('Select a city:', ['Prague','Brno','Ostrava','Pilsen','Liberec'])
if ctry == 'Denmark':
    citty =  st.selectbox('Select a city:', ['Copenhagen','Arhus','Odense','Aalborg','Frederiksberg'])
if ctry == 'Estonia':
    citty =  st.selectbox('Select a city:', ['Tallinn','Tartu','Narva','Kohtla-Jaerve','Pärnu'])
if ctry == 'Finland':
    citty =  st.selectbox('Select a city:', ['Helsinki','Tampere','Espoo','Vantaa','Turku'])
if ctry == 'France':
    citty =  st.selectbox('Select a city:', ['Paris','Lyon','Marseille','Lille','Toulouse'])
if ctry == 'Germany':
    citty =  st.selectbox('Select a city:', ['Berlin','Hamburg','Munich','Cologne','Frankfurt'])
if ctry == 'Greece':
    citty =  st.selectbox('Select a city:', ['Athens','Thessaloniki','Patras','Piraeus','Larissa'])
if ctry == 'Hungary':
    citty =  st.selectbox('Select a city:', ['Budapest','Debrecen','Miskolc','Szeged','Pécs'])
if ctry == 'Ireland':
    citty =  st.selectbox('Select a city:', ['Dublin','Cork','Dun Laoghaire','Luimneach','Gaillimh'])
if ctry == 'Italy':
    citty =  st.selectbox('Select a city:', ['Rome','Venice','Milan','Florence','Rimini'])
if ctry == 'Latvia':
    citty =  st.selectbox('Select a city:', ['Rīga','Daugavpils','Liepāja','Jelgava','Jūrmala'])
if ctry == 'Lithuania':
    citty =  st.selectbox('Select a city:', ['Vilnius','Kaunas','Klaipėda','Šiauliai','	Panevėžys'])
if ctry == 'Moldova':
    citty =  st.selectbox('Select a city:', ['Chișinău','Tiraspol','Bălți','Bender','Rîbnița'])
if ctry == 'Netherlands':
    citty =  st.selectbox('Select a city:', ['Amsterdam','Rotterdam','The Hague','Utrecht','Eindhoven'])
if ctry == 'North Macedonia':
    citty =  st.selectbox('Select a city:', ['Skopje','Bitola','Kumanovo','Prilep','Tetovo'])
if ctry == 'Norway':
    citty =  st.selectbox('Select a city:', ['Oslo','Bergen','Trondheim','Stavanger','Drammen'])
if ctry == 'Poland':
    citty =  st.selectbox('Select a city:', ['Warsaw','Kraków','Łódź','Wrocław','Poznań'])
if ctry == 'Portugal':
    citty =  st.selectbox('Select a city:', ['Lisbon','Porto','Amadora','Braga','Setúbal'])
if ctry == 'Romania':
    citty =  st.selectbox('Select a city:', ['Bucharest','Iași','Cluj-Napoca','Timișoara','Constanța'])
if ctry == 'Russia':
    citty =  st.selectbox('Select a city:', ['Moscow','Saint Petersburg','Novosibirsk','Yekaterinburg','Kazan'])
if ctry == 'Serbia':
    citty =  st.selectbox('Select a city:', ['Belgrade','Niš','Novi Sad','Zemun','Kragujevac'])
if ctry == 'Slovakia':
    citty =  st.selectbox('Select a city:', ['Bratislava','Košice','Prešov','Nitra','Žilina'])
if ctry == 'Slovenia':
    citty =  st.selectbox('Select a city:', ['Piran','Kranjska Gora','Ljubljana','Bohinj','Bled'])
if ctry == 'Spain':
    citty =  st.selectbox('Select a city:', ['Madrid','Barcelona','Valencia','Zaragoza','Seville'])
if ctry == 'Sweden':
    citty =  st.selectbox('Select a city:', ['Stockholm','Gothenburg','Malmö','Uppsala','Sollentuna'])
if ctry == 'Switzerland':
    citty =  st.selectbox('Select a city:', ['Zürich','Geneva','Basel','Lausanne','Bern'])
if ctry == 'Turkey':
    citty =  st.selectbox('Select a city:', ['Istanbul','Ankara','İzmir','Bursa','Adana'])
if ctry == 'Ukraine':
    citty =  st.selectbox('Select a city:', ['Kyiv','Kharkiv','Odesa','Dnipro','Donetsk'])
if ctry == 'United Kingdom':
    citty =  st.selectbox('Select a city:', ['London','Manchester','Birmingham','Glasgow','Southampton'])

st.subheader('When is your vacation?')
st.write('Must be 2-7 days')
fday = st.date_input('First day')
lday = st.date_input('Last day')
fdaysplit = str(fday).split('-')
ldaysplit = str(lday).split('-')
fdaynum = datetime.date(year = int(fdaysplit[0]), month = int(fdaysplit[1]), day = int(fdaysplit[2]))
ldaynum = datetime.date(year = int(ldaysplit[0]), month = int(ldaysplit[1]), day = int(ldaysplit[2]))
dur = (ldaynum-fdaynum).days
if dur < 2:
    st.write('Please make your vacation at least 2 days long')
if dur > 7:
    st.write('Please make your vacation less than 7 days long')
if dur == 2:
    day1, day2 = st.tabs(
        ['Day 1 Plan', 'Day 2 Plan']
    )
    with day1:
        st.subheader('What kind of activities are you looking for?')
        st.write('Select up to three types of activities')
        boattr = st.checkbox('Boat tours')
        fdr = st.checkbox('Food and drink')
        lndm = st.checkbox('Landmarks')
        nat = st.checkbox('Nature')
        vehtr = st.checkbox('Vehicle tours')
        wlktr = st.checkbox('Walking tours')
        tagtotal = boattr + fdr + lndm + nat + vehtr + wlktr
        tags = []
        vchoice = 0
        Ready = st.radio('Are you ready to find activities?',['Not yet','Yes'])
        if Ready == 'Yes' and tagtotal > 3:
            st.write('You Selected Too Many Tags')
        if Ready == 'Yes' and tagtotal == 0:
            st.write('You Need To Select At Least One Tag')
        if Ready == 'Yes' and tagtotal < 4 and tagtotal > 0:
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
            vacay = vacayitems(ctry,citty,fday)
            st.write(vacay)
            st.subheader('Which activity are you choosing?')
            vchoice = st.radio("Choose the number that matches the activity's list number", ['Not sure yet','1','2','3','4','5'])
            actchoice(vchoice)
