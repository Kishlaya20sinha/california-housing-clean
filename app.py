import streamlit as st
import pandas as pd
import joblib

<<<<<<< HEAD
model = joblib.load("your_model.pkl")  # Save your ML model using joblib or pickle
=======
model = joblib.load("california_housing_model.pkl")  # Save your ML model using joblib or pickle
>>>>>>> b4c1e1b (Updated app.py and requirements.txt)

st.title("🏡 California Housing Price Predictor")

# Collect input
median_income = st.slider("Median Income", 0.0, 15.0, 3.0)
house_age = st.slider("House Age", 1, 50, 10)
total_rooms = st.number_input("Total Rooms", value=2000)

# Predict
if st.button("Predict Price"):
    input_df = pd.DataFrame([[median_income, house_age, total_rooms]], 
                            columns=["median_income", "housing_median_age", "total_rooms"])
    prediction = model.predict(input_df)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
