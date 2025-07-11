import streamlit as st

st.set_page_config(page_title="Saanvi Ravikiran's Resume", layout='wide')

# Sidebar navigation
st.sidebar.title('Navigation')
options = ['Education', 'Experience', 'Projects', 'Certifications', 'Skills', 'Contact']
choice = st.sidebar.radio('Go to', options)

# Define content for each section
if choice == 'Education':
    st.title("Education")
    st.write("### Degree: Bachelor of Science in Computer Science")
    st.write("- **Institution**: XYZ University")
    st.write("- **Year**: 2020")
    st.write("- **GPA**: 3.8/4.0")

elif choice == 'Experience':
    st.title("Experience")
    st.write("### Software Engineer")
    st.write("- **Company**: ABC Tech")
    st.write("- **Duration**: June 2020 - Present")
    st.write("- Responsibilities include developing and maintaining web applications.")

elif choice == 'Projects':
    st.title("Projects")
    st.write("### Project: Automated Attendance System")
    st.write("- Developed using Python and OpenCV for facial recognition.")

elif choice == 'Certifications':
    st.title("Certifications")
    st.write("### Certified Data Scientist")
    st.write("- **Issued by**: Data Science Authority")
    st.write("- **Year**: 2021")

elif choice == 'Skills':
    st.title("Skills")
    st.write("- Python, Java, SQL")
    st.write("- Data Analysis, Machine Learning")

elif choice == 'Contact':
    st.title("Contact")
    st.write("- **Email**: saanvi.email@example.com")
    st.write("- **LinkedIn**: linkedin.com/in/saanviravikiran")