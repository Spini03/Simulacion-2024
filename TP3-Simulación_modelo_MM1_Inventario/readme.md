# TP3 - Simulación de Modelos M/M/1 e Inventario

## Descripción

Este trabajo práctico implementa y analiza la simulación de dos modelos clásicos:

1.  **Modelo de Colas M/M/1**: Se simula un sistema de colas con arribos Poisson (M), tiempos de servicio Exponenciales (M) y un único servidor (1). Se analizan variantes con cola infinita (M/M/1) y cola finita (M/M/1/K).
2.  **Modelo de Inventario**: Se simula un sistema de inventario simple para analizar costos y niveles de servicio.

Se realiza una comparación entre los resultados teóricos, los resultados de la simulación implementada en Python y los resultados de un modelo en el software AnyLogic.

## Contenido del Repositorio

* **Scripts de Python (`.py`):**
    * `mm1_model*.py`: Diversos scripts que implementan la simulación del modelo de colas M/M/1.
    * `inventory_model*.py` (y otros scripts de inventario): Implementaciones de la simulación del modelo de inventario.
* **Proyecto AnyLogic (`.alp`):**
    * `M_M_1_K.alp`: Archivo de proyecto de AnyLogic que modela la simulación del sistema M/M/1/K, permitiendo la comparación entre la simulación por código y una herramienta de software.
* **Resultados (`/Capturas_corridas/`):**
    * Contiene capturas de pantalla de las corridas de simulación realizadas en AnyLogic. Estas están clasificadas en subcarpetas según los parámetros utilizados (ej. tasa de arribo Lambda, capacidad de la cola K).

## Dependencias

Para los scripts de Python, se requieren:
```bash
pip install numpy matplotlib scipy
