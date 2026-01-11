# 🐍 Semana 03: Domando Datos con Pandas

¡Bienvenidos a la tercera semana! En este módulo dejaremos de jugar con datos de juguete y nos enfrentaremos a **problemas reales** de ingeniería: sensores rotos, fechas mal formateadas y bases de datos desconectadas.

**Objetivo:** Pasar de datos "sucios" (Raw Data) a información valiosa (Insights) usando `pandas` y `matplotlib`.

---

## 🛠️ Configuración Inicial

Antes de empezar, asegúrate de tener las librerías necesarias e instalar las dependencias.

```bash
pip install pandas matplotlib
```
### 🚜 Reto 1: Auditoría Climática (Limpieza)
Rol: Data Scientist Junior en AgroTech Solutions.

Misión: La estación meteorológica "La Finca" se ha vuelto loca. Tu trabajo es limpiar el dataset para que el agrónomo pueda tomar decisiones.

#### 1. Preparación
Ejecuta el generador para crear el archivo sucio:

```Bash
python generar_dataset.py
# Esto creará el archivo 'clima_corrupto.csv' ingresa al archivo y lo entiendes
```
#### 2. Los Bugs a Cazar 🐛
El ingeniero de campo reportó los siguientes fallos en los sensores:
```text

Bug,Síntoma,Causa Probable,Acción Requerida

Fiebre del Sensor,Temp > 50°C (picos de 200°C),Ruido eléctrico,Convertir a NaN.

Lluvia Congelada,Valor idéntico por horas (ej. 12.5mm),Sensor trabado,Detectar diff() == 0 y anular.

Agujeros Negros,Faltan días en Octubre,Apagón del sistema,Resample rellenará el eje X.

Humedad Imposible,< 0% o > 100%,Descalibración,Filtrar y anular.
```
### 3. Tus Tareas en `main.py`
1.  **Ingesta:** Carga el CSV (¡Ojo con el separador `;`!).
2.  **Limpieza:** Aplica las correcciones de la tabla anterior.
3.  **Agregación:** Convierte los datos horarios a **Diarios** (Temp → Promedio, Lluvia → Suma).
4. **Visualización:** Grafica los datos limpios y **guarda la imagen como `clima_limpio.png`**.
---

## ☕ Reto 2: La Crisis del Café (Merge & Join)

**Rol:** Analista Financiero en Cooperativa "Café de Altura".
**Misión:** Unir los datos de producción (campo) con los precios de bolsa (finanzas) para calcular la rentabilidad real.

### 1. Preparación
Ejecuta el generador:
```bash
python generar_reto2.py
# Esto creará 'produccion.csv' y 'precios_mercado.csv'
```

### 2. Tus Tareas en `reto2.py`
1.  **Limpieza:** Elimina kilos negativos y rellena precios faltantes usando el precio del día anterior (`df.ffill()`).
2.  **El Cruce (Merge):** Une ambas tablas usando la **fecha** como llave.
    * *Nota:* No pierdas días de cosecha solo porque no hubo cotización de bolsa ese día (`how='left'`).
3.  **Analytics:** Calcula `Ingresos = Kilos * Precio` y dinos qué lote fue el más rentable.

---

## 💡 Cheat Sheet (Ayuda Memoria)

Si te atascas, recuerda estos comandos del manual:

* **Leer CSV raro:** `pd.read_csv('archivo.csv', sep=';', parse_dates=['fecha'])`
* **Filtrar y reemplazar:** `df.loc[df['columna'] > 100, 'columna'] = pd.NA`
* **Diferencia entre filas:** `df['columna'].diff()`
* **Rellenar hacia adelante:** `df.fillna(method='ffill')`
* **Unir tablas:** `pd.merge(tabla1, tabla2, on='columna_comun', how='left')`
* **Guardar gráfico:** `plt.savefig('archivo.png')`

## ✅ Entregable Final

Sube tu trabajo al repositorio para registrar tu avance:

```bash
git add semana_03/
git commit -m "Semana 03: Domando datos reales con Pandas"
git push origin main
```

¡Buena suerte, ingenieros! 🚀