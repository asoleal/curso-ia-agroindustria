# 🚜 Ingeniería de Inteligencia Artificial Aplicada al Agro

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-HPC-013243?style=for-the-badge&logo=numpy&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange?style=for-the-badge&logo=tensorflow&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Shell-yellow?style=for-the-badge&logo=linux&logoColor=black)
![Status](https://img.shields.io/badge/Status-Activo-green?style=for-the-badge)

> **"De la Terminal al Campo."**
> Un programa de ingeniería intensivo para transformar datos agronómicos en decisiones automatizadas mediante Computación de Alto Rendimiento, Deep Learning y Modelos de Lenguaje (LLMs).

---

## 📖 Visión del Curso

Este no es un bootcamp superficial. Es una formación de **Ingeniería de Software** aplicada.
Mientras otros cursos enseñan a "copiar y pegar código", aquí nos enfocamos en:

1.  **Fundamentos Matemáticos:** Entender el álgebra lineal y el cálculo detrás de las redes neuronales.
2.  **Infraestructura Real:** Manejo de servidores Linux (Headless), automatización Bash y control de versiones.
3.  **Ética y Soberanía:** Desarrollo de tecnología frugal, auditable y desconectada de la nube (Edge AI).

> 🎓 **Nivel Académico:** Cada semana incluye un **Manual de Ingeniería (PDF/LaTeX)** y presentaciones formales, elevando el estándar de un tutorial a una cátedra universitaria.

---

## 👥 Perfil de Ingreso

Diseñado para ingenieros agroindustriales, agrónomos y científicos de datos que:
* Buscan ir más allá de Excel.
* Quieren entender la "caja negra" de la IA.
* Necesitan procesar datos masivos (imágenes satelitales, sensores IoT) de forma eficiente.
* **No requieren experiencia previa**, pero sí alta disposición al pensamiento lógico y matemático.

---

## 🌱 Principios Éticos y Pedagógicos

La tecnología en el agro no es neutra. Nos regimos por:

* **Explicabilidad (XAI):** Rechazamos las cajas negras. Si el modelo dice "hay plaga", debemos saber por qué.
* **Diseño Frugal:** Algoritmos eficientes que corran en hardware modesto (no solo en supercomputadoras).
* **Soberanía de Datos:** Los datos del campo pertenecen al agricultor, no a la nube.
* **Rigor Matemático:** La programación es la herramienta; la matemática es el fundamento.

---

## 🗺️ Mapa Curricular (8 Semanas)

### 🟢 Módulo 1: Ingeniería de Datos y HPC
*La base: Infraestructura, Linux y optimización matemática.*

| Semana | Tema | Enfoque Técnico | Proyecto / Entregable |
| :--- | :--- | :--- | :--- |
| **01** | **El Entorno del Ingeniero** | Linux Kernel, Shell Scripting, Git DAGs. | `deploy.sh`: Automatización de infraestructura de sensores simulados. |
| **02** | **Cómputo de Alto Rendimiento** | Vectorización NumPy, SIMD, Complejidad $O(n)$. | Procesamiento matricial de imágenes satelitales (1M px) en milisegundos. |

### 🟡 Módulo 2: Data Science y Machine Learning Clásico
*Descubrimiento de patrones y modelado estadístico.*

| Semana | Tema | Enfoque Técnico | Proyecto / Entregable |
| :--- | :--- | :--- | :--- |
| **03** | **Análisis Exploratorio (EDA)** | Estadística Descriptiva, Limpieza de Datos, Pandas. | Auditoría forense de dataset de cosecha corrupto. |
| **04** | **Modelado Predictivo** | Regresión, Función de Costo, Descenso del Gradiente. | Predicción de rendimiento (Toneladas/Ha) basado en química del suelo. |

### 🔴 Módulo 3: Deep Learning y Visión Artificial
*Redes Neuronales y percepción computacional.*

| Semana | Tema | Enfoque Técnico | Proyecto / Entregable |
| :--- | :--- | :--- | :--- |
| **05** | **Clasificación y Lógica** | Árboles de Decisión, Métricas (F1-Score, Recall). | Clasificador automático de calidad de fruta para exportación. |
| **06** | **Redes Neuronales (CNNs)** | Convoluciones, Backpropagation, Tensores. | Detección de enfermedades (Roya/Broca) en imágenes de hojas. |

### 🟣 Módulo 4: Fronteras de la IA (GenAI & MLOps)
*Modelos Generativos y Puesta en Producción.*

| Semana | Tema | Enfoque Técnico | Proyecto / Entregable |
| :--- | :--- | :--- | :--- |
| **07** | **Modelos de Lenguaje (LLMs)** | RAG (Retrieval-Augmented Generation), Prompt Engineering. | Asistente técnico que responde preguntas leyendo manuales agrícolas (PDFs). |
| **08** | **Despliegue y APIs** | Arquitectura REST, Docker, Latencia. | API pública con FastAPI para servir predicciones en tiempo real. |

---

## 🤖 Sobre la Semana 7 (GenAI para Agro)
Integramos lo último en IA Generativa con un enfoque práctico:
* No entrenaremos un GPT desde cero (es costoso e ineficiente).
* Implementaremos sistemas **RAG (Búsqueda Aumentada)**: Una IA que lee normativas agrícolas locales y responde dudas técnicas sin alucinar.
* Uso de modelos locales (Llama 3 / Mistral) para zonas sin internet.

---

## 🛠️ Stack Tecnológico

Gracias a **GitHub Codespaces**, el entorno está contenerizado en la nube:

* **Core:** Python 3.9, Bash.
* **HPC & Data:** NumPy, Pandas, Scikit-Learn.
* **Deep Learning:** TensorFlow/Keras.
* **GenAI:** LangChain, Ollama (Opcional).
* **Web:** FastAPI.
* **Documentación:** LaTeX (TexLive).

---

## 🚀 Inicio Rápido

1.  **Abrir Entorno:** Haz clic en el botón para lanzar un servidor Ubuntu configurado.
    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/TU_USUARIO/curso-ia-agro)

2.  **Verificar Instalación:**
    ```bash
    python test_entorno.py
    ```

3.  **Generar Documentación:**
    ```bash
    cd semana_01/docs
    pdflatex manual_tecnico.tex
    ```

---

## 📄 Licencia

Material desarrollado con fines académicos.
**Licencia:** MIT.
