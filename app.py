import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("airbnb_price_model.pkl")

st.title("Airbnb Price Optimisation Tool(NYC)")

latitude = st.number_input("Latitude", value=40.7128)
longitude = st.number_input("Longitude", value=-74.0060)
minimum_nights = st.number_input("Minimum Nights", value=1)
reviews = st.number_input("Number of Reviews", value=10)
reviews_per_month = st.number_input("Reviews Per Month", value=0.5)
listings = st.number_input("Host Listings Count", value=1)
availability = st.number_input("Availability (days/year)", value=365)

# Dummy variables (room_type and neighbourhood_group)
room_type = st.selectbox("Room Type", ["Private room", "Entire home/apt", "Shared room"])
neighbourhood = st.selectbox("Neighbourhood Group", ["Brooklyn", "Manhattan", "Queens", "Bronx", "Staten Island"])

# Encode manually
room_encoding = {
    "Private room": [1, 0],
    "Entire home/apt": [0, 1],
    "Shared room": [0, 0]
}

neigh_encoding = {
    "Brooklyn": [1, 0, 0, 0],
    "Manhattan": [0, 1, 0, 0],
    "Queens": [0, 0, 1, 0],
    "Bronx": [0, 0, 0, 1],
    "Staten Island": [0, 0, 0, 0]
}

input_data = np.array([
    latitude, longitude, minimum_nights, reviews,
    reviews_per_month, listings, availability
] + neigh_encoding[neighbourhood] + room_encoding[room_type]).reshape(1, -1)

if st.button("Predict Price"):
    price = model.predict(input_data)[0]
    st.success(f"Suggested Price: ${round(price, 2)}")
