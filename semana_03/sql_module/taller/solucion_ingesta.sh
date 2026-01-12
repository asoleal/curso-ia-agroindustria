#!/bin/bash

# --- PASO 1: Limpieza ---
# Borramos la DB anterior para evitar duplicados si corremos el script dos veces
rm -f finca.db
echo "🗑️  Base de datos anterior eliminada."

# --- PASO 2: Crear Estructura (DDL) ---
echo "🏗️  Creando tabla 'lecturas'..."
sqlite3 finca.db "CREATE TABLE lecturas (
    id INTEGER PRIMARY KEY,
    fecha TEXT,
    zona TEXT,
    temperatura REAL,
    humedad REAL,
    ph REAL
);"

# --- PASO 3: Ingesta (ETL) ---
echo "📥 Importando CSV..."
# Usamos --skip 1 para saltar la fila de encabezados del CSV
sqlite3 finca.db <<CMD
.mode csv
.import --skip 1 lecturas_campo.csv lecturas
CMD

# --- PASO 4: Verificación ---
echo "✅ Ingesta terminada. Total de filas:"
sqlite3 finca.db "SELECT count(*) FROM lecturas;"
