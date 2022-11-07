import streamlit as st
from PIL import Image
img = Image.open('anime.jpg')
st.set_page_config(page_title="Anime Recommendation System", page_icon=img)

import pandas as pd
from utilities.db_functions import download_database,import_mongodb_to_dataframe
from utilities.design_functions import add_bg_from_url,hide_menu_style,side_bar_menu,progress_bar,color_survived
from utilities.df_functions import check_col_datatypes,st_show_datatypes,st_show_nullvalues, filter_tv_rows
from utilities.state_functions import clean_col,null_val,filter_tv



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

            if 'clean_columns' not in st.session_state:
                st.session_state.clean_columns = False

            if 'check_null_val' not in st.session_state:
                st.session_state.check_null_val = False

            if 'filter_tv' not in st.session_state:
                st.session_state.filter_tv = False

            st.subheader("Data Cleaning")
            col1,col2 = st.columns(2)
            with col1:
                st_show_datatypes(dataFrame=data_frame)
            st.button('Clean columns datatypes', on_click=clean_col)
            if st.session_state.clean_columns:
                progress_bar()
                anime_df = check_col_datatypes(dataFrame = data_frame)
                df_types = pd.DataFrame(anime_df.dtypes, columns=['Data Type'])
                
                with col2:
                    con_table=df_types.astype(str)
                    st.table(con_table.style.applymap(color_survived, subset=['Data Type']))
                    # st_show_datatypes(dataFrame=anime_df)
                    
            st.button('Check Null Values', on_click=null_val)
            if st.session_state.check_null_val:
                # anime_df = check_col_datatypes(dataFrame = data_frame)
                st_show_nullvalues(dataFrame=anime_df)
            st.button('Filter | TV', on_click=filter_tv)
            if st.session_state.filter_tv:
                # anime_df = check_col_datatypes(dataFrame = data_frame)
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
