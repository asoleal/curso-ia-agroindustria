import pandas as pd
import matplotlib.pyplot as plt

# NOTA: En servidores sin pantalla, usamos 'Agg' para guardar imágenes en vez de mostrarlas
import matplotlib
matplotlib.use('Agg') 

print("\n--- 📊 ANÁLISIS VISUAL: BUSCANDO PATRONES ---")

# 1. CARGAMOS EL DATASET LIMPIO (Simulamos que ya limpiamos el anterior)
# Para este ejercicio creamos un DF rápido para asegurar que corra
data = {
    'Humedad': [55, 60, 45, 50, 65, 70, 40, 58, 62, 48],
    'Temperatura': [24, 23, 27, 25, 22, 21, 28, 24, 23, 26],
    'Rendimiento': [4.5, 5.0, 3.5, 4.0, 5.2, 5.5, 3.2, 4.7, 4.9, 3.8]
}
df = pd.DataFrame(data)

print("Datos cargados:")
print(df.head())

# 2. CORRELACIÓN MATEMÁTICA
# Esto es lo que mira la IA. 
# 1.0 = Relación perfecta positiva (Sube uno, sube el otro)
# -1.0 = Relación perfecta negativa (Sube uno, baja el otro)
matriz_corr = df.corr()
print("\n🔢 Matriz de Correlación:")
print(matriz_corr)
print("OBSERVA: ¿El Rendimiento depende más de la Humedad o de la Temperatura?")

# 3. GENERACIÓN DE GRÁFICOS
print("\n🎨 Generando gráficos de análisis...")

# Gráfico de Dispersión (Scatter Plot)
# Eje X: Humedad, Eje Y: Rendimiento
plt.figure(figsize=(10, 6))
plt.scatter(df['Humedad'], df['Rendimiento'], color='green', marker='o')
plt.title('Impacto de la Humedad en el Rendimiento')
plt.xlabel('Humedad del Suelo (%)')
plt.ylabel('Rendimiento (Toneladas)')
plt.grid(True)

# Guardar el gráfico
nombre_archivo = 'relacion_humedad_rendimiento.png'
plt.savefig(nombre_archivo)
print(f"✅ Gráfico guardado como: {nombre_archivo}")
print("   (Usa el explorador de archivos para abrir la imagen)")

# ==========================================
# 🧠 ZONA DE RETOS
# ==========================================
print("\n--- 🔨 TUS RETOS ---")

# RETO 1: Análisis de Temperatura
# Crea un gráfico nuevo (scatter) que compare Temperatura (X) vs Rendimiento (Y).
# Guárdalo como 'relacion_temp_rendimiento.png'.
# Pista: Copia el bloque de código de arriba y cambia las variables.
# Escribe tu código aquí:


# RETO 2: Interpretación (Print)
# Basado en la matriz de correlación impresa arriba, imprime un mensaje que diga
# cuál variable es más importante. Ejemplo: "La variable clave es..."
# Escribe tu código aquí:

print("---------------------------------------------")
