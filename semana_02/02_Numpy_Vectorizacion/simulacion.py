import time
import numpy as np
import random

"""
MÓDULO 2: Benchmark de Rendimiento (CPU Bound)
Propósito: Demostrar la diferencia entre O(N) en Python puro vs Vectorización SIMD en NumPy.
Escenario: Calcular el 'Índice de Vigor' de 1 millón de plantas.
Fórmula: Vigor = (Altura * Grosor) + 0.5
"""

N_PLANTAS = 1_000_000  # Un millón de datos

print(f"--- INICIANDO SIMULACIÓN CON {N_PLANTAS} PLANTAS ---\n")

# ==========================================
# ENFOQUE 1: LISTAS DE PYTHON (Lento)
# ==========================================
print("1. Generando datos nativos (Listas)...")
alturas_list = [random.random() for _ in range(N_PLANTAS)]
grosores_list = [random.random() for _ in range(N_PLANTAS)]

print("   -> Procesando con bucle FOR tradicional...")
start_time = time.time()

vigor_list = []
for i in range(N_PLANTAS):
    # Operación escalar (uno por uno)
    calculo = (alturas_list[i] * grosores_list[i]) + 0.5
    vigor_list.append(calculo)

end_time = time.time()
tiempo_python = end_time - start_time
print(f"   ⏱️ Tiempo Python: {tiempo_python:.5f} segundos")


# ==========================================
# ENFOQUE 2: NUMPY (Vectorizado)
# ==========================================
print("\n2. Generando datos NumPy (Arrays Contiguos)...")
alturas_np = np.array(alturas_list)
grosores_np = np.array(grosores_list)

print("   -> Procesando con Vectorización (C Backend)...")
start_time = time.time()

# Operación Vectorizada (Sin bucles explícitos)
vigor_np = (alturas_np * grosores_np) + 0.5

end_time = time.time()
tiempo_numpy = end_time - start_time
print(f"   ⏱️ Tiempo NumPy:  {tiempo_numpy:.5f} segundos")

# ==========================================
# CONCLUSIÓN
# ==========================================
speedup = tiempo_python / tiempo_numpy
print(f"\n🚀 CONCLUSIÓN: NumPy fue {speedup:.2f} veces más rápido.")
if speedup > 10:
    print("   (Por esto usamos NumPy para Inteligencia Artificial)")
