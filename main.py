import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data Dashboard
st.title('Data Dashboard')
df = pd.DataFrame(np.random.randn(100, 5), columns=list('ABCDE'))
st.line_chart(df)

# Machine Learning Predictions
st.title('Machine Learning Predictions')
X = np.random.rand(100, 1) * 100
y = X * 0.5 + np.random.normal(0, 10, (100, 1))
model = LinearRegression()
model.fit(X, y)
X_new = np.array([[50]])
pred = model.predict(X_new)
st.write(f'Prediction for input 50: {pred[0]}')

# Data Exploration
st.title('Data Exploration')
st.dataframe(df.describe())

# User Input Forms
st.title('User Input Form')
name = st.text_input('Enter your name:')
if st.button('Submit'):
    st.write(f'Hello, {name}!')

# Simple Game or Simulator
st.title('Simple Dice Roll Game')
dice_roll = st.button('Roll a dice')
if dice_roll:
    dice_result = np.random.randint(1, 7)
    st.write(f'You rolled a {dice_result}!')

# Text Processing
st.title('Text Processing')
text = st.text_area('Enter text:')
if st.button('Analyze Text'):
    st.write(f'Text Length: {len(text)} characters')

# Financial Analysis
st.title('Financial Analysis')
financial_data = {'Prices': np.random.rand(30) * 100}
st.line_chart(financial_data)

# Geospatial Data
st.title('Geospatial Data')
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)