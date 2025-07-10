import streamlit as st

# Title of the app
st.title("Saanvi Ravikiran's Portfolio")

# Sidebar with personal information
st.sidebar.header("Personal Information")
st.sidebar.write("**Name:** Saanvi Ravikiran")
st.sidebar.write("**Email:** saanvi.ravi@example.com")
st.sidebar.write("**Phone:** +1 123 456 7890")  

# Sidebar sections for skills, languages, and interests
st.sidebar.header("Skills")
st.sidebar.write("- Python")
st.sidebar.write("- Streamlit")
st.sidebar.write("- Data Analysis")
st.sidebar.write("- Machine Learning")

st.sidebar.header("Languages")
st.sidebar.write("- English")
st.sidebar.write("- Hindi")

st.sidebar.header("Interests")
st.sidebar.write("- Artificial Intelligence")
st.sidebar.write("- Traveling")
st.sidebar.write("- Photography")

# Main content area
st.header("Education")
st.write("**Bachelor of Technology in Computer Science**")
st.write("ABC University, 2016-2020")
st.write("GPA: 3.8/4.0")

st.header("Work Experience")
st.subheader("Software Engineer at Tech Solutions")
st.write("2020 - Present")
st.write("- Developed numerous machine learning models to improve company products.")
st.write("- Collaborated with cross-functional teams to enhance product functionality.")

st.header("Certifications")
st.write("- Machine Learning by Stanford University through Coursera")
st.write("- Data Science Professional Certificate by IBM")

st.header("Projects")
st.subheader("Project A")
st.write("Developed a full-stack web application using Python and Streamlit.")

st.subheader("Project B")
st.write("Implemented various machine learning algorithms to predict market trends.")

# Corrected f-string at line 67
st.write("This is a sample text with a number at the end: {number}.".format(number=123))