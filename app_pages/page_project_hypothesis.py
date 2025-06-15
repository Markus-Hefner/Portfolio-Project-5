import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "02 - Productivity Study" notebook
    st.success(
        f"* We suspect that the most relevant factors will be `sleep_hours` "
        f"(because sleeping to little leads to a lack of focus), `distractions` "
        f"(since that holds someone back from doint the work), `ai_usage_hours` "
        f"(since depending on the amount, too much usage will result in a "
        f"poorer outcome)."
        f"This proved to be mostly incorrect. The most relevant factors are "
        f"`caffeine_intake_mg` and `hours_coding` which show a strong positive "
        f"correlation to `task_success`. The use of AI shows only a weak "
        f"correlation.\n\n"

        f"* We hypothesize that there is a certain range of usage that is "
        f"beneficial for task success. However, too much might lead to a "
        f"confusing code or even distract from doing the work.\n"
        f"This proved to be correct. At 2-hour mark of AI usage the data shows "
        f"the biggest discrepancy between task success and no task success "
        f"suggesting that this might be the sweet spot for AI usage.\n\n"

        f"* We suspect that we can create a model that can reliably predict "
        f"which developer needs help based on the most relevant factors."
        f"This proved to be correct (see test results under Predict Task Success)."
        f"However, we were suprised to learn that `caffeine_intake_mg` was the "
        f"most relevant factor with more than double the importance than the "
        f"second place which was `cognitive_load` and common sense suggests "
        f"that there might be more to it. That is why further analysis might "
        f"be justifed to see if it really is just the caffeine intake that "
        f"drives the successful completion of a task or if it just a proxy for "
        f"an underlying correlation that is the real reason. (E.g. maybe "
        f"developers who take in more caffeine also code more hours like others "
        f"but are also more alert thus making more progress with less errors.)"
    )
