import numpy as np

print("--- 🔴 SISTEMA SATELITAL (CLASES + NUMPY) ---")

class SateliteIA:
    def __init__(self, nombre, resolucion):
        """Constructor: Configura el satélite."""
        self.nombre = nombre
        self.resolucion = resolucion
        self.matriz = None # Aquí guardaremos la imagen
        print(f"🛰️ Satélite '{self.nombre}' en órbita. Resolución: {resolucion}x{resolucion}")

    def escanear_terreno(self):
        """Genera una matriz aleatoria simulando calor (0 a 100 grados)."""
        # Usamos NumPy para crear 10,000 datos instantáneos (100x100)
        self.matriz = np.random.uniform(0, 100, (self.resolucion, self.resolucion))
        print("📸 Escaneo completado.")

    def detectar_incendios(self, temperatura_limite):
        """Detecta puntos calientes usando VECTORIZACIÓN (Sin bucles)."""
        if self.matriz is None:
            print("❌ Error: No hay datos escaneados.")
            return

        # FILTRADO VECTORIAL (La magia de NumPy)
        # Esto crea una máscara de Verdadero/Falso instantánea
        mapa_incendios = self.matriz > temperatura_limite
        
        # Contamos cuántos 'True' hay
        num_alertas = np.sum(mapa_incendios)
        
        print(f"\n📊 ANÁLISIS DE '{self.nombre}':")
        print(f"   - Temp Máxima detectada: {np.max(self.matriz):.2f}°C")
        print(f"   - Puntos críticos (> {temperatura_limite}°C): {num_alertas} zonas.")

# ==========================================
# ZONA DE EJECUCIÓN
# ==========================================
# 1. Instanciamos el objeto (Creamos el satélite)
sat_1 = SateliteIA("Landsat-9", 100) # Matriz de 100x100

# 2. Usamos sus métodos
sat_1.escanear_terreno()
sat_1.detectar_incendios(85.0) # Buscar temperaturas mayores a 85

# ==========================================
# 🏋️ EJERCICIOS PARA EL ESTUDIANTE
# ==========================================
# 1. Crea un segundo satélite llamado "Sentinel-2" con resolución 500.
# 2. Agrega un método dentro de la clase llamado 'reporte_promedio' que imprima 
#    la temperatura promedio de toda la matriz. (Usa np.mean(self.matriz)).
# 3. Ejecuta el método detectar_incendios con un umbral más bajo (ej. 50) y observa cómo suben las alertas.
