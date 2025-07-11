import streamlit as st

# Title of the app
st.title("Basic Calculator")

# Number inputs
a = st.number_input("Enter the first number:", value=0)
b = st.number_input("Enter the second number:", value=0)

# Dropdown for selecting operation
operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Perform button
def calculate(a, b, operation):
    if operation == "Add":
        return a + b
    elif operation == "Subtract":
        return a - b
    elif operation == "Multiply":
        return a * b
    elif operation == "Divide":
        return a / b if b != 0 else "Infinity"

if st.button("Perform"):
    result = calculate(a, b, operation)
    st.write(f"The result is: {result}")