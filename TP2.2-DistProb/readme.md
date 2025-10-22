# TP 2.2 - Generadores de Distribuciones de Probabilidad

Este proyecto contiene scripts para generar números pseudoaleatorios que siguen diferentes distribuciones de probabilidad, tanto continuas como discretas. Se implementan diversos métodos como la transformada inversa, aceptación y rechazo, y composición.

## Scripts y Distribuciones

Cada script genera una muestra (por defecto N=1000) para una distribución específica, la grafica en un histograma y la compara con la función de densidad de probabilidad (PDF) o función de masa de probabilidad (PMF) teórica provista por `scipy.stats`.

### Distribuciones Continuas
* `01-exponencial.py`: Distribución Exponencial (método de la transformada inversa).
* `02-gamma.py`: Distribución Gamma (método de aceptación y rechazo).
* `03-normal.py`: Distribución Normal (método de Box-Muller).
* `04-uniforme.py`: Distribución Uniforme (basada en el generador GCL).

### Distribuciones Discretas
* `05-binomial.py`: Distribución Binomial.
* `06-pascal.py`: Distribución de Pascal (Binomial Negativa).
* `07-hipergeometrica.py`: Distribución Hipergeométrica.
* `08-poisson.py`: Distribución de Poisson.
* `09-empirica.py`: Distribución Empírica Discreta (basada en probabilidades de entrada).

## Documentación

* `SIMULACIÓN_2024_TP2_2.pdf`: Informe del trabajo práctico con la teoría y el análisis de resultados.
* `Cap 4 - Tecnicas de Simulación en Computadoras (Naylor).pdf`: Material teórico de referencia.

## Dependencias

Asegúrese de tener instaladas las bibliotecas necesarias:
```bash
pip install numpy matplotlib scipy
