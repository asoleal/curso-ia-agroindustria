"""
MÓDULO 1: Lógica Computacional y Validación de Datos
Propósito: Demostrar el uso de lógica booleana defensiva (Short-Circuit Evaluation).
"""


def validar_riego(humedad: float, temperatura: float, sistema_activo: bool) -> str:
    """
    Decide si activar el riego basado en lógica de sensores.

    Reglas de Negocio:
    1. Si el sistema está inactivo -> APAGADO (Critical Stop).
    2. Si los datos son erróneos (fuera de rango) -> ERROR.
    3. Si humedad < 30% Y temperatura > 25°C -> RIEGO.
    """

    # --- PASO 1: Guard Clause (Cláusula de Protección) ---
    # Si el sistema está apagado, retornamos inmediatamente.
    # Esto ahorra procesamiento (Short-circuit).
    if not sistema_activo:
        return "[SISTEMA]: Inactivo por mantenimiento."

    # --- PASO 2: Validación de Integridad de Datos ---
    # Un sensor roto puede enviar -999 o 2000. Validamos rangos físicos.
    datos_invalidos = (humedad < 0 or humedad > 100) or (
        temperatura < -50 or temperatura > 60
    )

    if datos_invalidos:
        return f"[ALERTA]: Lectura de sensores corrupta (H:{humedad}, T:{temperatura})"

    # --- PASO 3: Lógica de Negocio (Core Logic) ---
    # Aplicamos la regla agronómica
    necesita_agua = (humedad < 30) and (temperatura > 25)

    if necesita_agua:
        return f"[ACCIÓN]: 💧 Activando bombas (Humedad Crítica: {humedad}%)"
    else:
        return "[ESTADO]: ✅ Condiciones óptimas. Esperando."


# --- BLOQUE PRINCIPAL (Testing) ---
if __name__ == "__main__":
    print("--- INICIANDO DIAGNÓSTICO DE SENSORES ---\n")

    # Caso 1: Todo normal
    print(validar_riego(humedad=45, temperatura=22, sistema_activo=True))

    # Caso 2: Sequía extrema
    print(validar_riego(humedad=20, temperatura=30, sistema_activo=True))

    # Caso 3: Sensor roto (Humedad imposible)
    print(validar_riego(humedad=150, temperatura=25, sistema_activo=True))

    # Caso 4: Sistema apagado manualmente
    print(validar_riego(humedad=10, temperatura=40, sistema_activo=False))
