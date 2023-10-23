import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

import joblib
from predict_page import show_predict_page

import pandas as pd
import numpy as np


def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def show_eda_page():
    lottie_url = "https://lottie.host/031b997c-970d-4453-bda9-dcc31f27c4d2/44wm5aMu3F.json"
    lottie_animation = load_lottie_url(lottie_url)

    st_lottie(lottie_animation, key="sidebar_lottie")