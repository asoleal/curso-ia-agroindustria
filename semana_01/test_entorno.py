import pandas as pd
import matplotlib.pyplot as plt

print("--- INICIANDO SISTEMA AGRO-IA ---")

# 1. Cargar datos
try:
    df = pd.read_csv('datos/produccion_lote.csv')
    print("✅ Datos cargados exitosamente:")
    print(df)
    
    # 2. Estadística básica (Prueba de Pandas)
    promedio = df['temperatura'].mean()
    print(f"\n🌡️ Temperatura promedio del lote: {promedio:.2f} °C")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("Verifica que el archivo produccion_lote.csv exista en la carpeta /datos")
