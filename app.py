import streamlit as st

st.set_page_config(page_title="Custom Title Here")

st.write("hello world!")

x = st.slider("X:", 0, 100, 50)

st.write(x**2)
