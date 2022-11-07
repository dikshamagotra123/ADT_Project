import streamlit as st

# Data cleaning state functions

def clean_col():
    st.session_state.clean_columns = True

def null_val():
    st.session_state.check_null_val = True

def filter_tv():
    st.session_state.filter_tv_val = True

def rating_val():
    st.session_state.rating_data = True

def null_tv():
    st.session_state.null_tv_val = True

def replace_rating():
    st.session_state.replace_rating_val = True

def data_count():
    st.session_state.count_data = True

def csv_file():
    st.session_state.export_csv = True

# Content based filtering state functions

def anime_data():
    st.session_state.anime_data_val = True

def drop_col_func():
    st.session_state.drop_col = True

def drop_na_func():
    st.session_state.drop_na_col = True
    
def set_delimeter_func():
    st.session_state.set_delimeter = True

def hot_encode_func():
    st.session_state.hot_encode = True

def rating_data():
    st.session_state.rating_data_val = True

def na_data_func():
    st.session_state.na_data = True

def sum_null_func():
    st.session_state.sum_null_val = True
