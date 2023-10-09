# streamlit_app.py
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read(worksheet="Gatherizer")

# Print results.
for row in df.itertuples():
    st.write(f"{row.id} has a :{row.nom}:")
