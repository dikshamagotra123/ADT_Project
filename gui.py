import streamlit as st
from PIL import Image
img = Image.open('anime.jpg')
st.set_page_config(page_title="Anime Recommendation System", page_icon=img)
import pandas as pd
from utilities.db_functions import import_mongodb_to_dataframe,download_database
from utilities.design_functions import add_bg_from_url,hide_menu_style,side_bar_menu,progress_bar,color_survived,info_text,success_text
from utilities.df_functions import replace_col_datatypes,st_show_datatypes,st_show_nullvalues, filter_tv_rows,st_show_head,replace_rating_datatypes,export_cleandata_to_csv,total_shape,import_csv_to_dataframe
from utilities.state_functions import clean_col,null_val,filter_tv,rating_val,null_tv,replace_rating,data_count,csv_file



st.markdown(hide_menu_style, unsafe_allow_html=True)

add_bg_from_url()

def main():
    st.title("Anime Recommendation System")
    st.button(label="Import Anime Data from Kaggle", on_click = download_database)

    options = side_bar_menu()

    if options == "Data Cleaning":
        data_frame = import_mongodb_to_dataframe(collection_name="anime")
        rating_df = import_csv_to_dataframe(folder_name="archive",csv_name="rating.csv") 

        if not data_frame.empty:
            st.write(data_frame.head(10))
            if 'clean_columns' not in st.session_state:
                st.session_state.clean_columns = False

            if 'check_null_val' not in st.session_state:
                st.session_state.check_null_val = False

            if 'filter_tv_val' not in st.session_state:
                st.session_state.filter_tv_val = False

            if 'null_tv_val' not in st.session_state:
                st.session_state.null_tv_val = False

            st.subheader("Data Cleaning")
            col1,col2 = st.columns(2)
            with col1:
                st_show_datatypes(dataFrame=data_frame)
            st.button('Clean columns datatypes', on_click=clean_col)
            if st.session_state.clean_columns:
                progress_bar()
                anime_df = replace_col_datatypes(dataFrame = data_frame)
                df_types = pd.DataFrame(anime_df.dtypes, columns=['Data Type'])
                
                with col2:
                    con_table=df_types.astype(str)
                    st.table(con_table.style.applymap(color_survived, subset=['Data Type']))
                    
            st.button('Check Null Values', on_click=null_val)
            if st.session_state.check_null_val:
                progress_bar()
                st_show_nullvalues(dataFrame=anime_df)
            
            st.button('Filter | TV', on_click=filter_tv)
            if st.session_state.filter_tv_val:
                progress_bar()
                tv_df = filter_tv_rows(dataFrame=anime_df)
                st_show_head(tv_df)

            st.button('Null Values Check | TV', on_click=null_tv)
            if st.session_state.null_tv_val:
                progress_bar()
                tv_df = filter_tv_rows(dataFrame=anime_df) #TODO: Diksha 
                st_show_nullvalues(dataFrame=tv_df)  
                st.caption(info_text)         
        else:
            st.warning("MongoDB Anime Empty!")
        if 'rating_data' not in st.session_state:
            st.session_state.rating_data = False
        st.button("Import Ratings Data from Kaggle", on_click = rating_val)
        if st.session_state.rating_data:
            st.write(rating_df.head(10))
            if 'replace_rating_val' not in st.session_state:
                st.session_state.replace_rating_val = False
            
            if 'count_data' not in st.session_state:
                st.session_state.count_data = False
            
            if 'export_csv' not in st.session_state:
                st.session_state.export_csv = False
            
            st.button('Replace Rating Datatypes', on_click=replace_rating)
            if st.session_state.replace_rating_val:
                progress_bar()
                replace_df = replace_rating_datatypes(dataFrame=rating_df)
                st_show_head(replace_df)

            st.button('Total Count of Data', on_click=data_count)
            if st.session_state.count_data:
                progress_bar()
                st.write(total_shape(dataFrame=rating_df))
            
            st.button('Export Clean CSV Files', on_click=csv_file)
            if st.session_state.export_csv:
                progress_bar()
                export_cleandata_to_csv(data_frame,rating_df)
                st.caption(success_text)
            

        else:
            st.warning("MongoDB Anime Empty!")
                
    elif options == "Content-Based Recommendation":
        st.subheader("Content-Based Recommendation")
    else:
        st.subheader("Collaborative Recommendation")




if __name__ == '__main__':
    main()
