import streamlit as st
import pandas as pd
from src.data_management import load_ai_developer_data, load_pkl_file
from src.machine_learning.predict_task_success import (predict_task_success)

def page_help_needed_body():

    st.write("### Help Needed?")
