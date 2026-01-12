#!/bin/bash

echo "--- 1. INICIANDO ETL CON BASH ---"
DB_NAME="empresa.db"

# Limpiar ejecución anterior
rm -f $DB_NAME

echo "--- 2. CREANDO ESTRUCTURA SQL ---"
sqlite3 $DB_NAME "CREATE TABLE empleados (id INTEGER PRIMARY KEY, nombre TEXT, salario REAL);"

echo "--- 3. GENERANDO DATOS RAW (CSV) ---"
echo "Carlos,5000" > nuevos_empleados.csv
echo "Ana,6200" >> nuevos_empleados.csv
echo "Luis,4800" >> nuevos_empleados.csv

echo "--- 4. IMPORTANDO A SQLITE ---"
# Importación mágica de SQLite
sqlite3 $DB_NAME <<SQL_CMD
.mode csv
.import nuevos_empleados.csv empleados
SQL_CMD

echo "--- 5. VERIFICACIÓN ---"
sqlite3 $DB_NAME "SELECT * FROM empleados;"
echo "--- FIN ---"
