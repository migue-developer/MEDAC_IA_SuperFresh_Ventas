# Proyecto: Predicción de ventas - SuperFresh

Este proyecto tiene como objetivo implementar un sistema de **predicción de ventas** para **SuperFresh**, una tienda en línea de ropa y accesorios. Utilizando **Amazon Rekognition** para el análisis de imágenes, el sistema asignará etiquetas automáticamente a las imágenes de productos subidos, optimizando así la gestión del catálogo y mejorando la eficiencia en la publicación de productos en la plataforma.

## 🚀 Requisitos Previos

Asegúrate de tener instalados:

- **Python 3.8+**
- **Node.js y npm**
- **Git**

## ⚙️ Configuración del Backend

1️⃣ Clona el repositorio y accede al directorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2️⃣ Crea y activa un entorno virtual:

- En **Linux/Mac**:

```bash
python -m venv venv
source venv/bin/activate
```

- En **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

3️⃣ Instala las dependencias del backend:

```bash
pip install -r requirements.txt
```

4️⃣ Ejecuta el servidor FastAPI:

```bash
python run_fastapi.py
```

5️⃣ Ejecuta el servidor Dash:

```bash
python run_dashboard.py
```

El backend estará disponible en: `http://localhost:8000`.
El dashboard estará dispobible en: `http://localhost:8050` 

Puedes ver la documentación automática de la API en:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc UI**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Estructura del Backend

- `./api/main.py`: Archivo principal donde se define la API FastAPI y los endpoints para las predicciones.
- `./api/model.py`: Archivo donde se crea y entrena el modelo para la prediccion de ventas.
- `./api/s3_utils.py`: Archivo donde se definen los métodos para descargan o suben ficheros de s3.
- `./dashboard/dashboard.py`: Archivo donde se definen los métodos para la visualización de la predicción de ventas usando Dash.


¡Disfruta desarrollando el sistema de predicción de vebtas de SuperFresh! 🚀
