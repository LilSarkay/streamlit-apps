__updated__ = "Fri Jul 11 10:45:10 UTC 2025"
import streamlit as st

def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return 'Error: Division by zero'

st.title('Basic Calculator')

num1 = st.number_input('Enter the first number', format='%f')
num2 = st.number_input('Enter the second number', format='%f')

operation = st.selectbox('Select operation', ('Add', 'Subtract', 'Multiply', 'Divide'))

if st.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.write(f'The result is: {result}')