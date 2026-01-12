# 🌾 Taller Práctico: Sistema de Alerta Temprana

**Rol:** Ingeniero de Datos en "AgroFuture"  
**Misión:** Los sensores de los lotes de café han estado enviando datos durante todo el mes. Tu trabajo es consolidar esos datos en una base de datos segura y generar un reporte de riesgos.

---

## 📂 Archivos del Taller

- `generar_sensores.py`: Script que debes ejecutar para crear los datos sucios.  
- `lecturas_campo.csv`: Archivo generado que simula la salida de los sensores.  
- `ingesta.sh` (o comandos en terminal): Tu solución para cargar datos.  
- `analisis.py`: Tu solución para analizar y reportar riesgos.

---

## 📝 Paso 1: Generación de Datos (El Caos)

Ejecuta el generador para crear el archivo CSV crudo que simula lo que envían los sensores.

```bash
python generar_sensores.py
```

Esto creará el archivo `lecturas_campo.csv` con aproximadamente **1500 registros**.

---

## 📝 Paso 2: Ingesta con Bash y SQL (El Orden)

**Regla:** No uses Python para este paso. Utiliza la potencia de la terminal y SQLite nativo.

### Objetivo
Crear una base de datos llamada `finca.db` e importar los datos del CSV.

### Esquema de la tabla

- `id` (INTEGER)  
- `fecha` (TEXT)  
- `zona` (TEXT)  
- `temperatura` (REAL)  
- `humedad` (REAL)  
- `ph` (REAL)

### Importación del CSV

- Usa el comando `.import` de `sqlite3`.
- **Ojo:** El CSV tiene encabezados. Investiga cómo ignorar la primera línea (`--skip 1`) o elimina el encabezado antes de importar.

---

## 📝 Paso 3: Análisis de Riesgo (La Inteligencia)

Crea un script en Python llamado `analisis.py` que realice las siguientes tareas:

1. Conectarse a `finca.db` usando `sqlite3`.
2. Ejecutar una consulta SQL (`SELECT`) para extraer solo los registros con **Riesgo de Hongo**.

**Regla de negocio:**  
Riesgo = Humedad > 70% **y** Temperatura > 20 °C.

3. Cargar los datos filtrados en un `DataFrame` de **Pandas**.
4. Agrupar por `zona` y contar cuántas alertas existen.
5. Exportar el resumen a un archivo `reporte_alertas.csv`.

---

## 🏆 Bonus (Opcional)

Si terminas rápido:

- Investiga cómo crear un índice en la columna `zona` usando SQL:
  ```sql
  CREATE INDEX idx_zona ON lecturas(zona);
  ```
- Agrega una columna calculada en Python llamada **Nivel de Riesgo** (`Alto` / `Medio`)  
  y guarda esta información nuevamente en la base de datos.

---

✅ **Objetivo final:** construir un flujo completo de **ingesta → limpieza → análisis → reporte**, tal como se hace en proyectos reales de datos agroambientales.
