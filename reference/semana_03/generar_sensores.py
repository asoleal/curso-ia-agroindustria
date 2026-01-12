import csv
import random
from datetime import datetime, timedelta

NUM_REGISTROS = 2000
ARCHIVO = 'lecturas_campo.csv'
ZONAS = ['Norte', 'Sur', 'Este', 'Oeste', 'Vivero']

print(f"--- 🚜 Generando {NUM_REGISTROS} registros simulados ---")

with open(ARCHIVO, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Escribimos encabezados (Esto es la "trampa" para la ingesta SQL)
    writer.writerow(['id', 'fecha', 'zona', 'temperatura', 'humedad', 'ph'])

    fecha_base = datetime(2026, 1, 1)

    for i in range(1, NUM_REGISTROS + 1):
        fecha = (fecha_base + timedelta(minutes=i*20)).strftime("%Y-%m-%d %H:%M:%S")
        zona = random.choice(ZONAS)
        
        # Datos normales
        temp = round(random.uniform(18.0, 30.0), 1)
        hum = round(random.uniform(40.0, 80.0), 1)
        ph = round(random.uniform(5.5, 7.0), 2)

        # Inyectar anomalías (Hongo: Alta Temp + Alta Humedad)
        if random.random() < 0.10: # 10% de probabilidad de riesgo
            temp = round(random.uniform(25.0, 35.0), 1)
            hum = round(random.uniform(85.0, 99.0), 1)

        writer.writerow([i, fecha, zona, temp, hum, ph])

print(f"✅ Datos creados en '{ARCHIVO}'")
