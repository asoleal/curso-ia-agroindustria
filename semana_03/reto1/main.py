import pandas as pd
import matplotlib.pyplot as plt

# Configuración visual
plt.style.use("ggplot")


def auditar_estacion():
    print("--- INICIANDO AUDITORIA CLIMATICA ---")

    # ---------------------------------------------------------
    # 1. INGESTA DE DATOS
    # TODO: Cargar 'clima_corrupto.csv'
    # PISTA: Ojo con el separador (sep) y parsear fechas (parse_dates)
    # ---------------------------------------------------------
    file_path = "clima_corrupto.csv"

    # CODIGO AQUI (Reemplaza el None)
    df = None

    if df is None:
        print("❌ Error: Debes cargar el CSV primero en el paso 1.")
        return

    # Fijar fecha como índice para poder re-muestrear luego
    # df = df.set_index('fecha_hora') # Descomentar cuando cargues los datos

    print(f"Datos cargados: {df.shape}")

    # ---------------------------------------------------------
    # 2. LIMPIEZA DE TEMPERATURA
    # TODO: Las temperaturas > 50 son errores de sensor. Conviértelas a NaN.
    # ---------------------------------------------------------

    # CODIGO AQUI

    # ---------------------------------------------------------
    # 3. LIMPIEZA DE LLUVIA (SENSOR TRABADO)
    # TODO: Si la lluvia es EXACTAMENTE igual a la anterior durante mucho tiempo, es error.
    # PISTA: df['lluvia'].diff() == 0  indica que el valor se repitió
    # ---------------------------------------------------------

    # CODIGO OPCIONAL AQUI

    # ---------------------------------------------------------
    # 4. RESAMPLING (AGREGACIÓN)
    # TODO: Convierte los datos horarios a DIARIOS ('D')
    # Reglas: Temp -> Promedio (mean), Lluvia -> Suma (sum)
    # ---------------------------------------------------------

    # CODIGO AQUI (Reemplaza el None)
    df_diario = None

    # ---------------------------------------------------------
    # 5. VISUALIZACIÓN
    # ---------------------------------------------------------
    if df_diario is not None:
        print("📊 Generando reporte gráfico...")
        plt.figure(figsize=(12, 6))

        # Graficamos Temperatura
        plt.subplot(2, 1, 1)
        plt.plot(
            df_diario.index,
            df_diario["temp_c"],
            label="Temp Promedio Diario",
            color="tab:orange",
        )
        plt.title("Temperatura 2024 (Limpia)")
        plt.legend()

        # Graficamos Lluvia
        plt.subplot(2, 1, 2)
        plt.bar(
            df_diario.index,
            df_diario["precipitacion_mm"],
            label="Lluvia Acumulada",
            color="tab:blue",
        )
        plt.title("Precipitación Diaria")
        plt.legend()

        plt.tight_layout()
        plt.savefig("reporte_clima.png")
        print("✅ Gráfico guardado como 'reporte_clima.png'")
        plt.show()
    else:
        print("⚠️ No se pudo generar el gráfico porque falta el paso 4.")


if __name__ == "__main__":
    auditar_estacion()
