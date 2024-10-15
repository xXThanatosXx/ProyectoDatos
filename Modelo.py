import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Crear el modelo
model = Sequential()

# Capa de entrada
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))

# Capas ocultas
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))  # Dropout para prevenir sobreajuste

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))

# Capa de salida
model.add(Dense(1))  # Una salida para predecir el precio futuro

# Compilar el modelo
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Evaluar el modelo
loss, mae = model.evaluate(X_test, y_test)
print(f'MAE en el conjunto de prueba: {mae}')
