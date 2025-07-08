import streamlit as st
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("housing.csv")

# Title
st.title("🏡 California Housing Price Predictor")
st.write("Predict house prices based on features like median income, population, and more.")

# Sidebar Inputs
st.sidebar.header("Input Features")

median_income = st.sidebar.slider("Median Income", 0.0, 15.0, 3.0)
population = st.sidebar.slider("Population", 0, 35000, 1000)
housing_median_age = st.sidebar.slider("Housing Median Age", 1, 52, 20)
total_rooms = st.sidebar.slider("Total Rooms", 500, 50000, 2000)
total_bedrooms = st.sidebar.slider("Total Bedrooms", 100, 10000, 500)

# Train a simple model (on the fly)
features = ['median_income', 'population', 'housing_median_age', 'total_rooms', 'total_bedrooms']
X = data[features]
y = data['median_house_value']

model = RandomForestRegressor()
model.fit(X, y)

# Prediction
input_df = pd.DataFrame([[median_income, population, housing_median_age, total_rooms, total_bedrooms]],
                        columns=features)

prediction = model.predict(input_df)[0]

st.success(f"🏠 Predicted House Price: ${int(prediction):,}")
