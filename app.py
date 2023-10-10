# streamlit_app.py
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from barfi import st_barfi, Block
from streamlit_discourse import st_discourse


# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read()

if st.button("New Worksheet"):
    conn.create(worksheet="Orders", data=[0,1])
    st.success("Worksheet Created 🎉")

st.dataframe(df)

import streamlit as st

# Title of the application
st.title("Kanban Board with Streamlit")

# Create three columns for representing Kanban stages
col1, col2, col3 = st.columns(3)

# Create empty lists to store tasks in each column
todo_list = []
doing_list = []
done_list = []

# Widgets to add tasks to columns
with col1:
    st.header("Group1")
    new_task = st.text_input("New Task:")
    if st.button("Add"):
        if new_task:
            todo_list.append(new_task)

with col2:
    st.header("Group2")
    for task in doing_list:
        st.write(f"- {task}")

with col3:
    st.header("Group3")
    for task in done_list:
        st.write(f"- {task}")

# Widgets to move tasks between columns
selected_task = st.selectbox("Select a task to move:", todo_list)
if st.button("Move to 'Doing'"):
    if selected_task in todo_list:
        todo_list.remove(selected_task)
        doing_list.append(selected_task)
elif st.button("Move to 'Done'"):
    if selected_task in doing_list:
        doing_list.remove(selected_task)
        done_list.append(selected_task)

# https://discuss.streamlit.io/t/discourse-component/8061

discourse_url = "discuss.streamlit.io"
topic_id = 8061

st_discourse(discourse_url, topic_id)
