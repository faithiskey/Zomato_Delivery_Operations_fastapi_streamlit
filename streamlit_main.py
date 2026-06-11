import streamlit as st
import requests

# FastAPI URL
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Delivery Time Predictor", layout="centered")

st.title("🚚 Delivery Time Prediction App")
st.write("Enter order details below to predict delivery time (in minutes).")

# Input fields
weather = st.selectbox("Weather Conditions", ["Sunny", "Stormy", "Cloudy", "Fog"])
traffic = st.selectbox("Road Traffic Density", ["Low", "Medium", "High", "Jam"])
vehicle_condition = st.number_input("Vehicle Condition", min_value=0, max_value=5, step=1)
order_type = st.selectbox("Type of Order", ["Snack", "Meal", "Drinks", "Buffet"])
vehicle_type = st.selectbox("Type of Vehicle", ["motorcycle", "scooter", "bicycle"])
multiple_deliveries = st.number_input("Multiple Deliveries", min_value=0, max_value=5, step=1)
festival = st.selectbox("Festival", ["Yes", "No"])
city = st.selectbox("City", ["Urban", "Semi-Urban", "Rural"])

# Predict button
if st.button("Predict Delivery Time"):

    payload = {
        "Weather_conditions": weather,
        "Road_traffic_density": traffic,
        "Vehicle_condition": vehicle_condition,
        "Type_of_order": order_type,
        "Type_of_vehicle": vehicle_type,
        "multiple_deliveries": multiple_deliveries,
        "Festival": festival,
        "City": city
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"⏱ Predicted Delivery Time: {result['predicted_time_minutes']} minutes")
        else:
            st.error(f"Error: {response.text}")

    except Exception as e:
        st.error(f"Request failed: {e}")