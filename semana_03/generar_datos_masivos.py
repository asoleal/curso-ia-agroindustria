import pandas as pd
import numpy as np
import random

# --- GENERADOR DE DATOS DE PRODUCCIÓN (MES DE ENERO) ---
print("Generando base de datos histórica...")

# 1. Configuración
num_registros = 1000
np.random.seed(42) # Para que siempre salgan los mismos datos

# 2. Generar datos simulados
data = {
    'id_lote': range(1001, 1001 + num_registros),
    'fecha': pd.date_range(start='2024-01-01', periods=num_registros, freq='H'),
    'brix': np.random.normal(loc=12.0, scale=0.5, size=num_registros), # Promedio 12, desv 0.5
    'ph': np.random.normal(loc=6.7, scale=0.1, size=num_registros),    # Promedio 6.7
    'temperatura': np.random.uniform(3.5, 8.0, size=num_registros),    # Entre 3.5 y 8
    'proveedor': np.random.choice(['Finca A', 'Finca B', 'Finca C'], num_registros)
}

df = pd.DataFrame(data)

# 3. Introducir "Datos Sucios" (Ruido para limpiar en clase)
# A veces el sensor falla y marca 0 o negativo
indices_error = np.random.choice(df.index, size=20, replace=False)
df.loc[indices_error, 'brix'] = -1.0 

# A veces el pH se dispara (leche ácida)
indices_acido = np.random.choice(df.index, size=15, replace=False)
df.loc[indices_acido, 'ph'] = 5.5

# 4. Guardar archivo
ruta = 'semana_03/datos/historico_calidad.csv'
df.to_csv(ruta, index=False)
print(f"✅ Archivo generado: {ruta}")
print(df.head())
