import streamlit as st
import random

st.title('Welcome to our motivational app!')
st.subheader('Motivational Quote of the Day')

quotes = [
    'Believe in yourself.',
    'You can achieve anything.',
    'Stay positive and strong.',
    'Your limitation—it’s only your imagination.',
    'Push yourself, because no one else is going to do it for you.'
]

quote = random.choice(quotes)
st.write(quote)