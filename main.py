from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_excel("Forecasting Case- Study.xlsx")

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.get("/forecast/{state}")
def get_forecast(state: str):
    result = df[df['State'] == state]
    return result.to_dict(orient='records')