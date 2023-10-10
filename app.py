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

import streamlit as st

# Titre de l'application
st.title("Tableau Kanban avec Streamlit")

# Créez trois colonnes pour représenter les étapes du Kanban
column1 = st.beta_container()
column2 = st.beta_container()
column3 = st.beta_container()

# Créez des listes vides pour stocker les tâches dans chaque colonne
todo_list = []
doing_list = []
done_list = []

# Widgets pour ajouter des tâches dans les colonnes
with column1:
    st.header("À faire")
    new_task = st.text_input("Nouvelle tâche :")
    if st.button("Ajouter"):
        if new_task:
            todo_list.append(new_task)

with column2:
    st.header("En cours")
    for task in doing_list:
        st.write(f"- {task}")

with column3:
    st.header("Terminé")
    for task in done_list:
        st.write(f"- {task}")

# Widgets pour déplacer des tâches entre les colonnes
selected_task = st.selectbox("Sélectionnez une tâche à déplacer :", todo_list)
if st.button("Déplacer vers 'En cours'"):
    if selected_task in todo_list:
        todo_list.remove(selected_task)
        doing_list.append(selected_task)
elif st.button("Déplacer vers 'Terminé'"):
    if selected_task in doing_list:
        doing_list.remove(selected_task)
        done_list.append(selected_task)
