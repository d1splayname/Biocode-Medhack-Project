import streamlit as st
import numpy as np
import pandas as pd
import qualify_data
import readData
import aqi_pm_calculator


# Heading
title = '<div align="center">' \
        '<span style="font-family: sans-serif; color: LightBlue; font-size: 40px;">Aera</span>' \
        '<span style="font-family: sans-serif; color: Crimson; font-size: 40px;">+</span>' \
        '<span style="font-family: sans-serif; color: LightBlue; font-size: 40px;">e</span>' \
        '</div>'
st.markdown(title, unsafe_allow_html=True)

subtitle = '<p style="color: #c3d6ea; font-size: 18px; text-align: center; margin: 0, auto;">Helping inform ' \
           'people about the impacts of pollution on health</p>'
st.markdown(subtitle, unsafe_allow_html=True)

st.write("\n")


# Text/Description
text1 = '<p style="color: #cbc3e3; font-size: 16px; text-align: center;">Everyone has heard about climate change and ' \
        'the effects of greenhouse gases on the environment. But how do these environmental changes affect our ' \
        'health?</p>'
st.markdown(text1, unsafe_allow_html=True)
text2 = '<p style="color: #cbc3e3; font-size: 16px; text-align: center;">Your weather app may show you the air ' \
        'quality in your area, and you may have heard about how polluted cities in China and India, but what does ' \
        'this number mean?</p>'
st.markdown(text2, unsafe_allow_html=True)

# Horizontal Rule
text = """
---
"""
st.markdown(text)

# Air Quality Index Qualifying Descriptors
df = pd.DataFrame({
    'AQI Level': ["0-50", "51-100", "101-150", "151-200", "201-300", "301-500"],
    'Qualitative Descriptor': ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy",
                             "Hazardous"],
    'Cautionary Statement': [qualify_data.cautionary_statement("Good"), qualify_data.cautionary_statement("Moderate"),
                             qualify_data.cautionary_statement("Unhealthy for Sensitive Groups"),
                             qualify_data.cautionary_statement("Unhealthy"),
                             qualify_data.cautionary_statement("Very Unhealthy"),
                             qualify_data.cautionary_statement("Hazardous")]
})
st.write(df)


# Horizontal Rule
text = """
---
"""
st.markdown(text)


# Dropdown menu to select and view data for a certain city
option = st.selectbox(
    "Select a city:",
    ('Shanghai; China', 'Huntsville; USA', 'London; UK', 'New Delhi; India', 'Moscow; Russia', 'New York City; USA', 'Tokyo; Japan', 'Beijing; China', 'Bangkok; Thailand', 'Jakarta; Indonesia', 'Ho Chi Minh City; Vietnam', 'Mumbai; India', 'Dubai; UAE', 'Cairo; Egypt', 'Kinshasa; Democratic Republic of Congo', 'Johannesburg; South Africa', 'Rio de Janeiro; Brazil', 'Buenos Aires; Argentina', 'Sao Paulo; Brazil', 'Mexico City; Mexico', 'Los Angeles; USA', 'Paris; France', 'Istanbul; Turkey', 'Baghdad; Iraq', 'Khartoum; Sudan', 'Lima; Peru', 'Rome; Italy', 'Kolkata; India', 'Seoul; South Korea', 'Lagos; Nigeria', 'Sydney; Australia', 'Melbourne; Australia'))

st.write(f"The AQI in {option} is {readData.getCityData(option)}, this is {qualify_data.qualify_aqi(readData.getCityData(option))}.")
st.write(f"Cautionary statement: {qualify_data.cautionary_statement(qualify_data.qualify_aqi(readData.getCityData(option)))}")


# Display coordinates of cities on a map
cities, lat, lon = readData.getLatLon()

map_data = pd.DataFrame({
    'lat': lat,
    'lon': lon
})

st.map(map_data)


# Horizontal Rule
text = """
---
"""
st.markdown(text)


# More Text
text3 = '<p style="color: #cbc3e3; font-size: 16px; text-align: center;">The World Health Organization (WHO) ' \
        'reported that ambient air pollution was responsible for 3.7 million deaths in 2012, representing 6.7% of ' \
        'total deaths worldwide, and was the cause of 16% of lung cancer deaths, 11% of chronic obstructive ' \
        'pulmonary disease-related death, 29% of heart disease and stroke, and approximately 13% of deaths due ' \
        'to respiratory infection. </p>'
st.markdown(text3, unsafe_allow_html=True)


# Horizontal Rule
text = """
---
"""
st.markdown(text)


# SLIDERS
slider_text = '<p style="font-family: TimesNewRoman; color: LightBlue; font-size: 22px; text-align: center">Adjust ' \
              'the Slider Below to See How Concentration of Particulate Matter Affects AQI</p>'
st.markdown(slider_text, unsafe_allow_html=True)

conc_pm10 = '<p style="font-family: TimesNewRoman; color: LightGreen; font-size: 18px; text-align: center">' \
            'Concentration of PM10 (micrograms/cubic meter)</p>'
st.markdown(conc_pm10, unsafe_allow_html=True)
conc_pm10 = st.slider("PM10 Slider", min_value=0, max_value=500)

st.write("Concentration: " + str(conc_pm10))
aqi = aqi_pm_calculator.calc_pm10(conc_pm10)
st.write("AQI: " + str(aqi))
st.write("Air Quality: " + str(qualify_data.qualify_aqi(aqi)))


conc_pm25 = '<p style="font-family: TimesNewRoman; color: LightGreen; font-size: 18px; text-align: center">' \
            'Concentration of PM2.5 (micrograms/cubic meter)</p>'
st.markdown(conc_pm25, unsafe_allow_html=True)
conc_pm25 = st.slider('PM2.5 Slider', min_value=0, max_value=500)

st.write("Concentration: " + str(conc_pm25))
aqi = aqi_pm_calculator.calc_pm25(conc_pm25)
st.write("AQI: " + str(aqi))
st.write("Air Quality: " + str(qualify_data.qualify_aqi(aqi)))


# Horizontal Rule
text = """
---
"""
st.markdown(text)


# Data Table
if st.checkbox('Show Correlation Between Pollutant and Disease'):
    chart_data = pd.DataFrame({
        'Pollutant': ["O3", "NO2", "SO2", "PM2.5", "PM10"],
        'COVID': ["Positive", "Positive", "Negative", "Positive", "Positive"],
        'Lung Cancer': ["No Correlation", "No Correlation", "Positive", "Positive", "Positive"],
        'Cardiovascular Diseases': ["Positive", "Positive", "Positive", "Positive", "Positive"]
    })

    chart_data

# st.text_input('Enter some text')
