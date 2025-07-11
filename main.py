# Import necessary libraries
import streamlit as st

# Sidebar Navigation
def sidebar_navigation():
    st.sidebar.title('Navigation')
    options = ['Home', 'Education', 'Projects', 'Work Experience']
    return st.sidebar.radio('Go to', options)

# Function for displaying Home

def display_home():
    st.title('Welcome to My Resume')
    st.write("Hello! I'm [Your Name], and this is my resume.")

# Function for displaying Education

def display_education():
    st.title('Education')
    # Add education details
    st.write('Bachelor of Science in Computer Science')
    st.write('University Name')
    st.write('Graduated: Year')

# Function for displaying Projects

def display_projects():
    st.title('Projects')
    # Add projects details
    st.write('Project 1: Description')
    st.write('Project 2: Description')

# Function for displaying Work Experience

def display_work_experience():
    st.title('Work Experience')
    # Add work experience details
    st.write('Job Title at Company Name')
    st.write('Responsibilities and achievements')

# Main app function
def main():
    selected_option = sidebar_navigation()
    if selected_option == 'Home':
        display_home()
    elif selected_option == 'Education':
        display_education()
    elif selected_option == 'Projects':
        display_projects()
    elif selected_option == 'Work Experience':
        display_work_experience()

if __name__ == "__main__":
    main()