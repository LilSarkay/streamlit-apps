import streamlit as st

# Sidebar Navigation
st.sidebar.title('Navigation')
sections = ['Home', 'Education', 'Experience', 'Projects', 'Skills', 'Contact']
section = st.sidebar.radio('Go to', sections)

# Home Section
if section == 'Home':
    st.title("Saanvi Ravikiran's Portfolio")
    st.write("Welcome to the portfolio of Saanvi Ravikiran!")

# Education Section
elif section == 'Education':
    st.title('Education')
    st.write("Details about Saanvi's education.")

# Experience Section
elif section == 'Experience':
    st.title('Experience')
    st.write("Professional experiences and roles held by Saanvi.")

# Projects Section
elif section == 'Projects':
    st.title('Projects')
    st.write("Projects undertaken by Saanvi and their descriptions.")

# Skills Section
elif section == 'Skills':
    st.title('Skills')
    st.write("A list of Saanvi's skills.")

# Contact Section
elif section == 'Contact':
    st.title('Contact')
    st.write("Contact information for Saanvi.")