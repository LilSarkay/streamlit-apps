import streamlit as st

def main():
    st.title("Saanvi's Portfolio")
    st.write("Welcome to the portfolio app based on Saanvi's resume.")
    # Here we simulate the resume content structure
    st.header("Education")
    st.subheader("Master of Science in Computer Science")
    st.write("University of Example, 2020")

    st.subheader("Bachelor of Technology in Information Technology")
    st.write("Institute of Example, 2018")

    st.header("Experience")
    st.subheader("Software Developer")
    st.write("Tech Company Inc. (2020 - Present)")
    st.write("- Developed multiple back-end services using Python and Django.")
    st.write("- Collaborated with the front-end team to enhance user interfaces.")

    st.header("Projects")
    st.subheader("Portfolio Web Application")
    st.write("Developed a personal portfolio web app using Streamlit and Python.")

    st.header("Skills")
    st.write("Programming Languages: Python, Java, C++")
    st.write("Web Technologies: Django, Flask, HTML, CSS")
    st.write("Databases: MySQL, PostgreSQL")

    st.header("Achievements")
    st.write("- Dean's List for academic excellence.")
    st.write("- Led a team to win the State Coding Championship.")

if __name__ == "__main__":
    main()