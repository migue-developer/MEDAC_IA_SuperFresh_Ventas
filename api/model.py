import pandas as pd
from prophet import Prophet
from s3_utils import download_from_s3, upload_to_s3
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Cargar datos desde S3
FILE_KEY = "data/ventas_simuladas.csv"
df = download_from_s3(FILE_KEY)

df['fecha'] = pd.to_datetime(df['fecha'])

df_prophet = df[['fecha', 'total_ventas', 'clima', 'evento_especial', 'promocion']].copy()
df_prophet.rename(columns={'fecha': 'ds', 'total_ventas': 'y'}, inplace=True)

df_prophet['clima'] = df['clima'].astype('category').cat.codes
df_prophet['evento_especial'] = df['evento_especial'].astype('category').cat.codes
df_prophet['promocion'] = df['promocion'].astype('category').cat.codes

df_prophet['y_lag1'] = df_prophet['y'].shift(1)
df_prophet['y_lag7'] = df_prophet['y'].shift(7)
df_prophet.dropna(inplace=True)

# Entrenar modelo Prophet
model = Prophet(
    daily_seasonality=True,
    yearly_seasonality=True,
    changepoint_prior_scale=0.1,
    seasonality_prior_scale=10
)

model.add_regressor('clima')
model.add_regressor('evento_especial')
model.add_regressor('promocion')
model.add_regressor('y_lag1')
model.add_regressor('y_lag7')

model.fit(df_prophet)

def make_predictions(periods=30):
    """Genera predicciones para los próximos 'periods' días y las sube a S3."""
    
    # Obtener la última fecha en los datos históricos
    last_date = df_prophet['ds'].max()
    
    # Crear fechas futuras empezando DESPUÉS del último dato
    future = model.make_future_dataframe(periods=periods, freq='D')
    future = future[future['ds'] > last_date]  # Filtrar solo fechas futuras
    
    last_known_y = df_prophet['y'].iloc[-1]

    # Asignar valores categóricos correctamente
    future['clima'] = df['clima'].astype('category').cat.codes
    future['evento_especial'] = df['evento_especial'].astype('category').cat.codes
    future['promocion'] = df['promocion'].astype('category').cat.codes

    future['y_lag1'] = pd.Series([last_known_y] * len(future)).shift(1)
    future['y_lag7'] = pd.Series([last_known_y] * len(future)).shift(7)
    future.fillna(last_known_y, inplace=True)

    forecast = model.predict(future)

    # Subir predicciones a S3
    upload_to_s3(forecast, "data/predicciones.csv")

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

# Evaluar el rendimiento del modelo en los datos históricos
def evaluate_model():
    """Evaluar el rendimiento del modelo utilizando MAE, RMSE y R^2."""
    # Realizar predicciones sobre los datos de entrenamiento
    forecast = model.predict(df_prophet)

    # Comparar las predicciones con los valores reales
    y_true = df_prophet['y']
    y_pred = forecast['yhat']

    # Calcular MAE, RMSE y R^2
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    print(f'MAE: {mae}')
    print(f'RMSE: {rmse}')
    print(f'R²: {r2}')

# Llamar a la función para evaluar el rendimiento
evaluate_model()