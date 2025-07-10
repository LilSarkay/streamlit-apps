__updated__ = "Thu Jul 10 11:14:33 UTC 2025"
import streamlit as st

# Define sidebar navigation
def sidebar_navigation():
    st.sidebar.title('Navigation')
    return st.sidebar.radio('Go to', ['Home', 'Experience', 'Education', 'Skills'])

# Main function to run the Resume App
def run_resume_app():
    st.title("Saanvi Ravikiran's Resume")
    page = sidebar_navigation()
    
    if page == 'Home':
        st.write("""
        ## Welcome to My Resume
        
        This is a quick overview of my qualifications and experiences, presented using a Streamlit app.
        """)
    elif page == 'Experience':
        st.write("""
        ## Experience
        - Data Analyst at XYZ Corporation
        - Research Intern at ABC Labs
        - Freelance Data Scientist
        """)
    elif page == 'Education':
        st.write("""
        ## Education
        - M.Sc in Data Science
        - B.Sc in Computer Science
        """)
    elif page == 'Skills':
        st.write("""
        ## Skills
        - Python, R
        - Machine Learning
        - Data Visualization
        - SQL
        """)

# Run the app
if __name__ == '__main__':
    run_resume_app()