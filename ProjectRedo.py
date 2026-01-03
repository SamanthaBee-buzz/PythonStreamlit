import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import os
from openai import OpenAI
import datetime
from datetime import timedelta

client = OpenAI(api_key=KEYHERE)
st.markdown("<h1 style='text-align: center; color: white;'>Plan Your European Vacation</h1>", unsafe_allow_html=True)

@st.cache_data
def vacayitems(ctry, citty, fdaygpt, longchoice,tags,repeatlist,timey):
    if longchoice == "I'm not picky":
        longchoice == '1-6 hours'
    if len(tags) == 1:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} available on {fdaygpt} involving {tags[0]}. Do not include {repeatlist}. Make sure they are {longchoice} long and start at {timey}. Include a one sentence description and its duration in hours. If the duration is a range, put the duration as the higher estimate.
                    Format the list like this:
            
                    Attraction Name
                    *new line*
                    One to two sentence description
                    *new line*
                    Duration
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
                    Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} available on {fdaygpt} involving {tags[0]} and/or {tags[1]}. Do not include {repeatlist}. Make sure they are {longchoice} long and start at {timey}. Include a one sentence description and its duration in hours. If the duration is a range, put the duration as the higher estimate.
                    Format the list like this:       

                    Attraction Name
                    *new line*
                    One to two sentence description
                    *new line*
                    Duration
                    """
                }
            ],
            temperature=0.8,
            max_tokens=1000
        )
    if len(tags) == 3:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} available on {fdaygpt} involving {tags[0]}, {tags[1]}, and/or {tags[2]}. Do not include {repeatlist}. Make sure they are {longchoice} long and start at {timey}. Include a one sentence description and its duration in hours. If the duration is a range, put the duration as the higher estimate.
                    Format the list like this:
                
                    Attraction Name
                    *new line*
                    One to two sentence description
                    *new line*
                    Duration
                    """
                }
            ],
            temperature=0.8,
            max_tokens=1000
        )
    vacaylist = response.choices[0].message.content
    pos = vacaylist.find('1.')
    vacaylist = vacaylist[pos:]
    return vacaylist

@st.cache_data
def vacayitemsactone(ctry, citty, fdaygpt, longchoice,tags,timey):
    if longchoice == "I'm not picky":
        longchoice == '1-6 hours'
    if len(tags) == 1:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} available on {fdaygpt} involving {tags[0]}. Make sure they are {longchoice} long and start at {timey}. Include a one sentence description and its duration in hours. If the duration is a range, put the duration as the higher estimate.
                    Format the list like this:
            
                    Attraction Name
                    *new line*
                    One to two sentence description
                    *new line*
                    Duration
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
                    Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} available on {fdaygpt} involving {tags[0]} and/or {tags[1]}. Make sure they are {longchoice} long and start at {timey}. Include a one sentence description and its duration in hours. If the duration is a range, put the duration as the higher estimate.
                    Format the list like this:       

                    Attraction Name
                    *new line*
                    One to two sentence description
                    *new line*
                    Duration
                    """
                }
            ],
            temperature=0.8,
            max_tokens=1000
        )
    if len(tags) == 3:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Make a list of the 5 most popular tourist attractions/destinations in {citty}, {ctry} available on {fdaygpt} involving {tags[0]}, {tags[1]}, and/or {tags[2]}. Make sure they are {longchoice} long and start at {timey}. Include a one sentence description and its duration in hours. If the duration is a range, put the duration as the higher estimate.
                    Format the list like this:
                
                    Attraction Name
                    *new line*
                    One to two sentence description
                    *new line*
                    Duration
                    """
                }
            ],
            temperature=0.8,
            max_tokens=1000
        )
    vacaylist = response.choices[0].message.content
    pos = vacaylist.find('1.')
    vacaylist = vacaylist[pos:]
    return vacaylist
    
def actdur(vchoice,vacay):
    cdur = ""
    start = vacay.find(f"{vchoice}.")
    end = vacay.find("hours", start)
    c = vacay[start:end]
    start = c.find("Duration:")
    end = c.find("hour", start)
    cdur = c[start:end]
    cdur = cdur[10:len(cdur)]
    cdur.strip()
    cdur = float(cdur)
    return cdur

def actchoice(vchoice,vacay):
    vsl = ''
    start = vacay.find(f"{vchoice}. ") + 3
    end = vacay.find("\n", start)
    vsl = vacay[start:end]
    return vsl

