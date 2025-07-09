# Updated at Wed Jul  9 07:19:42 UTC 2025
import streamlit as st

# Define a function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else 'Error: Division by zero'

# Set the title of the app
st.title('Simple Calculator')

# Create input fields for the two numbers
num1 = st.number_input('Enter first number', value=0.0)
num2 = st.number_input('Enter second number', value=0.0)

# Create a dropdown to select the arithmetic operation
operation = st.selectbox('Select an operation', ('+', '-', '*', '/'))

# Initialize session state for result if not present
if 'result' not in st.session_state:
    st.session_state.result = null

# Create a button to perform the calculation
if st.button('Calculate'):
    st.session_state.result = calculate(num1, num2, operation)

# Display the result
if st.session_state.result is not null:
    st.write('Result:', st.session_state.result)