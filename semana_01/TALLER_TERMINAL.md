# 🛠️ Taller 1: Fundamentos de Ingeniería de Software (Terminal, Git y Scripting)

Bienvenido. En este taller dejarás de ser un usuario que solo hace "clic" para convertirte en un creador que da órdenes directas al sistema operativo. Aprenderemos a navegar, automatizar tareas y gestionar versiones de nuestro trabajo.

---

## 📍 PARTE 1: El Terreno (Navegación y Archivos)
Antes de construir, necesitamos dominar el entorno. **Regla de oro:** No uses el mouse.

### 1. Ubicación y Movimiento
* **`pwd`**: (Print Working Directory) ¿Dónde estoy parado?
* **`ls`**: (List) Muestra qué hay en la carpeta.
    * `ls -l`: Ver detalles (tamaño, permisos).
    * `ls -a`: Ver ocultos.
* **`cd carpeta`**: Entrar a una carpeta.
    * `cd ..`: Regresar atrás.
    * `cd ~`: Ir al inicio (Home).

### 2. Gestión de Archivos (Crear, Copiar, Borrar)
* **`mkdir nombre`**: Crea una carpeta.
    * `mkdir -p a/b/c`: Crea una jerarquía completa.
* **`touch archivo.txt`**: Crea un archivo vacío.
* **`cp origen destino`**: Copia archivos.
    * `cp -r carpeta destino`: Copia carpetas completas (**r**ecursivo).
* **`mv origen destino`**: Mueve o cambia el nombre.
* **`rm archivo`**: ⚠️ Borra un archivo para siempre.
    * `rm -rf carpeta`: Borra una carpeta y todo su contenido a la fuerza.

> **🧠 Práctica Rápida:**
> 1. Crea una carpeta `lab_01` y entra en ella.
> 2. Crea un archivo `experimento.txt`.
> 3. Hazle una copia de seguridad: `cp experimento.txt backup.txt`.
> 4. Borra el original: `rm experimento.txt`.

---

## 📝 PARTE 2: Edición y Manipulación (`nano`, `cat`, `sed`)
No necesitamos Word para escribir código o configuaciones.

### 1. El Editor (`nano`)
* **`nano archivo.txt`**: Abre un editor en la terminal.
    * **Guardar:** `Ctrl + O` -> `Enter`.
    * **Salir:** `Ctrl + X`.

### 2. El Visor (`cat`)
* **`cat archivo.txt`**: Muestra el contenido sin abrir el editor.

### 3. El Cirujano de Texto (`sed`)
Imagina que tienes que corregir una palabra en 1,000 líneas.
* **Sintaxis:** `sed -i 's/viejo/nuevo/g' archivo.txt`
    * `-i`: Guarda los cambios en el archivo (in-place).
    * `s`: Sustituir.
    * `g`: Global (todas las ocurrencias).

> **🧠 Práctica de Edición:**
> 1. Crea un archivo: `echo "Hola Mundo" > saludo.txt`
> 2. Usa sed para cambiarlo: `sed -i 's/Mundo/Ingeniero/g' saludo.txt`
> 3. Verifica: `cat saludo.txt` (Debería decir "Hola Ingeniero").

---

## 🤖 PARTE 3: Scripting (Automatización)
Aquí ocurre la magia. Un **Script (.sh)** es un archivo con una lista de comandos que la computadora ejecuta por ti.

### Pasos para crear un script:
1.  **Crear:** `nano programa.sh`
2.  **Cabecera:** La primera línea debe ser `#!/bin/bash`.
3.  **Permisos:** Debes hacerlo ejecutable: `chmod +x programa.sh`.
4.  **Ejecutar:** `./programa.sh`

---

## 🔗 PARTE 4: Git (Trazabilidad y Control)
Git es la bitácora de tu proyecto. Guarda la historia de cada cambio.

1.  **`git status`**: ¿Qué ha cambiado? (Rojo = sin guardar, Verde = listo).
2.  **`git add .`**: Preparar todos los cambios (La Cosecha).
3.  **`git commit -m "Mensaje"`**: Guardar la versión en el historial (El Sello).
4.  **`git push`**: Subir cambios a la nube (GitHub).

---

## 🏆 RETO INTEGRAL: "El Automatizador"
Vas a crear un script que prepare automáticamente un entorno de trabajo y luego subirás todo a GitHub.

**Paso 1: Crear el Script de Instalación**
Crea un archivo llamado `setup_proyecto.sh` con el siguiente contenido (usa `nano`):

```bash
#!/bin/bash
echo "--- 🚀 Iniciando configuración automática del entorno ---"

# 1. Crear estructura de carpetas
mkdir -p datos resultados logs
echo "✅ Carpetas creadas: datos, resultados, logs."

# 2. Generar un log de inicio
date > logs/inicio_proyecto.txt
echo "✅ Log de fecha generado."

# 3. Crear archivo de configuración base
echo "status=inactivo" > config.cfg

# 4. Activar el sistema automáticamente usando sed
sed -i 's/inactivo/ACTIVO/g' config.cfg
echo "✅ Sistema activado en config.cfg"

echo "--- 🏁 Entorno listo para trabajar ---"
