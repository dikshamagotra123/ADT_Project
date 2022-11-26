def customize_button(label,on_click):
    import streamlit as st
    st.markdown(""" 
    <style>
    div.stButton > button:first-child {
        background-color: #764E81;
        color:#ffffff;
        font-size:18px;
        height:3em;
        width:100%;
        border-radius:20px 20px 20px 20px;
    }
    div.stButton > button:hover {
        background-color: #575B86;
        color:#FDFCFC;
        font-size:18px;
        height:3em;
        width:100%;
        border-radius:20px 20px 20px 20px;
    }
    </style>""", unsafe_allow_html=True)    

    col1, col2, col3 = st.columns((1, 2, 1))

    with col3:
        pass
    with col1:
        pass
    with col2 :
        st.button(label=label, on_click = on_click)