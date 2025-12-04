import streamlit as st
from predict import predict

# Iris species names
species_names = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

st.title("Iris Species Predictor")
st.write("Enter the measurements of an iris flower to predict its species.")

# Input fields for the 4 features
st.header("Flower Measurements")
col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.0, step=0.1)

with col2:
    petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2, step=0.1)

# Predict button
if st.button("Predict"):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    prediction = predict(features)
    species = species_names[prediction]
    
    st.success(f"Predicted Species: **{species}**")
    st.write(f"Class: {prediction}")

