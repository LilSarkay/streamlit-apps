import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        'meters': 1,
        'kilometers': 0.001,
        'miles': 0.000621371,
        'feet': 3.28084
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return null
    value_in_meters = value / conversion_factors[from_unit]
    return value_in_meters * conversion_factors[to_unit]

st.title('Unit Converter')

value = st.number_input('Enter the value to be converted', min_value=0.0)
from_unit = st.selectbox('From Unit', ['meters', 'kilometers', 'miles', 'feet'])
to_unit = st.selectbox('To Unit', ['meters', 'kilometers', 'miles', 'feet'])

if st.button('Convert'):
    result = convert_units(value, from_unit, to_unit)
    if result is not null:
        st.write(f'{value} {from_unit} is equal to {result} {to_unit}')
    else:
        st.write('Invalid unit conversion')