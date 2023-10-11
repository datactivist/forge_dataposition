# streamlit_app.py
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import hydralit_components as hc
import datetime

# Make it look nice from the start
st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

# Specify the primary menu definition
menu_data = [
    {'icon': "far fa-copy", 'label': "Colorizer"},
    {'icon': "far fa-copy", 'label': "Gatherizer"},
    {'icon': "far fa-copy", 'label': "Dispenser"},
]

# Define the content for the tabs
def colorizer_tab():
    st.title("Colorizer Tab")
    # Add content for the Colorizer tab here

def gatherizer_tab():
    st.title("Gatherizer Tab")
    # Add content for the Gatherizer tab here

def dispenser_tab():
    st.title("Dispenser Tab")
    # Add content for the Dispenser tab here

# Create a function to display the selected tab content
def display_tab_content(tab_label):
    if tab_label == "Colorizer":
        colorizer_tab()
    elif tab_label == "Gatherizer":
        gatherizer_tab()
    elif tab_label == "Dispenser":
        dispenser_tab()

# Create the navigation bar
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    home_name='Home',
    login_name='Logout',
    hide_streamlit_markers=False,
    sticky_nav=True,
    sticky_mode='pinned',
)

# Get the selected tab label from the menu
selected_tab_label = st.session_state.get('selected_tab', 'Colorizer')

# Display the selected tab content
display_tab_content(selected_tab_label)

if st.button('Click me'):
    st.info('You clicked at: {}'.format(datetime.datetime.now()))

if st.sidebar.button('Click me too'):
    st.info('You clicked at: {}'.format(datetime.datetime.now()))

# Store the selected tab in the session state
if selected_tab_label != st.session_state.selected_tab:
    st.session_state.selected_tab = selected_tab_label

# Get the id of the menu item clicked
st.info(f"Selected tab: {selected_tab_label}")



