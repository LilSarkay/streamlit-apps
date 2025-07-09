import streamlit as st
from PIL import Image

# Load a random profile image
profile_image = Image.open('path_to_random_image.jpg')

# App title and Profile Image
st.title("John Doe - Software Engineer Portfolio")
st.image(profile_image, caption='John Doe', use_column_width=true)

# Background
st.header("Background")
st.write("John Doe is a seasoned software engineer with a passion for developing innovative programs that expedite the efficiency and effectiveness of organizational success.")

# Experience
st.header("Experience")
st.write("With over 10 years in the tech industry, John Doe has worked with a wide array of technologies and teams worldwide.")

# Skills
st.header("Skills")
st.write("- Programming Languages: Python, Java, C++")
st.write("- Web Technologies: HTML, CSS, JavaScript, React")
st.write("- Databases: MySQL, PostgreSQL, MongoDB")
st.write("- Tools & Platforms: AWS, Docker, Jenkins")

# Projects
st.header("Projects")
st.write("1. Project A - A cutting-edge platform for real-time data processing.")
st.write("2. Project B - An AI tool that enhances customer service efficiencies.")

# Contact
st.header("Contact")
st.write("Email: johndoe@example.com")