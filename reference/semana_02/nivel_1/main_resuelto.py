# REFERENCE: Solución S02 Lógica
sensores = [24.5, 25.1, None, 23.8, -100.0, 26.2]
datos_limpios = [x for x in sensores if x is not None and 0 <= x <= 50]
datos_limpios.append(45.0) # Reto 1
print(f"Promedio: {sum(datos_limpios)/len(datos_limpios)}") # Reto 2
