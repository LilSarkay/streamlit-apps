__updated__ = "Thu Jul 10 10:06:27 UTC 2025"
import streamlit as st

# Title
st.title('Saanvi Ravikiran: Portfolio')

# Sidebar for navigation
st.sidebar.title('Navigation')
sections = ['Personal Information', 'Skills', 'Languages', 'Interests', 'Education', 'Work Experience', 'Certificates', 'Projects']
selection = st.sidebar.radio('Go to', sections)

# Resume sections
def display_personal_information():
    st.header('Personal Information')
    st.write('Name: Saanvi Ravikiran')
    st.write('Email: saanvi@example.com')
    st.write('LinkedIn: linkedin.com/in/saanviravikiran')

def display_skills():
    st.header('Skills')
    st.write('- Python')
    st.write('- Data Analysis')
    st.write('- Machine Learning')

def display_languages():
    st.header('Languages')
    st.write('English, Hindi, Spanish')

def display_interests():
    st.header('Interests')
    st.write('Artificial Intelligence, Entrepreneurship, Photography')

def display_education():
    st.header('Education')
    st.write('Degree: Bachelor of Science in Computer Science')
    st.write('University: Example University')
    st.write('Year: 2022')

def display_work_experience():
    st.header('Work Experience')
    st.write('Position: Data Analyst')
    st.write('Company: Tech Solutions Inc.')
    st.write('Duration: 2022-Present')

def display_certificates():
    st.header('Certificates')
    st.write('- Certified Data Scientist')
    st.write('- Advanced Machine Learning Analyst')

def display_projects():
    st.header('Projects')
    st.write('Project Name: Portfolio Builder')
    st.write('Description: Streamlit-based resume portfolio application')
    st.write('Duration: 3 Months')

# Handling Navigation
if selection == 'Personal Information':
    display_personal_information()
elif selection == 'Skills':
    display_skills()
elif selection == 'Languages':
    display_languages()
elif selection == 'Interests':
    display_interests()
elif selection == 'Education':
    display_education()
elif selection == 'Work Experience':
    display_work_experience()
elif selection == 'Certificates':
    display_certificates()
elif selection == 'Projects':
    display_projects()