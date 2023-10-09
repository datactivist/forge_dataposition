# streamlit_app.py
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read(worksheet="Gatherizer",ttl="10m",usecols=[0, 1],nrows=1)

# Print results.
for row in df.itertuples():
    st.write(f"{row.id} has a :{row.name}:")
