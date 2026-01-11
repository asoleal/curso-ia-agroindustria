import pandas as pd
import matplotlib.pyplot as plt

# Estilo visual consistente
plt.style.use("ggplot")


def analizar_rentabilidad():
    print("--- ☕ SOLUCIÓN: ANÁLISIS DE COSECHA ---")

    # ---------------------------------------------------------
    # PASO 1: CARGA DE DATOS
    # ---------------------------------------------------------
    # CLAVE: Usamos parse_dates en AMBOS. Si una fecha es texto (String)
    # y la otra es Fecha (Timestamp), el Merge fallará o dará vacío.
    print("1. Cargando archivos...")
    prod = pd.read_csv("produccion.csv", parse_dates=["fecha"])
    precios = pd.read_csv("precios_mercado.csv", parse_dates=["fecha"])

    # ---------------------------------------------------------
    # PASO 2: LIMPIEZA INDIVIDUAL
    # ---------------------------------------------------------
    print("2. Limpiando datos...")

    # A. Eliminar kilos negativos (Error físico/humano)
    # Filtramos solo lo que sea mayor o igual a 0
    filas_antes = len(prod)
    prod = prod[prod["kilos_recolectados"] >= 0]
    borrados = filas_antes - len(prod)
    print(f"   -> Se eliminaron {borrados} registros con peso negativo.")

    # B. Rellenar precios faltantes (Lógica Financiera)
    # Usamos ffill() (Forward Fill): "Si hoy no hay precio, usa el de ayer".
    # Es más correcto financieramente que usar un promedio mensual.
    precios["precio_usd_kg"] = precios["precio_usd_kg"].ffill()

    # Validación rápida: verificar si quedan nulos
    nulos_quedan = precios["precio_usd_kg"].isna().sum()
    print(f"   -> Precios nulos restantes tras ffill: {nulos_quedan}")

    # ---------------------------------------------------------
    # PASO 3: FUSIÓN DE DATOS (MERGE)
    # ---------------------------------------------------------
    print("3. Cruzando tablas (Merge)...")

    # how='left': Mantenemos TODAS las filas de producción (tabla izquierda).
    # Si no hay precio para un día, aparecerá NaN, pero no perdemos el dato de que se cosechó.
    df_final = pd.merge(prod, precios, on="fecha", how="left")

    # ---------------------------------------------------------
    # PASO 4: LÓGICA DE NEGOCIO
    # ---------------------------------------------------------
    # Calculamos ingreso. Si el precio sigue siendo NaN (ej. primer día), el resultado será NaN.
    df_final["ingreso_total"] = (
        df_final["kilos_recolectados"] * df_final["precio_usd_kg"]
    )

    # Limpieza final: Si algún ingreso quedó NaN, lo llenamos con 0 para poder sumar
    df_final["ingreso_total"] = df_final["ingreso_total"].fillna(0)

    print("   -> Ejemplo de datos unidos:")
    print(df_final.head())

    # ---------------------------------------------------------
    # PASO 5: REPORTE Y VISUALIZACIÓN
    # ---------------------------------------------------------
    print("4. Generando reporte...")

    # GroupBy por Lote y suma de dinero
    reporte_lotes = df_final.groupby("id_lote")["ingreso_total"].sum()

    print("\n--- 💰 INGRESOS POR LOTE ---")
    print(reporte_lotes.round(2))

    # Gráfico
    plt.figure(figsize=(10, 6))

    # Truco visual: Ordenar los valores para que el gráfico se vea mejor (de mayor a menor)
    reporte_lotes.sort_values(ascending=False).plot(
        kind="bar", color=["#8B4513", "#A0522D", "#CD853F"]
    )

    plt.title("Ingresos Totales por Lote (Trimestre 1)", fontsize=14)
    plt.ylabel("Ingresos (USD)", fontsize=12)
    plt.xlabel("Lote", fontsize=12)
    plt.xticks(rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig("solucion_cafe.png")
    print("✅ Gráfico guardado: solucion_cafe.png")
    plt.show()


if __name__ == "__main__":
    analizar_rentabilidad()
