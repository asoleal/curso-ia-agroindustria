import time

print("--- 🟢 INICIANDO SISTEMA DE LIMPIEZA DE DATOS ---")

# ==========================================
# PASO 1: RECEPCIÓN DE DATOS (Listas)
# ==========================================
# Simulamos datos de un sensor de temperatura.
# Nota: Hay valores erróneos (-500, 200) y correctos (20-40).
datos_crudos = [23.5, 24.1, -500.0, 25.3, 200.0, 22.8, 24.0]
print(f"📡 Datos recibidos: {datos_crudos}")

# ==========================================
# PASO 2: LÓGICA DE PROCESAMIENTO (Funciones)
# ==========================================
def filtrar_temperaturas(lista_datos):
    """
    Recorre la lista y elimina valores que no sean físicos.
    Rango válido: 0°C a 50°C.
    """
    datos_validos = []
    log_errores = 0
    
    for lectura in lista_datos:
        # Lógica de validación
        if 0 <= lectura <= 50:
            datos_validos.append(lectura)
        else:
            log_errores += 1
            
    return datos_validos, log_errores

# Usamos la función
datos_limpios, errores = filtrar_temperaturas(datos_crudos)

print(f"✅ Datos válidos: {datos_limpios}")
print(f"⚠️ Errores descartados: {errores}")

# ==========================================
# PASO 3: ESTRUCTURACIÓN (Diccionarios)
# ==========================================
# Calculamos el promedio
promedio = sum(datos_limpios) / len(datos_limpios)

# Empaquetamos todo en un objeto estructurado (tipo JSON)
reporte = {
    "fecha": "2024-05-20",
    "ubicacion": "Invernadero A",
    "total_muestras": len(datos_limpios),
    "valor_promedio": round(promedio, 2),
    "estado": "NOMINAL"
}

print("\n--- 📝 REPORTE FINAL ---")
for clave, valor in reporte.items():
    print(f"  > {clave.upper()}: {valor}")

# ==========================================
# 🏋️ EJERCICIOS PARA EL ESTUDIANTE
# ==========================================
# 1. Modifica la lista 'datos_crudos' agregando un valor de 1000. Ejecuta y mira qué pasa.
# 2. Agrega una nueva clave al diccionario 'reporte' llamada "maxima_temp" que tenga el valor máximo de la lista limpia.
#    Pista: usa la función max(datos_limpios).
# 3. Cambia la condición del 'if' para que solo acepte temperaturas entre 20 y 30 grados.
