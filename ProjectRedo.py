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

CtrySel = option_menu(None, ["A", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
if CtrySel == "A":
    st.write("Albania")
    st.write("Andorra")
    st.write("Austria")

