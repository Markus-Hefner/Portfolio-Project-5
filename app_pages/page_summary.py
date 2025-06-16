import streamlit as st
import matplotlib.pyplot as plt

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* Examples for AI tools: ChatGPT, Copilot\n\n"
        f"**Project Dataset**\n"
        f"* The dataset contains information about AI developers over 500 days.\n\n"
    )

    st.markdown('''
        | Variable | Meaning | Unit |
        | :-----: | :----- | :-----|
        | hours_coding | Total focused hours spent on software development work (0–12 hours) | 0–12 hours |
        | coffee_intake_mg | Daily caffeine intake in milligrams | 0–600 mg |
        | distractions | Number of distractions (e.g., meetings, Slack notifications) | 0–10 |
        | sleep_hours | Number of hours of sleep the previous night | 3–10 hours |
        | commits | Number of code commits pushed during the day | 0–20 |
        | bugs_reported | Number of bugs reported in code written that day | 0–10 |
        | ai_usage_hours | Number of hours spent using AI tools  | 0–12 |
        | cognitive_load | Self-reported mental strain | a scale of 1 to 10 |
        | task_success | Whether the daily productivity goal was achieved | 0 or 1 where 0 = no and 1 = yes |\n\n'''
    )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Markus-Hefner/Portfolio-Project-5).")
    

    # Copied from README file - "Business Requirements" section
    st.success(
        f"The project has 3 business requirements:\n"
        f"* 1. The client would like to know which factors are most relevant for task success.\n"
        f"* 2. Furthermore the client is interested if there is a 'sweet spot' for the use of AI tools in terms of hours in relation to task success.\n"
        f"* 3. The client would like to have a model to predict whether or not a developer is likely to not succeed based on the most relevant factors."
        )
