import sqlite3
import pandas as pd

DB_FILE = "finca.db"
CSV_SALIDA = "reporte_alertas.csv"

print("--- 🔬 Iniciando Análisis de Riesgo Fitosanitario ---")

try:
    # 1. Conexión a la DB creada por Bash
    conn = sqlite3.connect(DB_FILE)

    # 2. Query SQL (Filtrado Inteligente)
    # Regla: Humedad > 70% Y Temperatura > 20°C
    query = """
    SELECT zona, fecha, temperatura, humedad
    FROM lecturas
    WHERE humedad > 70 AND temperatura > 20
    """
    
    # 3. Cargar a Pandas
    df = pd.read_sql(query, conn)

    if df.empty:
        print("✅ No se encontraron riesgos activos.")
    else:
        print(f"⚠️  ALERTA: Se encontraron {len(df)} registros de riesgo.")

        # 4. Agregación por Zona
        resumen = df.groupby('zona').size().reset_index(name='conteo_alertas')
        resumen = resumen.sort_values('conteo_alertas', ascending=False)

        print("\n--- Zonas Críticas ---")
        print(resumen)

        # 5. Exportar reporte final
        resumen.to_csv(CSV_SALIDA, index=False)
        print(f"\n📄 Reporte generado: {CSV_SALIDA}")

except Exception as e:
    print(f"❌ Error: {e}")
    print("Consejo: ¿Ejecutaste primero 'solucion_ingesta.sh'?")
finally:
    if 'conn' in locals():
        conn.close()
