# TP 2.1 - Generadores Pseudoaleatorios

Este proyecto implementa y evalúa diferentes generadores de números pseudoaleatorios (GCL, ERNIE, ItaRNG, PCG64) como parte del Trabajo Práctico 2.1.

## Archivos Principales

* `gen_pseudo.py`: Contiene las implementaciones de los distintos generadores (GCL, ERNIE, ItaRNG, PCG64).
* `tests.py`: Contiene las implementaciones de los tests estadísticos para evaluar la calidad de los generadores (Test Chi-cuadrado, Test de Corridas, Test de Arreglos Inversos, Test de Sumas Superpuestas).
* `imagen.py`: Script para generar una imagen de ruido utilizando uno de los generadores, permitiendo una visualización de la aleatoriedad.

## Documentación de Referencia

* `SIMULACIÓN_2024_TP2_1.pdf`: Informe del trabajo práctico.
* `itamaraca-a-novel-simple-way-to-generate-pseudo-random-numbers.pdf`: Paper de referencia para el generador ItaRNG.

## Dependencias

Asegúrese de tener instaladas las bibliotecas necesarias:
```bash
pip install numpy matplotlib scipy
```

## Bibliografía

PCG: https://numpy.org/doc/stable/reference/random/bit_generators/pcg64.html#
