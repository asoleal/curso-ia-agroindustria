# 🚀 Taller 01: Supervivencia en la Terminal

**Objetivo:** Dominar navegación, archivos y pipelines básicos para procesar datos de sensores agrícolas.

**Duración estimada:** 45 minutos

## 📋 Instrucciones

1. **Abre la terminal** en el directorio `talleres/01_terminal/`
2. **Lee cada ejercicio COMPLETO** antes de ejecutar comandos
3. **Ejecuta `./check_01.sh`** después de cada sección para validar
4. **¡IMPORTANTE!** Haz commit al final para desbloquear el Taller 02

## 📊 Dataset


Crea el archivo: `sensores.csv` de tal forma que contenga 1000 mediciones de 4 sensores en una finca:

```text

id_sensor,fecha,temperatura,humedad,pH_suelo
SENSOR_01,2026-01-01 08:00,24.5,65.2,6.8
SENSOR_02,2026-01-01 08:05,25.1,68.4,6.9
```
---

## 🚀 Ejercicio 1: Estructura del Proyecto

Crea la estructura básica de carpetas para un proyecto de datos:

```bash
# 1. Crea las carpetas necesarias
mkdir -p data/{raw,processed} scripts reports

# 2. Copia el dataset a raw
cp sensores.csv data/raw/sensores.csv

# 3. Verifica que todo esté correcto
ls -lh data/
```
✅ Verifica:

```bash
./check_01.sh ejercicio1

```

## 🚀 Ejercicio 2: Exploración Inicial
Analiza el dataset sin abrirlo en un editor:

```bash
cd data/raw

# 1. Cuenta total de registros
wc -l sensores.csv

# 2. Primeras 5 líneas
head -5 sensores.csv

# 3. Últimas 5 líneas
tail -5 sensores.csv

# 4. Tamaño del archivo
du -sh sensores.csv

```
Pregunta: ¿Cuántos registros hay? ¿Cuántos sensores únicos?

✅ Verifica:

```bash
./check_01.sh ejercicio2
```

## 🚀 Ejercicio 3: Pipeline de Conteo
Cuenta cuántos registros hay por cada sensor:

```bash
cd data/raw

# Pipeline completo en UNA LÍNEA:
cut -d',' -f1 sensores.csv | sort | uniq -c | sort -nr
```

```text
Salida esperada
    250 SENSOR_04
    250 SENSOR_03
    250 SENSOR_02
    250 SENSOR_01
```

✅ Verifica:

```bash
./check_01.sh ejercicio3
```

## 🚀 Ejercicio 4: Procesamiento con awk
Realiza cálculos estadísticos y guarda alertas:

```bash
cd data/raw

# 1. Temperatura promedio
awk -F',' '{s+=$3} END {print "Temperatura promedio:", s/NR}' sensores.csv

# 2. Humedad máxima
awk -F',' 'NR>1 {if($4>max) max=$4} END {print "Humedad máxima:", max}' sensores.csv

# 3. Guardar alertas (humedad > 80)
awk -F',' 'NR>1 && $4 > 80 {print $0}' sensores.csv > ../reports/alertas_humedad.csv

```

✅ Verifica:
```bash
./check_01.sh ejercicio4

```
## 🚀 Ejercicio 5: Pipeline Completo
Crea un reporte rápido de calidad de datos:

```bash
cd data/raw

# Pipeline: líneas vacías + caracteres raros + estadísticas
echo "=== REPORTE DE CALIDAD ===" > ../../reports/reporte_calidad.txt
echo "Total registros: $(wc -l < sensores.csv)" >> ../../reports/reporte_calidad.txt
grep ",," sensores.csv | wc -l >> ../../reports/reporte_calidad.txt
echo "Sensores únicos:" >> ../../reports/reporte_calidad.txt
cut -d',' -f1 sensores.csv | sort | uniq -c | sort -nr >> ../../reports/reporte_calidad.txt
```
✅ Verifica:
```bash
./check_01.sh ejercicio5

```
🎉 ¡Taller Completado!
Ejecuta la validación final:

```bash
./check_01.sh final

```
Si todo sale ✅, ¡felicidades! Has dominado los fundamentos de terminal para ciencia de datos.

