# REFERENCE: Solución S02 Numpy Avanzado
import numpy as np

# Configuración
mapa_termico = np.random.uniform(20.0, 45.0, (1000, 1000))
promedio = np.mean(mapa_termico)
maximo = np.max(mapa_termico)
minimo = np.min(mapa_termico)

# --- SOLUCIONES ---

# RETO 1: Normalización (Min-Max Scaling)
# Operación vectorial: se aplica a cada celda de la matriz simultáneamente
mapa_normalizado = (mapa_termico - minimo) / (maximo - minimo)
print(f"Reto 1 - Rango normalizado: {np.min(mapa_normalizado):.1f} a {np.max(mapa_normalizado):.1f}")

# RETO 2: Coordenada del Máximo
# np.argmax devuelve el índice "aplanado", unravel_index lo convierte a (x, y)
indice_flat = np.argmax(mapa_termico)
coordenada = np.unravel_index(indice_flat, mapa_termico.shape)
print(f"Reto 2 - Punto más caliente en coordenada: {coordenada}")

# RETO 3: Limpieza condicional (np.where)
# Sintaxis: np.where(condición, valor_si_verdadero, valor_si_falso)
mapa_corregido = np.where(mapa_termico < 21, promedio, mapa_termico)
print(f"Reto 3 - Mínimo después de corregir: {np.min(mapa_corregido):.2f}")
