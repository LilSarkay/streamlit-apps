import streamlit as st
import random

# Predefined list of motivational quotes
quotes = [
    "Believe you can and you're halfway there.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction.",
]

# Streamlit app
def main():
    st.title("Random Motivational Quote Generator")
    
    if st.button('Get Quote'):
        quote = random.choice(quotes)
        st.write(quote)

if __name__ == "__main__":
    main()