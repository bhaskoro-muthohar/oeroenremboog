import streamlit as st
from database_config import connect_to_db

class WelcomePage:
    def __call__(self):
        self.welcome_page()

    def welcome_page(self):
        st.write("Debug: Starting Welcome Page")  # Debug print
        with open("src/frontend/welcome.html", "r") as f:
            html_content = f.read()

        with open("src/frontend/welcome.css", "r") as f:
            welcome_css_content = f.read()

        with open("src/frontend/welcome.js", "r") as f:
            js_content = f.read()

        with open("src/frontend/welcome_responsive.css", "r") as f:
            responsive_css_content = f.read()

        combined_css = f"{welcome_css_content}\n{responsive_css_content}"

        st.markdown(f"<style>{combined_css}</style>", unsafe_allow_html=True)
        st.markdown(html_content, unsafe_allow_html=True)
        st.components.v1.html(f"<script>{js_content}</script>", height=100, width=100)