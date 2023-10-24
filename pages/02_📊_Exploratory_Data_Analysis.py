import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

import joblib


import pandas as pd
import numpy as np

st.set_page_config(
    page_title = "EDA", 
    page_icon = "📊"
)

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def show_eda_page():
    lottie_url = "https://lottie.host/031b997c-970d-4453-bda9-dcc31f27c4d2/44wm5aMu3F.json"
    lottie_animation = load_lottie_url(lottie_url)

    st_lottie(lottie_animation, key="sidebar_lottie")

show_eda_page()


def calculate_bmi_pounds_feet_inches(weight_pounds, height_feet, height_inches):
    total_inches = (height_feet * 12) + height_inches
    height_m = total_inches * 0.0254
    weight_kg = weight_pounds * 0.453592
    if height_m == 0:
        return "Invalid height"
    bmi = weight_kg / (height_m ** 2)
    return bmi

st.title('BMI Calculator')

# User inputs
weight_pounds = st.number_input('Enter your weight (in pounds):', min_value=1.0, max_value=600.0, step=0.1)
height_feet = st.number_input('Enter your height (feet):', min_value=0, max_value=7, step=1)
height_inches = st.number_input('Enter your height (additional inches):', min_value=0, max_value=11, step=1)

# Button to trigger BMI calculation
if st.button('Calculate BMI'):
    bmi_value = calculate_bmi_pounds_feet_inches(weight_pounds, height_feet, height_inches)
    st.write(f'Your BMI is: {bmi_value:.2f}')

    # Additional information based on BMI value
    if bmi_value < 18.5:
        st.write('You are underweight.')
    elif 18.5 <= bmi_value < 24.9:
        st.write('You have a normal weight.')
    elif 25 <= bmi_value < 29.9:
        st.write('You are overweight.')
    else:
        st.write('You are obese.')