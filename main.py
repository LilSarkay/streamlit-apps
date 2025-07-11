__updated__ = "Fri Jul 11 07:12:49 UTC 2025"
import streamlit as st

st.title('Basic Calculator')

number1 = st.number_input('Enter first number', value=0.0)
number2 = st.number_input('Enter second number', value=0.0)

operation = st.selectbox('Select operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

result = null

try:
    if operation == 'Add':
        result = number1 + number2
    elif operation == 'Subtract':
        result = number1 - number2
    elif operation == 'Multiply':
        result = number1 * number2
    elif operation == 'Divide':
        if number2 != 0:
            result = number1 / number2
        else:
            st.error('Error: Division by zero is not allowed.')
except Exception as e:
    st.error(f'An error occurred: {e}')

if result is not null:
    st.write('The result is:', result)