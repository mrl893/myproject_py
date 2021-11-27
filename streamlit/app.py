import streamlit as st
st.text = ("googd morning")
st.subheader("Sub Header")
st.title("Title")
st.header("Header")
st.markdown("Markdown")
st.success("Success")
st.warning("Warning")
st.error("Error")


original_title = '<p style="font-family:Courier; color:blue; font-size:20px;">good mornig</p>'
st.markdown(original_title, unsafe_allow_html=True)

new_title = '<p style="font-family:san-serif; color:green; font-size: 42px;">good morning</p>'
st.markdown(new_title, unsafe_allow_html=True)


