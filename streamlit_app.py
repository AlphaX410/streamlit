import streamlit as st
import numpy as np
import pandas as pd

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)