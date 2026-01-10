# 🛠️ Taller 1: Fundamentos de Ingeniería de Software (Terminal, Git y Scripting)

Bienvenido. En este taller dejarás de ser un usuario que solo hace "clic" para convertirte en un creador que da órdenes directas al sistema operativo. Aprenderemos a navegar, automatizar tareas y gestionar versiones.

---

## 📍 PARTE 1: El Terreno (Navegación y Archivos)
**Regla de oro:** No uses el mouse.

### 1. Ubicación y Movimiento
* **`pwd`**: ¿Dónde estoy?
* **`ls -l`**: Listar archivos con detalles.
* **`cd carpeta`**: Entrar a una carpeta (`cd ..` para salir).

### 2. Gestión Básica
* **`mkdir -p a/b/c`**: Crea carpetas anidadas.
* **`touch archivo`**: Crea archivo vacío.
* **`cp -r origen destino`**: Copia carpetas.
* **`mv origen destino`**: Mueve o renombra.
* **`rm -rf carpeta`**: ⚠️ Borra carpeta y contenido a la fuerza.

---

## 📝 PARTE 2: Edición y Manipulación

### 1. El Editor (`nano`)
* **`nano script.py`**: Abre el editor. `Ctrl+O` (Guardar), `Ctrl+X` (Salir).

### 2. El Cirujano (`sed`)
* **`sed -i 's/viejo/nuevo/g' archivo.txt`**: Reemplaza texto en un archivo automáticamente.

### 3. Escritura en Bloque (`cat`) 🔥 *Nivel Pro*
¿Cómo crear un archivo con muchas líneas sin abrir nano? Usamos un "Heredoc".

Ejemplo:
\`\`\`bash
cat << EOF > mensaje.txt
Linea 1: Hola
Linea 2: Esto se escribió automático
EOF
\`\`\`
*Todo lo que escribas entre los dos `EOF` se guardará en el archivo.*

---

## 🤖 PARTE 3: Scripting (Bucles y Automatización)
Un script `.sh` automatiza tareas repetitivas. Vamos a aprender a usar **bucles** para repetir acciones.

**La lógica del bucle `for`:**
\`\`\`bash
for i in {1..5}
do
   echo "Repetición número $i"
done
\`\`\`

---

## 🔗 PARTE 4: Git (Guardar en la nube)
1. `git add .` (Preparar)
2. `git commit -m "Mensaje"` (Guardar)
3. `git push` (Subir)

---
## PARTE 5:📝 Gestión de Archivos

Vamos a manipular ese archivo de datos.

### a. Lectura de Archivos (El CSV perdido)
Encontramos un archivo `produccion_lote.csv`. Vamos a leerlo desde la terminal.
* **`cat datos/produccion_lote.csv`**: Imprime todo el contenido en pantalla.
* **`head -n 2 datos/produccion_lote.csv`**: Muestra solo las primeras 2 líneas (útil para archivos gigantes).

### b. Copias de Seguridad (`cp`)
Imagina que vas a procesar los datos, pero no quieres dañar el original. Hagamos un backup.
* **`cp datos/produccion_lote.csv datos/backup_lote.csv`**: Crea una copia exacta.
* Comprueba con `ls datos/` que ahora existan dos archivos.

### c. Organización (`mkdir` y `mv`)
Vamos a crear una carpeta para los respaldos y mover el archivo ahí.
* **`mkdir respaldos`**: Crea la carpeta.
* **`mv datos/backup_lote.csv respaldos/`**: Mueve el archivo dentro de la nueva carpeta.

### d. Limpieza (`rm`)
El jefe dice que el respaldo ya no es necesario.
* **`rm -rf respaldos`**: ⚠️ Borra la carpeta y todo lo que tenga dentro. ¡Cuidado con este comando!

---

## 📝 PARTE 6: Edición y Automatización

### 1. El Editor (`nano`)
* **`nano notas.txt`**: Escribe una nota rápida sobre lo que has aprendido hoy. `Ctrl+O` (Guardar), `Ctrl+X` (Salir).

### 2. Escritura Automática (`cat` + Redirección)
Crearemos un archivo de configuración sin abrir el editor.
\`\`\`bash
cat << EOF > config.env
MODO=PRODUCCION
DB_HOST=localhost
EOF
\`\`\`

---
## 🏆 RETO FINAL: "El Generador de Cultivos"

**Misión:** Eres el ingeniero encargado de configurar 3 zonas de monitoreo. No vas a crear las carpetas y códigos a mano. Harás un script que lo haga por ti.

**PASO 1: Crea el script maestro**
Crea un archivo `deploy.sh` usando `nano` y escribe este código exacto:

\`\`\`bash
#!/bin/bash

echo "--- 🚜 INICIANDO DESPLIEGUE AUTOMÁTICO ---"

# Bucle para crear 3 zonas (Zona 1, Zona 2, Zona 3)
for i in {1..3}
do
    echo "Configurando Zona $i..."
    
    # 1. Crear carpeta iterativa
    mkdir -p "zona_$i/sensores"
    
    # 2. Crear un script de Python DENTRO de esa carpeta usando CAT
    # Fíjate cómo inyectamos la variable $i dentro del código Python
    cat << FIN_PYTHON > "zona_$i/sensores/main.py"
import random

def leer_sensor():
    temperatura = random.uniform(20, 35)
    humedad = random.uniform(40, 80)
    print(f"📡 ZONA $i reportando: Temp={temperatura:.1f}°C, Hum={humedad:.1f}%")

if __name__ == "__main__":
    leer_sensor()
FIN_PYTHON

done

echo "--- ✅ DESPLIEGUE TERMINADO ---"
echo "Prueba ejecutando: python zona_1/sensores/main.py"
\`\`\`

**PASO 2: Ejecuta y Prueba**
1. Dale permisos: `chmod +x deploy.sh`
2. Ejecuta el generador: `./deploy.sh`
3. Verifica las carpetas y prueba el código Python generado.

**PASO 3: Sube tu tarea**
Usa Git para subir el script y las carpetas al repositorio.
