# Módulo 1: Lógica Computacional y Validación de Datos 🛡️

> **Concepto Clave:** "Fail Fast" (Fallar Rápido) y Diseño Defensivo.
> **Objetivo:** Aprender a proteger tu código de datos basura ("Garbage In, Garbage Out").

---

## 📖 Introducción Técnica: El Arte de Decir "No"

En ingeniería de software crítica (como en medicina o agricultura), procesar un dato incorrecto es peor que no procesar nada. Si un sensor dice que la humedad es `-500%`, tu código no debe intentar corregirlo; debe detenerse inmediatamente.

### 1. El Problema: "Arrow Code" (Código Flecha)
Cuando usas muchos `if/else` anidados, el código toma forma de flecha hacia la derecha. Es difícil de leer y propenso a errores.



### 2. La Solución: Guard Clauses (Cláusulas de Guardia)
Invertimos la lógica. En lugar de verificar si todo está *bien* para entrar, verificamos si algo está *mal* para salir (`return`).
* **Lógica Tradicional:** "Si el sistema está activo, entra. Si la humedad es válida, entra..."
* **Lógica Defensiva:** "¿Sistema apagado? Fuera. ¿Humedad inválida? Fuera. (Si llegas aquí, todo está bien)".

---

## 🧪 Laboratorio: Tu Misión (Paso a Paso)

El script `main.py` simula el cerebro de un sistema de riego. Actualmente funciona, pero le falta una regla de seguridad crítica.

### Paso 1: Ejecución y Diagnóstico
Corre el script base para entender su comportamiento actual.
```bash
python main.py
```
> **Observa:** Mira cómo el sistema responde con mensajes claros ante "Sistema Inactivo" o "Datos Corruptos".

### Paso 2: "Chaos Monkey" (Pruebas Destructivas)
Vamos a intentar romper el código existente. Abre `main.py`, ve al final (sección `if __name__ == "__main__":`) y agrega estas líneas de prueba:

```python
# Prueba de estrés manual
print(validar_riego(humedad=500, temperatura=20, sistema_activo=True)) # ¿Detecta el error?
print(validar_riego(humedad=30, temperatura=60, sistema_activo=True))  # ¿Detecta el calor extremo?
```
### Paso 3: Implementar la Regla de Fuego (Reto)
Actualmente, si la temperatura es `60°C` (incendio), el sistema solo dice "Error de sensor" o intenta regar. Necesitamos una alerta específica.

**Tu Tarea:**
Modifica la función `validar_riego` en `main.py`. Agrega una nueva Cláusula de Guardia **después** de validar la integridad de los datos pero **antes** de la lógica de riego.



* **Condición:** Si `temperatura > 50`.
* **Acción:** Retornar exactamente el string `"[ALERTA CRÍTICA]: 🔥 Peligro de incendio detectado."`.

---

## 🚀 Entregable Obligatorio
Para dar por finalizado este módulo, debes demostrar que tu nueva lógica funciona.

1.  Asegúrate de haber modificado la función `validar_riego`.
2.  Agrega el siguiente caso de prueba al final del archivo `main.py` (en el bloque `__main__`):

    ```python
    # CASO 5: PRUEBA DE FUEGO (Debe salir Alerta Crítica)
    print(validar_riego(humedad=10, temperatura=55, sistema_activo=True))
    ```

3.  Ejecuta el script de nuevo. Si ves el mensaje `🔥 Peligro de incendio detectado`, has tenido éxito.

### ✅ Confirmación de Entrega
Sube el archivo modificado con tu nueva lógica de seguridad:

```bash
git add 01_Fundamentos_Logica/main.py
git commit -m "Laboratorio Lógica: Implementada alerta crítica de incendio"
git push origin main