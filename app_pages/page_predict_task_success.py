import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


# The 'blueprint' for this code was taken from Code Institute's second
# walkthrough project of their 'Predictive Analytics' course and adjusted for
# this project's purposes.


def page_predict_task_success_body():

    version = 'v1'
    # load needed files
    task_success_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_task_success/{version}/clf_pipeline_feat_eng.pkl')
    task_success_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_task_success/{version}/clf_pipeline_model.pkl")
    task_success_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_task_success/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_task_success/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_task_success/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_task_success/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_task_success/{version}/y_test.csv").values

    st.write("### ML Pipeline: Predict Task Success")
    st.info(
        f"* The client would like to have a model to predict whether or not a "
        f"developer is likely to not succeed based on the most relevant factors."
    )
    # display pipeline training summary conclusions
    st.info(
        f"* The pipeline was tuned aiming at least 0.80 Recall on 'No task success' class, "
        f"since we are interested in this project in detecting a potential developer "
        f"who might need some help. \n"
        f"* The pipeline performance on train and test set is 0.90 and 0.95, respectively."
    )

    # show pipelines
    st.write("---")
    st.write("#### There were 2 ML Pipelines created.")

    st.write(" * The first is responsible for data cleaning and feature engineering.")
    st.write(task_success_pipe_dc_fe)

    st.write("* The second is for feature scaling and modelling.")
    st.write(task_success_pipe_model)

    st.info(
        f"* However, since there was no missing data in the dataset and "
        f"`ai_usage_hours` was the only variable that improved by feature "
        f"engineering but was not one of the two most important factors that "
        f"were eventually used to train the model, the pipeline for data "
        f"cleaning and feature engineering was not applied."
    )

    # show feature importance plot
    st.write("---")
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(task_success_feat_importance)

    # We don't need to apply dc_fe pipeline, since X_train and X_test
    # were already transformed in the jupyter notebook (Predict Task Success.ipynb)

    # evaluate performance on train and test set
    st.write("---")
    st.write("### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=task_success_pipe_model,
                    label_map=["No Task Success", "Task Success"])