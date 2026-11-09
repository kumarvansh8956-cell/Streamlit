import streamlit as st

st.title("Programming Languages")
st.subheader(" Welcome to your preferable language understanding.")

lang = st.selectbox("Select your language:", ["java","C++","Python","Rust","Go","Ruby"])

if not lang :
    st.text(" Please select at least one language")
else:
    st.success(f" You selected {lang} language")
    st.text("Nice choice Sir...")