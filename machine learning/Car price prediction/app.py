import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("logreg_model.pkl", "rb"))

# Streamlit App
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="centered")
st.title("🚗 Car Price Prediction App")
st.markdown("Predict the **selling price** of a car based on its features")

# Input fields
col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, value=2015)
    present_price = st.number_input("Present Price (in lakhs)", min_value=0.0, value=5.0, step=0.1)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, value=20000, step=500)

with col2:
    owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# Encode categorical features (adjust mapping according to your notebook preprocessing)
fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Manual": 0, "Automatic": 1}

# Create input array
input_data = np.array([[year,
                        present_price,
                        kms_driven,
                        owner,
                        fuel_map[fuel_type],
                        seller_map[seller_type],
                        trans_map[transmission]]])

# Prediction
if st.button("🔍 Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Selling Price: ₹ {prediction:.2f} lakhs")
