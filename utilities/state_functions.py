import streamlit as st

def clean_col():
    st.session_state.clean_columns = True
def null_val():
    st.session_state.check_null_val = True
def filter_tv():
    st.session_state.filter_tv = True
