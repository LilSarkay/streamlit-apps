import streamlit as st
from streamlit_color_picker import st_color_picker

# Set page config
define_page_config = st.set_page_config(
    page_title="Color Mood Picker",
    page_icon=":rainbow:",
    layout="wide"
)

# Custom CSS for unique UI
define_custom_css = st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(to bottom right, #f0f4f8, #d9e4f5);
        color: #333333;
    }
    .color-picker {
        text-align: center;
        margin-top: 50px;
    }
    .mood-message {
        font-size: 1.5rem;
        margin-top: 30px;
        color: #0d3b66;
        text-shadow: 1px 1px 2px #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=true
)

# Function to get mood message
def get_mood(color):
    """Returns a mood message based on the selected color."""
    mood_dict = {
        "#0000ff": "You feel calm today.",  # Blue
        "#ff0000": "You're energetic!",   # Red
        "#00ff00": "You're feeling lively!",  # Green
        "#ffff00": "You're cheerful!",  # Yellow
        "#ffa500": "You're feeling inspired!",  # Orange
        "#800080": "You're in a creative mood!",  # Purple
    }
    return mood_dict.get(color, "You're feeling unique today!")

# App layout and elements
st.title("Color Mood Picker")

# Displaying Color Picker
with st.container():
    st.subheader("Pick a Color")
    selected_color = st_color_picker("Choose a color", "#0000ff", key="color-picker", label_visibility='collapsed')
    st.write("Selected color:", selected_color)

# Displaying Mood Message
with st.container():
    st.subheader("Mood Reflection")
    mood_message = get_mood(selected_color)
    st.markdown(f'<div class="mood-message">{mood_message}</div>', unsafe_allow_html=true)