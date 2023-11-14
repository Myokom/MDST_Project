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

# Cache the data loading
@st.cache_data
def load_data():
    df = pd.read_csv('./data_files/eda_data.csv')
    return df

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



def show_eda_page():
    # Load the data using the cached function
    df = load_data()
    pr = ProfileReport(df, title="Diabetes Dataset", explorative=True)
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
