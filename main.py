import streamlit as st

# Title of the app
st.title("Basic Calculator")

# Input fields for numbers
number1 = st.number_input("Enter first number", format="%.2f")
number2 = st.number_input("Enter second number", format="%.2f")

# Selection box for operation
operation = st.selectbox("Choose operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation
if st.button("Compute"):
    if operation == "Add":
        result = number1 + number2
        st.write(f"Result: {result}")
    elif operation == "Subtract":
        result = number1 - number2
        st.write(f"Result: {result}")
    elif operation == "Multiply":
        result = number1 * number2
        st.write(f"Result: {result}")
    elif operation == "Divide":
        if number2 != 0:
            result = number1 / number2
            st.write(f"Result: {result}")
        else:
            st.write("Error: Division by zero is not allowed.")