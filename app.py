
import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

import joblib
from predict_page import show_predict_page
from eda_page import show_eda_page

import pandas as pd
import numpy as np

#########################################################

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def display_sidebar():

    page = st.sidebar.selectbox("EDA or Predict", ("Predict", "Exploratory Data Analysis"))

    if page == "Predict":
        show_predict_page()
    else:
        show_eda_page()

    st.sidebar.header("Welcome to our Diabetes-predictor! :mag:")
    st.sidebar.markdown("""
    This application offers users the chance to complete a brief survey. Based on your responses, we predict the likelihood of you having diabetes. Our prediction model is trained using data sourced from NHANES.
    
    **What is NHANES?**  
    The National Health and Nutrition Examination Survey (NHANES) is an initiative designed to gauge the health and nutritional status of adults and children across the United States. Through this comprehensive survey, valuable insights into various health concerns are gathered and analyzed, making it an invaluable resource for predictive models like ours.
    """)
    
    st.sidebar.header("Reference")
    st.sidebar.markdown("[NHANES 2017-2020](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2017-2020)")


display_sidebar()