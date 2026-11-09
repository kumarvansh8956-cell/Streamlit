import streamlit as st
st.header("Taking uncontroable Inputs")
st.subheader("For text")
name = st.text_input(" Your name?")
if name:
    st.success("Welcome Mr.{name}. It plesure to meet you")

st.subheader(" For numbers")

exp = st.number_input("How many years experence", min_value= 1, max_value= 20, step= 1)
if exp:
    st.success(f" You have {exp} years experence")

st.subheader(" for Date of Birth")
DoB = st.date_input(" your date of birth")
if DoB:
    st.success(f"DOB is {DoB}")