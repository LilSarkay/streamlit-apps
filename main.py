import streamlit as st
import random

# List of motivational quotes
defined_quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Not how long, but how well you have lived is the main thing. - Seneca",
    "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon"
]

# Function to get a random quote
def get_random_quote():
    return random.choice(defined_quotes)

# App title
st.title("Motivational Quote Generator")

# Display a random quote initially
displayed_quote = st.empty()
displayed_quote.text(get_random_quote())

# Button to get a new quote
if st.button('New Quote'):
    new_quote = get_random_quote()
    displayed_quote.text(new_quote)

# Allow users to suggest a new quote
st.write("### Suggest a New Quote")
user_quote = st.text_input("Enter your motivational quote suggestion:")

if st.button('Submit Quote'):
    if user_quote:
        st.success("Thank you for your suggestion!")
    else:
        st.error("Please enter a quote before submitting.")