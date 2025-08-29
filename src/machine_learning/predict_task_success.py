import streamlit as st

# copied and adapted changed all churn to task_success and statement
def predict_task_success(X_live, task_success_features, task_success_pipeline_dc_fe, task_success_pipeline_model):

    # from live data, subset features related to this pipeline
    X_live_task_success = X_live.filter(task_success_features)

    # apply data cleaning / feat engine pipeline to live data
    X_live_task_success_dc_fe = task_success_pipeline_dc_fe.transform(X_live_task_success)

    # predict
    task_success_prediction = task_success_pipeline_model.predict(X_live_task_success_dc_fe)
    task_success_prediction_proba = task_success_pipeline_model.predict_proba(
        X_live_task_success_dc_fe)
    # st.write(task_success_prediction_proba)

    # Create a logic to display the results
    task_success_prob = task_success_prediction_proba[0, task_success_prediction][0]*100
    if task_success_prediction == 1:
        task_success_result = 'will achieve today\'s productivity goal'
    else:
        task_success_result = 'will not achieve today\'s productivity goal and needs additional help'

    statement = (
        f'### There is {task_success_prob.round(1)}% probability '
        f'that this developer {task_success_result}.')

    st.write(statement)

    return task_success_prediction