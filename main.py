__updated__ = "Thu Jul 10 07:08:12 UTC 2025"
import streamlit as st

# Define a list of colors
colors = ['Red', 'Green', 'Blue']

# Select a color
selected_color = st.selectbox('Choose a color', colors)

# Update the background color based on the selected color
if selected_color:
    # Convert the color to lowercase for CSS
    css_color = selected_color.lower()
    # Style settings to change background color
    st.markdown(f'<style>body {{ background-color: {css_color}; }}</style>', unsafe_allow_html=true)