import plotly.express as px
import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_ai_developer_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_productivity_study_body():

    # load data
    df = load_ai_developer_data()

    # hard copied from churned customer study notebook
    vars_to_study = ['ai_usage_hours', 'coffee_intake_mg', 'commits', 'hours_coding']

    st.write("### Productivity Study")
    st.info(
        f"* The client would like to know which factors are most relevant for task success."
        f"* Furthermore the client is interested if there is a 'sweet spot' for the use of AI tools in terms of hours in relation to task success.\n"
    )

    # inspect data
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
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "02 - Churned Customer Study" notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlation indications and plots below interpretation converge. "
        f"It suggests that developers who successfully accomplish their task tend to:\n"
        f"* drink more caffeine (strong correlation). \n"
        f"* spend more hours coding (strong correlation). \n"
        f"* commit more often (weak correlation). \n"
        f"* use AI tools more (weak correlation). \n"
    )

    # Code copied from "02 - Churned Customer Study" notebook - "EDA on selected variables" section
    df_eda = df.filter(vars_to_study + ['task_success'])

    # Individual plots per variable
    if st.checkbox("Task Success Levels per Variable"):
        task_success_level_per_variable(df_eda)

    # # Parallel plot
    # if st.checkbox("Parallel Plot"):
    #     st.write(
    #         f"* Information in white indicates the profile from a churned customer")
    #     parallel_plot_churn(df_eda)


# function created using "02 - Churned Customer Study" notebook code - "Variables Distribution by Churn" section
def task_success_level_per_variable(df_eda):
    target_var = 'task_success'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        plot_numerical(df_eda, col, target_var)


# # code copied from "02 - Churned Customer Study" notebook - "Variables Distribution by Churn" section
# def plot_categorical(df, col, target_var):
#     fig, axes = plt.subplots(figsize=(12, 5))
#     sns.countplot(data=df, x=col, hue=target_var,
#                   order=df[col].value_counts().index)
#     plt.xticks(rotation=90)
#     plt.title(f"{col}", fontsize=20, y=1.05)
#     st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


# code copied from "02 - Churned Customer Study" notebook - "Variables Distribution by Churn" section
def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


# # function created using "02 - Churned Customer Study" notebook code - Parallel Plot section
# def parallel_plot_churn(df_eda):

#     # hard coded from "disc.binner_dict_['tenure']"" result,
#     tenure_map = [-np.Inf, 6, 12, 18, 24, np.Inf]
#     # found at "02 - Churned Customer Study" notebook
#     # under "Parallel Plot" section
#     disc = ArbitraryDiscretiser(binning_dict={'tenure': tenure_map})
#     df_parallel = disc.fit_transform(df_eda)

#     n_classes = len(tenure_map) - 1
#     classes_ranges = disc.binner_dict_['tenure'][1:-1]
#     LabelsMap = {}
#     for n in range(0, n_classes):
#         if n == 0:
#             LabelsMap[n] = f"<{classes_ranges[0]}"
#         elif n == n_classes-1:
#             LabelsMap[n] = f"+{classes_ranges[-1]}"
#         else:
#             LabelsMap[n] = f"{classes_ranges[n-1]} to {classes_ranges[n]}"

#     df_parallel['tenure'] = df_parallel['tenure'].replace(LabelsMap)
#     fig = px.parallel_categories(
#         df_parallel, color="Churn", width=750, height=500)
#     # we use st.plotly_chart() to render, in notebook is fig.show()
#     st.plotly_chart(fig)