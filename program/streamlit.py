import streamlit as st
import numpy as np
import pandas as pd
import qualify_data
import readData
import aqi_pm_calculator

# Heading
title = '<p style="font-family: sans-serif; color: LightBlue; font-size: 40px; text-align: center">Aera+e</p>'
st.markdown(title, unsafe_allow_html=True)
subtitle = '<p style="color: #c3d6ea; font-size: 18px; text-align: center; margin: 0, auto;">Helping inform ' \
           'people about the impacts of pollution on health</p>'
st.markdown(subtitle, unsafe_allow_html=True)

# Air Quality Index Qualifying Descriptors
df = pd.DataFrame({
  'AQI Level': ["0-50", "51-100", "101-150", "151-200", "201-300", "301-500"],
  'Qualitative Descriptor': ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy",
                             "Hazardous"]
})
st.write(df)




if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


# Display coordinates of cities on a map
cities, lat, lon = readData.getLatLon()

map_data = pd.DataFrame({
    'lat': lat,
    'lon': lon
})

st.map(map_data)


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.bar_chart(chart_data)

st.slider('Slide me', min_value=0, max_value=500)
st.text_input('Enter some text')