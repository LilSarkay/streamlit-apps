__updated__ = "Thu Jul 10 10:14:46 UTC 2025"
import streamlit as st

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ['Personal Information', 'Skills', 'Languages', 'Interests', 'Education', 'Work Experience', 'Certificates', 'Projects'])

# Title of the Portfolio
st.title("Saanvi Ravikiran - Portfolio")

# Data
personal_information = {
    "Name": "Saanvi Ravikiran",
    "Email": "saanvi.r@example.com",
    "Phone": "123-456-7890",
    "LinkedIn": "linkedin.com/in/saanviravikiran",
}

skills = [
    "Python", "Data Analysis", "Machine Learning", "Deep Learning",
    "Statistics", "Communication", "Team Collaboration"
]

languages = [
    "English", "Spanish", "French"
]

interests = [
    "Artificial Intelligence", "Photography", "Traveling", "Reading"
]

education = [
    {
        "Degree": "Bachelor of Science in Computer Science",
        "Institution": "University of Somewhere",
        "Year": "2020"
    },
    {
        "Degree": "Master of Science in Artificial Intelligence",
        "Institution": "Institute of Advanced Studies",
        "Year": "2022"
    }
]

work_experience = [
    {
        "Role": "Data Scientist",
        "Company": "Tech Innovators",
        "Year": "2020-2023",
        "Description": "Worked on various machine learning projects and lead a team of junior data scientists."
    }
]

certificates = [
    "Certified Data Scientist", "AI/ML Specialist"
]

projects = [
    {
        "Project Name": "AI Chatbot",
        "Description": "Developed an AI-powered chatbot for customer service automation."
    },
    {
        "Project Name": "Image Classification System",
        "Description": "Implemented a deep learning model for automatic image classification."
    }
]

# Content Display Based on Navigation
if section == 'Personal Information':
    st.header('Personal Information')
    for key, value in personal_information.items():
        st.write(f"**{key}:** {value}")

elif section == 'Skills':
    st.header('Skills')
    st.write(', '.join(skills))

elif section == 'Languages':
    st.header('Languages')
    st.write(', '.join(languages))

elif section == 'Interests':
    st.header('Interests')
    st.write(', '.join(interests))

elif section == 'Education':
    st.header('Education')
    for edu in education:
        st.write(f"**{edu['Degree']}** - {edu['Institution']} ({edu['Year']})")

elif section == 'Work Experience':
    st.header('Work Experience')
    for exp in work_experience:
        st.subheader(exp['Role'])
        st.write(f"{exp['Company']} ({exp['Year']})")
        st.write(exp['Description'])

elif section == 'Certificates':
    st.header('Certificates')
    st.write(', '.join(certificates))

elif section == 'Projects':
    st.header('Projects')
    for project in projects:
        st.subheader(project['Project Name'])
        st.write(project['Description'])