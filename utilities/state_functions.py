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

def random_user_func():
    st.session_state.random_user = True

def get_user_func():
    st.session_state.get_user = True

def get_anime_user_id_func():
    st.session_state.get_anime_user_id = True

def drop_orphan_func():
    st.session_state.drop_orphan = True

def sort_matrix_func():
    st.session_state.sort_matrix = True

def create_matrix_func():
    st.session_state.create_matrix = True

def user_rating_func():
    st.session_state.user_rating = True

def dot_product_func():
    st.session_state.dot_product = True

def set_index_func():
    st.session_state.set_index = True

def get_weight_func():
    st.session_state.get_weight = True

def sort_desc_func():
    st.session_state.sort_desc = True
    
def top_10_val_func():
    st.session_state.top_10_val = True

#collaborative_filtering state function

def rm_info_func():
    st.session_state.rm_info = True

def load_data_func():
    st.session_state.load_data = True

def drop_na_col_func():
    st.session_state.drop_na_coll = True

def load_df_surprise_func():
    st.session_state.load_df_surprise = True

def pred_data_func():
    st.session_state.pred_data = True

def param_func():
    st.session_state.param = True

def svd_func():
    st.session_state.svd = True

def pred_rating_func():
    st.session_state.pred_rating = True

def dump_func():
    st.session_state.dump = True