import numpy as np

"""
TALLER INTEGRAL SEMANA 02: Agricultura de Precisión con NumPy
Misión: Analizar salud de cultivos, detectar anomalías y calcular presupuesto de riego.
Conceptos: Máscaras, np.where, Agregaciones, Aritmética de Matrices.
"""


def renderizar_mapa(matriz, titulo):
    """
    Helper visual para ver la matriz en la terminal.
    Hacemos un 'downsampling' (tomamos 1 de cada 5 pixeles) para que quepa en pantalla.
    """
    print(f"\n🗺️  {titulo} (Visualización Simplificada 20x20):")
    # Slicing con paso [::5] para reducir 100x100 a 20x20
    vista = matriz[::5, ::5]

    for fila in vista:
        linea = ""
        for valor in fila:
            if valor > 0.8:
                linea += "🟦"  # Exceso de agua
            elif valor < 0.2:
                linea += "🟫"  # Sequía severa
            elif valor < 0.4:
                linea += "🟨"  # Alerta
            else:
                linea += "🟩"  # Saludable
        print(linea)
    print("Referencias: 🟦=Inundado | 🟩=Ok | 🟨=Bajo | 🟫=Sequía\n")


def gestion_inteligente_cultivos():
    print("🚀 INICIANDO SISTEMA DE GESTIÓN AGRÍCOLA SATELITAL (S.G.A.S)\n")

    # 1. GENERACIÓN DE DATOS (Simulación de Sensores)
    # Creamos un terreno de 100x100 metros (10,000 pixeles)
    # np.random.normal genera una distribución más realista que uniform
    print("📡 Recibiendo telemetría de humedad del suelo...")
    humedad = np.random.normal(loc=0.45, scale=0.15, size=(100, 100))

    # Clip para asegurar que los valores estén entre 0.0 y 1.0
    humedad = np.clip(humedad, 0.0, 1.0)

    # 2. INTRODUCIR ANOMALÍAS (Simulación de Problemas Reales)
    # Falla de aspersor en la esquina superior izquierda (Sequía)
    humedad[0:20, 0:20] = 0.15
    # Fuga de tubería en el centro (Inundación)
    humedad[45:55, 45:55] = 0.95

    renderizar_mapa(humedad, "MAPA DE HUMEDAD ACTUAL")

    # 3. DIAGNÓSTICO VECTORIZADO (np.select o np.where)
    # Clasificamos cada metro cuadrado sin usar bucles for
    # Condiciones:
    # - Sequía: < 0.2
    # - Óptimo: Entre 0.2 y 0.8
    # - Inundado: > 0.8

    total_pixeles = humedad.size

    # np.sum cuenta los 'True'
    area_sequia = np.sum(humedad < 0.2)
    area_inundada = np.sum(humedad > 0.8)
    area_optima = total_pixeles - (area_sequia + area_inundada)

    # 4. CÁLCULO DE RECURSOS (Ingeniería de Datos)
    # Objetivo: Queremos llevar todo lo que está < 0.4 a por lo menos 0.5
    # Fórmula: Agua Necesaria = (Objetivo - Actual) * Litros_por_m2
    # Pero SOLO aplicamos esto donde hace falta (humedad < 0.4).

    OBJETIVO_HUMEDAD = 0.5

    # np.where(condicion, valor_si_true, valor_si_false)
    # Si la humedad es baja, calculamos la diferencia. Si no, necesitamos 0 agua.
    deficit_matriz = np.where(humedad < 0.4, OBJETIVO_HUMEDAD - humedad, 0)

    # Asumimos que subir 0.1 de humedad requiere 1 Litro de agua por m2
    litros_totales = np.sum(deficit_matriz) * 10

    # 5. REPORTE EJECUTIVO
    print("📊 REPORTE DE INTELIGENCIA DE NEGOCIOS:")
    print(f"---------------------------------------")
    print(f"🌲 Área Saludable:     {area_optima} m2")
    print(f"🔥 Área Crítica (Seca): {area_sequia} m2")
    print(f"🌊 Área Inundada:      {area_inundada} m2")
    print(f"---------------------------------------")
    print(f"💧 AGUA REQUERIDA:     {litros_totales:.2f} Litros")

    # Decisión automatizada
    if litros_totales > 5000:
        print("\n⚠️  ALERTA: Consumo de agua elevado. Solicitar autorización manual.")
    elif area_inundada > 500:
        print(
            "\n⚠️  ALERTA: Posible rotura de tubería detectada. Cerrar válvulas sector B."
        )
    else:
        print("\n✅ ACCIÓN: Iniciando protocolo de riego automatizado.")


if __name__ == "__main__":
    gestion_inteligente_cultivos()