## 🔒 Commit Obligatorio (para desbloquear Taller 02)
```bash
cd ../..  # Volver a la raíz del proyecto
git add talleres/01_terminal/
git commit -m "T01: completa taller terminal - estructura, pipelines y awk"

```

## ❓ ¿Dudas?
Abre un Issue en el repo

Revisa soluciones/ejemplo_01.md (solo si estás atascado)

Pregunta en clase

¡Siguiente: Taller 02 - Git como Bitácora Científica! 🚀


## 2. `talleres/01_terminal/check_01.sh`

```bash
#!/bin/bash

echo "🔍 Verificando Taller 01..."

function check_ejercicio1() {
  if [ -d "data/raw" ] && [ -d "data/processed" ] && [ -d "scripts" ] && [ -d "reports" ] && [ -f "data/raw/sensores.csv" ]; then
    echo "✅ Ejercicio 1: Estructura OK"
  else
    echo "❌ Ejercicio 1: Falta alguna carpeta o sensores.csv"
    exit 1
  fi
}

function check_ejercicio2() {
  cd data/raw
  if [ "$(wc -l < sensores.csv)" -eq 1001 ]; then  # 1 header + 1000 datos
    echo "✅ Ejercicio 2: Conteo correcto (1001 líneas)"
  else
    echo "❌ Ejercicio 2: Conteo incorrecto"
    exit 1
  fi
  cd ../..
}

function check_ejercicio3() {
  RESULT=$(cd data/raw && cut -d',' -f1 sensores.csv | sort | uniq -c | sort -nr | head -1 | awk '{print $1}')
  if [ "$RESULT" = "250" ]; then
    echo "✅ Ejercicio 3: Pipeline correcto (250 registros por sensor)"
  else
    echo "❌ Ejercicio 3: Pipeline incorrecto"
    exit 1
  fi
}

function check_ejercicio4() {
  if [ -f "data/reports/alertas_humedad.csv" ] && [ "$(wc -l < data/reports/alertas_humedad.csv)" -gt 0 ]; then
    echo "✅ Ejercicio 4: Alertas guardadas correctamente"
  else
    echo "❌ Ejercicio 4: No se creó alertas_humedad.csv o está vacío"
    exit 1
  fi
}

function check_ejercicio5() {
  if [ -f "data/reports/reporte_calidad.txt" ]; then
    LINES=$(wc -l < data/reports/reporte_calidad.txt)
    if [ "$LINES" -ge 5 ]; then
      echo "✅ Ejercicio 5: Reporte completo generado"
    else
      echo "❌ Ejercicio 5: Reporte incompleto"
      exit 1
    fi
  else
    echo "❌ Ejercicio 5: No existe reporte_calidad.txt"
    exit 1
  fi
}

function check_final() {
  check_ejercicio1
  check_ejercicio2
  check_ejercicio3
  check_ejercicio4
  check_ejercicio5
  echo "🎉 ¡TALLER 01 COMPLETADO CORRECTAMENTE!"
}

case "$1" in
  ejercicio1) check_ejercicio1 ;;
  ejercicio2) check_ejercicio2 ;;
  ejercicio3) check_ejercicio3 ;;
  ejercicio4) check_ejercicio4 ;;
  ejercicio5) check_ejercicio5 ;;
  final) check_final ;;
  *) echo "Uso: ./check_01.sh [ejercicio1|ejercicio2|ejercicio3|ejercicio4|ejercicio5|final]"; exit 1 ;;
esac

```
# 3. talleres/01_terminal/sensores.csv
```text
id_sensor,fecha,temperatura,humedad,pH_suelo
SENSOR_01,2026-01-01 08:00:00,24.5,65.2,6.8
SENSOR_02,2026-01-01 08:05:00,25.1,68.4,6.9
SENSOR_03,2026-01-01 08:10:00,23.8,72.1,7.0
SENSOR_04,2026-01-01 08:15:00,26.2,59.8,6.7
SENSOR_01,2026-01-01 08:20:00,24.9,67.3,6.9
SENSOR_02,2026-01-01 08:25:00,25.4,85.2,6.8
SENSOR_03,2026-01-01 08:30:00,24.1,63.9,7.1
SENSOR_04,2026-01-01 08:35:00,25.8,78.4,6.6

```
(Genera 1000 filas similares para el CSV real)

# 4. Hacer ejecutable
```bash
chmod +x talleres/01_terminal/check_01.sh
```