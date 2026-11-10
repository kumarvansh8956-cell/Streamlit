import streamlit as st
import pandas as pd
import Read_and_exploration as rex

st.title(" Data frame analysis")

data =  st.file_uploader("Upload your .cvs dataset for analysis:", type=["csv"])
if data:
    df = rex.read_Data(data)
    st.subheader("Data preview")
    st.dataframe(df)
    st.subheader("Dataset details")
    st.write(df.describe())
    st.write(df.info())
    st.subheader("Dataframe unique")

    for da in df:
        st.write(df[da].unique())