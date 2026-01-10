import time

print("--- 🟢 NIVEL 1: GESTIÓN DE DATOS AGRÍCOLAS ---")

# 1. LISTAS (Secuencias ordenadas)
# Imaginemos lecturas crudas de un sensor de humedad
lecturas_crudas = [45.2, 46.5, 500.0, 44.8, -10.0, 45.0]
print(f"📡 Datos recibidos: {lecturas_crudas}")

# 2. FUNCIONES Y LÓGICA DE LIMPIEZA
def limpiar_sensor(datos):
    """Recibe una lista, elimina errores y devuelve datos válidos."""
    datos_validos = []
    for lectura in datos:
        # Filtramos valores imposibles (0% a 100% humedad)
        if 0 <= lectura <= 100:
            datos_validos.append(lectura)
        else:
            print(f"⚠️ Alerta: Valor descartado por error ({lectura})")
    return datos_validos

datos_limpios = limpiar_sensor(lecturas_crudas)
print(f"✅ Datos limpios: {datos_limpios}")

# 3. DICCIONARIOS (Estructura Clave-Valor)
# Así se ven los datos en una base de datos real o API
lote_info = {
    "id": "LOTE-2024-X",
    "ubicacion": "Zona Norte",
    "cultivo": "Maíz Híbrido",
    "promedio_humedad": sum(datos_limpios) / len(datos_limpios)
}

print("\n--- 📝 REPORTE GENERADO (Formato Diccionario) ---")
print(f"Lote ID: {lote_info['id']}")
print(f"Cultivo: {lote_info['cultivo']}")
print(f"Humedad Promedio: {lote_info['promedio_humedad']:.2f}%")
