import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests
import joblib
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# from pydantic_settings import BaseSettings
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import streamlit.components.v1 as components



st.set_page_config(
    page_title = "EDA", 
    page_icon = "📊",
    layout = "wide"
)

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def show_eda_page():
    df = pd.read_csv('/Users/tobiasmadsen/Documents/UMich/MDST/NHANES/data_files/eda_data.csv')
    pr = ProfileReport(df, title="Diabetes Dataset", explorative = True)
    st_profile_report(pr)

def sidebar():
    with st.sidebar:
        
        st.sidebar.title('Dive deeper here!🔍')
        st.sidebar.markdown('Dive into the dataset that powers our predictions. See the first few rows of data to get a feel for what information we analyze.')
        
        st.sidebar.header("Reference")
        st.sidebar.markdown("The dataset is compiled from a variety of questionnaires collected from [NHANES 2017-2020](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2017-2020)")
        
        lottie_url = "https://lottie.host/031b997c-970d-4453-bda9-dcc31f27c4d2/44wm5aMu3F.json"
        lottie_animation = load_lottie_url(lottie_url)
        st_lottie(lottie_animation, key="sidebar_lottie")

sidebar()
show_eda_page()



# def calculate_bmi_pounds_feet_inches(weight_pounds, height_feet, height_inches):
#     total_inches = (height_feet * 12) + height_inches
#     height_m = total_inches * 0.0254
#     weight_kg = weight_pounds * 0.453592
#     if height_m == 0:
#         return "Invalid height"
#     bmi = weight_kg / (height_m ** 2)
#     return bmi
# 
# def calculate_bmi_metric(weight_kg, height_cm):
#     height_m = height_cm / 100  # Convert cm to meters
#     if height_m == 0:
#         return "Invalid height"
#     bmi = weight_kg / (height_m ** 2)
#     return bmi
# 
# st.title('BMI Calculator')
# 
# # User selects the unit system
# unit_system = st.radio("Select the unit system", ['Imperial (pounds, feet, inches)', 'Metric (kilograms, centimeters)'])
# 
# if unit_system == 'Imperial (pounds, feet, inches)':
#     weight_pounds = st.number_input('Enter your weight (in pounds):', min_value=1.0, max_value=600.0, step=0.1, value=None, placeholder="Type a number...")
#     height_feet = st.number_input('Enter your height (feet):', min_value=0, max_value=7, step=1, value=None, placeholder="Type a number...")
#     height_inches = st.number_input('Enter your height (additional inches):', min_value=0, max_value=11, step=1, value=None, placeholder="Type a number...")
# elif unit_system == 'Metric (kilograms, centimeters)':
#     weight_kg = st.number_input('Enter your weight (in kilograms):', min_value=1.0, max_value=300.0, step=0.1, value=None, placeholder="Type a number...")
#     height_cm = st.number_input('Enter your height (in centimeters):', min_value=50, max_value=250, step=1,  value=None, placeholder="Type a number...")
# 
# # Button to trigger BMI calculation
# if st.button('Calculate BMI'):
#     if unit_system == 'Imperial (pounds, feet, inches)':
#         bmi_value = calculate_bmi_pounds_feet_inches(weight_pounds, height_feet, height_inches)
#     else:
#         bmi_value = calculate_bmi_metric(weight_kg, height_cm)
# 
#     if isinstance(bmi_value, str):
#         st.write(bmi_value)  # Display error message
#     else:
#         st.write(f'Your BMI is: {bmi_value:.2f}')
# 
#         # Additional information based on BMI value
#         if bmi_value < 18.5:
#             st.write('You are underweight.')
#         elif 18.5 <= bmi_value < 24.9:
#             st.write('You have a normal weight.')
#         elif 25 <= bmi_value < 29.9:
#             st.write('You are overweight.')
#         else:
#             st.write('You are obese.')