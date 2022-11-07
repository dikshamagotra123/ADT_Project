import streamlit as st
from PIL import Image
img = Image.open('anime.jpg')
st.set_page_config(page_title="Anime Recommendation System", page_icon=img)
import pandas as pd
from utilities.db_functions import import_mongodb_to_dataframe,download_database
from utilities.design_functions import add_bg_from_url,hide_menu_style,side_bar_menu,progress_bar,color_survived,info_text,success_text
from utilities.df_functions import replace_col_datatypes,st_show_datatypes,st_show_nullvalues, filter_tv_rows,st_show_head,replace_rating_datatypes,export_cleandata_to_csv,total_shape,import_csv_to_dataframe
from utilities.state_functions import clean_col,null_val,filter_tv,rating_val,null_tv,replace_rating,data_count,csv_file,anime_data,drop_na_func,drop_col_func,set_delimeter_func,hot_encode_func,rating_data,na_data_func,sum_null_func
from utilities.content_filtering import drop_columns,drop_na_columns,set_delimeter,hot_encode_dataframe,drop_na_values,sum_null_values



st.markdown(hide_menu_style, unsafe_allow_html=True)

add_bg_from_url()

def main():
    st.title("Anime Recommendation System")

    options = side_bar_menu()

    if options == "Data Cleaning":
        st.button(label="Import Anime Data from Kaggle", on_click = download_database)
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
        cleaned_anime_data = import_csv_to_dataframe(folder_name="datasets",csv_name="cleaned_anime.csv")
        if 'anime_data_val' not in st.session_state:
            st.session_state.anime_data_val = False
        
        if 'drop_col' not in st.session_state:
            st.session_state.drop_col = False
        
        if 'drop_na_col' not in st.session_state:
            st.session_state.drop_na_col = False
        
        if 'set_delimeter' not in st.session_state:
            st.session_state.set_delimeter = False
        
        if 'hot_encode' not in st.session_state:
            st.session_state.hot_encode = False

        st.button('Import Anime Cleaned Data', on_click = anime_data)
        if st.session_state.anime_data_val:
            st_show_head(cleaned_anime_data)
        
        st.button('Drop Columns', on_click = drop_col_func)
        if st.session_state.drop_col:
            drop_data = drop_columns(cleaned_anime_data)
            st_show_head(drop_data)
        
        st.button('Drop NA Values', on_click = drop_na_func)
        if st.session_state.drop_na_col:
            print("HEREEEE")
            # drop_na_columns(drop_data)
            drop_data.dropna(subset=["genre"], inplace=True)
            st.write(drop_data)
        
        st.button('Set Delimeter', on_click = set_delimeter_func)
        if st.session_state.set_delimeter:
            print("DELIMITER")
            set_delimeter_data = set_delimeter(drop_data)
            st_show_head(set_delimeter_data)
        
        st.button('Hot Encode Dataframe', on_click = hot_encode_func)
        if st.session_state.hot_encode:
            hot_encode_data = hot_encode_dataframe(set_delimeter_data)
            print(type(hot_encode_data))
            # st.table(hot_encode_data)
        
        cleaned_rating_data = import_csv_to_dataframe(folder_name="datasets",csv_name="cleaned_rating.csv")
        if 'rating_data_val' not in st.session_state:
            st.session_state.rating_data_val = False
        
        if 'na_data' not in st.session_state:
            st.session_state.na_data = False
        
        if 'sum_null_val' not in st.session_state:
            st.session_state.sum_null_val = False
        
        st.button('Import Rating Cleaned Data', on_click = rating_data)
        if st.session_state.rating_data_val:
            st_show_head(cleaned_rating_data)
        
        st.button('Drop rating NA values', on_click = na_data_func)
        if st.session_state.na_data:
            cleaned_rating_data.dropna(inplace=True)
            st_show_head(cleaned_rating_data)
        
        st.button('Sum rating Null values', on_click = sum_null_func)
        if st.session_state.sum_null_val:
            st_show_nullvalues(cleaned_rating_data)
    else:
        st.subheader("Collaborative Recommendation")




if __name__ == '__main__':
    main()
