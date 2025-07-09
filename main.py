import streamlit as st

# Title of the app
st.title('Simple Calculator')

# Input numbers
a = st.number_input('Enter the first number:', min_value=0)
b = st.number_input('Enter the second number:', min_value=0)

# Dropdown for selecting operations
operation = st.selectbox('Choose an operation:', ('Add', 'Subtract', 'Multiply', 'Divide'))

# Calculation logic
def calculate(a, b, operation):
    if operation == 'Add':
        return a + b
    elif operation == 'Subtract':
        return a - b
    elif operation == 'Multiply':
        return a * b
    elif operation == 'Divide':
        return a / b if b != 0 else 'Error: Division by zero'

# Button to perform calculation
if st.button('Calculate'):
    result = calculate(a, b, operation)
    st.write('Result:', result)