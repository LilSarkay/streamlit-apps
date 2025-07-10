import streamlit as st

# Set page title
st.set_page_config(page_title='Saanvi Ravikiran Resume')

# Sidebar for easy navigation
st.sidebar.title('Navigation')
sections = ['Profile', 'Education', 'Work Experience', 'Skills']
chosen_sections = st.sidebar.radio('Go to', sections)

# Placeholder for personal information
if chosen_sections == 'Profile':
    st.title('Saanvi Ravikiran')
    st.image('profile_photo.png', width=150)
    st.write('Contact: saanvi.ravikiran@example.com')
    st.write('Location: Hyderabad, India')

# Education section
elif chosen_sections == 'Education':
    st.header('Education')
    st.write('**Masters of Science in Computer Science**')
    st.write('University of Hyderabad, 2020-2022')
    st.write('**Bachelors of Technology in Information Technology**')
    st.write('Vellore Institute of Technology, 2016-2020')

# Work Experience section
elif chosen_sections == 'Work Experience':
    st.header('Work Experience')
    st.write('**Data Scientist at XYZ Corp**')
    st.write('June 2022 - Present')
    st.write('Working on machine learning models and data analysis')
    st.write('**Intern Data Analyst at ABC Pvt. Ltd**')
    st.write('Jan 2020 - May 2022')
    st.write('Involved in data cleaning and visualization projects')

# Skills section
elif chosen_sections == 'Skills':
    st.header('Skills')
    st.write('- Python Programming')
    st.write('- Machine Learning')
    st.write('- Data Analytics')
    st.write('- Visualization using Matplotlib and Seaborn')