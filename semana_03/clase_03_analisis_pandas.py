import pandas as pd
import matplotlib.pyplot as plt

# --- CLASE 3: CIENCIA DE DATOS AGRÍCOLAS CON PANDAS ---

print("--- INFORME MENSUAL DE CALIDAD ---")

# 1. CARGA DE DATOS
df = pd.read_csv('semana_03/datos/historico_calidad.csv')
print(f"📊 Datos cargados: {df.shape[0]} registros.")

# 2. LIMPIEZA DE DATOS (DATA CLEANING)
# Detectamos errores de sensor (Brix negativo)
errores = df[df['brix'] < 0]
print(f"⚠️ Se encontraron {len(errores)} lecturas erróneas de sensor. Eliminando...")

# Filtramos solo los datos válidos
df_clean = df[df['brix'] >= 0]

# 3. ANÁLISIS ESTADÍSTICO
# Promedio de Brix y pH
print(f"\n📈 Promedio BRIX: {df_clean['brix'].mean():.2f}")
print(f"📈 Promedio pH:   {df_clean['ph'].mean():.2f}")

# 4. AGRUPACIÓN (GROUP BY) - La herramienta más poderosa
# Comparamos proveedores
print("\n🏆 RANKING DE PROVEEDORES (Por calidad de Brix):")
ranking = df_clean.groupby('proveedor')['brix'].mean().sort_values(ascending=False)
print(ranking)

# 5. VISUALIZACIÓN
plt.figure(figsize=(10, 6))
# Histograma de Brix
plt.hist(df_clean['brix'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(df_clean['brix'].mean(), color='red', linestyle='dashed', linewidth=1, label='Promedio')
plt.title('Distribución de Calidad (Grados Brix) - Enero')
plt.xlabel('Grados Brix')
plt.ylabel('Frecuencia (Cantidad de Lotes)')
plt.legend()

# Guardamos la gráfica en la carpeta de reportes
ruta_img = 'reportes/imagenes/distribucion_brix.png'
plt.savefig(ruta_img)
print(f"\n✅ Gráfica de distribución guardada en: {ruta_img}")
