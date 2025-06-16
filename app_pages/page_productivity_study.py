import plotly.express as px
import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_ai_developer_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


# The 'blueprint' for this code was taken from Code Institute's second
# walkthrough project of their 'Predictive Analytics' course and extensively
# adjusted for this project's purposes.


def page_productivity_study_body():

    # load data
    df = load_ai_developer_data()

    # Hard copied from 'Productivity Study' notebook
    relevant_variables = ['ai_usage_hours', 'coffee_intake_mg', 'commits', 'hours_coding']

    st.write("### Productivity Study")
    st.info(
        f"* The client would like to know which factors are most relevant for task success."
        f"* Furthermore the client is interested if there is a 'sweet spot' for the use of AI tools in terms of hours in relation to task success.\n"
    )

    # Inspect data
    if st.checkbox("Inspect AI Developer Productivity Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to task success. \n"
        f"The most correlated variable are: **{relevant_variables}**"
    )
    
    st.info(
        f"The correlation indications and plots below interpretation converge. "
        f"It suggests that developers who successfully accomplish their task tend to:\n"
        f"* drink more coffee (strong correlation). \n"
        f"* spend more hours coding (strong correlation). \n"
        f"* commit more often (weak correlation). \n"
        f"* use AI tools more (weak correlation). \n"
    )

    # Code copied from 'Productivity Study' notebook - 'Exploratory Data Analysis on relevant variables' section
    df_eda = df.filter(relevant_variables + ['task_success'])

    # Individual plots per variable
    if st.checkbox("Task Success Levels per Variable"):
        task_success_level_per_variable(df_eda)


def task_success_level_per_variable(df_eda):
    target_var = 'task_success'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        plot_numerical(df_eda, col, target_var)


# Code copied from 'Productivity Study' notebook - 'The distribution by task_success' section
def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()