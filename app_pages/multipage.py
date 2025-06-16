import streamlit as st


# The 'blueprint' for this code was taken from Code Institute's second
# walkthrough project of their 'Predictive Analytics' course and adjusted for
# this project's purposes.


# Class to generate multiple Streamlit pages using an object oriented approach 
class MultiPage: 

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="✔️")
    
    def add_page(self, title, func) -> None: 
        self.pages.append({"title": title, "function": func })

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']() 