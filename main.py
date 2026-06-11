from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd

main = FastAPI()

model = joblib.load("model/delivery_time_model.pkl")


class DeliveryData(BaseModel):
    Weather_conditions: str
    Road_traffic_density: str
    Vehicle_condition: int
    Type_of_order: str
    Type_of_vehicle: str
    multiple_deliveries: int
    Festival: str
    City: str


@main.post("/predict")
def predict(data: DeliveryData):

    # Convert Pydantic model → dictionary → DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Predict
    prediction = model.predict(input_df)[0]

    return {
        "predicted_time_minutes": round(float(prediction), 2)
    }