# Importing Python Libraries
import pandas as pd
import streamlit as st

pd.options.display.float_format = '{:,.3f}'.format # Rounding off the floats to 3rd decimal point

# def upload_file():
#     import streamlit as st
#     import streamlit.components.v1 as stc
#     uploaded_file = st.file_uploader("Choose a file")
#     if uploaded_file is not None:
#         # Can be used wherever a "file-like" object is accepted:
#         dataframe = pd.read_csv(uploaded_file)
#         st.write(dataframe.head(10))
#         return dataframe
#     else:
#         return None

def check_col_datatypes(dataFrame):
    import numpy as np
    # replace animes where the number of episodes are unknown into nan and then convert\
    #  everything to float
    dataFrame["episodes"].replace({"Unknown": "nan", "unknown": "nan"}, inplace=True)
    dataFrame["episodes"] = dataFrame["episodes"].astype("float")

    dataFrame["anime_id"].replace({"Unknown": "nan", "unknown": "nan"}, inplace=True)
    dataFrame["anime_id"] = dataFrame["anime_id"].astype("int")

    dataFrame["rating"].replace({"Unknown": "nan", "unknown": "nan"}, inplace=True)
    dataFrame["rating"] = pd.to_numeric(dataFrame['rating'])

    dataFrame["members"].replace({"Unknown": "nan", "unknown": "nan"}, inplace=True)
    dataFrame["members"] = dataFrame["members"].astype("int")
    return dataFrame

def st_show_head(dataFrame):
    st.write(dataFrame.head(10))

def st_show_datatypes(dataFrame):
    df_types = pd.DataFrame(dataFrame.dtypes, columns=['Data Type'])
    st.table(df_types.astype(str))

def check_null_values(dataFrame):
    # Check which rows have missing values
    null_val = pd.isnull(dataFrame).sum()
    return null_val
    
def st_show_nullvalues(dataFrame):
    import streamlit as st
    null_df = check_null_values(dataFrame=dataFrame)
    st.table(null_df.astype(str))
    return None
    
    # st.table(con_table.style.applymap(color_nullval, subset=['Data Type']))


# def check_missing_values(dataFrame):
#     test_df=dataFrame.isnull().sum()
#     return test_df

def filter_tv_rows(dataFrame):
    dataFrame = dataFrame[dataFrame["type"]== "TV"]
    st.write(dataFrame.head(10))
    return None