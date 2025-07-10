__updated__ = "Thu Jul 10 10:30:21 UTC 2025"
import streamlit as st

# Sidebar navigation
st.sidebar.title('Navigation')
sections = ['Personal Information', 'Skills', 'Languages', 'Interests', 'Education', 'Work Experience', 'Certificates', 'Projects']
section = st.sidebar.radio('Go to', sections)

# Portfolio content based on navigation
if section == 'Personal Information':
    st.title('Saanvi Ravikiran')
    st.write('Email: saanvi@example.com')
    st.write('Phone: +123456789')

elif section == 'Skills':
    st.header('Skills')
    st.write("- Python")
    st.write("- Data Analysis")
    st.write("- Machine Learning")

elif section == 'Languages':
    st.header('Languages')
    st.write("- English: Fluent")
    st.write("- Spanish: Intermediate")

elif section == 'Interests':
    st.header('Interests')
    st.write("- Reading")
    st.write("- Traveling")
    st.write("- Music")
    
elif section == 'Education':
    st.header('Education')
    st.write('Bachelor of Science in Computer Science')
    st.write('University of Somewhere, 2022')

elif section == 'Work Experience':
    st.header('Work Experience')
    st.write('Data Analyst at DataCorp')
    st.write('June 2022 - Present')

elif section == 'Certificates':
    st.header('Certificates')
    st.write('Certified Data Scientist')

elif section == 'Projects':
    st.header('Projects')
    st.write('Project A: Description of Project A')
    st.write('Project B: Description of Project B')

# Footer
st.sidebar.info('Streamlit App showcasing Saanvi Ravikiran Portfolio with Navigation Sidebar.')