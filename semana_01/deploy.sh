#!/bin/bash
# deploy.sh - Automatización de Infraestructura de Sensores
# Curso de Ingeniería de IA - Semana 01

echo "--- 🚜 INICIANDO DESPLIEGUE AGRÍCOLA ---"

# Bucle para simular 3 zonas de cultivo
for i in {1..3}
do
    echo "Creating infrastructure for Zone $i..."
    mkdir -p "zona_$i/sensores"
    
    # Heredoc: Generación dinámica de código Python
    cat << FIN > "zona_$i/sensores/main.py"
import random
import time

# Simulacion de sensor IoT
id_zona = $i
temp = random.uniform(20.0, 35.0)
hum = random.uniform(40.0, 80.0)

print(f"[ZONA {id_zona}] Reporte:")
print(f"   Temperatura: {temp:.2f} C")
print(f"   Humedad:     {hum:.1f} %")
FIN

    echo "✅ Zona $i configurada."
done

echo "--- DESPLIEGUE COMPLETADO ---"
