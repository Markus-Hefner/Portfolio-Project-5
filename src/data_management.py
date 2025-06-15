import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_data
def load_ai_developer_data():
    df = pd.read_csv("outputs/datasets/collection/Productivity_with_AI.csv")
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)