import csv
import random
from datetime import datetime, timedelta

# Configuración
NUM_REGISTROS = 2000
ZONAS = ['Norte', 'Sur', 'Este', 'Oeste', 'Vivero']
ARCHIVO = 'lecturas_campo.csv'

print(f"--- 🚜 Generando {NUM_REGISTROS} registros de sensores ---")

with open(ARCHIVO, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Encabezados (¡Ojo! Esto causará problemas en SQLite si no se salta)
    writer.writerow(['id', 'fecha', 'zona', 'temperatura', 'humedad', 'ph'])

    fecha_base = datetime(2026, 1, 1)

    for i in range(1, NUM_REGISTROS + 1):
        # Avanzar el tiempo 30 minutos por registro
        fecha = fecha_base + timedelta(minutes=i*30)
        fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S")
        
        zona = random.choice(ZONAS)
        
        # Datos normales
        temp = round(random.uniform(18.0, 32.0), 1)
        hum = round(random.uniform(40.0, 85.0), 1)
        ph = round(random.uniform(5.5, 7.0), 2)

        # Inyectar anomalías (Riesgo de Hongo: Alta Temp + Alta Humedad)
        # Hacemos que ocurra aprox el 5% de las veces
        if random.random() < 0.05:
            temp = round(random.uniform(26.0, 35.0), 1)
            hum = round(random.uniform(80.0, 99.0), 1)

        writer.writerow([i, fecha_str, zona, temp, hum, ph])

print(f"✅ Archivo '{ARCHIVO}' generado. Listo para la ingesta.")
