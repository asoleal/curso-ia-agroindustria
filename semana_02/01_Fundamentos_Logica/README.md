# Módulo 1: Lógica Computacional y Diseño Defensivo 🛡️

> **Concepto Clave:** "Fail Fast" (Fallar Rápido) y Validación de Datos.

## 📖 Descripción Técnica
En la ingeniería de IA, los datos nunca son perfectos. Los sensores fallan, las APIs se caen y los usuarios introducen valores erróneos. Este módulo demuestra cómo escribir **Lógica Defensiva**.

No usamos `if` simplemente para bifurcar caminos, lo usamos para **proteger la integridad del sistema** antes de realizar cálculos costosos.

### Conceptos Tratados
1.  **Short-Circuit Evaluation:** Python deja de evaluar una condición tan pronto sabe el resultado final.
    * `False and (Calculo_Pesado)` -> Python ni siquiera toca el cálculo pesado.
2.  **Guard Clauses (Cláusulas de Guardia):** Validar y retornar temprano en lugar de anidar múltiples `if` (Hell's Nesting).
3.  **Álgebra Booleana:** Uso correcto de `not`, `and`, `or` para modelar reglas de negocio agrícolas.

---

## 🛠️ El Código (`main.py`)

El script implementa un validador para un **Sistema de Riego Autónomo**.

### Estructura de la Función
```python
def validar_riego(humedad, temperatura, sistema_activo):
    # 1. Check de Sistema (Guard Clause)
    # 2. Validación de Rangos Físicos (Integridad)
    # 3. Lógica de Negocio (Algoritmo de Riego)