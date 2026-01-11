# Módulo 2: Computación de Alto Rendimiento (HPC) con NumPy ⚡

> **Concepto Central:** Vectorización (SIMD) vs. Iteración Escalar.
> **Objetivo:** Demostrar empíricamente por qué los bucles `for` están prohibidos en el procesamiento de Big Data.

---

## 📖 Introducción Técnica: La Arquitectura de Memoria

En Ingeniería de Datos, la velocidad no depende solo de qué tan rápido es tu procesador (CPU), sino de qué tan eficientemente accedes a la memoria RAM.

### 1. El Cuello de Botella de Python (Listas)
Las listas en Python son flexibles pero ineficientes. Son colecciones de **punteros** dispersos en la memoria.
* **Visualización:** Imagina a un bibliotecario que debe buscar libros (datos) que están esparcidos aleatoriamente por toda la biblioteca.
* **Costo:** La CPU gasta más tiempo "buscando" direcciones de memoria y verificando tipos de datos (`int`, `float`, `str`) que haciendo la suma matemática.

### 2. La Potencia de NumPy (Arrays)
NumPy utiliza bloques de **memoria contigua** (como C o Fortran).
* **Visualización:** Imagina una cinta transportadora donde todos los datos llegan ordenados uno tras otro.
* **SIMD:** La CPU carga un bloque entero en su caché y usa instrucciones especiales (Single Instruction, Multiple Data) para operar 4, 8 o 16 números en un solo ciclo de reloj.



---

## 🧪 El Experimento: Benchmark (`simulacion.py`)

Realizaremos una prueba de estrés procesando **1,000,000 de registros** de plantas simuladas (equivalente a 100 hectáreas de datos).

### El Escenario
Calculamos el "Índice de Vigor" para un cultivo masivo usando la fórmula:
$$Vigor = (Altura \times Grosor) + 0.5$$

### Los Contendientes
1.  **Enfoque Nativo (Lento):** Listas estándar + Bucle `for`.
    * *Complejidad:* $O(N)$ con alto overhead de interpretación.
2.  **Enfoque Vectorizado (Rápido):** Arrays de NumPy + Operación Matricial.
    * *Complejidad:* $O(N)$ optimizado en C.

---

## ⚙️ Laboratorio: Instrucciones Paso a Paso

No te limites a ejecutar el código. Sigue estos pasos para entender los límites de tu hardware.

### Paso 1: La Línea Base (Benchmark)
Ejecuta el script para establecer una referencia.
```bash
python simulacion.py
```

> **Tu Misión:** Anota el "Speedup" (veces más rápido). Debería estar entre **50x y 100x**.

### Paso 2: Análisis de Resultados
Mira la salida en la terminal.

* **Tiempo Python:** Probablemente 0.15s - 0.40s.
* **Tiempo NumPy:** Probablemente 0.002s - 0.005s.

> **Reflexión:** Si tuvieras que procesar imágenes satelitales (billones de pixeles), el método de Python tardaría **días**, mientras que NumPy tardaría **minutos**.

### Paso 3: "Stress Test" (Prueba de Estrés)
Vamos a llevar tu RAM al límite.

1.  Abre `simulacion.py` en tu editor.
2.  Busca la variable `N_PLANTAS = 1_000_000`.
3.  Cámbiala a **10,000,000** (Diez millones).
4.  Ejecuta de nuevo.

> **Pregunta:** ¿Sigue siendo lineal el aumento de tiempo? ¿Notas que tu computador se congela un instante al crear las listas de Python?

---

## 🧠 Reto de Ingeniería: Operaciones Complejas

Modifica `simulacion.py` para agregar una operación más pesada y ver si NumPy sigue ganando.

**Tu Tarea:**
Cambia la fórmula del vigor para incluir una función trigonométrica (muy costosa para la CPU).

1.  Importa math: `import math`
2.  En el bucle Python, cambia la fórmula a:
    ```python
    calculo = math.sin(alturas_list[i]) * grosores_list[i]
    ```
3.  En NumPy, usa la versión vectorizada:
    ```python
    vigor_np = np.sin(alturas_np) * grosores_np
    ```

**¿El resultado?** Verás que la diferencia de velocidad se vuelve **aún mayor**, porque NumPy optimiza funciones matemáticas complejas mejor que Python puro.