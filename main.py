__updated__ = "Fri Jul 11 11:11:04 UTC 2025"
import streamlit as st

# Title of the app
st.title("Unit Converter")

# Sidebar for selecting conversion type
conversion_type = st.sidebar.selectbox("Select conversion type", ('Length', 'Weight', 'Temperature'))

# Function to convert length
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        'meters': 1.0,
        'kilometers': 0.001,
        'centimeters': 100.0,
        'millimeters': 1000.0,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084,
        'inches': 39.3701
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Function to convert weight
def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        'kilograms': 1.0,
        'grams': 1000.0,
        'pounds': 2.20462,
        'ounces': 35.274
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return value

if conversion_type == 'Length':
    st.header("Length Converter")
    length_units = ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches']
    value = st.number_input("Enter length", min_value=0.0)
    from_unit = st.selectbox("From", length_units)
    to_unit = st.selectbox("To", length_units)
    result = convert_length(value, from_unit, to_unit)
    st.write("{} {} is {} {}".format(value, from_unit, result, to_unit))

elif conversion_type == 'Weight':
    st.header("Weight Converter")
    weight_units = ['kilograms', 'grams', 'pounds', 'ounces']
    value = st.number_input("Enter weight", min_value=0.0)
    from_unit = st.selectbox("From", weight_units)
    to_unit = st.selectbox("To", weight_units)
    result = convert_weight(value, from_unit, to_unit)
    st.write("{} {} is {} {}".format(value, from_unit, result, to_unit))

elif conversion_type == 'Temperature':
    st.header("Temperature Converter")
    temperature_units = ['celsius', 'fahrenheit', 'kelvin']
    value = st.number_input("Enter temperature")
    from_unit = st.selectbox("From", temperature_units)
    to_unit = st.selectbox("To", temperature_units)
    result = convert_temperature(value, from_unit, to_unit)
    st.write("{} {} is {} {}".format(value, from_unit, result, to_unit))