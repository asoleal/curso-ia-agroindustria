import numpy as np
print("\n--- 🔴 SIMULACIÓN VECTORIAL ---")

class EscanerTerreno:
    def __init__(self, tamano):
        self.tamano = tamano
        self.mapa = None
    
    def escanear(self):
        self.mapa = np.random.uniform(0, 100, (self.tamano, self.tamano))
        print(f"📸 Mapa {self.tamano}x{self.tamano} generado.")

    def filtrar_peligro(self, umbral):
        # Vectorización: Sin bucles for
        return np.sum(self.mapa > umbral)

satelite = EscanerTerreno(100)
satelite.escanear()
peligros = satelite.filtrar_peligro(80)
print(f"🔥 Puntos críticos (>80°C): {peligros}")

# --- 🧠 ZONA DE RETOS ---
# RETO 1: Imprime la temperatura MÁXIMA (np.max(satelite.mapa)).
# RETO 2: Imprime el promedio del terreno (np.mean(satelite.mapa)).
