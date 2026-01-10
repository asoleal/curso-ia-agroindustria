import numpy as np

print("\n--- 🔴 INICIO SIMULACIÓN VECTORIAL (NUMPY) ---")

# =======================================================
# TEORÍA RÁPIDA:
# En IA, no usamos listas. Usamos ARRAYS (Matrices).
# Son mucho más rápidos y permiten operar todo de golpe.
# =======================================================

class EscanerTerreno:
    def __init__(self, tamano):
        self.tamano = tamano
        self.mapa = None
    
    def escanear(self):
        # Genera una matriz de tamano x tamano con valores aleatorios (0 a 100)
        self.mapa = np.random.uniform(0, 100, (self.tamano, self.tamano))
        print(f"📸 Escaneo de {self.tamano}x{self.tamano} completado.")

    def filtrar_zonas_peligrosas(self, umbral):
        # AQUÍ ESTÁ LA MAGIA: No usamos 'for'. Filtramos toda la matriz de golpe.
        # Esto crea una "máscara" (True/False)
        zonas_calientes = self.mapa > umbral
        cantidad = np.sum(zonas_calientes)
        return cantidad

# EJECUCIÓN DEL SISTEMA
satelite = EscanerTerreno(100) # Matriz de 100x100 (10,000 datos)
satelite.escanear()

peligros = satelite.filtrar_zonas_peligrosas(80) # Buscar mayores a 80 grados
print(f"📊 Se detectaron {peligros} puntos críticos en el terreno.")

# =======================================================
# 🧠 ZONA DE RETOS (Tu turno)
# =======================================================
print("\n--- 🔨 TUS EJERCICIOS ---")

# RETO 1: Calcula e imprime la temperatura MÁXIMA detectada en el mapa.
# Pista: Busca en Google o ChatGPT "numpy max value". La variable es self.mapa (pero accedes desde 'satelite.mapa')
# Escribe tu código aquí abajo:


# RETO 2: Calcula el promedio de temperatura de todo el terreno.
# Pista: numpy.mean()
# Escribe tu código aquí abajo:

print("---------------------------------------------")
