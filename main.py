import streamlit as st

st.title('Simple Calculator')

# Getting user input for numbers
number1 = st.number_input('Enter first number', value=0)
number2 = st.number_input('Enter second number', value=0)

# Perform calculations
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
try:
    division = number1 / number2
except ZeroDivisionError:
    division = 'Infinity'

# Display results
st.write(f"Addition: {addition}")
st.write(f"Subtraction: {subtraction}")
st.write(f"Multiplication: {multiplication}")
st.write(f"Division: {division}")