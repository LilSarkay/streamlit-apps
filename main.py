import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return 'Cannot divide by zero'

st.title('Simple Calculator')

operation = st.selectbox('Select operation', ['Add', 'Subtract', 'Multiply', 'Divide'])
a = st.number_input('Enter first number', value=0)
b = st.number_input('Enter second number', value=0)

if st.button('Calculate'):
    if operation == 'Add':
        result = add(a, b)
    elif operation == 'Subtract':
        result = subtract(a, b)
    elif operation == 'Multiply':
        result = multiply(a, b)
    elif operation == 'Divide':
        result = divide(a, b)
    else:
        result = 'Invalid operation'
    
    st.write('Result:', result)