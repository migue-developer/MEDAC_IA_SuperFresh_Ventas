import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import requests

# Obtener datos desde la API
API_URL = "http://127.0.0.1:8000/predict/"
response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
else:
    df = pd.DataFrame(columns=["ds", "yhat"])

# Crear Dash App
app = dash.Dash(__name__)

# Crear gráfico de líneas
fig = px.line(df, x='ds', y='yhat', title="Predicción de Ventas",
              labels={"ds": "Fecha", "yhat": "Ventas Estimadas"},
              markers=True)

# Diseño del dashboard
app.layout = html.Div(children=[
    html.H1("Dashboard de Predicción de Ventas"),
    dcc.Graph(figure=fig)
])