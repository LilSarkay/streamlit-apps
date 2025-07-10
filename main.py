import streamlit as st

# Simple Calculator App
def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        if num2 == 0:
            return 'Error! Division by zero.'
        else:
            return num1 / num2

st.title('Simple Calculator')

num1 = st.number_input('Enter first number:', value=0)
num2 = st.number_input('Enter second number:', value=0)

operation = st.selectbox('Choose an operation:', ('Add', 'Subtract', 'Multiply', 'Divide'))

if st.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.write('Result: ', result)