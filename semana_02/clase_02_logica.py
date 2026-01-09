# --- CLASE 2: LÓGICA DE PROGRAMACIÓN PARA AGROINDUSTRIA ---

print("--- INICIO DEL ANÁLISIS DE CALIDAD ---")

# 1. VARIABLES (El estado actual del proceso)
# Imaginemos que un sensor nos envía estos datos de un tanque de leche:
temperatura = 4.5  # Grados centígrados
acidez = 16        # Grados Dornic
volumen = 5000     # Litros

print(f"Estado del Tanque: Temp={temperatura}°C, Acidez={acidez}°D")

# 2. CONDICIONALES (El 'Cerebro' que toma decisiones)
# Regla de negocio: La leche se rechaza si T > 5°C o Acidez > 18°D
if temperatura > 5 or acidez > 18:
    estado = "RECHAZADO ❌"
    accion = "Desviar a tanque de cuarentena"
else:
    estado = "APROBADO ✅"
    accion = "Iniciar pasteurización"

print(f"Resultado de Calidad: {estado}")
print(f"Acción recomendada: {accion}")

# 3. LISTAS Y BUCLES (Procesando muchos datos a la vez)
# Supongamos que tomamos muestras de grados Brix cada hora en una mermelada:
lecturas_brix = [45, 48, 52, 55, 60, 62, 65]
target_brix = 62

print("\n--- MONITOREO DE COCCIÓN (BRIX) ---")

# Vamos a revisar cada lectura una por una
for lectura in lecturas_brix:
    if lectura >= target_brix:
        print(f"Lectura {lectura}: ¡PUNTO FINAL ALCANZADO! Apagar vapor. 🛑")
        break # Detener el ciclo
    else:
        print(f"Lectura {lectura}: Cocinando... ⏳")
