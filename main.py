import streamlit as st

def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by zero'

st.title('Simple Calculator')

num1 = st.number_input('Enter the first number:', value=0, format="%.2f")
num2 = st.number_input('Enter the second number:', value=0, format="%.2f")

operation = st.selectbox('Choose an operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

if st.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.write('Result:', result)