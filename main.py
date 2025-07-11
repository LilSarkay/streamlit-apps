import streamlit as st

st.title('Basic Calculator')

num1 = st.number_input('Enter first number:', value=0)
num2 = st.number_input('Enter second number:', value=0)
operation = st.selectbox('Select operation', ('Add', 'Subtract', 'Multiply', 'Divide'))

if operation == 'Add':
    result = num1 + num2
elif operation == 'Subtract':
    result = num1 - num2
elif operation == 'Multiply':
    result = num1 * num2
elif operation == 'Divide':
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Infinity'
else:
    result = 'Invalid Operation'

st.write('Result:', result)