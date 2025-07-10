__updated__ = "Thu Jul 10 11:38:24 UTC 2025"
import streamlit as st

# Set page configuration
st.set_page_config(page_title='Saanvi Ravikiran - Resume', layout='centered')

# Sidebar navigation
def sidebar_navigation():
    st.sidebar.title('Navigation')
    options = ['Home', 'Education', 'Work Experience', 'Projects', 'Skills']
    choice = st.sidebar.radio('Go to', options)
    return choice

# Resume sections
def display_home():
    st.title('Saanvi Ravikiran')
    st.write('Welcome to my interactive resume!')
    st.image('https://example.com/path_to_profile_picture.jpg', caption='Saanvi Ravikiran')

def display_education():
    st.header('Education')
    st.write('Details about Saanvi's educational background.')

def display_work_experience():
    st.header('Work Experience')
    st.write('Details about Saanvi's work experience.')

def display_projects():
    st.header('Projects')
    st.write('Details about projects that Saanvi has worked on.')

def display_skills():
    st.header('Skills')
    st.write('Details about Saanvi's skills.')

# Main application logic
def main():
    choice = sidebar_navigation()

    if choice == 'Home':
        display_home()
    elif choice == 'Education':
        display_education()
    elif choice == 'Work Experience':
        display_work_experience()
    elif choice == 'Projects':
        display_projects()
    elif choice == 'Skills':
        display_skills()

if __name__ == '__main__':
    main()