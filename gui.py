import streamlit as st
from PIL import Image
from utilities.utilities import download_database,import_data_to_mongo

img = Image.open('anime.jpg')
st.set_page_config(page_title="Anime Recommendation System", page_icon=img)

hide_menu_style = """ 
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

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
add_bg_from_url()

from utilities.utilities import upload_file,side_bar_menu,check_col_datatypes,st_show_datatypes,check_null_values,st_show_nullvalues
from annotated_text import annotated_text

st.button(
    label="Download data as from Kaggle",
    on_click = download_database
    )

st.button(
    label="Import DataFrom Mongo",
    on_click = import_data_to_mongo
    )


annotated_text(("""
Before loading, a scraper will run or a data saved in MongoDb will be converted to CSV and then 
pandas will read it.
""","#faa"))


def main():
    st.title("Anime Recommendation System")
    options = side_bar_menu()

    if options == "Data Cleaning":
        data_frame = upload_file()
        if data_frame is not None and not data_frame.empty:
            st.subheader("Data Cleaning")
            anime_df = check_col_datatypes(dataFrame = data_frame)
            if st.button('Clean columns datatypes'):
                anime_df = check_col_datatypes(dataFrame = data_frame)
                import time
                my_bar = st.progress(0)

                for percent_complete in range(100):
                    time.sleep(0.1)
                    my_bar.progress(percent_complete + 1)
                st_show_datatypes(anime_df)

            if st.button('Check Null Values'):
                anime_df = check_null_values(dataFrame = data_frame)
                import time
                my_bar = st.progress(0)

                for percent_complete in range(100):
                    time.sleep(0.1)
                    my_bar.progress(percent_complete + 1)
                st_show_nullvalues(anime_df)
                
    elif options == "Content-Based Recommendation":
        st.subheader("Content-Based Recommendation")
    else:
        st.subheader("Collaborative Recommendation")
        st.subheader("Powered by Streamlit and Pandas")




if __name__ == '__main__':
    main()
