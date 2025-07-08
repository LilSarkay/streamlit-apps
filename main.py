import streamlit as st
import random

# Set the title of the Streamlit app
st.title('Motivational Quote Generator')

# List of motivational quotes
quotes = [
    "Believe you can and you're halfway there. -Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
    "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. -Winston S. Churchill",
    "It always seems impossible until it's done. -Nelson Mandela"
]

# Function to get a random quote
def get_random_quote():
    return random.choice(quotes)

# Create a button in the UI to generate a quote
if st.button('Get Quote'):
    st.write(get_random_quote())