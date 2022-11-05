import streamlit as st
import pandas as pd
from utilities.db_functions import download_database,import_mongodb_to_dataframe
from utilities.design_functions import add_bg_from_url,img,hide_menu_style,side_bar_menu,progress_bar,color_survived
from utilities.df_functions import check_col_datatypes,st_show_datatypes,check_null_values,st_show_nullvalues

pd.options.display.float_format = '{:,.3f}'.format # Rounding off the floats to 3rd decimal point
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
                progress_bar()
                anime_df = check_col_datatypes(dataFrame = data_frame)
                df_types = pd.DataFrame(anime_df.dtypes, columns=['Data Type'])
                
                with col2:
                    con_table=df_types.astype(str)
                    st.table(con_table.style.applymap(color_survived, subset=['Data Type']))
                    # st_show_datatypes(dataFrame=anime_df)
                    
            if st.button('Check Null Values'):
                # check_null_values(dataFrame = data_frame)
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
