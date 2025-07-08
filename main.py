import streamlit as st

# Title
st.title("Simple Calculator App")

# Input numbers
a = st.number_input("Enter first number", format="%.2f")
b = st.number_input("Enter second number", format="%.2f")

# Select operation
operation = st.selectbox("Choose an operation", ("Addition", "Subtraction", "Multiplication", "Division"))

result = null

# Perform calculation
if operation == "Addition":
    result = a + b
elif operation == "Subtraction":
    result = a - b
elif operation == "Multiplication":
    result = a * b
elif operation == "Division":
    if b != 0:
        result = a / b
    else:
        st.error("Error: Cannot divide by zero.")

# Display result
if result is not null:
    st.write("The result of ", operation.lower(), " is: ", result)