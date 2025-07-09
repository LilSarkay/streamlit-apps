import streamlit as st

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by zero'

st.title('Simple Calculator')

num1 = st.number_input('Enter first number:', step=1.0)
num2 = st.number_input('Enter second number:', step=1.0)

operation = st.selectbox('Select operation:', ('+', '-', '*', '/'))

if st.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.write('Result:', result)