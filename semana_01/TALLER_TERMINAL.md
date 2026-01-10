# 🚜 Taller 01: Dominando la Terminal Linux

**Objetivo:** Dejar de usar el mouse y empezar a controlar el sistema como un Ingeniero de Software.
**Contexto:** Eres el administrador de un servidor agrícola remoto. No tienes interfaz gráfica, solo texto.

---

## 📍 Parte 1: Reconocimiento del Terreno
Lo primero es saber dónde estás parado y qué hay alrededor.

1. **¿Dónde estoy?**
   Escribe `pwd` (Print Working Directory).
   > Debería mostrarte la ruta completa a `semana_01`.

2. **¿Qué hay aquí?**
   Escribe `ls` (List).
   > Verás los archivos.
   > Intenta `ls -F` (Para ver cuáles son carpetas).
   > Intenta `ls -R` (Para ver todo el árbol de archivos recursivamente).

---

## 📂 Parte 2: Creación de Infraestructura
Vamos a simular que creamos zonas de cultivo.

1. **Crear carpetas:**
   ```bash
   mkdir zona_norte
   mkdir zona_sur
