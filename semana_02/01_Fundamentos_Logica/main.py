import time

print("\n--- 🟢 TALLER DE FUNDAMENTOS (Listas y Lógica) ---")

# 1. DATOS SUCIOS
# Recibimos esto de un sensor. Nota que hay 'None' y valores erróneos.
sensores = [24.5, 25.1, None, 23.8, -100.0, 26.2]
print(f"📡 Datos crudos: {sensores}")

# 2. LIMPIEZA DE DATOS
datos_limpios = []

for lectura in sensores:
    # Si es None, saltamos al siguiente
    if lectura is None:
        continue
    
    # Validamos rango físico (0 a 50 grados)
    if 0 <= lectura <= 50:
        datos_limpios.append(lectura)

print(f"✅ Datos limpios: {datos_limpios}")

# 3. CÁLCULO DE PROMEDIO
promedio = sum(datos_limpios) / len(datos_limpios)
print(f"📊 Promedio actual: {promedio:.2f}")

# ==========================================
# 🧠 ZONA DE RETOS
# ==========================================
print("\n--- 🔨 TUS EJERCICIOS ---")

# RETO 1: Imprime cuántos datos tiene la lista 'datos_limpios' usando len().
# Escribe tu código aquí:


# RETO 2: Crea un if que imprima "⚠️ ALERTA DE CALOR" si el promedio es mayor a 25.
# Escribe tu código aquí:


# RETO 3: Agrega el valor de 45.0 a la lista 'datos_limpios' usando append().
# (Imprime la lista después para verificar que se agregó).
# Escribe tu código aquí:


print("---------------------------------------------")
