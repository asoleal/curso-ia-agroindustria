import numpy as np

print("--- 🔴 NIVEL 2: SISTEMA DE PROCESAMIENTO VECTORIAL ---")

# 1. CLASES (Programación Orientada a Objetos)
# Creamos un "plano" de cómo debe comportarse nuestro sensor avanzado
class SensorSatelital:
    def __init__(self, resolucion):
        """Constructor: Se ejecuta al crear el objeto."""
        self.resolucion = resolucion
        self.matriz_datos = None
        print(f"🛰️ Inicializando satélite con resolución {resolucion}x{resolucion}")

    def escanear(self):
        """Simula la captura de datos usando Matrices (NumPy)."""
        # Generamos una matriz de 100x100 con valores aleatorios (0 a 100)
        # Esto es miles de veces más rápido que usar listas anidadas
        self.matriz_datos = np.random.uniform(0, 100, (self.resolucion, self.resolucion))
        print("📸 Escaneo completado (Matriz generada).")

    def analizar_puntos_calientes(self, umbral):
        """Detecta zonas críticas usando VECTORIZACIÓN (Sin bucles for)."""
        if self.matriz_datos is None:
            print("❌ Error: Primero debes escanear.")
            return

        # --- AQUÍ OCURRE LA MAGIA DE LA IA ---
        # Filtramos toda la matriz de un solo golpe (Broadcasting/Masking)
        mapa_calor = self.matriz_datos > umbral
        cantidad_alertas = np.sum(mapa_calor)
        
        promedio = np.mean(self.matriz_datos)
        
        print(f"\n📊 ANÁLISIS RÁPIDO:")
        print(f"   - Promedio del terreno: {promedio:.2f}")
        print(f"   - Puntos críticos (> {umbral}): {cantidad_alertas} píxeles encontrados.")

# 2. IMPLEMENTACIÓN (Instanciando la clase)
# El estudiante ve cómo se usa el código de forma limpia
satelite = SensorSatelital(resolucion=1000) # Matriz de 1,000 x 1,000 (1 millón de datos)
satelite.escanear()
satelite.analizar_puntos_calientes(umbral=95.0)

print("\n💡 NOTA: Procesar 1 millón de datos con listas normales tardaría mucho más.")
