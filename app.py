# streamlit_app.py
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from barfi import st_barfi, Block

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read()

if st.button("New Worksheet"):
    conn.create(worksheet="Orders", data=[0,1])
    st.success("Worksheet Created 🎉")

st.dataframe(df)
