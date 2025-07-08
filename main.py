import streamlit as st

st.title("BMI Calculator")

# User inputs
height = st.number_input("Enter your height (in cm):", min_value=50, max_value=250, step=1)
weight = st.number_input("Enter your weight (in kg):", min_value=10, max_value=300, step=1)

# Calculate BMI
if height and weight:
    bmi = weight / ((height / 100) ** 2)
    st.write(f"Your BMI is: **{bmi:.2f}**")

    # Interpret result
    if bmi < 18.5:
        st.info("You're underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a healthy weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You're overweight.")
    else:
        st.error("You are obese.")
