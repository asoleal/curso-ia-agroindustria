# Módulo 2: Computación de Alto Rendimiento (HPC) con NumPy ⚡

> **Concepto Central:** Vectorización (SIMD) vs. Iteración Escalar.
> **Objetivo:** Demostrar empíricamente por qué los bucles `for` están prohibidos en el procesamiento de Big Data.

---

## 📖 Introducción Técnica: La Arquitectura de Memoria

En Ingeniería de Datos, la velocidad no depende solo del procesador (CPU), sino de la eficiencia en el acceso a la memoria RAM.

### 1. El Cuello de Botella de Python (Listas)
Las listas en Python son flexibles pero ineficientes (colecciones de punteros dispersos).
* **Visualización:** Imagina buscar libros esparcidos aleatoriamente por toda una biblioteca.
* **Costo:** La CPU gasta más tiempo "buscando" direcciones que calculando.

### 2. La Potencia de NumPy (Arrays)
NumPy utiliza bloques de **memoria contigua** (como C o Fortran).
* **Visualización:** Imagina una cinta transportadora donde los datos llegan ordenados.
* **SIMD:** La CPU carga bloques enteros y opera múltiples datos en un solo ciclo de reloj.



---

## 🧪 El Experimento Base

Realizaremos una prueba de estrés procesando **1,000,000 de registros**.

### El Escenario
Calculamos el "Índice de Vigor" para un cultivo masivo:
$$Vigor = (Altura \times Grosor) + 0.5$$

### Instrucciones de Ejecución
1.  Ubicado en la carpeta raíz `semana_02`, ejecuta:
    ```bash
    python 02_Numpy_Vectorizacion/simulacion.py
    ```
2.  **Observa la terminal:** Verás que NumPy es entre 50x y 100x más rápido que el Python estándar.

---

## 🚀 Tu Misión (Entregable Obligatorio)

Para completar este módulo, debes modificar el código original para demostrar que puedes vectorizar operaciones matemáticas complejas.

### Paso 1: Implementar el Reto Trigonométrico
Modifica el archivo `simulacion.py`. Cambia la fórmula simple por una operación pesada que incluya el **Seno (sin)**:

1.  Importa la librería matemática estándar: `import math`
2.  **En el bucle Python (Lento):**
    ```python
    # Cambia la multiplicación simple por esto:
    calculo = math.sin(alturas_list[i]) * grosores_list[i]
    ```
3.  **En la versión NumPy (Rápida):**
    ```python
    # Usa la función vectorizada universal (ufunc):
    vigor_np = np.sin(alturas_np) * grosores_np
    ```

### Paso 2: Ejecutar y Registrar
Vuelve a correr el script `python 02_Numpy_Vectorizacion/simulacion.py`.
* Verás que la diferencia de velocidad es aún mayor (posiblemente >150x).

### Paso 3: Documentar el Hallazgo
Ve al final de tu archivo `simulacion.py` y agrega un comentario con tus resultados. Debe verse así:

```python
# ---------------------------------------------------------
# REPORTE DE INGENIERÍA
# ---------------------------------------------------------
# Operación: Función Seno (Trigonométrica)
# Tiempo Python: X.XX segundos
# Tiempo NumPy:  X.XX segundos
# Aceleración (Speedup): XXX veces más rápido
# ---------------------------------------------------------