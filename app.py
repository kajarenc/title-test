import streamlit as st

st.set_page_config(page_title="Custom Title Here")

st.write("hello world!")

x = st.slider("X:", 0, 100, 50)

st.write(x**2)

st.write(st.config.get_option("server.enableCORS"))
st.write(st.config.get_option("server.enableXsrfProtection"))
