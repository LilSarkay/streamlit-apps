import streamlit as st

st.title('Temperature Converter')

st.write('Convert temperatures between Celsius and Fahrenheit.')

# Get user input
input_temp = st.number_input('Enter temperature')
option = st.selectbox('Convert to:', ('Celsius', 'Fahrenheit'))

# Conversion logic
def convert_temperature(temp, to_scale):
    if to_scale == 'Celsius':
        return (temp - 32) * 5.0/9.0
    elif to_scale == 'Fahrenheit':
        return (temp * 9.0/5.0) + 32

# Perform conversion
converted_temp = convert_temperature(input_temp, option)

# Display the result
st.write('Converted temperature:', converted_temp)