def dayvac(fdaygpt,ctry,citty,keynum,repeatlist):
    st.subheader(f"Let's plan {fdaygpt}")
    st.write('Select up to three types of activities for this day')
    boattr = st.checkbox('Boat tours', key = f'boa{keynum}')
    fdr = st.checkbox('Food and drink', key = f'fdr{keynum}')
    lndm = st.checkbox('Landmarks', key = f'lnd{keynum}')
    nat = st.checkbox('Nature', key = f'nat{keynum}')
    vehtr = st.checkbox('Vehicle tours', key = f'veh{keynum}')
    wlktr = st.checkbox('Walking tours', key = f'wlk{keynum}')
    tagtotal = boattr + fdr + lndm + nat + vehtr + wlktr
    tags = []
    timehr = 10
    timemin = 0
    vchoice = 0
    actnum = 0
    actnum =  int(st.selectbox(f'How many activities will you do on {fdaygpt}?', ['1','2','3'], key = f'act{keynum}'))
    Ready = st.radio('Are you ready to find activities?',['Not yet','Yes'], key = f'rea1{keynum}')
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
        if actnum == 1:
            st.subheader('Activity 1')
            timey = st.slider("When will this activity start?", time(timehr,timemin), time(22,00), step = timedelta(minutes = 30), key = f'time1{keynum}')
            longchoice = st.radio('How long do you want this activity to be?', ['Not sure yet',"I'm not picky",'1-2 hours','2-4 hours','4-6 hours'], key = f'len1{keynum}')
            if longchoice != 'Not sure yet':
                if repeatlist == []:
                    vacay = vacayitemsactone(ctry,citty,fdaygpt,longchoice,tags,timey)
                else:
                    vacay = vacayitems(ctry,citty,fdaygpt,longchoice,tags,repeatlist,timey)
                st.write(vacay)
                vchoice = st.radio('What will this activity be?', ['Not sure yet','1','2','3','4','5'], key = f'vch1{keynum}')
                vacselect = actchoice(vchoice,vacay)
                repeatlist.append(vacselect)
        if actnum == 2:
            st.subheader('Activity 1')
            timey = st.slider("When will the first activity start?", time(timehr,timemin), time(22,00), step = timedelta(minutes = 30), key = f'time1{keynum}')
            longchoice = st.radio('How long do you want the first activity to be?', ['Not sure yet',"I'm not picky",'1-2 hours','2-4 hours','4-6 hours'], key = f'len1{keynum}')
            if longchoice != 'Not sure yet':
                if repeatlist == []:
                    vacay = vacayitemsactone(ctry,citty,fdaygpt,longchoice,tags,timey)
                else:
                    vacay = vacayitems(ctry,citty,fdaygpt,longchoice,tags,repeatlist,timey)
                st.write(vacay)
                vchoice = st.radio('What will the first activity be?', ['Not sure yet','1','2','3','4','5'], key = f'vch1{keynum}')
                if vchoice != 'Not sure yet':
                    vacselect = actchoice(vchoice,vacay)
                    repeatlist.append(vacselect)
                    ddur = actdur(vchoice,vacay)
                    decdur = isinstance(ddur,float)
                    if decdur and timemin == 0:
                        timehr = timehr + ddur + .5
                        timemin = timemin + 30
                    elif decdur and timemin == 30:
                        timehr = timehr + ddur + .5
                        timemin = timemin - 30
                    else:
                        timehr = timehr + ddur + 1
                    timehr = int(timehr)
                    st.subheader('Activity 2')
                    timey = st.slider("When will the second activity start?", time(timehr,timemin), time(22,00), step = timedelta(minutes = 30), key = f'time2{keynum}')
                    longchoice = st.radio('How long do you want the second activity to be?', ['Not sure yet',"I'm not picky",'1-2 hours','2-4 hours','4-6 hours'], key = f'len2{keynum}')
                    if longchoice != 'Not sure yet':
                        vacay = vacayitems(ctry,citty,fdaygpt,longchoice,tags,repeatlist,timey)
                        st.write(vacay)
                        vchoice = st.radio('What will the second activity be?', ['Not sure yet','1','2','3','4','5'], key = f'vch2{keynum}')
                        vacselect = actchoice(vchoice,vacay)
                        repeatlist.append(vacselect)
        if actnum == 3:
            st.subheader('Activity 1')
            timey = st.slider("When will the first activity start?", time(timehr,timemin), time(22,00), key = f'time1{keynum}')
            longchoice = st.radio('How long do you the first activity to be?', ['Not sure yet',"I'm not picky",'1-2 hours','2-4 hours','4-6 hours'], key = f'len1{keynum}')
            if longchoice != 'Not sure yet':
                if repeatlist == []:
                    vacay = vacayitemsactone(ctry,citty,fdaygpt,longchoice,tags,timey)
                else:
                    vacay = vacayitems(ctry,citty,fdaygpt,longchoice,tags,repeatlist,timey)
                st.write(vacay)
                vchoice = st.radio('What will the first activity be?', ['Not sure yet','1','2','3','4','5'], key = f'vch1{keynum}')
                if vchoice != 'Not sure yet':
                    vacselect = actchoice(vchoice,vacay)
                    repeatlist.append(vacselect)
                    ddur = actdur(vchoice,vacay)
                    decdur = isinstance(ddur,float)
                    if decdur and timemin == 0:
                        timehr = timehr + ddur + .5
                        timemin = timemin + 30
                    elif decdur and timemin == 30:
                        timehr = timehr + ddur + .5
                        timemin = timemin - 30
                    else:
                        timehr = timehr + ddur + 1
                    timehr = int(timehr)
                    st.subheader('Activity 2')
                    timey = st.slider("When will the second activity start?", time(timehr,timemin), time(22,00), key = f'time2{keynum}')
                    longchoice = st.radio('How long do you the second activity to be?', ['Not sure yet',"I'm not picky",'1-2 hours','2-4 hours','4-6 hours'], key = f'len2{keynum}')
                    if longchoice != 'Not sure yet':
                        vacay = vacayitems(ctry,citty,fdaygpt,longchoice,tags,repeatlist,timey)
                        st.write(vacay)
                        vchoice = st.radio('What will the second activity be?', ['Not sure yet','1','2','3','4','5'], key = f'vch2{keynum}')
                        if vchoice != 'Not sure yet':
                            vacselect = actchoice(vchoice,vacay)
                            repeatlist.append(vacselect)
                            ddur = actdur(vchoice,vacay)
                            decdur = isinstance(ddur,float)
                            if decdur and timemin == 0:
                                timehr = timehr + ddur + .5
                                timemin = timemin + 30
                            elif decdur and timemin == 30:
                                timehr = timehr + ddur + .5
                                timemin = timemin - 30
                            else:
                                timehr = timehr + ddur + 1
                            timehr = int(timehr)
                            st.subheader('Activity 3')
                            timey = st.slider("When will the third activity start?", time(timehr,timemin), time(22,00), key = f'time3{keynum}')
                            longchoice = st.radio('How long do you the third activity to be?', ['Not sure yet',"I'm not picky",'1-2 hours','2-4 hours','4-6 hours'], key = f'len3{keynum}')
                            if longchoice != 'Not sure yet':
                                vacay = vacayitems(ctry,citty,fdaygpt,longchoice,tags,repeatlist,timey)
                                st.write(vacay)
                                vchoice = st.radio('What will the third activity be?', ['Not sure yet','1','2','3','4','5'], key = f'vch3{keynum}')
                                vacselect = actchoice(vchoice,vacay)
                                repeatlist.append(vacselect)
    return(repeatlist)

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
st.write('Must be 2-5 days')
fday = st.date_input('First day')
lday = st.date_input('Last day')
dur = (lday-fday).days
if dur < 2:
    st.write('Please make your vacation at least 2 days long')
