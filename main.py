import streamlit as st

# Set up the app title and sidebar
st.set_page_config(page_title="App Suite", layout="wide")

# Title of the app
st.title("Welcome to Our App Suite")

# Sidebar navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio(
    'Select a page:',
    ('Home', 'Contact')
)

# Home page message
if options == 'Home':
    st.header("Home")
    st.write("Welcome to our application suite where we make it easy to deploy and share data applications!")
    
    # New Section: Features Built Using Streamlit
    st.subheader("Features Built Using Streamlit")
    st.write("Explore the variety of applications you can build with Streamlit:")
    st.write("- **Data Dashboards**: Interactive and real-time data visualization tools.")
    st.write("- **Machine Learning Apps**: Deploy machine learning models easily with interactive interfaces.")
    st.write("- **Data Analysis Tools**: Powerful analytical dashboards to manipulate and analyze data.")
    st.write("- **Financial Tools**: Handy financial calculators and stock market prediction apps.")
    st.write("- **Scientific Notebooks**: Conduct experiments and display results right alongside your code.")
    st.write("- **Geospatial Applications**: Maps and geospatial data plots at your fingertips.")
    st.write("- **Survey Apps**: Collect and visualize survey data effortlessly.")
    st.write("- **Education Tools**: Interactive educational applications and modules.")
    st.write("- **Content Management Systems**: Simple CMS solutions for managing digital content.")
    st.write("- **Healthcare Dashboards**: Visualize and share healthcare data securely.")
    st.write("- **Gaming Interfaces**: Build engaging and interactive game interfaces.")
    
# Contact page message
if options == 'Contact':
    st.header("Contact")
    st.write("You can contact us at appdev@example.com")