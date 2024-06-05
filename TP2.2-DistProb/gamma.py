import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

def generar_gamma(k, theta, size=1000):
    return np.random.gamma(k, theta, size)

# Parámetros de la distribución gamma
k = 2.0
theta = 2.0

# Generar números pseudoaleatorios
valores_gamma = generar_gamma(k, theta, 1000)

# Graficar los resultados
plt.hist(valores_gamma, bins=30, density=True, alpha=0.6, color='g')

# Graficar la función teórica
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = gamma.pdf(x, a=k, scale=theta)
plt.plot(x, p, 'k', linewidth=2)
title = "Histograma de datos generados y la función teórica de la Gamma"
plt.title(title)
plt.show()
