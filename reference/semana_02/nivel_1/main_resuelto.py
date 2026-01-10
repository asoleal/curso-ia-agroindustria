# REFERENCE: Solución S02 Lógica
sensores = [24.5, 25.1, None, 23.8, -100.0, 26.2]
datos_limpios = [x for x in sensores if x is not None and 0 <= x <= 50]

# --- SOLUCIONES ---

# RETO 1: Longitud
print(f"Reto 1: Tenemos {len(datos_limpios)} datos válidos.")

# RETO 2: Lógica IF
promedio = sum(datos_limpios) / len(datos_limpios)
if promedio > 25:
    print(f"Reto 2: ⚠️ ALERTA DE CALOR (Promedio: {promedio:.2f})")

# RETO 3: Append
datos_limpios.append(45.0)
print(f"Reto 3: Lista actualizada -> {datos_limpios}")
