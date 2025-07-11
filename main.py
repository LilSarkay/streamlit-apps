import streamlit as st

# App Title
st.title('User Portfolio')

# Sidebar Navigation
st.sidebar.title('Navigation')

pages = ['Home', 'Experience', 'Education', 'Projects', 'Contact']

selection = st.sidebar.radio('Go to', pages)

# Page Contents
def home():
    st.write('Welcome to the User Portfolio Application. Navigate using the sidebar.')

def experience():
    st.header('Experience')
    st.write('Here is a detailed list of experiences.')
    
def education():
    st.header('Education')
    st.write('Here is a detailed list of educational qualifications.')

def projects():
    st.header('Projects')
    st.write('Here is a list of projects.')
    
def contact():
    st.header('Contact')
    st.write('Contact information here.')
    
# Render selected page
if selection == 'Home':
    home()
elif selection == 'Experience':
    experience()
elif selection == 'Education':
    education()
elif selection == 'Projects':
    projects()
elif selection == 'Contact':
    contact()