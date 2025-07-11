__updated__ = "Fri Jul 11 07:22:44 UTC 2025"
import streamlit as st

# Set the title of the app
st.set_page_config(page_title='Saanvi Ravikiran Portfolio')

# Sidebar navigation
with st.sidebar:
    selected = st.radio('Navigation', ['Home', 'Education', 'Experience', 'Certifications', 'Projects', 'Skills', 'Contact Information'])

# Define each section content
def home():
    st.title('Home')
    st.write('Welcome to Saanvi Ravikiran portfolio website!')
def education():
    st.title('Education')
    st.write('## Undergraduate')
    st.write('Bachelor of Science in Computer Science, 2023, University Name')
def experience():
    st.title('Experience')
    st.write('Software Engineering Intern at Tech Solutions, Summer 2022')
def certifications():
    st.title('Certifications')
    st.write('Certified Data Scientist, Data Science Academy, 2023')
def projects():
    st.title('Projects')
    st.write('Personal Portfolio Website, Real-time Chat Application')
def skills():
    st.title('Skills')
    st.write('Programming Languages: Python, Java, JavaScript')
def contact_info():
    st.title('Contact Information')
    st.write('Email: saanvi.r@example.com | Phone: (123) 456-7890')

# Mapping the navigation selection to the respective functions
section_functions = {
    'Home': home,
    'Education': education,
    'Experience': experience,
    'Certifications': certifications,
    'Projects': projects,
    'Skills': skills,
    'Contact Information': contact_info
}

# Invoke the function corresponding to the selected page
section_functions[selected]()