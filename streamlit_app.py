import streamlit as st
import pandas as pd

st.write("""
# Sales Model
Below are our sales predictions
for this customer.
""")
df = pd.read_csv("my_data.csv")
st.bar_chart(df)

st.form('my_form_identifier')
st.form_submit_button('Submit to me')
st.container()

st.expander('Expander')
