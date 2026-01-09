import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# --- MODELADO DE UN TANQUE DE REFRIGERACIÓN (LEY DE NEWTON) ---
def modelo_enfriamiento(T, t, k, T_ambiente):
    dT_dt = -k * (T - T_ambiente)
    return dT_dt

# Parámetros
T_inicial = 72.0
T_ambiente = 4.0
k = 0.15
tiempo = np.linspace(0, 60, 100)

# Resolver EDO
solucion = odeint(modelo_enfriamiento, T_inicial, tiempo, args=(k, T_ambiente))
temperatura_simulada = solucion.flatten()

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(tiempo, temperatura_simulada, label=f'Modelo Teórico (k={k})', color='blue')
plt.axhline(y=T_ambiente, color='r', linestyle='--', label='Temp. Refrigerante')
plt.title('Cinética de Enfriamiento - Tanque 01')
plt.xlabel('Tiempo (min)')
plt.ylabel('Temperatura (°C)')
plt.grid(True, alpha=0.3)
plt.legend()

# Guardar
plt.savefig('reportes/imagenes/simulacion_enfriamiento.png')
print("✅ Gráfica generada exitosamente.")
