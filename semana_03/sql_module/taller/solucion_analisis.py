import sqlite3
import pandas as pd
import os

DB_NAME = "finca.db"

# Verificar que exista la DB
if not os.path.exists(DB_NAME):
    print("❌ Error: No existe 'finca.db'. Ejecuta primero la ingesta (bash).")
    exit()

print("--- 🔬 Iniciando Análisis de Patología ---")

conn = sqlite3.connect(DB_NAME)

# Lógica de Negocio:
# Filtramos en SQL (Server-side) para eficiencia
query_riesgo = """
SELECT zona, fecha, temperatura, humedad
FROM lecturas
WHERE humedad > 80 AND temperatura > 25
"""

print("-> Buscando condiciones favorables para hongos (Hum>80% y Temp>25°C)...")
df = pd.read_sql(query_riesgo, conn)

if df.empty:
    print("🎉 No hay riesgos detectados hoy.")
else:
    print(f"⚠️  ALERTA: Se encontraron {len(df)} registros críticos.")
    
    # Agregación con Pandas
    reporte = df.groupby('zona').size().reset_index(name='conteo_alertas')
    reporte = reporte.sort_values('conteo_alertas', ascending=False)
    
    print("\n--- Zonas más afectadas ---")
    print(reporte)
    
    # Exportar
    reporte.to_csv('reporte_alertas.csv', index=False)
    print("\n📄 Reporte guardado en 'reporte_alertas.csv'")

conn.close()
