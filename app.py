import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_productivity_study import page_productivity_study_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_task_success import page_predict_task_success_body

app = MultiPage(app_name= "AI Developer Productivity") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Short Project Summary", page_summary_body)
app.add_page("Productivity Study", page_productivity_study_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Task Success", page_predict_task_success_body)
app.run() # Run the app