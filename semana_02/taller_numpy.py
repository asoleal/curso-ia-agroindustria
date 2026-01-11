import numpy as np

"""
TALLER SEMANA 02: Análisis Espacial de Cultivos
Misión: Analizar un lote de 100x100 metros usando matrices.
"""


def analizar_lote():
    # 1. Configuración del Terreno (Matriz 100x100)
    # Valores entre 0.0 (Seco) y 1.0 (Inundado)
    print("📡 Escaneando terreno satelital...")
    humedad_suelo = np.random.uniform(low=0.1, high=0.9, size=(100, 100))

    # 2. Simular un fallo en el sistema de riego (Zona central seca)
    # Slicing: [filas, columnas] -> Afectamos el centro
    humedad_suelo[40:60, 40:60] = 0.05
    print("⚠️  Alerta: Fallo de riego detectado en el sector central.")

    # 3. Análisis con Máscaras Booleanas
    # ¿Qué parcelas están en estado crítico (< 0.2)?
    # Esto crea una matriz de True/False
    mask_sequia = humedad_suelo < 0.2

    # 4. Estadísticas
    total_pixeles = humedad_suelo.size
    total_sequia = np.sum(mask_sequia)  # Suma los True como 1
    porcentaje_dano = (total_sequia / total_pixeles) * 100

    humedad_promedio = np.mean(humedad_suelo)

    # 5. Reporte de Ingeniería
    print("\n--- REPORTE DE ESTADO DEL LOTE ---")
    print(f"Dimensiones: {humedad_suelo.shape} ({total_pixeles} m2)")
    print(f"Humedad Promedio: {humedad_promedio:.2%}")
    print(f"Área Crítica (Sequía): {total_sequia} m2")
    print(f"Porcentaje de Daño: {porcentaje_dano:.2f}%")

    if porcentaje_dano > 10:
        print("\n🚨 ACCIÓN REQUERIDA: ACTIVAR RIEGO DE EMERGENCIA 🚨")
    else:
        print("\n✅ Estado controlable.")


if __name__ == "__main__":
    analizar_lote()
