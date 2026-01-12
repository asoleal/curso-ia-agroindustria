#!/bin/bash

# Limpieza inicial
rm -f finca.db
echo "🗑️  Base de datos limpia."

# 1. Crear la Tabla (DDL)
# Definimos los tipos correctamente para que SQL entienda los números
sqlite3 finca.db "CREATE TABLE lecturas (
    id INTEGER PRIMARY KEY,
    fecha TEXT,
    zona TEXT,
    temperatura REAL,
    humedad REAL,
    ph REAL
);"
echo "🏗️  Tabla 'lecturas' creada."

# 2. Importar el CSV (ETL)
# IMPORTANTE: Usamos --skip 1 para saltar la fila de encabezados del CSV
echo "📥 Importando datos..."
sqlite3 finca.db <<CMD
.mode csv
.import --skip 1 lecturas_campo.csv lecturas
CMD

# 3. Validación
echo "✅ Registros importados:"
sqlite3 finca.db "SELECT count(*) FROM lecturas;"
