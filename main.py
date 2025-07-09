import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

st.title("Simple Calculator")

num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)

operation = st.selectbox("Select operation:", ("Add", "Subtract", "Multiply", "Divide"))

if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    else:
        result = "Invalid operation"
    
    st.write(f"Result: {result}")