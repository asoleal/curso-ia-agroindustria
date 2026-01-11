import pandas as pd
import matplotlib.pyplot as plt

# Configuración visual
plt.style.use("ggplot")


def analizar_rentabilidad():
    print("--- ☕ INICIANDO ANÁLISIS DE COSECHA ---")

    # ---------------------------------------------------------
    # PASO 1: CARGA DE DATOS
    # TODO: Cargar 'produccion.csv' y 'precios_mercado.csv'
    # PISTA: Recuerda parsear las fechas en AMBOS dataframes
    # ---------------------------------------------------------
    print("1. Cargando archivos...")
    prod = None  # pd.read_csv...
    precios = None  # pd.read_csv...

    if prod is None or precios is None:
        print("❌ Error: Carga los archivos primero.")
        return

    # ---------------------------------------------------------
    # PASO 2: LIMPIEZA INDIVIDUAL
    # ---------------------------------------------------------
    print("2. Limpiando datos...")

    # TODO A: En 'prod', elimina las filas donde 'kilos_recolectados' sea menor a 0.

    # TODO B: En 'precios', hay valores vacíos (NaN).
    # Rellénalos usando el método 'ffill' (Forward Fill) para usar el precio del día anterior.
    # PISTA: precios['precio_usd_kg'] = precios['precio_usd_kg'].fillna(...)

    # ---------------------------------------------------------
    # PASO 3: FUSIÓN DE DATOS (MERGE)
    # TODO: Une la tabla de producción con la de precios.
    # Queremos pegar el precio CORRESPONDIENTE a la fecha de cada cosecha.
    # Usa: how='left' (para mandar la tabla de producción como la principal)
    # ---------------------------------------------------------
    print("3. Cruzando tablas (Merge)...")

    df_final = None  # pd.merge(...)

    # Verificación rápida
    # print(df_final.head())

    # ---------------------------------------------------------
    # PASO 4: LÓGICA DE NEGOCIO
    # TODO: Crea una nueva columna 'ingreso_total'
    # Fórmula: kilos_recolectados * precio_usd_kg
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # PASO 5: REPORTE Y VISUALIZACIÓN
    # TODO: Agrupa por 'id_lote' y suma el 'ingreso_total'
    # ---------------------------------------------------------
    print("4. Generando reporte...")

    # reporte_lotes = df_final.groupby(...)[...].sum()
    reporte_lotes = None  # Reemplaza esto con el groupby

    if reporte_lotes is not None:
        print(reporte_lotes)

        # Gráfico
        plt.figure(figsize=(8, 5))
        reporte_lotes.plot(kind="bar", color="brown")
        plt.title("Ingresos Totales por Lote (USD)")
        plt.ylabel("Dólares")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig("analisis_cafe.png")
        print("✅ Gráfico guardado: analisis_cafe.png")
        plt.show()
    else:
        print("⚠️ Falta completar el Paso 5")


if __name__ == "__main__":
    analizar_rentabilidad()
