import pandas as pd
import numpy as np
import random

print("\n--- 🏭 TALLER 2: FÁBRICA DE DATOS SINTÉTICOS ---")

def generar_dataset(n_filas):
    print(f"Generando {n_filas} registros simulados...")
    
    fechas = pd.date_range(start='2024-01-01', periods=n_filas, freq='H')
    temperaturas = np.random.uniform(20, 35, n_filas)
    humedad = np.random.uniform(50, 90, n_filas)
    
    df = pd.DataFrame({
        'fecha': fechas,
        'temperatura': temperaturas,
        'humedad': humedad
    })
    
    return df

# Ejecución
dataset_masivo = generar_dataset(100) # Prueba con 100, luego intenta 100000
print(dataset_masivo.head())          # Muestra las primeras 5 filas
print(f"\n📊 Estadísticas rápidas:\n{dataset_masivo.describe()}")

# --- 🧠 ZONA DE RETOS ---
# RETO 1: Modifica la función para agregar una columna 'sensor_id' que elija al azar entre ['S1', 'S2', 'S3'].
# Pista: Usa np.random.choice(...)
# RETO 2: Guarda el dataset generado en la carpeta '../datos/historico_simulado.csv'.
