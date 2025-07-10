import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
sections = [
    "Summary",
    "Skills",
    "Languages",
    "Interests",
    "Education",
    "Work Experience",
    "Certificates",
    "Projects"
]
selection = st.sidebar.radio("Go to", sections)

# Conditional display based on selection
if selection == "Summary":
    st.title("Saanvi Ravikiran")  # Ensure the app title is there
    st.header("Summary")
    st.text("Software developer with 5 years of experience in developing scalable applications.")
elif selection == "Skills":
    st.header("Skills")
    st.text("- Python\n- JavaScript\n- SQL\n- Streamlit")
# Add placeholder content for each section, assuming they exist in the original app.
elif selection == "Languages":
    st.header("Languages")
    st.text("English, Spanish, Mandarin")
elif selection == "Interests":
    st.header("Interests")
    st.text("Artificial Intelligence, Open Source Contribution")
elif selection == "Education":
    st.header("Education")
    st.text("B.S. in Computer Science from XYZ University")
elif selection == "Work Experience":
    st.header("Work Experience")
    st.text("Software Engineer at ABC Corp")
elif selection == "Certificates":
    st.header("Certificates")
    st.text("Certified Kubernetes Administrator")
elif selection == "Projects":
    st.header("Projects")
    st.text("Open Source Contribution to Streamlit Library")