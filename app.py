# streamlit_app.py
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read(worksheet="2147061722")
conn.create('Sheet1', 'A1', 'Hello, world!')

st.dataframe(df)
