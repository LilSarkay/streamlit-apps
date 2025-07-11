__updated__ = "Fri Jul 11 06:41:39 UTC 2025"
import streamlit as st

def main():
    st.title("Saanvi Ravikiran's Resume")
    st.sidebar.title('Navigation')
    options = ['Education', 'Projects', 'Work Experience']
    choice = st.sidebar.radio('Sections', options)

    if choice == 'Education':
        st.subheader('Education')
        st.text("B.Tech in Computer Science from XYZ University, 2015-2019")
        st.text("Relevant Coursework: Data Structures, Algorithms, Database Systems")

    elif choice == 'Projects':
        st.subheader('Projects')
        st.text("Project 1: XYZ - A web-based application for ABC")
        st.text("Project 2: ABC - Mobile app development for XYZ")

    elif choice == 'Work Experience':
        st.subheader('Work Experience')
        st.text("Software Developer at ABC Corp, 2019-Present")
        st.text("Responsibilities: Developing web applications, Collaborating with cross-functional teams")


if __name__ == "__main__":
    main()