import time

print("\n--- 🟢 INICIO DEL TALLER DE FUNDAMENTOS ---")

# =======================================================
# TEORÍA RÁPIDA:
# Las Listas [] guardan datos ordenados.
# Los Diccionarios {} guardan datos con etiquetas (Clave: Valor).
# =======================================================

# 1. DATOS SUCIOS (Simulación)
# Recibimos esto de un sensor. Nota que hay un 'None' y un negativo absurdo.
sensores = [24.5, 25.1, None, 23.8, -100.0, 26.2]
print(f"📡 Datos crudos: {sensores}")

# 2. LIMPIEZA (El algoritmo)
datos_limpios = []
for lectura in sensores:
    # Si el dato es None (vacío), lo saltamos
    if lectura is None:
        continue
    
    # Si el dato está en un rango físico real (0 a 50 grados)
    if 0 <= lectura <= 50:
        datos_limpios.append(lectura)
    else:
        print(f"   ⚠️ Dato descartado por error: {lectura}")

print(f"✅ Datos limpios: {datos_limpios}")

# 3. ESTRUCTURA FINAL (Diccionario)
promedio = sum(datos_limpios) / len(datos_limpios)

reporte = {
    "status": "OK",
    "muestras_validas": len(datos_limpios),
    "temperatura_promedio": round(promedio, 2)
}

print(f"\n📄 REPORTE GENERADO:\n{reporte}")

# =======================================================
# 🧠 ZONA DE RETOS (Tu turno)
# =======================================================
print("\n--- 🔨 TUS EJERCICIOS ---")

# RETO 1: Agrega manualmente el valor 45.0 a la lista 'datos_limpios' usando .append()
# Escribe tu código aquí abajo:


# RETO 2: Crea una condición if que imprima "ALERTA DE CALOR" si el promedio es mayor a 25.
# Escribe tu código aquí abajo:


print("---------------------------------------------")
