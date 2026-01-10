#!/bin/bash
# REFERENCE: Solución Semana 01
for i in {1..3}; do
    mkdir -p "zona_$i/sensores"
    echo "print('Zona $i OK')" > "zona_$i/sensores/main.py"
done
