__updated__ = "Thu Jul 10 11:58:46 UTC 2025"
import streamlit as st

# Sidebar menu options
menu = ['Education', 'Work Experience', 'Certificates', 'Projects', 'Contact', 'Skills', 'Languages', 'Interests']
selection = st.sidebar.radio("Navigate", menu)

# Content for each section
if selection == 'Education':
    st.title('Education')
    st.write("- **University of Example**: B.Sc in Example Studies (2015-2019)")
    st.write("- **Example High School**: High School Diploma (2013-2015)")

elif selection == 'Work Experience':
    st.title('Work Experience')
    st.write("- **Software Engineer at TechCorp (2019-Present)**")
    st.write("  - Developed web applications using Python and JavaScript.")
    st.write("  - Collaborated with cross-functional teams on various projects.")

elif selection == 'Certificates':
    st.title('Certificates')
    st.write("- **Certified Python Developer**")
    st.write("- **Project Management Professional (PMP)**")

elif selection == 'Projects':
    st.title('Projects')
    st.write("- **Project A**: Developed an innovative solution to improve process X.")
    st.write("- **Project B**: Led the team in a successful launch of product Y.")

elif selection == 'Contact':
    st.title('Contact')
    st.write("Feel free to reach out via LinkedIn or email.")
    st.write("- LinkedIn: [linkedin.com/in/saanvi-ravikiran](https://linkedin.com/in/saanvi-ravikiran)")
    st.write("- Email: saanvi@example.com")

elif selection == 'Skills':
    st.title('Skills')
    st.write("- Python, JavaScript, SQL")
    st.write("- Web Development, Machine Learning")

elif selection == 'Languages':
    st.title('Languages')
    st.write("- English, Hindi, Spanish")

elif selection == 'Interests':
    st.title('Interests')
    st.write("- Technology, Music, Traveling")