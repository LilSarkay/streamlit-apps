__updated__ = "Thu Jul 10 10:46:22 UTC 2025"
import streamlit as st

# Basic Information
name = "Saanvi Ravikiran"
role = "Data Scientist"
location = "San Francisco, CA"

# Contact Information
email = "saanvi.ravikiran@example.com"
phone = "+1 415 555 0199"
linkedin = "linkedin.com/in/saanvi-ravikiran"

# Summary
summary = """
Data Scientist with over 5 years of experience in applying
machine learning and data analysis techniques to solve real-world problems.
Specialized in predictive modeling, data visualization, and Big Data technologies.
"""

# Skills
skills = [
    "Python", "R", "SQL",
    "Machine Learning", "Deep Learning",
    "Data Visualization", "Big Data",
    "Natural Language Processing"
]

# Experience
experience = [
    {
        "company": "Tech Company A",
        "role": "Senior Data Scientist",
        "duration": "Jan 2020 - Present",
        "details": "Working on predictive analytics and data modeling."
    },
    {
        "company": "Tech Company B",
        "role": "Data Scientist",
        "duration": "May 2016 - Dec 2019",
        "details": "Developed machine learning models for customer analytics."
    }
]

# Education
education = [
    {
        "degree": "M.S. in Data Science",
        "institute": "University of California, Berkeley",
        "year": "2016"
    },
    {
        "degree": "B.S. in Computer Science",
        "institute": "Stanford University",
        "year": "2014"
    }
]

# Building the Streamlit App
st.title(f"{name}'s Portfolio")

# Display Basic Information
st.header("Basic Information")
st.write(f"**Role:** {role}")
st.write(f"**Location:** {location}")

# Display Contact Information
st.header("Contact Information")
st.write(f"**Email:** {email}")
st.write(f"**Phone:** {phone}")
st.write(f"**LinkedIn:** {linkedin}")

# Display Summary
st.header("Summary")
st.write(summary)

# Display Skills
st.header("Skills")
st.write(", ".join(skills))

# Display Experience
st.header("Experience")
for job in experience:
    st.subheader(job["company"])
    st.write(f"**Role:** {job['role']}")
    st.write(f"**Duration:** {job['duration']}")
    st.write(f"**Details:** {job['details']}")
    st.write("")

# Display Education
st.header("Education")
for edu in education:
    st.subheader(f"{edu['degree']}")
    st.write(f"**Institute:** {edu['institute']}")
    st.write(f"**Year:** {edu['year']}")
    st.write("")