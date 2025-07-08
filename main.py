import streamlit as st
import random

# Title of the app
st.title("Motivational Quote Generator")

# List of motivational quotes
quotes = [
    "The Best Way To Get Started Is To Quit Talking And Begin Doing.",
    "The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.",
    "Don’t Let Yesterday Take Up Too Much Of Today.",
    "You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.",
    "It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.",
    "If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You."
]

# Function to get a random quote
def get_random_quote():
    return random.choice(quotes)

# Display a random quote in red color
quote = get_random_quote()
st.markdown(f"<p style='color:red;'>{quote}</p>", unsafe_allow_html=true)