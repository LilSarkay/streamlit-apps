import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train a RandomForest model
clf = RandomForestClassifier()
clf.fit(X, y)

# Streamlit app
st.title('Iris Flower Prediction')
st.write('This app predicts the iris flower type!')

# User input
sepal_length = st.slider('Sepal length', float(X[:, 0].min()), float(X[:, 0].max()))
sepal_width = st.slider('Sepal width', float(X[:, 1].min()), float(X[:, 1].max()))
petal_length = st.slider('Petal length', float(X[:, 2].min()), float(X[:, 2].max()))
petal_width = st.slider('Petal width', float(X[:, 3].min()), float(X[:, 3].max()))

# Make prediction
user_input = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = clf.predict(user_input)

st.write(f'The predicted iris flower type is: {iris.target_names[prediction][0]}')