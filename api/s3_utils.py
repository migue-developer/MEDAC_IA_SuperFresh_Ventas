import pandas as pd
import boto3
import io

# Configuración de AWS S3
BUCKET_NAME = "superfresh-ventas"
s3_client = boto3.client("s3")

def download_from_s3(file_key):
    """Descarga un archivo CSV desde S3 y lo convierte en un DataFrame de Pandas."""
    obj = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_key)
    return pd.read_csv(io.BytesIO(obj['Body'].read()))

def upload_to_s3(df, file_key):
    """Sube un DataFrame de Pandas a S3 en formato CSV."""
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_client.put_object(Bucket=BUCKET_NAME, Key=file_key, Body=csv_buffer.getvalue())
