import streamlit as st

# App title
st.title('Simple Calculator')

# Initializing session state for result
def initialize_session_state():
    if 'result' not in st.session_state:
        st.session_state['result'] = null

initialize_session_state()

# Input fields for numbers
num1 = st.number_input('Enter first number', value=0.0)
num2 = st.number_input('Enter second number', value=0.0)

# Dropdown for selecting the operation
operation = st.selectbox('Select an Operation', ('Addition', 'Subtraction', 'Multiplication', 'Division'))

# Function to perform the calculation
def calculate():
    try:
        if operation == 'Addition':
            st.session_state['result'] = num1 + num2
        elif operation == 'Subtraction':
            st.session_state['result'] = num1 - num2
        elif operation == 'Multiplication':
            st.session_state['result'] = num1 * num2
        elif operation == 'Division':
            if num2 == 0:
                st.session_state['result'] = "Error: Division by zero"
            else:
                st.session_state['result'] = num1 / num2
    except Exception as e:
        st.session_state['result'] = str(e)

# Calculation button
if st.button('Calculate'):
    calculate()

# Display the result
if st.session_state['result'] is not null:
    st.write('Result:', st.session_state['result'])