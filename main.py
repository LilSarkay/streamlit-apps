import streamlit as st

# Sidebar for navigation
st.sidebar.title("Navigation")
sections = ["Education", "Work Experience", "Certifications", "Projects", "Skills", "Contact Information"]
selected_section = st.sidebar.radio("Go to", sections)

# Portfolio content from extracted markdown
portfolio_content = {
    "Education": """
        ### Education
        - **B-Tech in Data Science and Engineering**  
          Manipal Institute of Technology, Manipal, 06/2022 - 06/2026
        - **Elective - Marketing in a digital world**  
          Manipal Institute of Technology, Manipal, 01/2025 - 05/2025
        - **Elective - Digital Analytics for marketing**  
          Manipal Institute of Technology, Manipal, 01/2025 - 05/2025
    """,
    "Work Experience": """
        ### Work Experience
        - **Financial analyst, PropertyVerse**  
          11/2023 - 01/2024
          A one-stop-shop for all Real Estate Investments - Fueling Fractional Ownership
    """,
    "Certifications": """
        ### Certifications
        - **Data Science - Mood Indigo, IIT Bombay (06/2024 - 07/2024)**
          Structured approach to data analysis and visualization, providing hands-on experience with real-world datasets.
        - **Ethical Hacking Essentials - EC Council (08/2024 - 09/2024)**
          Key insights into ethical hacking, penetration testing, and identifying vulnerabilities.
        - **Equity Markets Analyst - Finlatics (06/2023 - 08/2023)**
          Private equity and portfolio optimization.
        - **Investment Banking Analyst - Finlatics (06/2023 - 08/2023)**
          Client profiling, private equity fund management, exit strategies, and venture capital analysis.
    """,
    "Projects": """
        ### Projects
        - **Aeturnum: Integrating Behavioral Modeling and Generative AI for Autonomous Cognitive Systems**
          Personal project
        - **Investigating the Influence of Continuance Intention and Intention to Recommend on User Engagement in Online Music Streaming Applications**
        - **Image-Based Pneumonia Detection and Classification: Leveraging Deep Neural Networks for Medical Imaging**
          Professional project
    """,
    "Skills": """
        ### Skills
        - Exploratory Data Analysis (EDA)
        - Machine Learning
        - Generative AI
        - Neural Networks
        - Programming Languages: Python, C++, Java, Hadoop, SQL, Excel
        - Financial Analysis
        - Ethical hacking
        - Digital marketing
    """,
    "Contact Information": """
        ### Contact Information
        - **Email**: saanvi.ravikiran@gmail.com
        - **Phone**: 9019525675
        - **LinkedIn**: [linkedin.com/in/saanvi-ravikiran-8b6b791b4](https://linkedin.com/in/saanvi-ravikiran-8b6b791b4)
    """
}

st.title("Saanvi Ravikiran's Portfolio")

if selected_section == "Home":
    st.header("Welcome to my Portfolio!")
    st.write("Use the navigation sidebar to explore various sections of my portfolio.")

else:
    st.markdown(portfolio_content[selected_section])