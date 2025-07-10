import streamlit as st

# App Title
st.title("Saanvi Ravikiran - Resume")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = ["Introduction", "Education", "Work Experience", "Certificates", "Projects", "Contact", "Skills", "Languages", "Interests"]
selection = st.sidebar.radio("Go to", options)

# Introduction
if selection == "Introduction":
    st.header("Introduction")
    st.write("Saanvi Ravikiran's Resume")

# Education Section
elif selection == "Education":
    st.header("Education")
    st.write("**Bachelor of Science in Computer Science**")
    st.write("XYZ University, City, Country")
    st.write("Graduated: 2022")

# Work Experience Section
elif selection == "Work Experience":
    st.header("Work Experience")
    st.write("**Software Engineer Intern**")
    st.write("ABC Company, City, Country")
    st.write("Jan 2022 - Dec 2022")

# Certificates Section
elif selection == "Certificates":
    st.header("Certificates")
    st.write("**Certified Python Developer**")
    st.write("Certification Authority, Year")

# Projects Section
elif selection == "Projects":
    st.header("Projects")
    st.write("**Data Analysis Project** - Analyzed sales data to improve business decisions at ABC Company.")

# Contact Section
elif selection == "Contact":
    st.header("Contact")
    st.write("Email: saanvi.ravikiran@email.com")
    st.write("Phone: +123456789")

# Skills Section
elif selection == "Skills":
    st.header("Skills")
    st.write("- Python")
    st.write("- Data Analysis")
    st.write("- Machine Learning")

# Languages Section
elif selection == "Languages":
    st.header("Languages")
    st.write("- English")
    st.write("- Hindi")

# Interests Section
elif selection == "Interests":
    st.header("Interests")
    st.write("- Reading")
    st.write("- Traveling")