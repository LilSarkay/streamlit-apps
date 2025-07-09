__updated__ = "Wed Jul  9 07:54:12 UTC 2025"
import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for numbers
number1 = st.number_input("Enter the first number:", format="%.2f")
number2 = st.number_input("Enter the second number:", format="%.2f")

# Select operationoperation = st.selectbox("Choose the operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Result calculation and display
if operation == "Add":
    result = number1 + number2
    st.write(f"The result is: {result}")
elif operation == "Subtract":
    result = number1 - number2
    st.write(f"The result is: {result}")
elif operation == "Multiply":
    result = number1 * number2
    st.write(f"The result is: {result}")
elif operation == "Divide":
    if number2 != 0:  # Avoid division by zero
        result = number1 / number2
        st.write(f"The result is: {result}")
    else:
        st.write("Cannot divide by zero!")