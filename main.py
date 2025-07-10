import streamlit as st

# Sidebar Navigation
st.sidebar.title('Navigation')
sections = ['Personal Information', 'Education', 'Work Experience', 'Certificates', 'Projects', 'Skills', 'Languages', 'Interests']
section = st.sidebar.radio('Go to', sections)

# Saanvi Ravikiran's Resume Data
resume_data = {
    'Personal Information': {
        'Name': 'Saanvi Ravikiran',
        'Email': 'saanvi.r@example.com',
        'LinkedIn': 'linkedin.com/in/saanviravikiran',
        'Phone': '+1234567890',
    },
    'Education': [
        {'Degree': 'B.Sc. Computer Science', 'Institution': 'XYZ University', 'Year': '2022'},
    ],
    'Work Experience': [
        {'Position': 'Software Developer', 'Company': 'Tech Solutions', 'Year': '2023-Present'},
    ],
    'Certificates': [
        'Certified Python Developer',
    ],
    'Projects': [
        'Automated Report Generator',
    ],
    'Skills': [
        'Python', 'Data Analysis', 'Machine Learning'
    ],
    'Languages': [
        'English', 'Spanish'
    ],
    'Interests': [
        'Hiking', 'Photography'
    ]
}

def display_section(section):
    st.header(section)
    items = resume_data.get(section, [])
    if isinstance(items, dict):
        for key, value in items.items():
            st.write(f"**{key}:** {value}")
    elif isinstance(items, list):
        for item in items:
            if isinstance(item, dict):
                st.subheader(" ")
                for key, value in item.items():
                    st.write(f"**{key}:** {value}")
            else:
                st.write(f"- {item}")

display_section(section)