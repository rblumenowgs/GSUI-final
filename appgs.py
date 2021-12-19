import streamlit as st
from streamlit.state.session_state import SessionState
# Custom imports 
from multipage2gs import MultiPage
#from multipage import save, MultiPage, start_app, clear_cache
import mainui, usertraining, datavalidation, DBDashboardStreamlit # import your pages here

from PIL import Image

from functions import *

# Create an instance of the app 
gsui = MultiPage()

ico = Functions.set_svg_icon('GSLogoico.jpg')

image=Image.open(ico)

st.set_page_config(layout="wide",page_title='Globalstratos UI', page_icon=image)

# SessionState.selectedsite = 'Dagara'

# Add all your applications (pages) here
gsui.add_page("Main Globalstratos UI", mainui.gsui)
gsui.add_page("Dashboard", DBDashboardStreamlit.dbrd)
gsui.add_page("Data validation", datavalidation.validation)
gsui.add_page("Show me how", usertraining.train)

# The main app
gsui.run()