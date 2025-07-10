import streamlit as st

# Saanvi Ravikiran's Resume App
def main():
    st.title("Saanvi Ravikiran's Resume")

    # Profile Image
    image_url = "https://via.placeholder.com/150"
    st.image(image_url, caption='Saanvi Ravikiran', use_column_width=true)

    # Personal Information
    st.header("Personal Information")
    st.write("**Name:** Saanvi Ravikiran")
    st.write("**Location:** New York, NY")
    st.write("**Email:** saanvi.ravikiran@example.com")

    # Professional Summary
    st.header("Professional Summary")
    st.write("Dedicated and efficient full stack developer with 5+ years experience in application layers, presentation layers, and databases. Certified in both frontend and backend technologies.")

    # Skills
    st.header("Skills")
    st.write("- Programming Languages: Python, JavaScript, SQL")
    st.write("- Frameworks: React, Node.js, Django")
    st.write("- Tools: Git, Docker, Jenkins")
    st.write("- Soft Skills: Problem-solving, Communication, Teamwork")

    # Experience
    st.header("Experience")
    st.subheader("Full Stack Developer at Tech Solutions Inc.")
    st.write("**Location:** San Francisco, CA")
    st.write("**Duration:** Jan 2018 - Present")
    st.write("- Developed new features and improved existing ones in the company's leading SaaS product.")
    st.write("- Collaborated with a distributed team to integrate machine learning models into the web services.")

    # Education
    st.header("Education")
    st.subheader("Bachelor of Technology in Computer Science")
    st.write("**University:** National Institute of Technology")
    st.write("**Graduation Year:** 2017")

if __name__ == "__main__":
    main()