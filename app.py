import streamlit as st
import joblib
import numpy as np
from huggingface_hub import hf_hub_download


# -----------------------------
# Load model from Hugging Face
# -----------------------------
@st.cache_resource
def load_model():
    model_path = hf_hub_download(
        repo_id="pratik07022002/airbnb-price-model",
        filename="airbnb_price_model.pkl"
    )
    return joblib.load(model_path)


model = load_model()


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Airbnb Price Optimisation Tool (NYC)")

latitude = st.number_input("Latitude", value=40.7128)
longitude = st.number_input("Longitude", value=-74.0060)
minimum_nights = st.number_input("Minimum Nights", value=1)
reviews = st.number_input("Number of Reviews", value=10)
reviews_per_month = st.number_input("Reviews Per Month", value=0.5)
listings = st.number_input("Host Listings Count", value=1)
availability = st.number_input("Availability (days/year)", value=365)


# -----------------------------
# Categorical inputs
# -----------------------------
room_type = st.selectbox(
    "Room Type",
    ["Private room", "Entire home/apt", "Shared room"]
)

neighbourhood = st.selectbox(
    "Neighbourhood Group",
    ["Brooklyn", "Manhattan", "Queens", "Bronx", "Staten Island"]
)


# -----------------------------
# Manual encoding
# -----------------------------
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


# -----------------------------
# Prepare input
# -----------------------------
input_data = np.array([
    latitude,
    longitude,
    minimum_nights,
    reviews,
    reviews_per_month,
    listings,
    availability
] + neigh_encoding[neighbourhood]
  + room_encoding[room_type]).reshape(1, -1)


# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Price"):
    price = model.predict(input_data)[0]
    st.success(f"Suggested Price: ${round(price, 2)}")
