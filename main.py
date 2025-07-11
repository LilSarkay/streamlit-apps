__updated__ = "Fri Jul 11 11:09:57 UTC 2025"
import streamlit as st

# Title of the app
st.title('Unit Converter')

# Select the type of conversion
type_of_conversion = st.selectbox('Select the type of conversion you would like to perform:', ['Length', 'Temperature', 'Weight'])

if type_of_conversion == 'Length':
    # Length conversion
    units = ['Meters', 'Kilometers', 'Miles', 'Feet']
    input_unit = st.selectbox('Choose unit to convert from:', units)
    output_unit = st.selectbox('Choose unit to convert to:', units)
    value = st.number_input(f'Enter value in {input_unit}:', min_value=0.0)
    
    # Conversion logic
    if input_unit == 'Meters' and output_unit == 'Kilometers':
        converted_value = value / 1000
    elif input_unit == 'Kilometers' and output_unit == 'Meters':
        converted_value = value * 1000
    elif input_unit == 'Meters' and output_unit == 'Miles':
        converted_value = value / 1609.34
    elif input_unit == 'Miles' and output_unit == 'Meters':
        converted_value = value * 1609.34
    elif input_unit == 'Kilometers' and output_unit == 'Miles':
        converted_value = value / 1.60934
    elif input_unit == 'Miles' and output_unit == 'Kilometers':
        converted_value = value * 1.60934
    elif input_unit == 'Feet' and output_unit == 'Meters':
        converted_value = value / 3.28084
    elif input_unit == 'Meters' and output_unit == 'Feet':
        converted_value = value * 3.28084
    elif input_unit == 'Feet' and output_unit == 'Miles':
        converted_value = value / 5280
    elif input_unit == 'Miles' and output_unit == 'Feet':
        converted_value = value * 5280
    elif input_unit == 'Feet' and output_unit == 'Kilometers':
        converted_value = value / 3280.84
    elif input_unit == 'Kilometers' and output_unit == 'Feet':
        converted_value = value * 3280.84
    else:
        converted_value = value  # Same unit
    
    st.write(f'{value} {input_unit} is equal to {converted_value} {output_unit}')
    
elif type_of_conversion == 'Temperature':
    # Temperature conversion
    units = ['Celsius', 'Fahrenheit', 'Kelvin']
    input_unit = st.selectbox('Choose unit to convert from:', units)
    output_unit = st.selectbox('Choose unit to convert to:', units)
    value = st.number_input(f'Enter temperature in {input_unit}:', min_value=-273.15)
    
    # Conversion logic
    if input_unit == 'Celsius' and output_unit == 'Fahrenheit':
        converted_value = (value * 9/5) + 32
    elif input_unit == 'Fahrenheit' and output_unit == 'Celsius':
        converted_value = (value - 32) * 5/9
    elif input_unit == 'Celsius' and output_unit == 'Kelvin':
        converted_value = value + 273.15
    elif input_unit == 'Kelvin' and output_unit == 'Celsius':
        converted_value = value - 273.15
    elif input_unit == 'Fahrenheit' and output_unit == 'Kelvin':
        converted_value = (value + 459.67) * 5/9
    elif input_unit == 'Kelvin' and output_unit == 'Fahrenheit':
        converted_value = (value * 9/5) - 459.67
    else:
        converted_value = value  # Same unit
    
    st.write(f'{value} {input_unit} is equal to {converted_value} {output_unit}')

elif type_of_conversion == 'Weight':
    # Weight conversion
    units = ['Grams', 'Kilograms', 'Pounds', 'Ounces']
    input_unit = st.selectbox('Choose unit to convert from:', units)
    output_unit = st.selectbox('Choose unit to convert to:', units)
    value = st.number_input(f'Enter weight in {input_unit}:', min_value=0.0)
    
    # Conversion logic
    if input_unit == 'Grams' and output_unit == 'Kilograms':
        converted_value = value / 1000
    elif input_unit == 'Kilograms' and output_unit == 'Grams':
        converted_value = value * 1000
    elif input_unit == 'Grams' and output_unit == 'Pounds':
        converted_value = value / 453.592
    elif input_unit == 'Pounds' and output_unit == 'Grams':
        converted_value = value * 453.592
    elif input_unit == 'Kilograms' and output_unit == 'Pounds':
        converted_value = value * 2.20462
    elif input_unit == 'Pounds' and output_unit == 'Kilograms':
        converted_value = value / 2.20462
    elif input_unit == 'Ounces' and output_unit == 'Grams':
        converted_value = value * 28.3495
    elif input_unit == 'Grams' and output_unit == 'Ounces':
        converted_value = value / 28.3495
    elif input_unit == 'Pounds' and output_unit == 'Ounces':
        converted_value = value * 16
    elif input_unit == 'Ounces' and output_unit == 'Pounds':
        converted_value = value / 16
    elif input_unit == 'Kilograms' and output_unit == 'Ounces':
        converted_value = value * 35.274
    elif input_unit == 'Ounces' and output_unit == 'Kilograms':
        converted_value = value / 35.274
    else:
        converted_value = value  # Same unit
    
    st.write(f'{value} {input_unit} is equal to {converted_value} {output_unit}')