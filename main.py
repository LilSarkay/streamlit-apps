import streamlit as st

st.title('Simple Calculator')

# Input fields for numbers
number1 = st.number_input('Enter first number', value=0.0)
number2 = st.number_input('Enter second number', value=0.0)

# Dropdown for selecting arithmetic operation
operation = st.selectbox('Select Operation', ('Add', 'Subtract', 'Multiply', 'Divide'))

# Calculate result based on the selected operation
def calculate(num1, num2, op):
    try:
        if op == 'Add':
            return num1 + num2
        elif op == 'Subtract':
            return num1 - num2
        elif op == 'Multiply':
            return num1 * num2
        elif op == 'Divide':
            if num2 == 0:
                return 'Error: Division by zero'
            else:
                return num1 / num2
    except Exception as e:
        return f'Error: {str(e)}'

# Button to perform calculation
if st.button('Calculate'):
    result = calculate(number1, number2, operation)
    st.write('Result:', result)