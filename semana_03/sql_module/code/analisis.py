import sqlite3
import pandas as pd
import os

print("--- PYTHON CONSUMIENDO SQL ---")

# Verificar que la DB exista (creada por el script de bash)
if not os.path.exists('empresa.db'):
    print("❌ Error: Ejecuta primero 'etl_bash.sh' para crear la base de datos.")
    exit()

conn = sqlite3.connect('empresa.db')

query = """
SELECT nombre, salario, 
       CASE WHEN salario > 6000 THEN 'Alto' ELSE 'Normal' END as categoria
FROM empleados
ORDER BY salario DESC
"""

df = pd.read_sql(query, conn)
print(df)

conn.close()
