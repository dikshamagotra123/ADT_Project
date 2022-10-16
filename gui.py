import streamlit as st
from PIL import Image
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

from utilities.utilities import side_bar_menu,check_col_datatypes,st_show_datatypes,check_null_values,st_show_nullvalues,download_database,progress_bar,import_mongodb_to_dataframe
from annotated_text import annotated_text


# annotated_text(("""
# Before loading, a scraper will run or a data saved in MongoDb will be converted to CSV and then 
# pandas will read it.
# ""","#faa"))


def main():
    st.title("Anime Recommendation System")
    st.button(
    label="Import data from Kaggle",
    on_click = download_database
    )

    options = side_bar_menu()
    if options == "Content-Based Recommendation":
        pass
        

    if options == "Data Cleaning":
        data_frame = import_mongodb_to_dataframe()
        st.write(data_frame.head(10))
        
        if not data_frame.empty:
            st.subheader("Data Cleaning")
            col1,col2 = st.columns(2)
            with col1:
                st_show_datatypes(dataFrame=data_frame)
            if st.button('Clean columns datatypes'):
                anime_df = check_col_datatypes(dataFrame = data_frame)
                progress_bar()
                with col2:
                    st_show_datatypes(dataFrame=anime_df)
                    
            if st.button('Check Null Values'):
                check_null_values(dataFrame = data_frame)
                st_show_nullvalues(data_frame)
        else:
            st.warning("MongoDB Empty!")
                
    elif options == "Content-Based Recommendation":
        st.subheader("Content-Based Recommendation")
    else:
        st.subheader("Collaborative Recommendation")
        st.subheader("Powered by Streamlit and Pandas")




if __name__ == '__main__':
    main()
