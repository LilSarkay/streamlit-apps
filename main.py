import streamlit as st

# Sidebar Navigation
def sidebar_navigation():
    st.sidebar.title("Navigate")
    section = st.sidebar.radio("Sections", ['Personal Information', 'Education', 'Work Experience', 'Certificates', 'Skills', 'Languages', 'Projects'])
    return section

# Personal Information Section
def personal_information():
    st.header("Personal Information")
    st.write("Name: Saanvi Ravikiran")
    st.write("Email: saanvi.ravikiran@example.com")
    st.write("Phone: +1234567890")
    st.write("Address: 123 Main St, Anytown, State, Country")

# Education Section
def education():
    st.header("Education")
    st.write("**Bachelor of Science in Computer Science**")
    st.write("University of Technology, 2015-2019")
    st.write("GPA: 3.8/4.0")

# Work Experience Section
def work_experience():
    st.header("Work Experience")
    st.write("**Software Engineer at Tech Solutions Inc.**")
    st.write("2019-Present")
    st.write("Responsibilities include developing web applications, collaborating with cross-functional teams, and managing project timelines.")

    st.write("**Intern at Web Innovators**")
    st.write("Summer 2018")
    st.write("Assisted in the development of a client-side application.")

# Certificates Section
def certificates():
    st.header("Certificates")
    st.write("**Certified Python Developer** - Python Institute, 2020")
    st.write("**Data Science Professional Certificate** - Coursera, 2021")

# Skills Section
def skills():
    st.header("Skills")
    st.write("Programming Languages: Python, Java, C++")
    st.write("Frameworks: Streamlit, Django, React")
    st.write("Tools: Git, Docker, Jenkins")

# Languages Section
def languages():
    st.header("Languages")
    st.write("English (Advanced)")
    st.write("Spanish (Intermediate)")

# Projects Section
def projects():
    st.header("Projects")
    st.write("**Project A** - Developed a full-stack web application using Django and React.")
    st.write("**Project B** - Implemented a machine learning model for predictive analysis.")

# Main Application
def main():
    st.title("Saanvi Ravikiran's Resume")
    section = sidebar_navigation()

    if section == 'Personal Information':
        personal_information()
    elif section == 'Education':
        education()
    elif section == 'Work Experience':
        work_experience()
    elif section == 'Certificates':
        certificates()
    elif section == 'Skills':
        skills()
    elif section == 'Languages':
        languages()
    elif section == 'Projects':
        projects()

if __name__ == "__main__":
    main()