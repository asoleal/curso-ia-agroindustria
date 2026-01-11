# Semana 02: Fundamentos de Computación Científica para el Agro 🌱

> **Curso:** Inteligencia Artificial Aplicada al Agro
> **Enfoque:** Ingeniería de Software, Lógica Algorítmica y Vectorización (NumPy)

---

## 📋 Visión General

En esta semana dejamos atrás la programación básica de scripts para adentrarnos en la **Ingeniería de Datos**. El objetivo no es solo que el código funcione, sino que sea **eficiente** y capaz de escalar a millones de datos (Big Data).

### Objetivos de Aprendizaje
1.  **Lógica Defensiva:** Validar datos de sensores antes de procesarlos.
2.  **Complejidad Computacional:** Entender por qué los bucles `for` son el enemigo en Python.
3.  **Vectorización:** Usar **NumPy** para procesar matrices de cultivos y datos satelitales.

---

## 📂 Estructura del Proyecto

```text
semana_02/
├── 01_Fundamentos_Logica/
│   └── main.py              # Validación de sensores (Lógica Booleana)
├── 02_Numpy_Vectorizacion/
│   └── simulacion.py        # Benchmark: Listas vs. NumPy (Prueba de velocidad)
├── docs/
│   ├── manual02.pdf         # Teoría: Matemáticas y Gestión de Memoria
│   └── slides_clase.pdf     # Presentación ejecutiva
└── taller_numpy.py          # RETO FINAL: Análisis satelital de terreno
```
# 🛠️ Instrucciones

Sigue este orden lógico para completar las actividades de la semana:

### 1. Carpeta `docs/` (Teoría)
Antes de tocar el código, necesitamos base teórica.
**Actividad**: Lee el archivo `manual02.pdf`.
**Objetivo**: Entender la diferencia en memoria RAM entre una **Lista** (punteros dispersos) y un **Array** (bloque contiguo), y qué significa la notación **"Big O"** ($O(N)$ vs $O(1)$).

### 2. Carpeta `01_Fundamentos_Logica/` (Calidad de Código)
Aquí aprenderás a escribir código robusto que no se rompe con datos malos.
**Comando**:
```bash
python 01_Fundamentos_Logica/main.py
```

### 3. Carpeta `02_Numpy_Vectorizacion/` (Rendimiento)
La demostración de por qué NumPy es el rey en IA.
* **Comando:** `python 02_Numpy_Vectorizacion/simulacion.py`
* **Actividad:**
    1. Ejecuta el benchmark.
    2. Compara los tiempos en consola.
    3. **Reflexión:** Verifica que NumPy sea al menos 50 veces más rápido que el método tradicional. Esto te enseñará a nunca usar bucles `for` para cálculos matemáticos masivos.

### 4. Archivo Raíz `taller_numpy.py` (Reto Final)
Aplicación de todo lo aprendido en un escenario satelital simulado.
* **Comando:** `python taller_numpy.py`
* **Actividad:**
    1. Ejecuta la simulación del terreno de 10,000 $m^2$.
    2. Analiza el reporte de daños generado.
    3. Revisa el código para entender cómo se usaron **Máscaras Booleanas** (ej. `terreno < 0.2`) para filtrar datos sin usar condicionales `if`.

---

## ✅ Entregable Final
Una vez completados los pasos anteriores, sube tu trabajo al repositorio para registrar tu avance:

```bash
git add .
git commit -m "Semana 02: Completado laboratorio de lógica y vectorización"
git push origin main
