__updated__ = "Thu Jul 10 10:18:19 UTC 2025"
import streamlit as st

# Data for Saanvi Ravikiran
personal_info = {
    "full_name": "Saanvi Ravikiran",
    "role": "Software Developer",
    "location": "Bangalore, India",
    "email": "saanvi.ravikiran@example.com",
    "phone": "+91-9876543210",
    "linkedin": "linkedin.com/in/saanvi-ravikiran"
}

skills = ["Python", "JavaScript", "SQL", "React", "Node.js"]

languages = ["English", "Hindi", "Kannada"]

interests = ["Artificial Intelligence", "Web Development", "Traveling"]

education = {
    "degree": "Bachelor of Technology in Computer Science",
    "university": "Indian Institute of Technology, Bombay",
    "year": "2018"
}

work_experience = {
    "company": "Tech Innovators Pvt Ltd",
    "position": "Software Developer",
    "duration": "June 2018 - Present",
    "responsibilities": [
        "Developed scalable web applications using React and Node.js",
        "Collaborated with cross-functional teams to define, design, and ship new features",
        "Optimized applications for maximum speed and scalability"
    ]
}

certificates = [
    "Certified Kubernetes Administrator",
    "AWS Certified Solutions Architect",
    "Microsoft Certified: Azure Developer Associate"
]

projects = [
    "Real-time Chat Application",
    "E-commerce Platform",
    "AI-Based Recommendation System"
]

st.title(f"Portfolio of {personal_info['full_name']}")

st.sidebar.title("Navigation")
options = ["Personal Info", "Skills", "Languages", "Interests", "Education", "Work Experience", "Certificates", "Projects"]
choice = st.sidebar.radio("Go to:", options)

if choice == "Personal Info":
    st.header("Personal Information")
    st.write(f"**Full Name:** {personal_info['full_name']}")
    st.write(f"**Role:** {personal_info['role']}")
    st.write(f"**Location:** {personal_info['location']}")
    st.write(f"**Email:** {personal_info['email']}")
    st.write(f"**Phone:** {personal_info['phone']}")
    st.write(f"**LinkedIn:** {personal_info['linkedin']}")

elif choice == "Skills":
    st.header("Skills")
    st.write(" ", ", ".join(skills))

elif choice == "Languages":
    st.header("Languages")
    st.write(" ", ", ".join(languages))

elif choice == "Interests":
    st.header("Interests")
    st.write(" ", ", ".join(interests))

elif choice == "Education":
    st.header("Education")
    st.write(f"**{education['degree']}**")
    st.write(f"{education['university']}, {education['year']}")

elif choice == "Work Experience":
    st.header("Work Experience")
    st.write(f"**{work_experience['company']}**")
    st.write(f"{work_experience['position']} ({work_experience['duration']})")
    st.write("Responsibilities:")
    for responsibility in work_experience['responsibilities']:
        st.write(f"- {responsibility}")

elif choice == "Certificates":
    st.header("Certificates")
    for certificate in certificates:
        st.write(f"- {certificate}")

elif choice == "Projects":
    st.header("Projects")
    for project in projects:
        st.write(f"- {project}")