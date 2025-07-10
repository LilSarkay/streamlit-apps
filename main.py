import streamlit as st

# Load resume data
resume_data = """
# Saanvi Ravikiran's Resume

## Contact Information
- **Email:** saanvi.ravikiran@email.com
- **Phone:** +123-456-7890
- **LinkedIn:** [linkedin.com/in/saanviravikiran](https://linkedin.com/in/saanviravikiran)

## Education
- **Master of Science in Computer Science**
  - University A, 2021
  - Thesis: Deep Learning Techniques
- **Bachelor of Technology in Information Technology**
  - University B, 2019

## Work Experience
- **Software Engineer** at Tech Solutions Inc.
  - Duration: 2021 - Present
  - Improved software performance by 30%
  - Led a team of 5 developers
- **Intern** at Web Develop Inc.
  - Duration: Summer 2019

## Certifications
- Certified Kubernetes Administrator
- AWS Certified Solutions Architect

## Projects
- **Project AI-Learn**: Developed a machine learning model for predicting learning patterns.
- **Project HealthCare++**: A healthcare app for patient data management.

## Skills
- Programming: Python, Java, C++
- Web Development: HTML, CSS, JavaScript
- Tools: Docker, Jenkins, Git

## Languages
- English (Professional)
- Hindi (Native)

## Interests
- AI Research
- Open Source Contributions

"""

# Display resume data
st.markdown(resume_data)