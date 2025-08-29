import streamlit as st
import pandas as pd
from src.data_management import load_ai_developer_data, load_pkl_file
from src.machine_learning.predict_task_success import (predict_task_success)


# The 'blueprint' for this code was taken from Code Institute's second
# walkthrough project of their 'Predictive Analytics' course and adjusted for
# this project's purposes.


def page_help_needed_body():

    # Load predict task success files
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
        f"Caution: Since the findings that answered business requirement 3 were "
        f"very suprising and might justify further analysis the information "
        f"the customer gleames from the calcuation are also not to be taken as "
        f"hard truths. (See Hypothesis page for further clarification.)"
    )
    st.write("---")

    # Generate Live Data
    X_live = DrawInputsWidgets()

    # Predict on live data
    if st.button("Run Help Analysis"):
        pipeline_features = pd.read_csv(f"outputs/ml_pipeline/predict_task_success/{version}/X_train.csv").columns.to_list()
        X_live = X_live.filter(pipeline_features)
        help_prediction = predict_task_success(
            X_live, task_success_features, task_success_pipe_fe, task_success_pipe_model)


def DrawInputsWidgets():

    # Load dataset
    df = load_ai_developer_data()

    # We create input widgets only for 2 features
    col1, col2 = st.columns(2)

    # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result

    # Create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # From here on we draw the widget based on the variable type
    # and set initial values
    # Since they are both numerical the syntax is almost identical.
    with col1:
        feature = "cognitive_load"
        st_widget = st.number_input(
            label="Cognitive load (1.0–10.0)",
            min_value=1.0,
            max_value=10.0,
            value=4.4,
            step=0.1,
            format="%.1f",
        )
    X_live[feature] = st_widget

    with col2:
        feature = "coffee_intake_mg"
        st_widget = st.number_input(
            label="Caffeine intake (0-600 mg/day)",
            min_value=0,
            max_value=600,
            value=420,
            step=1
        )
    X_live[feature] = st_widget

    return X_live
