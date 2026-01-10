# 🛠️ Taller 1: Fundamentos de Ingeniería (Terminal)

## 📍 PARTE 1: Navegación
Usa `cd`, `ls` y `mkdir` para explorar.

## 🏆 RETO FINAL: "El Generador de Cultivos"
Crea un archivo llamado `deploy.sh` con este contenido:

\`\`\`bash
#!/bin/bash
echo "--- 🚜 INICIANDO DESPLIEGUE ---"
for i in {1..3}
do
    echo "Configurando Zona $i..."
    mkdir -p "zona_$i/sensores"
    cat << FIN_PYTHON > "zona_$i/sensores/main.py"
import random
print(f"📡 ZONA $i: Temp={random.uniform(20,35):.1f}")
FIN_PYTHON
done
\`\`\`
Ejecútalo con `./deploy.sh` y sube los cambios a Git.
