# Simulación 2024 - UTN FRRO

Este repositorio contiene los trabajos prácticos desarrollados para la materia Simulación de la Universidad Tecnológica Nacional - Facultad Regional Rosario durante el año 2024.

## Estructura del Repositorio

El repositorio se organiza en carpetas, cada una correspondiente a un Trabajo Práctico (TP) específico o a simulaciones exploratorias:

* **`/Moneda_simulacion`**: Contiene scripts iniciales para simular lanzamientos de moneda y visualizar resultados.
* **`/TP1.1-Ruleta`**: Simulación de una ruleta para analizar su comportamiento estadístico.
* **`/TP1.2-ApuestaRuleta`**: Estudio económico-matemático de diferentes estrategias de apuestas en la ruleta.
* **`/TP2.1-GenPseudo`**: Implementación y testeo de generadores de números pseudoaleatorios (GCL, ERNIE, ItaRNG, PCG64).
* **`/TP2.2-DistProb`**: Generación de números pseudoaleatorios siguiendo distintas distribuciones de probabilidad (Uniforme, Exponencial, Gamma, Normal, Pascal, Binomial, Hipergeométrica, Poisson, Empírica Discreta).
* **`/TP3-Simulación_modelo_MM1_Inventario`**: Estudio de simulación de un modelo de colas M/M/1 y un modelo de inventario, comparando resultados teóricos, con implementaciones en Python y AnyLogic.

## Trabajos Prácticos

### TP 1.1: Simulación de una Ruleta

* **Objetivo:** Simular el funcionamiento de una ruleta y verificar su comportamiento mediante análisis estadísticos básicos (frecuencia relativa, promedio, varianza, desvío estándar).
* **Implementación:** Script en Python que permite configurar número de tiradas, corridas y número elegido. Utiliza `matplotlib` para graficar los resultados.
* **Más detalles:** Consulta el [README específico del TP1.1](TP1.1-Ruleta/readme.md).

### TP 1.2: Estudio de Apuestas en la Ruleta

* **Objetivo:** Simular y analizar diferentes estrategias de apuestas (Martingala, D'Alembert, Fibonacci, y una propuesta) bajo supuestos de capital finito e infinito.
* **Implementación:** Script en Python que extiende la simulación de ruleta, monitorizando el flujo de caja. Utiliza `matplotlib` para graficar los resultados.
* **Más detalles:** Consulta el [README específico del TP1.2](TP1.2-ApuestaRuleta/readme.md).

### TP 2.1: Generadores Pseudoaleatorios

* **Objetivo:** Construir y evaluar la calidad de diferentes generadores de números pseudoaleatorios (GCL, ERNIE, ItaRNG, PCG64) mediante tests estadísticos (Chi-cuadrado, corridas, arreglos inversos, sumas superpuestas).
* **Implementación:** Scripts en Python (`gen_pseudo.py`, `tests.py`, `imagen.py`) para generar números, aplicar tests y visualizar la aleatoriedad como ruido en imágenes.
* **Más detalles:** Consulta el [README específico del TP2.1](TP2.1-GenPseudo/readme.md).

### TP 2.2: Generadores para Distintas Distribuciones

* **Objetivo:** Implementar métodos (transformada inversa, rechazo, composición, etc.) para generar números pseudoaleatorios que sigan distribuciones de probabilidad específicas, tanto continuas como discretas.
* **Implementación:** Scripts individuales en Python para cada distribución (Uniforme, Exponencial, Gamma, Normal, Pascal, Binomial, Hipergeométrica, Poisson, Empírica Discreta), incluyendo visualización con `matplotlib` y comparación con funciones teóricas de `scipy.stats`.
* **Más detalles:** Consulta el [README específico del TP2.2](TP2.2-DistProb/readme.md).

### TP 3: Simulación Modelo M/M/1 e Inventario

* **Objetivo:** Realizar estudios de simulación para un modelo de colas M/M/1 (con cola finita e infinita) y un modelo de inventario. Analizar medidas de rendimiento clave, variar parámetros (tasa de arribo, capacidad de cola) y comparar resultados simulados (Python, AnyLogic) con valores teóricos.
* **Implementación:** Scripts en Python (`mm1_model*.py`, `inventory_model*.py`) para las simulaciones y un proyecto AnyLogic (`M_M_1_K.alp`). Incluye capturas de pantalla de las corridas en AnyLogic.
* **Más detalles:** Consulta el [README específico del TP3](TP3-Simulación_modelo_MM1_Inventario/readme.md).

## Cómo Empezar

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/usuario/simulacion-2024.git](https://github.com/usuario/simulacion-2024.git)
    cd simulacion-2024
    ```
    *(Reemplaza `usuario` con el nombre de usuario correcto)*

2.  **Instalar dependencias:**
    La mayoría de los scripts requieren Python 3.x y bibliotecas como `numpy`, `matplotlib` y `scipy`. Puedes instalar las dependencias listadas en los archivos `requirements.txt` dentro de las carpetas de los TP correspondientes, por ejemplo:
    ```bash
    cd TP1.1-Ruleta
    pip install -r requirements.txt
    cd ..
    ```
    *(Repite para otras carpetas si es necesario)*

3.  **Ejecutar los scripts:**
    Navega a la carpeta del TP deseado y ejecuta los scripts de Python. Algunos scripts aceptan argumentos por línea de comandos para configurar los parámetros de la simulación (consulta los README específicos de cada TP o el código fuente).
    ```bash
    cd TP1.1-Ruleta
    python ruleta.py -c 1000 -n 5 -e 14
    ```

## Contribuyentes

* Pedemonte Santiago
* Glocer Martin
* Fabbri Lucía
* Giménez Ulises
* Paratore Eneas
* Spini Santiago
