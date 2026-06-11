### 🚚 Zomato Delivery Operations - Delivery Time Prediction

A Machine Learning-powered web application that predicts food delivery time based on operational factors such as weather conditions, traffic density, vehicle condition, order type, and city characteristics.

The project combines Exploratory Data Analysis (EDA), Machine Learning, FastAPI, and Streamlit to provide an end-to-end predictive analytics solution.


## Project Overview

Food delivery companies face operational challenges that impact delivery times and customer satisfaction. This project analyzes delivery operation data and builds a predictive model that estimates the expected delivery time for an order.

The solution includes:

-Data cleaning and preprocessing
-Exploratory Data Analysis (EDA)
-Machine Learning model development
-FastAPI backend for model serving
-Streamlit frontend for user interaction
-Deployment-ready architecture

## Business Problem

Late deliveries can lead to:

-Reduced customer satisfaction
-Increased operational costs
-Lower delivery personnel efficiency

This project helps estimate delivery time in advance, enabling better operational planning and customer communication.


Features Used

The model uses the following features:

## Feature             	Description

-Weather_conditions	     Current weather condition
-Road_traffic_density   	Traffic intensity
-Vehicle_condition	      Vehicle health rating
-Type_of_order	          Meal, Snack, Drinks, Buffet
-Type_of_vehicle        	Motorcycle, Scooter, Bicycle
-multiple_deliveries    	Number of deliveries assigned
-Festival	                Whether a festival is occurring
-City	                    Urban, Semi-Urban, Rural

## Target Variable
Time_taken (min)

## Tech Stack
Data Science
-Python
-Pandas
-NumPy
-Matplotlib
-Seaborn
-Scikit-learn

## Backend
-FastAPI
-Uvicorn
-Pydantic


## Frontend
-Streamlit

## Machine Learning Workflow

1. Data Cleaning
Handled missing values
Removed duplicates
Treated inconsistent categorical values

2. Exploratory Data Analysis
Analyzed:

Delivery ratings
Traffic density impact
Weather effects
Festival impact
Multiple deliveries impact

3. Feature Engineering
Categorical encoding
Data preprocessing pipeline

5. Model Training

Model evaluated:
Linear Regression

-Evaluation Metrics
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
R² Score

## FastAPI Backend

Run locally:

-uvicorn main:app --reload

API Documentation:

-http://127.0.0.1:8000/docs

Prediction Endpoint:

-POST /predict

Sample Request:

{
  "Weather_conditions": "Sunny",
  "Road_traffic_density": "High",
  "Vehicle_condition": 4,
  "Type_of_order": "Meal",
  "Type_of_vehicle": "motorcycle",
  "multiple_deliveries": 1,
  "Festival": "No",
  "City": "Urban"
}


## Streamlit Frontend

Run locally:

-streamlit run app.py

Features:

-Interactive user interface
-Real-time predictions
-API integration with FastAPI
-User-friendly input controls

Project Structure
Zomato_Delivery_Operations_fastapi_streamlit/
│
├── model/
│   ├── delivery_time_model.pkl
│   
├── main.py
├── requirements.txt
├── runtime.txt
├── README.md
│
└── notebooks/

## Key Insights
-Increased traffic density generally leads to longer delivery times.
-Multiple deliveries significantly impact delivery efficiency.
-Festival periods are associated with longer delivery durations.
-Vehicle condition has a measurable influence on delivery performance.
