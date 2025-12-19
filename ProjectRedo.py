import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

st.title('Select A Country')

tabA, tabB, tabC, tabD, tabE, tabF, tabG, tabH, tabI, tabK, tabL, tabM, tabN, tabP, tabR, tabS, tabT, tabU= st.tabs(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U']
)
ctry = "nothing"

with tabA:
    Alba = st.button('Albania')
    if Alba == True:
        ctry = 'Albania'
    Ando = st.button('Andorra')
    if Ando == True:
        ctry = 'Andorra'
    Aus = st.button('Austria')
    if Aus == True:
        ctry = 'Austria'

with tabB:
    Bela = st.button('Belarus')
    if Bela == True:
        ctry = 'Belarus'
    Blg = st.button('Belgium')
    if Blg == True:
        ctry = 'Belgium'
    Bos = st.button('Bosnia and Herzegovina')
    if Bos == True:
        ctry = 'Bosnia and Herzegovina'
    Bul = st.button('Bulgaria')
    if Bul == True:
        ctry = 'Bulgaria'

with tabC:
    Cro = st.button('Croatia')
    if Cro == True:
        ctry = 'Croatia'
    Cz = st.button('Czechia')
    if Cz == True:
        ctry = 'Czechia'

with tabD:
    Dm = st.button('Denmark')
    if Dm == True:
        ctry = 'Denmark'

with tabE:
    Est = st.button('Estonia')
    if Est == True:
        ctry = 'Estonia'

with tabF:
    Fin = st.button('Finland')
    if Fin == True:
        ctry = 'Finland'
    Fra = st.button('France')
    if Fra == True:
        ctry = 'France'

with tabG:
    Grm = st.button('Germany')
    if Grm == True:
        ctry = 'Germany'
    Gce = st.button('Greece')
    if Gce == True:
        ctry = 'Greece'

with tabH:
    Hun = st.button('Hungary')
    if Hun == True:
        ctry = 'Hungary'

with tabI:
    Ice = st.button('Iceland')
    if Ice == True:
        ctry = 'Iceland'
    Irl = st.button('Ireland')
    if Irl == True:
        ctry = 'Ireland'
    Ita = st.button('Italy')
    if Ita == True:
        ctry = 'Italy'

with tabK:
    Kos = st.button('Kosovo')
    if Kos == True:
        ctry = 'Kosovo'

with tabL:
    Lat = st.button('Latvia')
    if Lat == True:
        ctry = 'Latvia'
    Lch = st.button('Liechtenstein')
    if Lch == True:
        ctry = 'Liechtenstein'
    Lith = st.button('Lithuania')
    if Lith == True:
        ctry = 'Lithuania'
    Lux = st.button('Luxembourg')
    if Lux == True:
        ctry = 'Luxembourg'

with tabM:
    Malt = st.button('Malta')
    if Malt == True:
        ctry = 'Malta'
    Mld = st.button('Moldova')
    if Mld == True:
        ctry = 'Moldova'
    Mon = st.button('Monaco')
    if Mon == True:
        ctry = 'Monaco'
    Mng = st.button('Montenegro')
    if Mng == True:
        ctry = 'Montenegro'

with tabN:
    Nth = st.button('Netherlands')
    if Nth == True:
        ctry = 'Netherlands'
    Mac = st.button('North Macedonia')
    if Mac == True:
        ctry = 'North Macedonia'
    Nor = st.button('Norway')
    if Nor == True:
        ctry = 'Norway'

with tabP:
    Pol = st.button('Poland')
    if Pol == True:
        ctry = 'Poland'
    Ptg = st.button('Portugal')
    if Ptg == True:
        ctry = 'Portugal'

with tabR:
    Rom = st.button('Romania')
    if Rom == True:
        ctry = 'Romania'
    Rus = st.button('Russia')
    if Rus == True:
        ctry = 'Russia'

with tabS:
    San = st.button('San Marino')
    if San == True:
        ctry = 'San Marino'
    Serb = st.button('Serbia')
    if Serb == True:
        ctry = 'Serbia'
    Slk = st.button('Slovakia')
    if Slk == True:
        ctry = 'Slovakia'
    Svn = st.button('Slovenia')
    if Svn == True:
        ctry = 'Slovenia'
    Spn = st.button('Spain')
    if Spn == True:
        ctry = 'Spain'
    Swed = st.button('Sweden')
    if Swed == True:
        ctry = 'Sweden'
    Swz = st.button('Switzerland')
    if Swz == True:
        ctry = 'Switzerland'

with tabT:
    Trk = st.button('Turkey')
    if Trk == True:
        ctry = 'Turkey'

with tabU:
    Ukra = st.button('Ukraine')
    if Ukra == True:
        ctry = 'Ukraine'
    Uk = st.button('United Kingdom')
    if Uk == True:
        ctry = 'United Kingdom'
