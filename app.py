# streamlit_app.py
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import hydralit_components as hc
import datetime
from streamlit_image_coordinates import streamlit_image_coordinates

# Make it look nice from the start
st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# Specify the primary menu definition
menu_data = [
    {'icon': "far fa-copy", 'label': "Gatherizer"},
    {'icon': "far fa-copy", 'label': "Colorizer"},
    {'icon': "far fa-copy", 'label': "Dispenser"},
]

# Initialize session state
if 'selected_tab' not in st.session_state:
    st.session_state.selected_tab = "Colorizer"


def colorizer_tab():
    st.title("Colorizer Tab")
    st.write("Add Questions and Answers to Google Sheets")

    col1, col2 = st.columns(2)

    if 'data' not in st.session_state:
        st.session_state.data = {
            'profile_type':[],
            'question': [],
            'answer': [],
            'score': []
        }

    with col1:
        profile_type = st.text_input("Profile_type")
        question = st.text_input("Question")
        answer = st.text_input("Possible Answer")
        score = st.selectbox("Profile Score", [1, 2, 3, 4])

        if st.button("Add to Google Sheets"):
            st.session_state.data['profile_type'].append(profile_type)
            st.session_state.data['question'].append(question)
            st.session_state.data['answer'].append(answer)
            st.session_state.data['score'].append(score)
            # Combine the existing data from Google Sheets and new data
            existing_data = conn.read(worksheet="Colorizer", usecols=["question","answer","score"],ttl=0, nrows=10)
            existing_df = pd.DataFrame(existing_data)
            st.write("Existing Data:")
            st.dataframe(existing_df)
            new_df = pd.DataFrame(st.session_state.data)
            st.write("New Data:")
            st.dataframe(new_df)
            combined_df = pd.concat([existing_df, new_df], ignore_index=True)
            st.write("Combined Data:")
            st.dataframe(combined_df)
            conn.update(worksheet="Colorizer", data=combined_df)
            st.success("Data added to Google Sheets")
            st.session_state.data = {
                'profile_type': [],
                'question': [],
                'answer': [],
                'score': []
            }

    
    with col2:
        value = streamlit_image_coordinates("https://images.unsplash.com/photo-1560017487-c44f80136c56?auto=format&fit=crop&q=80&w=300")
        if 'profile' not in st.session_state:
            st.session_state.profile = {
                'x': [],
                'y': [],
                'label': [],
                'text_inputs': []
            }
        if value is not None:
            for key, value in value.items():
                if st.button("Add to Google Sheets"):
                    text_input = st.text_input(f"Text for x={value}")
                    st.session_state.profile['x'].append(value)
                    st.session_state.profile['y'].append(value)  # Add a corresponding 'y' value
                    st.session_state.profile['label'].append("Label for x={}".format(value))  # Add a label
                    st.session_state.profile['text_inputs'].append(text_input)
                else:
                    text_input = ''
                # Check if text_inputs exist and are not empty
                if st.session_state.profile.get('text_inputs'):
                    # for every value inside st.session_state.profile['text_inputs'], print st.metric inside each column equally
                    cola, colb, colc = st.columns(3)
                    text_inputs = st.session_state.profile['text_inputs']

                    for i, text_display in enumerate(text_inputs):
                        if i % 3 == 0:
                            with cola:
                                st.metric(label="profile", value=text_display)
                        elif i % 3 == 1:
                            with colb:
                                st.metric(label="profile", value=text_display)
                        else:
                            with colc:
                                st.metric(label="profile", value=text_display)
                        

            # Loop through the text_inputs and display them in separate columns
            for i, text_display in enumerate(text_inputs):
                if i % 3 == 0:
                    with cola:
                        st.metric(label="profile", value=text_display)
                elif i % 3 == 1:
                    with colb:
                        st.metric(label="profile", value=text_display)
                else:
                    with colc:
                        st.metric(label="profile", value=text_display)
            
        

def gatherizer_tab():
    st.image('resource/logo_forge.png', width=400, use_column_width=True)
    st.title("Gatherizer Tab")
    st.markdown("Gatherizer Tab")
    #create an empty dataframe
    df_answers = pd.DataFrame(columns=['nom', 'prenom', 'mail', 'question', 'answer', 'score'])
    # Add content for the form
    question_data = conn.read(worksheet="Colorizer", usecols=["question","answer","score"],ttl=0, nrows=10)
    question_df = pd.DataFrame(question_data)
    unique_questions = question_df.question.unique()
    
    nom = st.text_input("Nom", key='nom')
    prenom = st.text_input("Prenom", key='prenom')
    mail = st.text_input("Mail", key='mail')
    #append the values of the inputs to the df_answers
    df_answers = df_answers.append({'nom': nom, 'prenom': prenom, 'mail': mail}, ignore_index=True)
    
    for question_people in unique_questions:
        st.write(question_people)
        answer_people = st.selectbox("Answers", question_df[question_df.question == question_people].answer, index=None)
        score = question_df[question_df.answer == answer_people].score.values
        df = pd.DataFrame({'nom': [nom], 'prenom': [prenom], 'mail': [mail],'question': [question_people], 'answer': [answer_people],'score': [score]})
        # Append the data to the df_answers DataFrame
        df_answers = df_answers.append(df, ignore_index=True)

        st.dataframe(df)
        conn.update(worksheet="Gatherizer", data=df_answers)
    # Now, outside the loop, you can display the complete df_answers DataFrame
    st.dataframe(df_answers)
    

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
#
over_theme = {'txc_inactive': 'white','menu_background':'#1c3f4b','txc_active':'#e95459','option_active':''}
# Create the navigation bar
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    #home_name='Home',
    login_name='Logout',
    hide_streamlit_markers=False,
    sticky_nav=True,
    sticky_mode='pinned',
)

# Get the selected tab label from the menu
selected_tab_label = menu_id

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
st.info(f"Menu {menu_id}")

#display the content of st.session_state
st.write(st.session_state)



