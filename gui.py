import streamlit as st
import pandas as pd
from utilities.db_functions import download_anime_database,import_mongodb_to_dataframe,download_rating_database
from utilities.design_functions import add_bg_from_url,img,hide_menu_style,side_bar_menu,progress_bar,color_survived
from utilities.df_functions import check_col_datatypes,st_show_datatypes,check_null_values,st_show_nullvalues, filter_tv_rows


st.set_page_config(page_title="Anime Recommendation System", page_icon=img)

st.markdown(hide_menu_style, unsafe_allow_html=True)

add_bg_from_url()



# annotated_text(("""
# Before loading, a scraper will run or a data saved in MongoDb will be converted to CSV and then 
# pandas will read it.
# ""","#faa"))

def main():
    st.title("Anime Recommendation System")
    st.button(
    label="Import data from Kaggle",
    on_click = download_anime_database
    )

    options = side_bar_menu()
    if options == "Content-Based Recommendation":
        pass
        

    if options == "Data Cleaning":
        data_frame = import_mongodb_to_dataframe(collection_name="anime")
        st.write(data_frame.head(10))
        
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
                # st.dataframe(anime_df)
                st_show_nullvalues(dataFrame=anime_df)
            if st.button('Filter | TV'):
                # anime_df = check_col_datatypes(dataFrame = data_frame)
                filter_tv_rows(dataFrame=data_frame)
        else:
            st.warning("MongoDB Empty!")
                
    elif options == "Content-Based Recommendation":
        st.subheader("Content-Based Recommendation")
    else:
        st.subheader("Collaborative Recommendation")




if __name__ == '__main__':
    main()
