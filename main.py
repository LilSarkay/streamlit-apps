# Import necessary libraries
import streamlit as st

# Define the main function to display Saanvi Ravikiran's Resume
def main():
    # Set the title of the Streamlit app
    st.title("Saanvi Ravikiran's Resume")
    
    # Education Section
    st.header("Education")
    st.subheader("Master of Science in Data Science")
    st.write("University of California, Berkeley\nGPA: 3.9/4.0\nAugust 2021 - May 2023")
    
    st.subheader("Bachelor of Technology in Computer Science")
    st.write("Indian Institute of Technology, Bombay\nGPA: 8.7/10\nJuly 2017 - May 2021")
    
    # Work Experience Section
    st.header("Work Experience")
    st.subheader("Data Scientist Intern")
    st.write("Google, Inc.\nMay 2022 - August 2022\n- Developed predictive models for product recommendation systems.\n- Worked on enhancing data processing speeds by 20%.\n- Collaborated with cross-functional teams to deliver insights.")
    
    st.subheader("Software Engineer Intern")
    st.write("Microsoft\nMay 2020 - July 2020\n- Assisted in developing cloud-based solutions for data management.\n- Optimized algorithm performance, reducing runtime by 30%.\n- Partook in code reviews and provided technical assistance to peers.")

    # Certifications Section
    st.header("Certifications")
    st.write("- AWS Certified Solutions Architect\n- TensorFlow Developer Certificate\n- Certified Data Science Specialist")
    
    # Projects Section
    st.header("Projects")
    st.subheader("AI-based Chatbot")
    st.write("Developed an AI-based chatbot for customer support that reduced response time by 60% using NLP techniques.")
    
    st.subheader("E-commerce Analytics Dashboard")
    st.write("Created a comprehensive analytics dashboard for an e-commerce company to track customer behavior and sales trends.")

    # Skills Section
    st.header("Skills")
    st.write("- Programming Languages: Python, Java, C++\n- Tools & Technologies: TensorFlow, PyTorch, Apache Spark, Docker\n- Databases: MySQL, MongoDB")
    
    # Languages Section
    st.header("Languages")
    st.write("- English: Professional Proficiency\n- Hindi: Native Speaker\n- Spanish: Intermediate Proficiency")
    
    # Interests Section
    st.header("Interests")
    st.write("- Artificial Intelligence\n- Blockchain Technology\n- Hiking and Outdoor Adventures")

    # Contact Information Section
    st.header("Contact Information")
    st.write("Email: saanvi.ravikiran@email.com\nPhone: (123) 456-7890\nLinkedIn: linkedin.com/in/saanviravikiran")

if __name__ == "__main__":
    main()