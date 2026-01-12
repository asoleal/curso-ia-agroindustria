import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import random

# Configuración
sensores = ["SENSOR_01", "SENSOR_02", "SENSOR_03", "SENSOR_04"]
start_date = datetime(2026, 1, 1, 8, 0)
n_registros = 1000

data = []
for i in range(n_registros):
    sensor = random.choice(sensores)
    fecha = start_date + timedelta(minutes=5 * i)
    temp = round(random.uniform(22, 28), 1)
    humedad = round(random.uniform(50, 90), 1)
    ph = round(random.uniform(6.5, 7.2), 1)

    data.append([sensor, fecha.strftime("%Y-%m-%d %H:%M:%S"), temp, humedad, ph])

df = pd.DataFrame(
    data, columns=["id_sensor", "fecha", "temperatura", "humedad", "pH_suelo"]
)
df.to_csv("sensores.csv", index=False)
print(f"✅ Generados {len(df)} registros en sensores.csv")
