import streamlit as st
import pandas as pd

st.write("""
# Sales Model
Below are our sales predictions
for this customer.
""")
df = pd.read_csv("my_data.csv")
st.line_chart(df)