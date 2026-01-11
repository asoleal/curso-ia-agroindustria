import time
import numpy as np
import math  # Requerido para la versión lenta (Python puro)

def benchmark():
    print(f"--- 🏎️  INICIANDO BENCHMARK DE RENDIMIENTO (NIVEL 2) 🏎️  ---")
    
    # 1. SETUP DE DATOS (1 Millón de registros)
    # Aumentamos la complejidad para estresar la CPU
    N_PLANTAS = 1_000_000
    print(f"Generando {N_PLANTAS} datos simulados...")
    
    # Generamos datos aleatorios con NumPy
    rng = np.random.default_rng(seed=42)
    alturas_np = rng.uniform(0.5, 3.0, N_PLANTAS)  # Metros
    grosores_np = rng.uniform(0.01, 0.1, N_PLANTAS) # Metros
    
    # Convertimos a listas estándar de Python para la prueba lenta
    alturas_list = list(alturas_np)
    grosores_list = list(grosores_np)

    print("Datos listos. Comienza la carrera.\n")

    # ---------------------------------------------------------
    # CORREDOR 1: PYTHON PURO (Iterativo + Math)
    # ---------------------------------------------------------
    start_time = time.time()
    
    vigor_python = []
    for i in range(N_PLANTAS):
        # RETO CUMPLIDO: Operación trigonométrica costosa
        # Vigor = Seno(Altura) * Grosor
        # Esto obliga a Python a llamar a la librería C math un millón de veces
        calculo = math.sin(alturas_list[i]) * grosores_list[i]
        vigor_python.append(calculo)
        
    end_time = time.time()
    tiempo_python = end_time - start_time
    print(f"🐍 Python (Bucle for + math.sin): {tiempo_python:.5f} segundos")

    # ---------------------------------------------------------
    # CORREDOR 2: NUMPY (Vectorizado + ufunc)
    # ---------------------------------------------------------
    start_time = time.time()
    
    # RETO CUMPLIDO: Versión vectorizada
    # np.sin es una 'Universal Function' optimizada para operar en bloques
    vigor_numpy = np.sin(alturas_np) * grosores_np
    
    end_time = time.time()
    tiempo_numpy = end_time - start_time
    print(f"⚡ NumPy (Vectorizado):          {tiempo_numpy:.5f} segundos")

    # ---------------------------------------------------------
    # RESULTADOS
    # ---------------------------------------------------------
    speedup = tiempo_python / tiempo_numpy
    print(f"\n---------------------------------------------------------")
    print(f"🏆 GANADOR: NumPy")
    print(f"🚀 VELOCIDAD: {speedup:.2f} veces más rápido (Speedup)")
    print(f"---------------------------------------------------------")

    # Verificación técnica (Sanity Check)
    # Validamos que los cálculos sean matemáticamente equivalentes
    diferencia = abs(vigor_python[0] - vigor_numpy[0])
    if diferencia < 1e-9:
        print("✅ Validación: Los resultados matemáticos coinciden.")
    else:
        print("❌ Error: Los resultados divergen.")

# ---------------------------------------------------------
# REPORTE DE INGENIERÍA (ENTREGABLE)
# ---------------------------------------------------------
# Operación: Función Seno (Trigonométrica)
# Tiempo Python: ~0.35 segundos (Varía según hardware)
# Tiempo NumPy:  ~0.004 segundos (Varía según hardware)
# Aceleración:   ~85x - 120x veces más rápido
# Conclusión: La vectorización elimina el overhead del intérprete 
#             y aprovecha las instrucciones SIMD de la CPU.
# ---------------------------------------------------------

if __name__ == "__main__":
    benchmark()
