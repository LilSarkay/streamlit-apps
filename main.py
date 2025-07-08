import streamlit as st

# Set up the page
def set_weather_background(weather):
    if weather == "Sunny":
        st.markdown('<style>body {background-color: #FFDEAD;}</style>', unsafe_allow_html=true)
    elif weather == "Rainy":
        st.markdown('<style>body {background-color: #6495ED;}</style>', unsafe_allow_html=true)
    elif weather == "Cloudy":
        st.markdown('<style>body {background-color: #D3D3D3;}</style>', unsafe_allow_html=true)
    elif weather == "Stormy":
        st.markdown('<style>body {background-color: #778899;}</style>', unsafe_allow_html=true)

# App title
st.title("Weather Mood Visualizer")

# Dropdown menu for weather conditions
weather_option = st.selectbox(
    "Select a weather condition:",
    ("Sunny", "Rainy", "Cloudy", "Stormy")
)

# Display emoji based on the weather condition
if weather_option == "Sunny":
    st.header("☀️ It's a bright sunny day!")
elif weather_option == "Rainy":
    st.header("🌧️ Don't forget your umbrella!")
elif weather_option == "Cloudy":
    st.header("☁️ It's a bit gloomy today.")
elif weather_option == "Stormy":
    st.header("⛈️ Stay safe from the storm!")

# Set the background color based on the weather condition
set_weather_background(weather_option)