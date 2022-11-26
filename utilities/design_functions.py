import streamlit as st

def progress_bar():
    import streamlit as st
    import time
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.001)
        my_bar.progress(percent_complete + 1)
    return None

def color_survived(val):
    color = '#365B6D' if val == 'object' else '#C1946C'
    return f'background-color: {color}'

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: linear-gradient(90deg, rgba(166,144,177,1) 0%, rgba(128,120,159,1) 35%, rgba(177,152,178,1) 100%);
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
    )

hide_menu_style = """ 
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

def side_bar_menu():
    import streamlit as st
    menu = ["Data Cleaning","Content-Based Recommendation","Collaborative Recommendation"]
    options = st.sidebar.selectbox("Menu",menu)
    return options
