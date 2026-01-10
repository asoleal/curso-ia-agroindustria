print("\n--- 🟢 TALLER DE FUNDAMENTOS ---")
sensores = [24.5, 25.1, None, 23.8, -100.0, 26.2]
datos_limpios = []

for lectura in sensores:
    if lectura is None: continue
    if 0 <= lectura <= 50:
        datos_limpios.append(lectura)

print(f"✅ Datos limpios: {datos_limpios}")
promedio = sum(datos_limpios) / len(datos_limpios)
print(f"📊 Promedio: {promedio:.2f}")

# --- 🧠 ZONA DE RETOS ---
# RETO 1: Agrega manualmente el valor 45.0 a la lista 'datos_limpios'.
# RETO 2: Crea un if que imprima "ALERTA" si el promedio > 25.
