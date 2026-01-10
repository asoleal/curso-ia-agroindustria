import numpy as np
import time

print("\n--- 🛰️  SISTEMA DE ANÁLISIS SATELITAL (HPC) ---")

# CONFIGURACIÓN: 1 Millón de Píxeles
FILAS, COLUMNAS = 1000, 1000
TOTAL_PIXELES = FILAS * COLUMNAS

print(f"📡 Generando imagen espectral de {FILAS}x{COLUMNAS}...")

# 1. SIMULACIÓN DE DATOS (Vectorizada)
inicio = time.time()
# Generamos matriz float64 en memoria contigua
mapa_termico = np.random.uniform(20.0, 45.0, (FILAS, COLUMNAS))
fin = time.time()

print(f"✅ Mapa generado en {fin - inicio:.4f} segundos.")
print(f"   Memoria usada: {mapa_termico.nbytes / 1024 / 1024:.2f} MB")

# 2. ANÁLISIS ESTADÍSTICO (Operaciones SIMD)
promedio = np.mean(mapa_termico)
maximo = np.max(mapa_termico)
std_dev = np.std(mapa_termico)

print("\n📊 ESTADÍSTICAS DEL TERRENO:")
print(f"   - Temp Promedio: {promedio:.2f} C")
print(f"   - Variabilidad:  {std_dev:.2f} C")

# 3. DETECCIÓN DE ALERTAS (Masking)
# Esto crea una mascara booleana instantanea
umbral = 40.0
mapa_alertas = mapa_termico > umbral
pixeles_peligro = np.sum(mapa_alertas)

print(f"\n⚠️  REPORTE DE ALERTA (> {umbral} C):")
print(f"   - Píxeles afectados: {pixeles_peligro:,}")
print(f"   - Área crítica: {(pixeles_peligro/TOTAL_PIXELES)*100:.2f}%")

# --- ZONA DE RETOS PARA EL ESTUDIANTE ---
# Reto 1: Normalización (0-1)
# Reto 2: Ubicar coordenada del máximo (argmax)
# Reto 3: Imputación de errores (where)
