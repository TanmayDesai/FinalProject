import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import webstreamlit, home, eyemovement

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("St. Francis Institute of Technology")

# Add all your applications (pages) here
app.add_page("Home Page", home.app)
app.add_page("Student Attention Detection System", webstreamlit.app)
app.add_page("Proctoring System", eyemovement.app)


# The main app
app.run()