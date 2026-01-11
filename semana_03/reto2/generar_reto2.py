import pandas as pd
import numpy as np
import random


def generar_datos_cafe():
    print("☕ Generando datos de la Cooperativa...")

    # Rango de fechas (Primer trimestre 2024)
    fechas = pd.date_range(start="2024-01-01", end="2024-03-31", freq="D")

    # --- 1. TABLA DE PRECIOS (Mercado Internacional) ---
    # El precio varia dia a dia
    precio_base = 2.50  # USD por kilo
    precios_vals = precio_base + np.random.normal(0, 0.2, len(fechas))

    df_precios = pd.DataFrame({"fecha": fechas, "precio_usd_kg": precios_vals.round(2)})

    # INYECTAR ERROR: Faltan precios algunos días (Domingos o errores de sistema)
    indices_borrar = np.random.choice(len(fechas), 10, replace=False)
    df_precios.loc[indices_borrar, "precio_usd_kg"] = np.nan

    # Guardar Precios
    df_precios.to_csv("precios_mercado.csv", index=False)
    print("✅ 'precios_mercado.csv' generado (con huecos en los datos).")

    # --- 2. TABLA DE PRODUCCIÓN (Cosecha en campo) ---
    data_prod = []
    lotes = ["Lote_Norte", "Lote_Sur", "Lote_Rio"]

    # Simulamos 100 registros de cosecha aleatorios en esas fechas
    for _ in range(100):
        fecha_random = random.choice(fechas)
        lote_random = random.choice(lotes)
        kilos = random.uniform(50, 200)  # Sacos de café

        data_prod.append([fecha_random, lote_random, round(kilos, 1)])

    df_prod = pd.DataFrame(
        data_prod, columns=["fecha", "id_lote", "kilos_recolectados"]
    )

    # INYECTAR ERROR: Kilos negativos (error de digitación)
    df_prod.loc[5, "kilos_recolectados"] = -50.0
    df_prod.loc[25, "kilos_recolectados"] = -120.5

    # Guardar Producción
    df_prod.to_csv("produccion.csv", index=False)
    print("✅ 'produccion.csv' generado (con errores de tipeo).")


if __name__ == "__main__":
    generar_datos_cafe()
