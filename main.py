import streamlit as st

# App title
st.title('Temperature Converter')

# Input: Temperature value
temperature = st.number_input('Enter temperature:', format='%f')

# Conversion choice
conversion = st.selectbox('Convert to:', ('Celsius to Fahrenheit', 'Fahrenheit to Celsius'))

# Conversion logic
if conversion == 'Celsius to Fahrenheit':
    converted_temp = temperature * 9 / 5 + 32
    st.write(f'{temperature}° Celsius is equal to {converted_temp:.2f}° Fahrenheit')
elif conversion == 'Fahrenheit to Celsius':
    converted_temp = (temperature - 32) * 5 / 9
    st.write(f'{temperature}° Fahrenheit is equal to {converted_temp:.2f}° Celsius')