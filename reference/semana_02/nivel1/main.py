"""
MÓDULO 1: Lógica Computacional y Validación de Datos
Propósito: Demostrar el uso de lógica booleana defensiva (Short-Circuit Evaluation).
"""

def validar_riego(humedad: float, temperatura: float, sistema_activo: bool) -> str:
    """
    Decide si activar el riego basado en lógica de sensores.

    Reglas de Negocio:
    1. Si el sistema está inactivo -> APAGADO.
    2. Si los datos son erróneos -> ERROR.
    3. [NUEVO] Si temperatura > 50°C -> PELIGRO INCENDIO.
    4. Si humedad < 30% Y temperatura > 25°C -> RIEGO.
    """

    # --- PASO 1: Guard Clause (Cláusula de Protección) ---
    if not sistema_activo:
        return "[SISTEMA]: Inactivo por mantenimiento."

    # --- PASO 2: Validación de Integridad de Datos ---
    # Validamos que los sensores no estén enviando basura (ej. 1000 grados)
    datos_invalidos = (humedad < 0 or humedad > 100) or (
        temperatura < -50 or temperatura > 60
    )

    if datos_invalidos:
        return f"[ALERTA]: Lectura de sensores corrupta (H:{humedad}, T:{temperatura})"

    # --- PASO 2.5: Seguridad Crítica (RETO RESUELTO) ---
    # Prioridad Alta: Si hace más de 50°C, hay riesgo de incendio.
    if temperatura > 50:
        return "[ALERTA CRÍTICA]: 🔥 Peligro de incendio detectado."

    # --- PASO 3: Lógica de Negocio (Core Logic) ---
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

    # --- NUEVOS CASOS DE PRUEBA (CHAOS MONKEY) ---
    print("\n--- NUEVOS CASOS (RETO) ---")
    
    # Caso 5: Prueba de Fuego (Solución al Reto)
    print(validar_riego(humedad=10, temperatura=55, sistema_activo=True))

    # Caso 6: Límite exacto de humedad
    print(validar_riego(humedad=30, temperatura=28, sistema_activo=True))
