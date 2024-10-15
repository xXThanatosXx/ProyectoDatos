# Instalar paquetes necesarios (si no están instalados)
if(!require(ggplot2)) install.packages("ggplot2")
if(!require(dplyr)) install.packages("dplyr")
if(!require(readr)) install.packages("readr")

# Cargar bibliotecas
library(ggplot2)
library(dplyr)
library(readr)

# Cargar el archivo CSV
# Reemplaza el nombre del archivo por el nombre de tu archivo CSV
data <- read_csv("precios_apartamentos_organizados.csv")

# Convertir la columna Precio a numérica (eliminar símbolos como $ y comas)
data$Precio <- as.numeric(gsub("[^0-9]", "", data$Precio))

# Resumir los datos por ubicación (ciudad)
data_summary <- data %>%
  group_by(Ubicación) %>%
  summarise(Costo_promedio = mean(Precio, na.rm = TRUE),
            Costo_min = min(Precio, na.rm = TRUE),
            Costo_max = max(Precio, na.rm = TRUE),
            Cantidad = n())

# Mostrar la tabla de resumen
print(data_summary)

# 1. Gráfico de barras: Costo promedio por ciudad
ggplot(data_summary, aes(x = reorder(Ubicación, -Costo_promedio), y = Costo_promedio)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Costo promedio de alquiler por ciudad", x = "Ciudad", y = "Costo promedio (COP)") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# 2. Gráfico de líneas: Evolución del costo mínimo, promedio y máximo por ciudad
ggplot(data_summary, aes(x = reorder(Ubicación, -Costo_promedio))) +
  geom_line(aes(y = Costo_min, group = 1, color = "Mínimo"), size = 1) +
  geom_line(aes(y = Costo_promedio, group = 1, color = "Promedio"), size = 1) +
  geom_line(aes(y = Costo_max, group = 1, color = "Máximo"), size = 1) +
  labs(title = "Costo de alquiler mínimo, promedio y máximo por ciudad",
       x = "Ciudad", y = "Costo de alquiler (COP)") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  scale_color_manual(values = c("Mínimo" = "red", "Promedio" = "blue", "Máximo" = "green"))

# 3. Mostrar tabla de resumen en R
print(data_summary)

# Guardar la tabla de resumen en un archivo CSV
write_csv(data_summary, "resumen_alquiler_por_ciudad.csv")
