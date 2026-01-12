import sqlite3
import pandas as pd

DB_FILE = "finca.db"
CSV_SALIDA = "reporte_alertas.csv"

print("--- 🔬 Iniciando Análisis de Riesgo ---")
try:
    conn = sqlite3.connect(DB_FILE)
    query = "SELECT zona, fecha, temperatura, humedad FROM lecturas WHERE humedad > 70 AND temperatura > 20"
    df = pd.read_sql(query, conn)

    if df.empty:
        print("✅ No se encontraron riesgos.")
    else:
        print(f"⚠️  ALERTA: {len(df)} registros de riesgo.")
        resumen = df.groupby('zona').size().reset_index(name='conteo_alertas').sort_values('conteo_alertas', ascending=False)
        print(resumen)
        resumen.to_csv(CSV_SALIDA, index=False)
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    if 'conn' in locals(): conn.close()
