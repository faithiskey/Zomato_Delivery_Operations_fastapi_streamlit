from fastapi import FastAPI
import joblib
import os
from pydantic import BaseModel
import pandas as pd

main = FastAPI()

# Load model safely (Render-ready)
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "model", "delivery_time_model.pkl")
model = joblib.load(model_path)


# Input schema
class DeliveryData(BaseModel):
    Weather_conditions: str
    Road_traffic_density: str
    Vehicle_condition: int
    Type_of_order: str
    Type_of_vehicle: str
    multiple_deliveries: int
    Festival: str
    City: str


# Predict endpoint
@main.post("/predict")
def predict(data: DeliveryData):

    input_df = pd.DataFrame([data.dict()])

    prediction = model.predict(input_df)[0]

    return {
        "predicted_time_minutes": round(float(prediction), 2)
    }