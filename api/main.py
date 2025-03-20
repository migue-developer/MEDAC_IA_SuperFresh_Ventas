from fastapi import FastAPI, HTTPException
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from s3_utils import download_from_s3
from model import make_predictions

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API de predicciones de ventas"}

@app.get("/predict/")
def predict(periods: int = 30):
    try:
        forecast = make_predictions(periods)
        return forecast.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/predicciones/")
def get_predictions():
    try:
        pred_df = download_from_s3("data/predicciones.csv")
        return pred_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
