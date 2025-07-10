import streamlit as st

# Streamlit App Title
title = "Saanvi Ravikiran's Resume"
st.set_page_config(page_title=title)
st.title(title)

# Sidebar Navigation
pages = {
    "Overview": "Overview",
    "Skills": "Skills",
    "Education & Courses": "Education & Courses",
    "Work Experience": "Work Experience",
    "Certificates & Projects": "Certificates & Projects"
}
selection = st.sidebar.radio("Navigation", list(pages.keys()))

# Data
resume_data = {
    "Name": "Saanvi Ravikiran",
    "Email": "saanvi.ravikiran@gmail.com",
    "Phone": "9019525675",
    "LinkedIn": "linkedin.com/in/saanvi-ravikiran-8b6b791b4",
    "Skills": [
        "Exploratory Data Analysis (EDA)", "Machine Learning", "Generative AI",
        "Neural Networks", "Python", "C++", "Java", "Hadoop", "SQL", "Excel",
        "Financial analysis", "Ethical hacking", "Digital marketing"
    ],
    "Education": "B-Tech in Data Science and Engineering from Manipal Institute of Technology (06/2022 - 06/2026)",
    "Courses": "AI and Big Data Analytics",
    "Work Experience": "Financial Analyst at PropertyVerse (11/2023 - 01/2024)",
    "Certificates & Projects": ["Ethical Hacking Essentials", "Aeturnum project"]
}

# Conditional display based on sidebar selection
if selection == "Overview":
    st.header("Contact Information")
    st.write(f"**Name:** {resume_data['Name']}")
    st.write(f"**Email:** {resume_data['Email']}")
    st.write(f"**Phone:** {resume_data['Phone']}")
    st.write(f"**LinkedIn:** {resume_data['LinkedIn']}")

if selection == "Skills":
    st.header("Skills")
    st.write(" , ".join(resume_data['Skills']))

if selection == "Education & Courses":
    st.header("Education")
    st.write(resume_data['Education'])
    st.header("Courses")
    st.write(resume_data['Courses'])

if selection == "Work Experience":
    st.header("Work Experience")
    st.write(resume_data['Work Experience'])

if selection == "Certificates & Projects":
    st.header("Certificates & Projects")
    st.write(" , ".join(resume_data['Certificates & Projects']))