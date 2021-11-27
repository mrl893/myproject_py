import streamlit as st
import pandas as pd
import plotly.express as px



df = pd.read_csv("fish-monetary-stock-account-1996-2019.csv")
st.write(df)


graph = px.line(df, x="species", y="data_value")
st.plotly_chart(graph)

graph1 = px.pie(df, values="year", names="variable")
st.plotly_chart(graph1)

graph2 = px.bar(df, x="units", y="source")
st.plotly_chart(graph2)


from  PIL import Image
image = Image.open("png-transparent-data-analysis-data-quality-analytics-pattaya-data-pattaya-analysis.png")

st.image(image, width=100)


