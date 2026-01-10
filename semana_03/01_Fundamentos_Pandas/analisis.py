import pandas as pd
import numpy as np

print("\n--- 🐼 TALLER 1: CALIDAD DE DATOS ---")

# Simulamos carga de datos (normalmente sería pd.read_csv)
data = {
    'lote': ['A-01', 'A-01', 'B-02', 'B-02', 'C-03'],
    'brix': [12.5, 12.8, np.nan, 11.2, 13.1], # NaN es un hueco en los datos
    'ph': [3.5, 3.6, 3.4, 300.0, 3.2]         # 300.0 es un error de sensor
}

df = pd.DataFrame(data)
print("1️⃣ DATOS CRUDOS:\n", df)

# Limpieza básica
# Rellenar huecos con el promedio
promedio = df['brix'].mean()
df['brix'] = df['brix'].fillna(promedio)

# Filtrar errores de pH (pH > 14 es imposible)
df_limpio = df[df['ph'] <= 14]

print("\n2️⃣ DATOS LIMPIOS:\n", df_limpio)

# Agrupación
reporte = df_limpio.groupby('lote').mean()
print("\n3️⃣ REPORTE POR LOTE:\n", reporte)

# --- 🧠 ZONA DE RETOS ---
# RETO 1: Exporta el 'df_limpio' a un archivo CSV llamado 'limpieza_final.csv'.
# RETO 2: Filtra y muestra solo los lotes que tengan Brix mayor a 12.0.
