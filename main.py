# Streamlit app for Saanvi Ravikiran's Portfolio

import streamlit as st

# Sidebar for navigation
st.sidebar.title('Navigation')
sections = ['Home', 'Education', 'Skills', 'Work Experience', 'Projects']
selection = st.sidebar.radio('Go to', sections)

# Title
st.title('Portfolio of Saanvi Ravikiran')

# Home Section
if selection == 'Home':
    st.header('Welcome to my Portfolio App')
    st.write("Explore the sections to know more about my professional journey and skills.")

# Education Section
elif selection == 'Education':
    st.header('Education')
    st.subheader('Bachelor of Science in Computer Science')
    st.write('XYZ University, 2020')
    st.write('Relevant coursework: Data Structures, Algorithms, AI')

# Skills Section
elif selection == 'Skills':
    st.header('Skills')
    st.write('Programming Languages: Python, Java, C++')
    st.write('Web Development: HTML, CSS, JavaScript, React')
    st.write('Data Science: Pandas, Numpy, Scikit-learn')

# Work Experience Section
elif selection == 'Work Experience':
    st.header('Work Experience')
    st.subheader('Software Developer at ABC Corp.')
    st.write('2021 - Present')
    st.write('Responsibilities include developing scalable software solutions.')

# Projects Section
elif selection == 'Projects':
    st.header('Projects')
    st.subheader('Portfolio Website')
    st.write('Developed a personal portfolio website using React and hosted on GitHub Pages.')