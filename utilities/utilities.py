# Importing Python Libraries
from xmlrpc.client import boolean
import pandas as pd
import numpy as np

pd.options.display.float_format = '{:,.3f}'.format # Rounding off the floats to 3rd decimal point

def upload_file():
    import streamlit as st
    import streamlit.components.v1 as stc
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe.head(10))
        return dataframe
    else:
        return None

def side_bar_menu():
    import streamlit as st
    menu = ["Data Cleaning","Content-Based Recommendation","Collaborative Recommendation"]
    options = st.sidebar.selectbox("Menu",menu)
    return options

def check_col_datatypes(dataFrame):
    # replace animes where the number of episodes are unknown into nan and then convert\
    #  everything to float
    dataFrame["episodes"].replace({"Unknown": "nan", "unknown": "nan"}, inplace=True)
    dataFrame["episodes"] = dataFrame["episodes"].astype("float")
    return dataFrame
def color_survived(val):
    color = 'green' if val else 'red'
    return f'background-color: {color}'

def st_show_datatypes(dataFrame):
    import streamlit as st
    col1,col2=st.columns(2)
    df_types = pd.DataFrame(dataFrame.dtypes, columns=['Data Type'])
    with col1:
        st.write(df_types.astype(str))

    with col2:
        # st.dataframe(df_types.style.applymap(color_survived, subset=['Data Type']))
        con_table=df_types.astype(str)
        st.table(con_table.style.applymap(color_survived, subset=['Data Type']))

def check_null_values(dataFrame):
    # Check which rows have missing values
    dataFrame.isnull().any()
    return dataFrame
#Adding a comment
def st_show_nullvalues(dataFrame):
    import streamlit as st
    import ast
    df_types = pd.DataFrame(dataFrame.dtypes, columns=['Data Type'])
    st.write(df_types.astype(bool))

def download_database():
    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file('CooperUnion/anime-recommendations-database','anime.csv')
    # api.dataset_download_file('CooperUnion/anime-recommendations-database','rating.csv')
    return None

def import_data_to_mongo():
    import csv
    import pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["anime_db"]
    mycol = mydb["anime"]
    #CSV to JSON Conversion
    csvfile = open('archive/anime.csv', 'r')
    reader = csv.DictReader( csvfile )
    header= ["anime_id", "name", "genre", "type", "episodes", "rating", "members"]

    for each in reader:
        row={}
        for field in header:
            row[field]=each[field]
            
        print(row)
        mycol.insert_one(row)
