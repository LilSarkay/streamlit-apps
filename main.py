__updated__ = "Thu Jul 10 11:09:43 UTC 2025"
import streamlit as st

# Original resume content without the sidebar

st.title("Saanvi Ravikiran")

st.subheader("Summary")
summary = """ Enthusiastic data analyst with a passion for uncovering insights and optimizing processes. """
st.write(summary)

st.subheader("Experience")
experience = """ 
- **Data Analyst**, XYZ Corp (2020-Present)
  - Developed data models that increased company efficiency by 20%
- **Intern**, ABC Inc. (2019-2020)
  - Assisted in the automation of data collection processes
"""
st.write(experience)

st.subheader("Education")
education = """ 
- M.S. in Data Science, University of Somewhere (2020)
- B.S. in Statistics, University of Anywhere (2018)
"""
st.write(education)

st.subheader("Skills")
skills = """ 
- Python, R, SQL
- Data Visualization
- Machine Learning
"""
st.write(skills)

st.subheader("Contact")
contact_info = """ 
- **Email**: saanvi@example.com
- **LinkedIn**: [linkedin.com/in/saanvi](https://linkedin.com/in/saanvi)
"""
st.write(contact_info)