#https://p4s.co/hackathon-talentotech-popayan-3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Configurar opciones de Chrome 
chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # Reducir el nivel de logs a solo errores
chrome_options.add_argument("--headless")  # Ejecutar en modo headless (sin ventana de navegador)

# Iniciar el driver de Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL del sitio web con los apartamentos
url = "https://www.ciencuadras.com/arriendo/apartamento?v=Bogota"  # Reemplaza con la URL real

# Abrir la página web
driver.get(url)

# Extraer los precios y ubicaciones 
precios = driver.find_elements(By.CLASS_NAME, "card__price-big")
ubicaciones = driver.find_elements(By.CLASS_NAME, "card__location-label")

# Crear una lista para almacenar los datos
data = []

# Recorrer los precios y ubicaciones y almacenarlos en la lista
for precio, ubicacion in zip(precios, ubicaciones):
    # Limpiar y organizar los datos
    precio_text = precio.text.strip()
    ubicacion_text = ubicacion.text.strip()
    
    # Agregar solo si ambos valores están presentes y son válidos
    if precio_text and ubicacion_text:
        data.append({
            'Precio': precio_text,
            'Ubicación': ubicacion_text
        })

# Crear un DataFrame de pandas con los datos
df = pd.DataFrame(data)

# Eliminar filas vacías o con datos no válidos
df.dropna(inplace=True)

# Guardar los datos en un archivo CSV con separación adecuada de columnas
df.to_csv("precios_apartamentos_organizados.csv", index=False)

print("Datos guardados en 'precios_apartamentos_organizados.csv'")

# Cerrar el navegador
driver.quit()
