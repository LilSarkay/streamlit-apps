__updated__ = "Thu Jul 10 10:48:49 UTC 2025"
# Necessary imports
import streamlit as st

# Define a function to extract data from Saanvi Ravikiran's resume
# This would simulate parsing or extracting from a resume file
# Here, we assume a dictionary format for simplicity

def get_resume_data():
    # Example data extracted from a resume
    data = {
        "name": "Saanvi Ravikiran",
        "email": "saanvi.ravikiran@example.com",
        "summary": "Experienced data scientist with a strong foundation in machine learning, data analytics, and research. Passionate about leveraging data-driven insights to drive strategic decision-making.",
        "projects": [
            {
                "title": "Predictive Analytics on Sales Data",
                "description": "Developed predictive models to forecast sales trends using machine learning algorithms.",
                "technologies": ["Python", "scikit-learn", "pandas"]
            },
            {
                "title": "Natural Language Processing for Social Media",
                "description": "Analyzed and processed large datasets from social media platforms to extract meaningful insights.",
                "technologies": ["Python", "NLTK", "TensorFlow"]
            }
        ],
        "skills": ["Python", "Machine Learning", "Data Analysis", "NLP", "TensorFlow"],
        "education": "M.S. in Data Science, University of Example, 2021"
    }
    return data


def main():
    st.title("Saanvi Ravikiran's Resume")
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Go to", ["Summary", "Projects", "Skills", "Education"])

    # Extract resume data
    resume_data = get_resume_data()

    # Display selected section from the navigation
    if options == "Summary":
        st.subheader("Summary")
        st.write(resume_data["summary"])

    elif options == "Projects":
        st.subheader("Projects")
        for project in resume_data["projects"]:
            st.markdown(f"**{project['title']}**")
            st.write(project['description'])
            st.text(f"Technologies: {', '.join(project['technologies'])}")

    elif options == "Skills":
        st.subheader("Skills")
        st.write(", ".join(resume_data["skills"]))

    elif options == "Education":
        st.subheader("Education")
        st.write(resume_data["education"])


if __name__ == '__main__':
    main()