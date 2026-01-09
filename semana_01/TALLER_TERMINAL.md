# 🚜 Taller 1: Herramientas del Agrónomo Digital (Consola y Git)

Bienvenido. En este curso no solo aprenderás IA, aprenderás a gestionar proyectos de software profesionalmente.
Hoy dominaremos dos herramientas:
1.  **La Terminal (Bash):** Tu navaja suiza para moverte por el sistema.
2.  **Git:** Tu libro de actas o sistema de trazabilidad digital.

---

## 📍 PARTE 1: La Terminal (El Terreno)
Imagina que la terminal es el campo. Aquí damos órdenes directas sin usar el mouse.

### 1. Ubicación y Visión (`pwd`, `ls`)
* **`pwd`** (Print Working Directory): ¿En qué lote de la finca estoy parado?
* **`ls`** (List): ¿Qué cultivos o herramientas tengo aquí?
* **`ls -l`**: Muestra detalles (quién es el dueño, tamaño, fecha).

> **👨‍🌾 Ejercicio 1:**
> 1. Escribe `ls` y mira qué carpetas existen.
> 2. Escribe `ls -l` y observa la diferencia.

### 2. Desplazamiento (`cd`)
* **`cd nombre_carpeta`**: Entrar a un lote.
* **`cd ..`**: Regresar a la casa principal (atrás).
* **`cd ~`**: Ir directo al inicio (Home).

> **👨‍🌾 Ejercicio 2:**
> 1. Entra a la semana 1: `cd semana_01`
> 2. Entra a datos: `cd datos`
> 3. Verifica dónde estás: `pwd`
> 4. Vuelve al inicio del repositorio: `cd ../..` (saltamos 2 atrás).

### 3. Sembrar y Escribir (`mkdir`, `touch`, `echo`)
* **`mkdir nombre`**: Crea una carpeta nueva.
* **`touch archivo.txt`**: Crea un archivo vacío.
* **`echo "Texto" > archivo.txt`**: Crea un archivo y le escribe algo adentro inmediatamente.

> **👨‍🌾 Ejercicio 3:**
> 1. Crea una carpeta de prácticas: `mkdir practicas_campo`
> 2. Entra en ella: `cd practicas_campo`
> 3. Crea una nota rápida: `echo "Hoy llovió 20mm" > clima.txt`
> 4. Lee la nota con: `cat clima.txt`

### 4. Limpieza (`rm`)
⚠️ **PELIGRO:** Aquí no hay papelera de reciclaje.
* **`rm archivo`**: Elimina un archivo.
* **`rm -r carpeta`**: Elimina una carpeta completa.

---

## 🔗 PARTE 2: Git (Trazabilidad y Calidad)
En agroindustria, si no está documentado, no existe. **Git** es tu sistema de certificación. Nos permite guardar la historia de cada cambio.

El ciclo de vida de un cambio (El flujo de trabajo):

### 1. `git status` (La Inspección)
Te dice qué ha cambiado en tu finca desde la última vez.
* *Rojo:* Cambios sin rastrear.
* *Verde:* Cambios listos para guardarse.

### 2. `git add .` (La Cosecha)
Selecciona todos los cambios y los pone en la "caja" para ser enviados. Es decir, preparas los archivos para el registro.

### 3. `git commit -m "Mensaje"` (El Sellado)
Cierra la caja y le pone una etiqueta oficial.
* Ejemplo: `git commit -m "Agregué datos de temperatura"`
* ⚠️ El mensaje es obligatorio. Es tu bitácora.

### 4. `git push` (El Envío)
Sube tus cambios confirmados a la nube (GitHub). Es como enviar el camión al puerto.

---

## 🏆 RETO FINAL DE LA SEMANA
¡Vamos a simular un día de trabajo real! Sigue estos pasos uno por uno en tu terminal:

1.  **Prepárate:** Asegúrate de estar en la carpeta principal del proyecto.
2.  **Crea:** Genera un archivo con tu nombre: `echo "Estudiante: Juan Perez" > asistencia.txt`
3.  **Inspecciona:** Ejecuta `git status`. (Deberías ver `asistencia.txt` en rojo).
4.  **Cosecha:** Ejecuta `git add .`
5.  **Verifica:** Ejecuta `git status` de nuevo. (Ahora debería estar verde).
6.  **Registra:** Ejecuta `git commit -m "Registrando mi asistencia a la Clase 1"`.
7.  **Envía:** Ejecuta `git push`.

**✅ Si al final GitHub no te dio errores, ¡felicidades! Eres oficialmente un Agrónomo Digital.**