if dur > 5:
    st.write('Please make your vacation at most 5 days long')
if dur == 2:
    day1, day2 = st.tabs(
        ['Day 1 Plan', 'Day 2 Plan']
    )
    repeatlist = []
    with day1:
        keynum = 21
        fdaygpt = fday
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
    with day2:
        keynum = 22
        fdaygpt = fday + timedelta(days=1)
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
    st.write(repeatlist)
elif dur == 3:
    day1, day2, day3 = st.tabs(
        ['Day 1 Plan', 'Day 2 Plan', 'Day 3 Plan']
    )
    repeatlist = []
    with day1:
        keynum = 31
        fdaygpt = fday
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
    with day2:
        keynum = 32
        fdaygpt = fday + timedelta(days=1)
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
    with day3:
        keynum = 33
        fdaygpt = fday + timedelta(days=2)
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
elif dur == 4:
    day1, day2, day3, day4 = st.tabs(
        ['Day 1 Plan', 'Day 2 Plan', 'Day 3 Plan', 'Day 4 Plan']
    )
    repeatlist = []
    with day1:
        keynum = 41
        fdaygpt = fday
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
    with day2:
        keynum = 42
        fdaygpt = fday + timedelta(days=1)
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
    with day3:
        keynum = 43
        fdaygpt = fday + timedelta(days=2)
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
    with day4:
        keynum = 44
        fdaygpt = fday + timedelta(days=3)
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
elif dur == 5:
    day1, day2, day3, day4, day5 = st.tabs(
        ['Day 1 Plan', 'Day 2 Plan', 'Day 3 Plan', 'Day 4 Plan', 'Day 5 Plan']
    )
    repeatlist = []
    with day1:
        keynum = 51
        fdaygpt = fday
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
    with day2:
        keynum = 52
        fdaygpt = fday + timedelta(days=1)
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
    with day3:
        keynum = 53
        fdaygpt = fday + timedelta(days=2)
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
    with day4:
        keynum = 54
        fdaygpt = fday + timedelta(days=3)
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)
    with day5:
        keynum = 55
        fdaygpt = fday + timedelta(days=4)
        dayvac(fdaygpt,ctry,citty,keynum,repeatlist)



