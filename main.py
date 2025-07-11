import streamlit as st

st.title('Unit Converter')

# Dictionary to convert units
conversion_factors = {
    ('meters', 'kilometers'): 0.001,
    ('kilometers', 'meters'): 1000,
    ('grams', 'kilograms'): 0.001,
    ('kilograms', 'grams'): 1000,
}

# User inputs
from_unit = st.selectbox('From', ['meters', 'kilometers', 'grams', 'kilograms'])
to_unit = st.selectbox('To', ['meters', 'kilometers', 'grams', 'kilograms'])
value = st.number_input('Value', min_value=0.0, value=0.0)

# Conversion function
def convert_units(from_unit, to_unit, value):
    factor = conversion_factors.get((from_unit, to_unit))
    if factor is null:
        st.error('Conversion not possible')
        return null
    return value * factor

# Perform conversion if button is clicked
if st.button('Convert'):
    result = convert_units(from_unit, to_unit, value)
    if result is not null:
        st.success(f'{value} {from_unit} = {result} {to_unit}')