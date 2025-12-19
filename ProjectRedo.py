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

CtrySel = option_menu(None, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V'], 
    icons=['globe-europe-africa', 'globe-europe-africa', 'globe-europe-africa', 'globe-europe-africa', 'globe-europe-africa', 
           'globe-europe-africa', 'globe-europe-africa', 'globe-europe-africa', 'globe-europe-africa', 'globe-europe-africa', 
           'globe-europe-africa', 'globe-europe-africa', 'globe-europe-africa', 'globe-europe-africa', 'globe-europe-africa', 
           'globe-europe-africa', 'globe-europe-africa', 'globe-europe-africa', 'globe-europe-africa', ], menu_icon = "cast",
           orientation="horizontal")
if CtrySel == "A":
    st.write("Albania")
    st.write("Andorra")
    st.write("Austria")
