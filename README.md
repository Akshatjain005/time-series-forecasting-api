# End-to-End Time Series Forecasting System with API

## Overview
This project presents a production-ready time series forecasting system that predicts the next 8 weeks of state-wise sales using historical data. It integrates data preprocessing, feature engineering, multiple model training, automated model selection, and API deployment into a unified pipeline.

---

## Objective
- Forecast next 8 weeks of sales for each state
- Handle missing dates and values
- Capture trend and seasonality
- Compare multiple models and select the best one
- Serve predictions via a REST API

---

## Dataset
The dataset contains:
- Date column (time-based index)
- Sales values
- State-wise data

---

## Feature Engineering
The following features were created to improve model performance:

- Lag Features:
  - t-1 (previous day)
  - t-7 (weekly lag)
  - t-30 (monthly lag)

- Rolling Statistics:
  - Rolling mean
  - Rolling standard deviation

- Time-Based Features:
  - Day of week
  - Month
  - Week number

---

## Models Implemented
The system trains and compares multiple models:

- ARIMA / SARIMA (Statistical Model)
- Prophet (Trend & Seasonality Model)
- XGBoost (Machine Learning Model)
- LSTM (Deep Learning Model)

---

## Model Evaluation
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

Time-series split is used to avoid data leakage.

The best model is automatically selected based on performance.

---

## Forecasting
The system generates predictions for:
- Next 8 weeks
- For each state individually

---

## API Implementation
A REST API is built using FastAPI.

### Endpoints:

- `/`
  - Health check endpoint

- `/forecast/{state}`
  - Returns forecast for the given state

### Example:
