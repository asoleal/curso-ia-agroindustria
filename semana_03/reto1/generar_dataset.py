import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def crear_caos():
    print("🌱 Generando datos corruptos de la estación 'La Finca'...")

    # 1. Crear rango de fechas (Año 2024, horario)
    fechas = pd.date_range(start="2024-01-01", end="2024-12-31 23:00", freq="h")
    n = len(fechas)

    # 2. Simular Temperatura (Curva sinusoidal + Ruido)
    # Enero frio, Julio caliente (Hemisferio Norte) o al revés. Haremos algo generico.
    temp_base = 20 + 10 * np.sin(np.linspace(0, 2 * np.pi, n))
    ruido = np.random.normal(0, 2, n)
    temp = temp_base + ruido

    # INYECTAR ERROR 1: Picos de voltaje (200 grados)
    indices_error_temp = np.random.choice(n, 50, replace=False)
    temp[indices_error_temp] = 200.0

    # 3. Simular Lluvia (Mayormente ceros, eventos esporadicos)
    lluvia = np.zeros(n)
    indices_lluvia = np.random.choice(n, 500, replace=False)
    lluvia[indices_lluvia] = np.random.exponential(5, 500)  # Lluvia exponencial

    # INYECTAR ERROR 2: Sensor trabado
    # El sensor se traba en la fila 4000 y repite el valor 15.4 durante 48 horas
    lluvia[4000:4048] = 15.4

    # 4. Simular Humedad
    humedad = np.random.uniform(30, 90, n)

    # INYECTAR ERROR 3: Humedad imposible (>100%)
    humedad[100:105] = 120.0
    humedad[200:205] = -5.0

    # Crear DataFrame
    df = pd.DataFrame(
        {
            "fecha_hora": fechas,
            "temp_c": temp.round(1),
            "precipitacion_mm": lluvia.round(1),
            "humedad_relativa": humedad.round(1),
            "sensor_id": "SN-4092",
        }
    )

    # INYECTAR ERROR 4: Datos faltantes (Apagón en Octubre)
    # Eliminamos 5 dias de octubre
    mask_borrar = (df["fecha_hora"] >= "2024-10-10") & (df["fecha_hora"] < "2024-10-15")
    df = df[~mask_borrar]

    # Guardar CSV sucio (usando punto y coma, tipico problema en Latam)
    df.to_csv("clima_corrupto.csv", sep=";", index=False)
    print("✅ Archivo 'clima_corrupto.csv' creado con éxito.")
    print(f"   Total de filas: {len(df)} (deberían ser {n}, pero borramos algunas).")


if __name__ == "__main__":
    crear_caos()
