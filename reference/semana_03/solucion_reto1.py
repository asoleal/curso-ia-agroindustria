import pandas as pd
import matplotlib.pyplot as plt

# Estilo para los gráficos
plt.style.use("ggplot")


def auditar_estacion():
    print("--- 🕵️‍♂️ INICIANDO AUDITORIA DE SOLUCIÓN ---")

    # ---------------------------------------------------------
    # 1. INGESTA DE DATOS
    # ---------------------------------------------------------
    # Solución: Usamos sep=';' y parseamos la fecha.
    # Usamos index_col para facilitar el resample posterior.
    df = pd.read_csv(
        "clima_corrupto.csv",
        sep=";",
        parse_dates=["fecha_hora"],
        index_col="fecha_hora",
    )

    print(f"✅ Datos cargados: {df.shape}")
    print(df.head(3))

    # ---------------------------------------------------------
    # 2. LIMPIEZA DE TEMPERATURA
    # ---------------------------------------------------------
    # Solución: Usamos .loc para filtrar temperaturas mayores a 50°C
    conteo_errores_temp = df[df["temp_c"] > 50].shape[0]
    print(f"   -> Se detectaron {conteo_errores_temp} registros de temperatura > 50°C.")

    # Asignamos pd.NA (Not a Number) a esos valores
    df.loc[df["temp_c"] > 50, "temp_c"] = pd.NA

    # ---------------------------------------------------------
    # 3. LIMPIEZA DE HUMEDAD (EXTRA)
    # ---------------------------------------------------------
    # Solución: Humedad no puede ser < 0 ni > 100
    mask_humedad = (df["humedad_relativa"] < 0) | (df["humedad_relativa"] > 100)
    df.loc[mask_humedad, "humedad_relativa"] = pd.NA

    # ---------------------------------------------------------
    # 4. LIMPIEZA DE LLUVIA (SENSOR TRABADO)
    # ---------------------------------------------------------
    # Lógica: Si la diferencia con el dato anterior es 0, el valor se repite.
    # PERO, que sea 0 repetido es normal (no llueve).
    # El error es cuando se repite un valor > 0.

    # diff() calcula: fila_actual - fila_anterior
    cambio = df["precipitacion_mm"].diff()

    # Máscara: No hubo cambio (0.0) Y el valor de lluvia es positivo
    mask_trabado = (cambio == 0) & (df["precipitacion_mm"] > 0)

    print(
        f"   -> Se detectaron {mask_trabado.sum()} horas con el sensor de lluvia trabado."
    )

    # Anulamos esos datos
    df.loc[mask_trabado, "precipitacion_mm"] = pd.NA

    # ---------------------------------------------------------
    # 5. RESAMPLING (AGREGACIÓN)
    # ---------------------------------------------------------
    # Solución: Agrupar por Día ('D')
    # Temp -> Promedio, Lluvia -> Suma total
    df_diario = df.resample("D").agg({"temp_c": "mean", "precipitacion_mm": "sum"})

    # Rellenar días vacíos (hueco de octubre) con 0 en lluvia para que no salga blanco en el gráfico
    # Ojo: No rellenamos temp con 0 porque alteraría el promedio, mejor dejarlo NaN o interpolar
    df_diario["precipitacion_mm"] = df_diario["precipitacion_mm"].fillna(0)

    print("✅ Resampling diario completado.")
    print(df_diario.head())

    # ---------------------------------------------------------
    # 6. VISUALIZACIÓN
    # ---------------------------------------------------------
    print("📊 Generando gráfico final...")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Gráfico 1: Temperatura
    # Graficamos la sucia original (resampleada rapido para fondo) vs la limpia
    ax1.plot(
        df_diario.index,
        df_diario["temp_c"],
        color="tab:orange",
        linewidth=2,
        label="Temp Limpia (Promedio)",
    )
    ax1.set_ylabel("Temp (°C)")
    ax1.set_title("Temperatura 2024: Detección de Anomalías")
    ax1.legend()
    ax1.grid(True)

    # Gráfico 2: Lluvia
    ax2.bar(
        df_diario.index,
        df_diario["precipitacion_mm"],
        color="tab:blue",
        label="Precipitación (mm)",
    )
    ax2.set_ylabel("Lluvia (mm)")
    ax2.set_title("Precipitación Diaria Acumulada")
    ax2.legend()
    ax2.grid(True, axis="y")

    plt.tight_layout()
    plt.savefig("solucion_reporte.png")
    print("🏆 ¡Misión cumplida! Gráfico guardado como 'solucion_reporte.png'")
    plt.show()


if __name__ == "__main__":
    auditar_estacion()
