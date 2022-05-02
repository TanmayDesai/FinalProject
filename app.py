import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import webstreamlit, home, eyemovement

st.set_page_config(page_title="Student Attention Detection System")
# Create an instance of the app 
app = MultiPage()

# Title of the main page

st.image("logo.jpg", width=150)

st.title("St. Francis Institute of Technology")

# Add all your applications (pages) here
app.add_page("Home Page", home.app)
app.add_page("Online Lecture", webstreamlit.app)
app.add_page("Proctoring System", eyemovement.app)


# The main app
app.run()