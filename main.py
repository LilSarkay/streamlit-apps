__updated__ = "Thu Jul 10 10:43:33 UTC 2025"
import streamlit as st
from saanvi_ravikiran_resume_data import data

st.title(f"Resume - {data['name']}")

# Contact Information
st.header("Contact Information")
st.write(f"**Email:** {data['contact']['email']}")
st.write(f"**LinkedIn:** {data['contact']['linkedin']}")

# Education Section
st.header("Education")
for edu in data['education']:
    st.subheader(edu['degree'])
    st.write(f"{edu['institution']} ({edu['year']})")

# Work Experience Section
st.header("Work Experience")
for exp in data['experience']:
    st.subheader(exp['role'])
    st.write(f"**Company:** {exp['company']}")
    st.write(f"**Years:** {exp['years']}")
    st.write(exp['description'])

# Skills Section
st.header("Skills")
st.write(", ".join(data['skills']))

# Projects Section
st.header("Projects")
for project in data['projects']:
    st.subheader(project['name'])
    st.write(project['description'])