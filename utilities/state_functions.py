import streamlit as st

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
    
