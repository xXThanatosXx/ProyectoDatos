import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Semilla para reproducibilidad
np.random.seed(42)

# Configuraciones básicas
n_samples = 1000  # Número de muestras que quieres generar
ciudades = ['Bogotá', 'Medellín', 'Cali', 'Cartagena', 'Barranquilla']
min_area = 40  # Área mínima en metros cuadrados
max_area = 200  # Área máxima en metros cuadrados
min_habitaciones = 1  # Mínimo de habitaciones
max_habitaciones = 5  # Máximo de habitaciones

# Generación de datos
fechas = [datetime(2020, 1, 1) + timedelta(days=i*30) for i in range(n_samples)]
ciudad = np.random.choice(ciudades, size=n_samples)
area = np.random.randint(min_area, max_area, size=n_samples)
habitaciones = np.random.randint(min_habitaciones, max_habitaciones, size=n_samples)

# Generar precios basados en área, habitaciones y ciudad
def generar_precio(ciudad, area, habitaciones):
    base_price = {
        'Bogotá': 10000,
        'Medellín': 9000,
        'Cali': 8000,
        'Cartagena': 11000,
        'Barranquilla': 8500
    }
    return base_price[ciudad] * (area / 50) * (habitaciones / 2)

precio = [generar_precio(c, a, h) for c, a, h in zip(ciudad, area, habitaciones)]

# Crear el DataFrame
data = {
    'Fecha': fechas,
    'Ciudad': ciudad,
    'Área (m²)': area,
    'Habitaciones': habitaciones,
    'Precio': precio
}

df_sintetico = pd.DataFrame(data)

# Guardar el dataset en un archivo CSV
df_sintetico.to_csv('precios_alquiler.csv', index=False)

# Mostrar las primeras filas del dataset
print(df_sintetico.head())
