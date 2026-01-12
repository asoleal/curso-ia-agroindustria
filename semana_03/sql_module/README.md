## 1. Introducción: ¿Por qué SQL en la era de la IA?

En la semana anterior aprendiste a limpiar datos en memoria con Pandas. Pero, ¿qué pasa cuando los datos de los sensores de una finca ocupan gigabytes? ¿O cuando necesitas guardar el histórico de 5 años?

La respuesta es la **Persistencia de Datos**.

### Arquitectura del Pipeline
No usamos una sola herramienta. Usamos la mejor herramienta para cada etapa:

1.  **Ingesta (Bash):** Mueve archivos crudos a la base de datos a velocidad rayo.
2.  **Almacenamiento (SQLite):** Organiza, tipifica y guarda los datos en disco.
3.  **Análisis (Python/Pandas):** Extrae solo lo necesario para modelar o visualizar.

---

## 2. Capítulo I: SQLite (El Silo Digital)

SQLite es una base de datos ligera que no requiere servidor. Es un simple archivo (`.db`), ideal para **Edge Computing** (Raspberry Pi en el campo) o aplicaciones locales.

### Estructura de una Tabla (DDL)
Imagina una tabla de sensores. Debemos definir qué tipo de dato entra en cada columna.

```sql
CREATE TABLE sensores (
    id INTEGER PRIMARY KEY,
    zona TEXT NOT NULL,      -- Ej: 'Lote Norte'
    fecha DATETIME,
    temperatura REAL,        -- Grados Celsius
    humedad REAL             -- Porcentaje %
);
```

### Consultas Esenciales (DML)
Filtrar datos críticos (WHERE):

```sql
-- Detectar riesgo de hongos (Alta humedad + Calor)
SELECT zona, fecha
FROM sensores
WHERE humedad > 80 AND temperatura > 25;
```

Agregación (GROUP BY):

```sql
-- Promedio de temperatura por zona
SELECT zona, AVG(temperatura) as temp_promedio
FROM sensores
GROUP BY zona;
```

---

## 3. Capítulo II: Ingesta Masiva con Bash
Insertar datos fila por fila (INSERT INTO...) es lento. Los ingenieros de datos usan Bulk Loading (Carga Masiva).
En SQLite, usamos el comando .import desde la terminal.

```bash
# Script de Bash para cargar un CSV de 1 millón de filas en segundos
sqlite3 finca.db << 'EOF_SQL'
.mode csv
.import --skip 1 lecturas_campo.csv sensores
EOF_SQL
```

⚠️ Nota: El flag --skip 1 es crucial si tu CSV tiene encabezados, para evitar que el texto "temperatura" se intente guardar en una columna numérica.

---

## 4. Capítulo III: Conexión con Python
Pandas tiene una integración nativa con SQL. La regla de oro es: "Filtra en SQL, analiza en Pandas".

❌ Forma Incorrecta (Lenta): Traer toda la base de datos a la RAM y luego filtrar.

```python
# NO HAGAS ESTO CON BIG DATA
df = pd.read_sql("SELECT * FROM sensores", conn)
df = df[df['humedad'] > 80]
```

✅ Forma Correcta (Eficiente): Delegar el filtro al motor de base de datos.

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('finca.db')

query = """
    SELECT zona, fecha, humedad
    FROM sensores
    WHERE humedad > 80
"""

df = pd.read_sql(query, conn) # Solo viajan los datos útiles
```

---

## 5. Ética: Soberanía Tecnológica 🛡️
En el contexto agroindustrial rural, depender 100% de la nube (AWS/Azure) puede ser peligroso por la conectividad inestable y los costos.

¿Por qué SQLite apoya la soberanía?

- Local: Los datos viven en la finca, en el disco duro del agricultor.
- Auditable: No es una "caja negra" en un servidor extranjero.
- Portable: Copiar el archivo .db es hacer un backup completo.

Una base de datos bien diseñada no solo guarda números, protege la historia productiva de la tierra.


## 🚜 Reto Final: Sistema de Monitoreo Local

**Misión**: Crear un pipeline completo desde datos crudos hasta alertas.

### Pasos:
1. Crea un archivo `sensores.csv` con datos simulados (usa el generador de la carpeta).
2. Importa los datos a `finca.db` usando Bash.
3. Escribe una consulta SQL que identifique zonas con **humedad < 40% y temperatura > 30°C**.
4. Carga el resultado en un DataFrame con Python y guárdalo como `alertas.csv`.
5. Sube todos los archivos a tu repositorio.