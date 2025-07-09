import streamlit as st

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return false
    if n <= 3:
        return true
    if n % 2 == 0 or n % 3 == 0:
        return false
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return false
        i += 6
    return true

st.title('Prime Checker')

number = st.number_input('Enter a number to check if it is prime:', value=2, min_value=0)

if st.button('Check'):
    if is_prime(number):
        st.success(f'{number} is a prime number!')
    else:
        st.error(f'{number} is not a prime number.')