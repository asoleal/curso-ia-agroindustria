# 🏋️ Entrenamiento Básico: Gestión de Archivos y Directorios

En este taller dominaremos los 4 movimientos fundamentales del sistema operativo.
**Regla de oro:** No uses el mouse.

---

## 1. CREACIÓN (`mkdir` y `touch`)
Cómo crear estructuras desde la nada.

* **`mkdir nombre`**: Crea una carpeta (Make Directory).
* **`mkdir -p a/b/c`**: Crea una ruta completa de carpetas una dentro de otra (Parents).
* **`touch archivo.txt`**: Crea un archivo vacío instantáneamente.

> **👉 PRÁCTICA 1:**
> 1. Asegúrate de estar en `semana_01`: `cd semana_01` (o verifica con `pwd`).
> 2. Crea una carpeta llamada `laboratorio`: `mkdir laboratorio`
> 3. Entra en ella: `cd laboratorio`
> 4. Crea una estructura profunda para organizar materias:
>    `mkdir -p universidad/semestre1/matematicas`
> 5. Crea un archivo vacío dentro de esa carpeta final:
>    `touch universidad/semestre1/matematicas/notas.txt`
> 6. Verifica todo el árbol visualmente (si tienes el comando `tree`) o navegando.

---

## 2. COPIADO (`cp`)

Cómo duplicar información (Backup).

* **`cp archivo_origen destino`**: Copia un archivo.
* **`cp -r carpeta_origen destino`**: Copia una carpeta **y todo su contenido** (Recursive). **¡Importante el -r!**

> **👉 PRÁCTICA 2:**
> (Seguimos dentro de `laboratorio`)
> 1. Crea un archivo de prueba: `touch reporte_final.txt`
> 2. Haz una copia de seguridad: `cp reporte_final.txt reporte_final_backup.txt`
> 3. Verifica que ahora tienes dos archivos idénticos con `ls`.
> 4. Intenta copiar la carpeta `universidad` a una llamada `universidad_backup`.
>    *Intento fallido:* `cp universidad universidad_backup` (Te dará error).
>    *Intento correcto:* `cp -r universidad universidad_backup`

---

## 3. MOVIMIENTO Y RENOMBRADO (`mv`)
En Linux, "Mover" y "Cambiar nombre" son el mismo comando.

* **`mv archivo ruta_nueva`**: Mueve el archivo a otro lugar.
* **`mv nombre_viejo nombre_nuevo`**: Le cambia el nombre (se "mueve" sobre sí mismo).

> **👉 PRÁCTICA 3:**
> 1. Vamos a cambiar el nombre del backup:
>    `mv reporte_final_backup.txt reporte_respaldo_2024.txt`
> 2. Vamos a mover ese respaldo adentro de la carpeta `universidad`:
>    `mv reporte_respaldo_2024.txt universidad/`
> 3. Entra a `universidad` y verifica que el archivo llegó ahí:
>    `cd universidad`
>    `ls`

---

## 4. ELIMINACIÓN (`rm`)
⚠️ **PELIGRO:** Aquí no hay "Papelera de Reciclaje". Lo que se borra, se va para siempre.

* **`rm archivo`**: Borra un archivo.
* **`rm -r carpeta`**: Borra una carpeta y todo lo que tiene dentro.
* **`rm -rf carpeta`**: Borra todo a la fuerza sin preguntar (Force). **Usar con precaución.**

> **👉 PRÁCTICA 4 (Limpieza):**
> 1. Vuelve a la raíz del laboratorio: `cd ..` (o los necesarios hasta volver).
> 2. Borra el archivo original: `rm reporte_final.txt`
> 3. Borra la carpeta de backup completa: `rm -r universidad_backup`
> 4. Verifica que ya no existen con `ls`.

---

## 🏆 RETO INTEGRAL: "El Arquitecto"
Combina todo lo aprendido. Escribe los comandos para lograr esto:

1. Crear una carpeta `proyecto_alpha`.
2. Crear dentro tres subcarpetas: `docs`, `img`, `code`.
3. Crear un archivo `main.py` dentro de `code`.
4. Hacer una copia de toda la carpeta `code` y llamarla `code_v1`.
5. Borrar la carpeta `img` porque no se usará.

*(Solución al final de la clase)*
