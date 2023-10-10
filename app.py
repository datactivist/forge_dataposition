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




add = Block(name='Addition')
sub = Block(name='Subtraction')
mul = Block(name='Multiplication')
div = Block(name='Division')

barfi_result = st_barfi(base_blocks= [add, sub, mul, div])
# or if you want to use a category to organise them in the frontend sub-menu
barfi_result = st_barfi(base_blocks= {'Op 1': [add, sub], 'Op 2': [mul, div]})
