import streamlit as st

# Set up the app title
st.title('Favorite Color App')

# Create a dropdown to select the favorite color
color = st.selectbox('Select your favorite color:', ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange'])

# Display the selected favorite color
st.write(f'Your favorite color is {color}.')