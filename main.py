# This is an example of a Streamlit app showcasing Saanvi Ravikiran's resume data

import streamlit as st

# Set the title of the Streamlit app
st.title("Saanvi Ravikiran's Resume")

# Add a navigation sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ['Overview', 'Education', 'Experience', 'Skills', 'Contact'])

# Example sections of the resume
if page == 'Overview':
    st.header("Overview")
    st.write("This section contains a brief overview of Saanvi Ravikiran's career milestones and achievements.")
elif page == 'Education':
    st.header("Education")
    st.write("This section lists Saanvi's educational background and qualifications.")
elif page == 'Experience':
    st.header("Experience")
    st.write("This section highlights Saanvi's professional experience and roles.")
elif page == 'Skills':
    st.header("Skills")
    st.write("This section details Saanvi's technical skills and competencies.")
elif page == 'Contact':
    st.header("Contact")
    st.write("This section provides contact information for Saanvi Ravikiran.")