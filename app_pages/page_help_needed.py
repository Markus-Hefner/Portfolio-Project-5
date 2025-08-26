import streamlit as st
import pandas as pd
from src.data_management import load_ai_developer_data, load_pkl_file
from src.machine_learning.predict_task_success import (predict_task_success)

def page_help_needed_body():

    
    # load predict task success files
    version = 'v1'
    task_success_pipe_fe = load_pkl_file(
        f"outputs/ml_pipeline/predict_task_success/{version}/clf_pipeline_feat_eng.pkl")
    task_success_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_task_success/{version}/clf_pipeline_model.pkl")
    task_success_features = (pd.read_csv(f"outputs/ml_pipeline/predict_task_success/{version}/X_train.csv").columns.to_list())

    st.write("### Help Needed?")
    st.info(
        f"Though all business requirements are answered on the other dashboard pages "
        f"as a small bonus we want to give the customer the ability to check "
        f"whether or not a developer needs help given that the customer has the "
        f"information about the developers caffeine intake and their cognitive load."
        f"Caution: Since the findings that answered business requirement 3 are "
        f"meant to be taken with caution (see Hypothesis page) the information "
        f"the customer gleames from the calcuation are also not to be taken as "
        f"hard truths."
    )
    st.write("---")