import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Function to fetch a random image
def fetch_random_image():
    response = requests.get("https://via.placeholder.com/150")
    return Image.open(BytesIO(response.content))

# Function to display the software engineer's profile
def display_profile():
    st.title("Software Engineer Portfolio")

    # Profile Image
    image = fetch_random_image()
    st.image(image, caption='Profile Image', use_column_width=true)

    # Profile Details
    st.header("John Doe")
    st.subheader("Background")
    st.write("""
    John Doe is a highly skilled software engineer with over 8 years of experience in developing scalable software solutions. 
    He has a strong passion for coding and leveraging modern technologies to solve complex problems.
    """)

    st.subheader("Experience")
    st.write("""
    - Senior Software Engineer at TechCorp (2019-Present)
    - Software Developer at Coding Solutions Inc. (2015-2019)
    """)

    st.subheader("Key Skills")
    st.write("""
    - Proficient in Python, JavaScript, and Java.
    - Expertise in web development frameworks like Django and React.
    - Strong understanding of cloud services such as AWS and Azure.
    """)

    st.subheader("Projects")
    st.write("""
    - Developed an e-commerce platform handling over 1 million users.
    - Led a team to build a real-time analytics tool for data processing.
    """)

    st.subheader("Contact Information")
    st.write("""
    - Email: johndoe@example.com
    - LinkedIn: [John Doe LinkedIn](https://www.linkedin.com)
    """)

def main():
    display_profile()

if __name__ == "__main__":
    main()