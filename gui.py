import streamlit as st
from PIL import Image
img = Image.open('anime.jpg')
st.set_page_config(page_title="Anime Recommendation System", page_icon=img)
import pandas as pd
from utilities.db_functions import import_mongodb_to_dataframe,download_database
from utilities.design_functions import add_bg_from_url,hide_menu_style,side_bar_menu,progress_bar,color_survived,info_text,success_text
from utilities.df_functions import replace_col_datatypes,st_show_datatypes,st_show_nullvalues, filter_tv_rows,st_show_head,replace_rating_datatypes,export_cleandata_to_csv,total_shape,import_csv_to_dataframe
from utilities.state_functions import clean_col,null_val,filter_tv,rating_val,null_tv,replace_rating,data_count,csv_file,anime_data,drop_na_func,drop_col_func,set_delimeter_func,hot_encode_func,rating_data,na_data_func,sum_null_func,random_user_func, get_user_func,get_anime_user_id_func,sort_matrix_func,drop_orphan_func,create_matrix_func,user_rating_func,dot_product_func,set_index_func,get_weight_func,sort_desc_func,top_10_val_func
from utilities.content_filtering import drop_columns,drop_na_columns,set_delimeter,hot_encode_dataframe,get_user_df,generate_random_user,get_anime_in_user_df,sort_anime_id,drop_orphan_anime,user_genre_matrix,user_rating,dot_product,set_index,get_weighted_avg,sort_desc_fun,top_10_recc



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

        if 'random_user' not in st.session_state:
            st.session_state.random_user = False
        
        if 'get_user' not in st.session_state:
            st.session_state.get_user = False
        
        if 'get_anime_user_id' not in st.session_state:
            st.session_state.get_anime_user_id = False
        
        if 'drop_orphan' not in st.session_state:
            st.session_state.drop_orphan = False
        
        if 'sort_matrix' not in st.session_state:
            st.session_state.sort_matrix = False
        
        if 'create_matrix' not in st.session_state:
            st.session_state.create_matrix = False
        
        if 'user_rating' not in st.session_state:
            st.session_state.user_rating = False
        
        if 'dot_product' not in st.session_state:
            st.session_state.dot_product = False
        
        if 'set_index' not in st.session_state:
            st.session_state.set_index = False
        
        if 'get_weight' not in st.session_state:
            st.session_state.get_weight = False
        
        if 'sort_desc' not in st.session_state:
            st.session_state.sort_desc = False
        
        if 'top_10_val' not in st.session_state:
            st.session_state.top_10_val = False

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
            print(f"{hot_encode_data=}")
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
        
        st.button('Random User Generator', on_click = random_user_func)
        if st.session_state.random_user:
            user_num = generate_random_user(cleaned_rating_data)
            st.write(user_num)
        
        st.button('Get User', on_click = get_user_func)
        if st.session_state.get_user:
            user_df = get_user_df(cleaned_rating_data,user_num)
            # print(f"{user_df=}")
            st_show_head(user_df)
            
        
        st.button('Get Anime User ID', on_click = get_anime_user_id_func)
        if st.session_state.get_anime_user_id:
            user_id_df = get_anime_in_user_df(cleaned_anime_data,user_df)
            hidden_encode = get_anime_in_user_df(hot_encode_data,user_df)
            # print(f"{hidden_encode=}")
            st_show_head(user_id_df)
        
        st.button('Sort Anime Matrix', on_click = sort_matrix_func)
        if st.session_state.sort_matrix:
            sort_anime = sort_anime_id(user_id_df)
            hidden_sorted_encode = sort_anime_id(hidden_encode)
            # print(f"{hidden_sorted_encode=}")
            st_show_head(sort_anime)
        
        st.button('Drop Orphan Anime', on_click = drop_orphan_func)
        if st.session_state.drop_orphan:
            drop_orphan_df = drop_orphan_anime(user_df)
            st_show_head(drop_orphan_df)
        
        st.button('Create Genre Matrix', on_click = create_matrix_func)
        if st.session_state.create_matrix:
            matrix_df = user_genre_matrix(sort_anime)
            hidden_matrix_encode = user_genre_matrix(hidden_sorted_encode)
            # print(hidden_matrix_encode)
            st_show_head(matrix_df)

        st.button('Rating Dataframe', on_click = user_rating_func)
        if st.session_state.user_rating:
            rating_user_df = user_rating(drop_orphan_df)
            st_show_head(rating_user_df)
        
        st.button('Dot Product', on_click = dot_product_func)
        if st.session_state.dot_product:
            weight = dot_product(hidden_matrix_encode,rating_user_df)
            # st_show_head(dot_product_df)
            st.write(weight)

        st.button('Set Index', on_click = set_index_func)
        if st.session_state.set_index:
            index_df = set_index(cleaned_anime_data)
            hidden_index_encoded = set_index(hot_encode_data)
            st_show_head(index_df)
        
        st.button('Get Average Weightage', on_click = get_weight_func)
        if st.session_state.get_weight:
            avg_df = get_weighted_avg(recommendation_table=hidden_index_encoded,weights=weight)
            st_show_head(avg_df)
        
        st.button('Sort(Descending order)', on_click = sort_desc_func)
        if st.session_state.sort_desc:
            sort_desc_df = sort_desc_fun(recommendation_series=avg_df)
            st_show_head(sort_desc_df)
        
        st.button('Get Top 10', on_click = top_10_val_func)
        if st.session_state.top_10_val:
            recc_df = top_10_recc(anime_df=hot_encode_data, recommendations=sort_desc_df)
            print(f"{recc_df=}")
            # recc_df_new = top_10_recc(anime_df=cleaned_anime_data, recommendations=sort_desc_df)
            st.write(recc_df)
            # st_show_head(recc_df)


    else:
        st.subheader("Collaborative Recommendation")




if __name__ == '__main__':
    main()
