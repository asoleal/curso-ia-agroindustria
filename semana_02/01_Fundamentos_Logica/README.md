# Módulo 1: Lógica Computacional y Validación de Datos 🛡️

> **¿El problema?** En el mundo real, los sensores mienten. Un sensor de humedad puede reportar `-500%` si se rompe. Si tu código no detecta esto, tu IA tomará decisiones desastrosas (como inundar un cultivo).
> **La solución:** Programación Defensiva.

---

## 🏆 ¿Qué vas a lograr?
Al finalizar este laboratorio, dejarás de usar `if/else` básicos para escribir **Software de Ingeniería**:
1.  **Validar datos sucios** antes de que rompan tu sistema ("Sanitización").
2.  **Aprender "Guard Clauses":** Una técnica para evitar el código "spaghetti" (anidación excesiva).
3.  **Entender el "Cortocircuito":** Cómo hacer que Python sea eficiente dejando de calcular si ya sabe la respuesta.

---

## 🧠 Conceptos Clave (Antes de empezar)

### 1. Cláusulas de Guardia (Guard Clauses)
En lugar de encerrar todo tu código en un `if` gigante, verificamos los errores primero y "retornamos" inmediatamente.

**❌ Código Novato (Nested Ifs):**
```python
if sistema_activo:
    if humedad > 0:
        if humedad < 100:
            # Hacer cálculos...
```

## 🧪 Laboratorio: Tu Misión

El script `main.py` simula un cerebro digital para un sistema de riego. Tu trabajo es ponerlo a prueba y entender cómo se protege a sí mismo.

### Paso 1: Ejecución Base
Corre el script tal como está para ver el diagnóstico de 4 casos predefinidos.
```bash
python main.py
```
### Paso 2: "Chaos Monkey" (Rompe el sistema)
Abre el archivo `main.py` con tu editor de código. Ve al final, a la sección `if __name__ == "__main__":` y crea tus propios casos de prueba:

1.  **Simula un sensor loco:** Llama a la función con `humedad = 500`. ¿Qué mensaje obtienes?
2.  **Simula un fallo eléctrico:** Llama a la función con `sistema_activo = False`.
3.  **Prueba el límite:** ¿Qué pasa si la humedad es exactamente `30`? (¿Riega o no riega?).

### Paso 3: Reto de Código
Modifica la función `validar_riego` dentro de `main.py` para agregar una **nueva regla de seguridad**:

* Si la `temperatura` es mayor a `50°C`, el sistema debe retornar una `[ALERTA CRÍTICA]: Peligro de incendio`, sin importar la humedad.
* *Pista:* Debes agregar esta "Guard Clause" antes de la lógica de riego.