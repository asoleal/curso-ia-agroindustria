echo "🔍 Verificando Taller 01..."

function check_ejercicio1() {
  if [ -d "data/raw" ] && [ -d "data/processed" ] && [ -d "scripts" ] && [ -d "reports" ] && [ -f "data/raw/sensores.csv" ]; then
    echo "✅ Ejercicio 1: Estructura OK"
  else
    echo "❌ Ejercicio 1: Falta alguna carpeta o sensores.csv"
    exit 1
  fi
}
