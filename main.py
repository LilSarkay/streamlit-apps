import streamlit as st
import random

st.title('Startup Name Generator')

st.write('Click the button below to generate a new startup name!')

tech_prefixes = ['Hyper', 'Neo', 'Quantum', 'Inno', 'Tech', 'Ultra']
suffixes = ['Sync', 'Labs', 'Stack', 'Works', 'Dynamics', 'Solutions']

def generate_startup_name():
    prefix = random.choice(tech_prefixes)
    suffix = random.choice(suffixes)
    return f"{prefix}{suffix}"

if st.button('Generate Name'):
    name = generate_startup_name()
    st.success(f'Your Startup Name: {name}')