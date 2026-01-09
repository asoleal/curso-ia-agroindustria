import numpy as np
import matplotlib.pyplot as plt

# --- CLASE 2: ANÁLISIS AUTOMÁTICO DE PROCESOS ---

print("--- INICIANDO AUDITORÍA DE CALIDAD ---")

# 1. SIMULAR DATOS (Recuperamos la curva de enfriamiento)
# Tiempos de 0 a 60 min
tiempo = np.linspace(0, 60, 60) 
# Temperatura bajando exponencialmente
temperaturas = 4 + (72 - 4) * np.exp(-0.15 * tiempo)

# 2. BÚSQUEDA SECUENCIAL (Lógica de bucles)
# Objetivo: Encontrar el minuto exacto donde T < 4.5°C
objetivo = 4.5

print(f"Buscando momento de conformidad (T < {objetivo}°C)...")

for t, temp in zip(tiempo, temperaturas):
    if temp < objetivo:
        print(f"✅ LOTE LIBERADO: Minuto {t:.0f} (Temp: {temp:.2f}°C)")
        print(f"   -> Acción: Detener refrigeración. Enviar a envasado.")
        break
    else:
        # Solo imprimimos cada 10 minutos para no llenar la pantalla
        if t % 10 == 0:
            print(f"⏳ Minuto {t:.0f}: En proceso... ({temp:.2f}°C)")

print("--- FIN DEL ANÁLISIS ---")
