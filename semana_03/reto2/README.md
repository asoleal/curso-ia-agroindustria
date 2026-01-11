# ☕ Reto 2: La Crisis del Café (Integración de Datos)

**Rol:** Analista Financiero en la Cooperativa "Café de Altura".
**Misión:** Tenemos un problema de silos de información. Los datos de la cosecha están en el sistema del agrónomo, pero los precios de venta están en el sistema de la bolsa de valores. Tu trabajo es **unir ambas fuentes** para calcular cuánto dinero real generó cada lote de café.

## 📂 Archivos del Proyecto
* `generar_reto2.py`: Script generador de datos. **¡Ejecuta esto primero!**
* `produccion.csv`: Registro de cuántos kilos se recogieron por día y lote.
* `precios_mercado.csv`: Histórico del precio del dólar por kilo de café.
* `reto2.py`: Tu espacio de trabajo.

## 🧩 El Desafío de los Datos
Tienes dos tablas desconectadas que presentan los siguientes problemas:

1.  **Producción (`produccion.csv`):** Contiene errores humanos (alguien digitó kilos negativos).
2.  **Precios (`precios_mercado.csv`):** Tiene días vacíos (días feriados o fallos de red donde no se registró precio).
3.  **Desconexión:** Necesitamos calcular `Ingresos = Kilos * Precio`, pero los datos están en archivos separados.

## 🎯 Tus Objetivos en `reto2.py`

Edita el archivo `reto2.py` y completa los pasos:

1.  **Ingesta Inteligente:**
    * Carga ambos CSVs.
    * **Vital:** Usa `parse_dates=['fecha']` en ambos. Si no conviertes a fecha, el cruce fallará.

2.  **Limpieza Previa:**
    * **Producción:** Elimina las filas donde `kilos_recolectados` sean menores a 0.
    * **Precios:** Rellena los valores `NaN` usando el método `ffill` (Forward Fill). *Lógica:* Si hoy no hay precio, asumimos que se mantiene el de ayer.

3.  **El Gran Cruce (Merge):**
    * Une la tabla de producción con la de precios usando la columna `fecha` como llave.
    * **Estrategia:** Usa un **Left Join** (`how='left'`).
    * *¿Por qué?* Porque la tabla de producción es la mandatoria. Si cosechamos café un domingo y no hubo precio de bolsa, el registro de cosecha debe existir (aunque el precio quede pendiente), no podemos borrar el café.

4.  **Cálculo y Reporte:**
    * Crea la columna `ingreso_total` multiplicando los kilos por el precio imputado.
    * Agrupa por `id_lote` y suma los ingresos.
    * Genera un gráfico de barras comparando los lotes.

## 💡 Cheat Sheet (Ayuda Memoria)

Comandos clave para este reto:

* **Rellenar huecos con el valor anterior:**
    ```python
    df['columna'].ffill(inplace=True)
    # O la versión moderna:
    df['columna'] = df['columna'].ffill()
    ```

* **Unir dos DataFrames:**
    ```python
    # izquierda = tabla principal (produccion)
    # derecha = tabla secundaria (precios)
    resultado = pd.merge(izquierda, derecha, on='columna_comun', how='left')
    ```

## 🚀 Cómo Empezar

```bash
# 1. Generar los archivos simulados
python generar_reto2.py

# 2. Programar tu solución
python reto2.py

```