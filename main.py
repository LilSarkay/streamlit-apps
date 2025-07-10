__updated__ = "Thu Jul 10 10:33:55 UTC 2025"
# Streamlit code for Saanvi Ravikiran's updated portfolio

import streamlit as st

st.set_page_config(page_title="Saanvi Ravikiran Portfolio", layout="wide")

st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to:", ('About Me', 'Projects', 'Contact'))

if option == 'About Me':
    st.title('About Me')
    st.write("Hello! I'm Saanvi Ravikiran, a passionate Data Scientist with expertise in Machine Learning and Data Analysis.")
    st.write("With a strong background in statistics and computer science, I have 5 years of experience in developing data-driven solutions.")
    st.write("I love transforming data into actionable insights and am constantly seeking new opportunities to grow in this ever-evolving field.")

elif option == 'Projects':
    st.title('Projects')
    st.write("Here are a few projects that I have worked on:")
    st.markdown("- **Project A:** Developed a predictive model for sales forecasting, which improved accuracy by 20%.")
    st.markdown("- **Project B:** Created a sentiment analysis tool that achieved 85% accuracy in classifying social media posts.")
    st.markdown("- **Project C:** Worked on a recommendation system that increased user engagement by 30%.")

elif option == 'Contact':
    st.title('Contact')
    st.write('Feel free to reach out to me via [LinkedIn](https://www.linkedin.com/in/saanviravikiran) or [Email](mailto:saanvi@example.com).')