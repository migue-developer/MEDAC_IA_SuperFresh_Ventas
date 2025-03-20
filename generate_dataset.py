import pandas as pd
import numpy as np
from datetime import datetime, timedelta

start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 12, 31)
dates = pd.date_range(start=start_date, end=end_date, freq='D')

productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E']
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3']
climas = ['Soleado', 'Nublado', 'Lluvia', 'Nevado']
eventos = ['Black Friday', 'Navidad', 'Ninguno', 'Semana Santa', 'Lunes de Pascua']
promociones = ['Descuento', 'Sin promoción']

np.random.seed(42)

data = []
for date in dates:
    for producto in productos:
        categoria = np.random.choice(categorias)
        clima = np.random.choice(climas)
        evento = np.random.choice(eventos)
        promocion = np.random.choice(promociones)
        
        # Variabilidad en ventas según el clima y evento
        base_ventas = np.random.randint(50, 500)
        if clima == 'Lluvia':
            base_ventas += np.random.randint(20, 100)  # Aumenta ventas en clima lluvioso
        elif clima == 'Soleado':
            base_ventas += np.random.randint(10, 50)
        
        # Tendencia según eventos especiales
        if evento in ['Black Friday', 'Navidad']:
            base_ventas += np.random.randint(200, 500)  # Incremento por eventos
        elif evento == 'Semana Santa':
            base_ventas += np.random.randint(100, 200)
        
        # Precios
        precio_unitario = np.random.randint(5, 50)
        
        # Calcular total ventas
        total_ventas = base_ventas * precio_unitario
        
        # Agregar información
        data.append([
            date.strftime('%Y-%m-%d'),
            producto,
            categoria,
            base_ventas,
            clima,
            evento,
            promocion,
            precio_unitario,
            total_ventas,
            date.month,
            'Primavera' if 3 <= date.month <= 5 else 
            'Verano' if 6 <= date.month <= 8 else 
            'Otoño' if 9 <= date.month <= 11 else 'Invierno'
        ])

# Crear DataFrame
df = pd.DataFrame(data, columns=[
    'fecha', 'producto', 'categoria', 'unidades_vendidas', 
    'clima', 'evento_especial', 'promocion', 'precio_unitario', 
    'total_ventas', 'mes', 'estacion'
])

# Guardar a CSV
df.to_csv('ventas_simuladas.csv', index=False)
