import streamlit as st

# Sidebar Navigation
st.sidebar.title('Navigation')
sections = ['Personal Information', 'Education', 'Experience', 'Skills']
choice = st.sidebar.radio('Go to', sections)

# Content based on choice
if choice == 'Personal Information':
    st.title('Saanvi Ravikiran')
    st.write('Email: saanvi.r@gmail.com')
    st.write('Phone: (555) 123-4567')
    st.write('LinkedIn: linkedin.com/in/saanviravikiran')
elif choice == 'Education':
    st.title('Education')
    st.header('Bachelor of Science in Computer Science')
    st.subheader('University of Example')
    st.write('Graduated: 2022')
elif choice == 'Experience':
    st.title('Experience')
    st.header('Software Developer at Tech Solutions')
    st.subheader('June 2022 - Present')
    st.write('Responsibilities:')
    st.write('- Developed user-friendly web applications')
    st.write('- Improved database performance by 20%')
elif choice == 'Skills':
    st.title('Skills')
    st.write('- Programming: Python, Java, C++')
    st.write('- Web Development: HTML, CSS, JavaScript, React')
    st.write('- Databases: SQL, MongoDB')