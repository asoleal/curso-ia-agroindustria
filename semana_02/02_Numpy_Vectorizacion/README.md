# Módulo 2: Computación de Alto Rendimiento (HPC) con NumPy ⚡

> **Concepto Central:** Vectorización (SIMD) vs. Iteración Escalar.
> **Objetivo:** Demostrar empíricamente por qué los bucles `for` están prohibidos en Big Data.

---

## 📖 Introducción Técnica: La Arquitectura de Memoria

En Ingeniería de Datos, la velocidad no depende solo del procesador, sino del **acceso a memoria**.

1.  **Listas de Python (Lentas):** Son colecciones de *punteros* a objetos dispersos en la memoria RAM. Para sumar dos números, la CPU debe "buscar" las direcciones, verificar tipos y luego operar. Esto genera *Cache Misses*.
2.  **Arrays de NumPy (Rápidos):** Son bloques **contiguos** de memoria (como en C o Fortran). La CPU carga bloques enteros en su caché y usa instrucciones **SIMD** (Single Instruction, Multiple Data) para operar en paralelo.

---

## 🧪 El Experimento: Benchmark (`simulacion.py`)

Realizaremos una prueba de estrés procesando **1,000,000 de registros** de plantas simuladas.

### El Escenario
Calculamos el "Índice de Vigor" para un cultivo masivo usando la fórmula:
$$Vigor = (Altura \times Grosor) + 0.5$$

### Los Contendientes
* **Enfoque 1 (Nativo):** Listas estándar + Bucle `for`. (Complejidad $O(N)$ con alto overhead).
* **Enfoque 2 (Vectorizado):** Arrays de NumPy + Operación Matricial. (Backend en C optimizado).

---

## ⚙️ Instrucciones de Ejecución

Desde la terminal, ubicado en la raíz del proyecto (`semana_02`), ejecuta:

```bash
python simulacion.py