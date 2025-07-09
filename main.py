import streamlit as st

st.title('Simple Calculator')

# User inputs
num1 = st.number_input('Enter the first number:', value=0.0)
num2 = st.number_input('Enter the second number:', value=0.0)
operation = st.selectbox('Select an operation:', ('Add', 'Subtract', 'Multiply', 'Divide'))

# Calculate
calculate = st.button('Calculate')

if calculate:
    try:
        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Multiply':
            result = num1 * num2
        elif operation == 'Divide':
            result = num1 / num2
        st.success(f'The result is: {result}')
    except Exception as e:
        st.error(f'Error: {e}')