import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Generar un dataset sintético
def generate_synthetic_data(n_samples=1000):
    np.random.seed(42)
    cities = ['Pasto', 'Bogotá', 'Cali', 'Medellin']
    city_data = np.random.choice(cities, size=n_samples)
    prices = np.random.randint(500, 5000, size=n_samples)
    years = np.random.randint(2010, 2024, size=n_samples)
    features = np.column_stack((city_data, years, prices))
    return pd.DataFrame(features, columns=['City', 'Year', 'Price'])

# Preprocesar los datos
def preprocess_data(df):
    df['Year'] = df['Year'].astype(int)
    df['Price'] = df['Price'].astype(float)
    df = pd.get_dummies(df, columns=['City'])  # One-hot encode 'City' feature
    
    X = df.drop('Price', axis=1).values  # Características (Year, City one-hot encoded)
    y = df['Price'].values  # Target (precio)
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Definir el modelo de redes neuronales
def build_model(input_shape):
    model = tf.keras.Sequential([
        layers.Dense(128, activation='relu', input_shape=(input_shape,)),
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dense(1)  # Una salida para la predicción de precio
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

# Entrenar el modelo
def train_model(model, X_train, y_train, X_val, y_val, epochs=50):
    history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=epochs, batch_size=32)
    return history

# Aumentación de datos sintética
def augment_data(X_train, y_train):
    noise_factor = 0.1
    augmented_X = X_train + noise_factor * np.random.randn(*X_train.shape)
    augmented_y = y_train + noise_factor * np.random.randn(*y_train.shape)
    return augmented_X, augmented_y

# Visualización de la historia del entrenamiento
def plot_training_history(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Generar datos
    df = generate_synthetic_data()
    
    # Preprocesar datos
    X_train, X_test, y_train, y_test = preprocess_data(df)
    
    # Data augmentation
    X_train_augmented, y_train_augmented = augment_data(X_train, y_train)
    
    # Crear modelo
    model = build_model(X_train.shape[1])
    
    # Entrenar modelo
    history = train_model(model, X_train_augmented, y_train_augmented, X_test, y_test)
    
    # Evaluar modelo
    loss, mae = model.evaluate(X_test, y_test)
    print(f"Mean Absolute Error on Test Set: {mae}")
    
    # Visualizar entrenamiento
    plot_training_history(history)
    
    # Guardar modelo
    model.save("rent_trend_prediction_model.h5")
