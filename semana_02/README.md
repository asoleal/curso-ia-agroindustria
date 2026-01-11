# Semana 02: Fundamentos de Computación Científica para el Agro 🌱

> **Rol:** Ingeniero de Datos / AI Specialist.
> **Objetivo:** Transición de scripts básicos a sistemas escalables de alto rendimiento.
> **Tech Stack:** Python, NumPy, Vectorización (SIMD).

---

## 📋 Visión General: ¿Por qué estamos aquí?

En la Semana 01 aprendiste a escribir código. En la Semana 02 aprenderás a escribir **código que escala**.

En el mundo real (AgTech), no procesamos 10 datos; procesamos imágenes satelitales con **millones de pixeles** o series temporales de sensores IoT con **miles de lecturas por segundo**. Si usas bucles `for` tradicionales, tu servidor colapsará.

### 🎯 Tus 3 Objetivos de Ingeniería
1.  **Programación Defensiva (🛡️):** Aprender el arte de "Fail Fast". Si un sensor envía basura, el sistema debe protegerse, no explotar.
2.  **Vectorización (⚡):** Entender cómo **NumPy** usa bloques contiguos de memoria (como C/Fortran) para ser 100x más rápido que Python puro.
3.  **Lógica Espacial (📡):** Manipular matrices para simular terrenos y tomar decisiones agronómicas sin iterar manualmente.

---

## 🧠 Modelos Mentales (Teoría Esencial)

Antes de abrir el editor, necesitas visualizar cómo funciona la memoria de tu computadora.

### 1. El Costo de la Memoria (Listas vs Arrays)
* **Python List:** Son punteros dispersos. Para leerlos, la CPU tiene que "saltar" por toda la RAM. (Lento).
* **NumPy Array:** Es un bloque sólido y contiguo. La CPU lo carga de un solo golpe. (Rápido).



### 2. Complejidad Algorítmica (Big O)
* **$O(N)$ (Lineal):** Si duplicas los datos, duplicas el tiempo. (Aceptable).
* **Vectorizado (SIMD):** Procesamiento paralelo a nivel de CPU. (Ideal para IA).



---

## 📂 Estructura del Módulo

```text
semana_02/
├── 01_Fundamentos_Logica/   # [MÓDULO 1] Calidad de Software
│   └── main.py              # Laboratorio: Validaciones y Guard Clauses
├── 02_Numpy_Vectorizacion/  # [MÓDULO 2] High Performance Computing (HPC)
│   └── simulacion.py        # Benchmark: La carrera contra el bucle 'for'
├── docs/                    # [RECURSOS]
│   ├── manual02.pdf         # Profundización teórica
│   └── slides_clase.pdf     # Resumen ejecutivo
└── taller_numpy.py          # [RETO FINAL] Análisis Satelital Integrado
```
## 🛠️ Tu Hoja de Ruta (Paso a Paso)

Sigue este orden estrictamente. Cada paso construye sobre el anterior.

### 🟢 Paso 1: Blindar el Código (Lógica)
Entra en la mente de un sensor defectuoso. Aprende a usar **Guard Clauses** para limpiar tu código de `if/else` anidados.

* **Archivo:** `01_Fundamentos_Logica/main.py`
* **Misión:** Ejecuta el script, observa los fallos y completa el **Reto de Incendio** (ver instrucciones dentro del archivo).
```bash
python 01_Fundamentos_Logica/main.py
```

### 🟡 Paso 2: La Velocidad de la Luz (Vectorización)
Demostración empírica. Vamos a procesar 1 millón de plantas y verás por qué los bucles `for` están prohibidos en Big Data.



* **Archivo:** `02_Numpy_Vectorizacion/simulacion.py`
* **Misión:** Corre el benchmark, implementa el **Reto Trigonométrico** y registra el "Speedup" (veces más rápido) que lograste.
```bash
python 02_Numpy_Vectorizacion/simulacion.py
```

### 🔴 Paso 3: El Boss Final (Taller Satelital)
Integra todo. Eres el ingeniero a cargo de un lote de **10,000 m²**. Tienes un mapa de humedad, zonas inundadas y zonas secas.



* **Archivo:** `taller_numpy.py`
* **Misión:**
    1.  Generar el mapa del terreno.
    2.  Usar **máscaras booleanas** (ej. `terreno < 0.2`) para detectar sequía sin `if`.
    3.  Calcular el presupuesto hídrico usando `np.where`.
    4.  Interpretar el reporte visual en ASCII.

```bash
python taller_numpy.py
```

## ✅ Definición de Hecho (DoD)
Para considerar esta semana completada, debes tener:

1.  [ ] `main.py` modificado con la alerta de incendio.
2.  [ ] `simulacion.py` con el cálculo de `sin()` y el reporte de tiempos al final.
3.  [ ] `taller_numpy.py` ejecutado y comprendido.

**Entrega tu progreso:**

```bash
git add .
git commit -m "Semana 02: Completados laboratorios de HPC y Lógica Defensiva"
git push origin main