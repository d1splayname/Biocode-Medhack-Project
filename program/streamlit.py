import streamlit as st
import numpy as np
import pandas as pd

st.title("Aera+e")
st.write("Helping inform people about the impacts of pollution on health")

df = pd.DataFrame({
  'AQI Level': ["0-50", "51-100", "101-150", "151-200", "201-300", "301-500"],
  'Descriptor': ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"]
})
st.write(df)
