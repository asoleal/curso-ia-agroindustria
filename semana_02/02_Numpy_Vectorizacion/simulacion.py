import numpy as np
import time

print("\n--- 🛰️  SISTEMA DE ANÁLISIS SATELITAL (NumPy) ---")

# CONFIGURACIÓN
FILAS = 1000
COLUMNAS = 1000
TOTAL_PIXELES = FILAS * COLUMNAS

print(f"📡 Generando imagen espectral de {FILAS}x{COLUMNAS} ({TOTAL_PIXELES:,} píxeles)...")

# 1. SIMULACIÓN DE DATOS (GENERACIÓN)
# Creamos una matriz gigante con temperaturas aleatorias entre 20°C y 45°C
# np.random.uniform(min, max, dimensiones) -> Genera matriz n-dimensional
inicio = time.time()
mapa_termico = np.random.uniform(20.0, 45.0, (FILAS, COLUMNAS))
fin = time.time()

print(f"✅ Mapa generado en {fin - inicio:.4f} segundos.")
print(f"   Muestra [0,0]: {mapa_termico[0,0]:.2f} °C")

# 2. ANÁLISIS ESTADÍSTICO (OPERACIONES DE AGREGACIÓN)
# Sin NumPy, tendrías que hacer dos bucles for anidados (LENTÍSIMO)
# Con NumPy, la operación se aplica a toda la matriz en C (ULTRA RÁPIDO)

promedio = np.mean(mapa_termico)  # Calcula la media de 1 millón de datos
maximo = np.max(mapa_termico)     # Encuentra el valor más alto
minimo = np.min(mapa_termico)     # Encuentra el valor más bajo
std_dev = np.std(mapa_termico)    # Desviación estándar (Variabilidad)

print("\n📊 ESTADÍSTICAS DEL TERRENO:")
print(f"   - Temp Promedio: {promedio:.2f} °C")
print(f"   - Temp Máxima:   {maximo:.2f} °C")
print(f"   - Temp Mínima:   {minimo:.2f} °C")
print(f"   - Variabilidad:  {std_dev:.2f} °C")

# 3. FILTRADO POR CONDICIONES (MÁSCARAS BOOLEANAS)
# Queremos encontrar zonas de peligro (> 40°C)
umbral_peligro = 40.0

# Esto crea una matriz de True/False (Máscara)
mapa_alertas = mapa_termico > umbral_peligro 

# np.sum() sobre una máscara cuenta cuántos 'True' existen
pixeles_peligro = np.sum(mapa_alertas)
porcentaje_peligro = (pixeles_peligro / TOTAL_PIXELES) * 100

print(f"\n⚠️  REPORTE DE ALERTA (> {umbral_peligro}°C):")
print(f"   - Píxeles afectados: {pixeles_peligro:,}")
print(f"   - Área crítica: {porcentaje_peligro:.2f}% del cultivo")

# ==========================================
# 🧠 ZONA DE RETOS (Operaciones Avanzadas)
# ==========================================
print("\n--- 🔨 TUS RETOS ---")

# RETO 1: Normalización de Datos
# En IA, a menudo necesitamos los datos entre 0 y 1.
# La fórmula es: (valor - min) / (max - min).
# Crea una variable 'mapa_normalizado' aplicando esa fórmula a todo 'mapa_termico'.
# Pista: NumPy permite restar una matriz menos un número (broadcasting).
# Escribe tu código aquí:


# RETO 2: Búsqueda de Coordenadas
# Encuentra EN QUÉ posición (fila, columna) está la temperatura máxima.
# Investiga y usa la función: np.unravel_index(np.argmax(mapa_termico), mapa_termico.shape)
# Imprime la coordenada.
# Escribe tu código aquí:


# RETO 3: Filtrado Avanzado (np.where)
# Crea una copia del mapa llamada 'mapa_corregido'.
# Usa np.where(condicion, valor_si_true, valor_si_false)
# Si la temperatura es < 21 (posible error de sensor), reemplázala por el promedio.
# Si es >= 21, deja el valor original.
# Escribe tu código aquí:

print("---------------------------------------------")
