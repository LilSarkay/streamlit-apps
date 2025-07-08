import streamlit as st

def main():
    st.title('Greeting App')
    name = st.text_input('Enter your name:')
    if name:
        st.write(f'Hello, {name}! Welcome to the Greeting App.')

if __name__ == '__main__':
    main()