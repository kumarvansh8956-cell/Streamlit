import streamlit as s

s.title("Streamlit visits introduction")
s.subheader("Select your favorate language")
if s.button("Java"):
    s.success("Java is add in list")
if s.button("Python"):
    s.success("Python is add in list")
if s.button("Ruby"):
    s.success("Ruby is add in list")
if s.button("Rust"):
    s.success("Rust is add in list")
if s.button("Go"):
    s.success("Go is add in list")
if s.button("C++"):
    s.success("C++ is add in list")

carr = s.radio(" Selected your career:",["Java Dev", "Python Dev", " Game Dev", "ML expert", "AI dev"])

carr = s.selectbox(" Selected your career:",["Java Dev", "Python Dev", " Rust", "C++", "Go"])

Year = s.slider("Your Degree years", 0,4,2)
s.write(f" You have a {Year} years degree")