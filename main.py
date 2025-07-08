import streamlit as st
import random

# List of prefixes and suffixes
prefixes = ['Hyper', 'Neo', 'Quantum']
suffixes = ['Sync', 'Labs', 'Stack']

# Function to generate a startup name
def generate_startup_name():
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    return f"{prefix}{suffix}"

# Streamlit app
def main():
    st.title('Startup Name Generator')
    st.write("Click the button to generate a random startup name.")

    if st.button('Generate Name'):
        name = generate_startup_name()
        st.success(f"Your startup name is: {name}")

if __name__ == "__main__":
    main()