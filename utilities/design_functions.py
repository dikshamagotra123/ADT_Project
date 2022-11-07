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
    color = 'green' if val == 'object' else 'red'
    return f'background-color: {color}'

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/premium-vector/abstract-blur-background-with-pastel-color-colorful-wallpaper_592487-785.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
    )

info_text = "It seems we still have 10 rows with missing genre values and also 116 rows with missing rating values. For the content based filtering, the genre of the show will be required so when it is time to develop the content based filtering model I will be dropping those 10 rows with missing genre values. On the other hand, with the collaborative filtering system, I am not required to used the genre values at all so I will simply use the whole dataset without the genre column."

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

def color_nullval(val):
    color = 'green' if val == True else 'red'
    return f'background-color: {color}'
