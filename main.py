import streamlit as st

def calculator():
    st.title("Basic Calculator")
    
    # Input fields for numbers
    num1 = st.number_input("Enter first number:")
    num2 = st.number_input("Enter second number:")
    
    # Dropdown for operation selection
    operation = st.selectbox("Select Operation", ("Add", "Subtract", "Multiply", "Divide"))
    result = null

    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero")
        
        st.success(f'The result is: {result}')

if __name__ == '__main__':
    calculator()