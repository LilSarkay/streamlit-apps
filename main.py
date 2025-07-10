import streamlit as st

# Set up the sidebar
st.sidebar.title("Saanvi Ravikiran's Portfolio")
section = st.sidebar.radio("Navigate", ['Personal Information', 'Skills', 'Education', 'Work Experience', 'Certificates', 'Projects'])

# Define the data for each section
personal_info = {
    "Name": "Saanvi Ravikiran",
    "Email": "saanvi.ravikiran@example.com",
    "Location": "Hyderabad, India"
}

skills = [
    "Python", 
    "Data Analysis", 
    "Machine Learning", 
    "Project Management", 
    "Communication"
]

education = [
    {"degree": "BSc in Computer Science", "institution": "University of Hyderabad", "year": "2022"}
]

work_experience = [
    {"role": "Data Analyst", "company": "Tech Solutions Inc.", "duration": "Jan 2023 - Present"}
]

certificates = [
    {"title": "Certified Data Professional", "issuer": "Data Institute", "year": "2023"}
]

projects = [
    {"name": "Customer Segmentation Analysis", "description": "A project focused on segmenting customers using machine learning techniques to enhance marketing strategies."}
]

# Display the content based on the selected section
if section == 'Personal Information':
    st.write("## Personal Information")
    for key, value in personal_info.items():
        st.write(f"**{key}:** {value}")

elif section == 'Skills':
    st.write("## Skills")
    st.write(", ".join(skills))

elif section == 'Education':
    st.write("## Education")
    for edu in education:
        st.write(f"**{edu['degree']}**, {edu['institution']} ({edu['year']})")

elif section == 'Work Experience':
    st.write("## Work Experience")
    for work in work_experience:
        st.write(f"**{work['role']}**, {work['company']} ({work['duration']})")

elif section == 'Certificates':
    st.write("## Certificates")
    for cert in certificates:
        st.write(f"**{cert['title']}**, {cert['issuer']} ({cert['year']})")

elif section == 'Projects':
    st.write("## Projects")
    for proj in projects:
        st.write(f"**{proj['name']}**: {proj['description']})