import streamlit as st
from PIL import Image
img = Image.open('anime.jpg')
st.set_page_config(page_title="Anime Recommendation System", page_icon=img)

import pandas as pd
from utilities.db_functions import download_database,import_mongodb_to_dataframe
from utilities.design_functions import add_bg_from_url,hide_menu_style,side_bar_menu,progress_bar,color_survived
from utilities.df_functions import check_col_datatypes,st_show_datatypes,st_show_nullvalues, filter_tv_rows



st.markdown(hide_menu_style, unsafe_allow_html=True)

add_bg_from_url()

def main():
    st.title("Anime Recommendation System")
    st.button(
        label="Import Data from Kaggle",
        on_click = download_database
        )
    

    options = side_bar_menu()
    if options == "Data Cleaning":
        data_frame = import_mongodb_to_dataframe(collection_name="anime")
        # rating_df = import_mongodb_to_dataframe(collection_name="rating")
        st.write(data_frame.head(10))
        # st.write(rating_df.head(10))
        if not data_frame.empty:
            st.subheader("Data Cleaning")
            col1,col2 = st.columns(2)
            with col1:
                st_show_datatypes(dataFrame=data_frame)
            if st.button('Clean columns datatypes'):
                progress_bar()
                anime_df = check_col_datatypes(dataFrame = data_frame)
                df_types = pd.DataFrame(anime_df.dtypes, columns=['Data Type'])
                
                with col2:
                    con_table=df_types.astype(str)
                    st.table(con_table.style.applymap(color_survived, subset=['Data Type']))
                    # st_show_datatypes(dataFrame=anime_df)
                    
            if st.button('Check Null Values'):
                anime_df = check_col_datatypes(dataFrame = data_frame)
                st_show_nullvalues(dataFrame=anime_df)
            if st.button('Filter | TV'):
                anime_df = check_col_datatypes(dataFrame = data_frame)
                filter_tv_rows(dataFrame=anime_df)       
        else:
            st.warning("MongoDB Empty!")
        
        # if not rating_df.empty:
        #     st.write(data_frame.head(10))
        #     pass
        # else:
        #     st.warning("MongoDB Empty!")
                
    elif options == "Content-Based Recommendation":
        st.subheader("Content-Based Recommendation")
    else:
        st.subheader("Collaborative Recommendation")




if __name__ == '__main__':
    main()
