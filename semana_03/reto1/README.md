# 🚜 Reto 1: Auditoría Climática "La Finca"

**Rol:** Data Scientist Junior en AgroTech Solutions.
**Misión:** La estación meteorológica automatizada de nuestra finca experimental ha sufrido fallos críticos. El agrónomo necesita un reporte confiable del clima de 2024, pero los datos actuales son un desastre. Tu trabajo es limpiarlos.

## 📂 Archivos del Proyecto
* `generar_dataset.py`: Script que simula la estación fallando. **¡Ejecuta esto primero!**
* `clima_corrupto.csv`: El archivo de datos sucio (generado por el script anterior).
* `main.py`: Tu espacio de trabajo. Aquí escribirás tu código.

## 🐛 Errores Reportados (Bugs a Cazar)
El ingeniero de hardware ha identificado 4 tipos de fallas en los sensores. Debes corregirlas todas:

| Nombre del Error | Síntoma en los Datos | Causa Probable | Acción Requerida |
| :--- | :--- | :--- | :--- |
| **Fiebre del Sensor** | Temperatura marca picos de **200°C**. | Cortocircuito momentáneo. | Reemplazar valores > 50°C por `NaN`. |
| **Lluvia Congelada** | El valor de lluvia se repite exacto (ej: 12.5) por horas. | Mecanismo trabado. | Detectar si `diff() == 0` y el valor es `> 0`. Anular esos datos. |
| **Humedad Imposible** | Valores negativos o mayores a 100%. | Descalibración. | Convertir a `NaN` cualquier valor fuera de 0-100. |
| **Apagón de Octubre** | Faltan días completos de registros. | Batería agotada. | El `resample` diario debe encargarse de llenar el eje temporal. |

## 🎯 Tus Objetivos en `main.py`

Edita el archivo `main.py` y completa los bloques `TODO` siguiendo estos pasos:

1.  **Ingesta de Datos:**
    * Carga el CSV `clima_corrupto.csv`.
    * **Ojo:** El archivo usa punto y coma (`;`) como separador.
    * Asegúrate de que la columna de fecha sea interpretada como objeto `datetime`.

2.  **Limpieza (Cleaning):**
    * Aplica las reglas de la tabla de arriba para limpiar Temperatura, Lluvia y Humedad.
    * Usa `df.loc[]` para filtrar y asignar `pd.NA`.

3.  **Transformación (Resampling):**
    * Los datos están hora por hora. Conviértelos a **Diarios**.
    * **Temperatura:** Calcula el promedio (`mean`).
    * **Lluvia:** Calcula el acumulado total (`sum`).

4.  **Visualización:**
    * Genera un gráfico que muestre la temperatura limpia y la lluvia acumulada por día.

## 🚀 Cómo Empezar

Abre tu terminal en la carpeta del proyecto y ejecuta:

```bash
# 1. Instalar librerías necesarias
pip install pandas matplotlib

# 2. Generar el archivo de datos sucio
python generar_dataset.py

# 3. Ejecutar tu solución (haz esto cada vez que hagas un cambio)
python main.py
```
¡Buena suerte salvando la cosecha! 🌱