import streamlit as st

st.header(" lay-out of website or pages")
col1, col2, col3 = st.columns(3)

with col1:
    st.header(" this is column 1(page1)")
    st.image("https://en.wikipedia.org/wiki/Python_%28programming_language%29", width= 200)
    vote1=st.button("Vote for python")

with col2:
    st.header(" this is column 2(page2)")
    st.image("https://www.google.com/imgres?q=Java&imgurl=https%3A%2F%2Fassets.learnvern.com%2Fcourse%2Ficons%2F82651.svg&imgrefurl=https%3A%2F%2Fwww.learnvern.com%2Fcourse%2Fcore-java-programming-tutorial&docid=BdokDBk1O2YChM&tbnid=giQeDlgU0lwXYM&vet=12ahUKEwjr9dCNx_yXAxW5TWwGHdQ0MNwQnPAOegUImAEQAA..i&w=800&h=800&hcb=2&ved=2ahUKEwjr9dCNx_yXAxW5TWwGHdQ0MNwQnPAOegUImAEQAA", width= 200)
    vote1=st.button("Vote for Java")

with col3:
    st.header(" this is column 3(page3)")
    st.image("https://www.google.com/imgres?q=C%2B%2B&imgurl=https%3A%2F%2Fthumb.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F1%2F18%2FISO_C%252B%252B_Logo.svg%2F1280px-ISO_C%252B%252B_Logo.svg.png%3Futm_source%3Dcommons.wikimedia.org%26utm_campaign%3Dindex%26utm_content%3Dthumbnail&imgrefurl=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3AISO_C%252B%252B_Logo.svg&docid=B1epl7HcsRGvDM&tbnid=1q0XLNZj8-3lDM&vet=12ahUKEwjRktybx_yXAxX6SWwGHTy-JaMQnPAOegQINxAA..i&w=1280&h=1441&hcb=2&ved=2ahUKEwjRktybx_yXAxX6SWwGHTy-JaMQnPAOegQINxAA",width= 200)
    vote1=st.button("Vote for C++")

name = st.sidebar.text_input(" What is your name = ")
contact = st.sidebar.number_input(" Enter your phone number: ")

with st.expander(" instructions for python install"):
    st.write("""
1. download python latest package from offical website.
2. download suitable code editor.
3. setup your code editor on system.
4. Test the setup with a small code.

""")

st.markdown("###  this is a markdown with '###'")
st.markdown("#  this is a markdown with '#'")
st.markdown("*  this is a markdown with '*'")
st.markdown("**  this is a markdown with '**'")
st.markdown(">  we write blockquote with this '>'")