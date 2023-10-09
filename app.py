# streamlit_app.py
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read(worksheet="2147061722")

if st.button("New Worksheet"):
    conn.create(worksheet="1874208743", data=orders)
    st.success("Worksheet Created 🎉")



st.dataframe(df)
