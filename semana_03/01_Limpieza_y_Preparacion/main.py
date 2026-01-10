import pandas as pd
import numpy as np

print("\n--- 🐼 DATA ENGINEERING: PREPARANDO EL DATASET ---")

# 1. CARGA DE DATOS
# Cargamos el CSV. 'na_values' ayuda a identificar valores vacíos extraños
df = pd.read_csv('../datos/cosecha_sucia.csv')

print("1️⃣ DATOS CRUDOS (Con errores):")
print(df)
print("\n📋 Info del Dataset:")
print(df.info())

# 2. LIMPIEZA DE VALORES NULOS (MISSING VALUES)
# En IA, no puedes tener huecos. O borras la fila, o rellenas el dato.
# Estrategia: Rellenar temperatura con el promedio.
promedio_temp = df['Temperatura_Promedio'].mean()
df['Temperatura_Promedio'].fillna(promedio_temp, inplace=True)

# Estrategia: Si falta el rendimiento (el objetivo), borramos la fila (no sirve para entrenar).
df.dropna(subset=['Rendimiento_Ton'], inplace=True)

print(f"\n2️⃣ DESPUÉS DE TRATAR NULOS (Rellenamos Temp con {promedio_temp:.1f}):")
print(df)

# 3. DETECCIÓN DE ANOMALÍAS (OUTLIERS)
# Un sensor falló y marcó 120% de humedad. Eso confundiría a la IA.
# Regla: Humedad debe estar entre 0 y 100.
mask_error = (df['Humedad_Suelo'] > 100) | (df['Humedad_Suelo'] < 0)
print("\n⚠️ Detectados errores de sensor en Humedad:")
print(df[mask_error])

# Corregimos: Reemplazamos el error con el valor máximo lógico (100)
df.loc[mask_error, 'Humedad_Suelo'] = 100.0

# 4. TRANSFORMACIÓN DE CATEGORÍAS (ENCODING)
# Las IAs no entienden texto como "N-High". Necesitan números.
# Mapeo: Low=1, Mid=2, High=3
mapeo_nitrogeno = {'N-Low': 1, 'N-Mid': 2, 'N-High': 3}
df['Nitrogeno_Num'] = df['Nitrogeno_Nivel'].map(mapeo_nitrogeno)

print("\n3️⃣ DATASET LISTO PARA IA (Limpio y Numérico):")
print(df[['ID_Lote', 'Humedad_Suelo', 'Nitrogeno_Num', 'Rendimiento_Ton']])

# ==========================================
# 🧠 ZONA DE RETOS
# ==========================================
print("\n--- 🔨 TUS RETOS ---")

# RETO 1: Filtrado
# Muestra solo las filas donde el 'Rendimiento_Ton' sea mayor a 4.0.
# Escribe tu código aquí:


# RETO 2: Guardado
# Guarda el dataset limpio (df) en un nuevo archivo '../datos/cosecha_limpia.csv'
# usa el método: df.to_csv('ruta', index=False)
# Escribe tu código aquí:

print("---------------------------------------------")
