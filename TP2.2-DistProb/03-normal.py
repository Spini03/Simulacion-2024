import numpy as np
import matplotlib.pyplot as plt

def generar_normal(mu, sigma, size=1000):
    # Generar números uniformes entre 0 y 1
    u = np.random.uniform(0, 1, size)
    
    # Aplicar la transformación inversa de la CDF normal
    z = np.sqrt(-2 * np.log(u)) * np.cos(2 * np.pi * u)
    
    # Transformar a la distribución normal deseada
    return mu + sigma * z

# Parámetros de la distribución normal
mu = 0
sigma = 1

# Generar números pseudoaleatorios
valores = generar_normal(mu, sigma, 1000)

# Graficar los resultados
plt.hist(valores, bins=30, density=True, alpha=0.6, color='g')

# Graficar la función teórica
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (np.sqrt(2 * np.pi) * sigma)
plt.plot(x, p, 'k', linewidth=2)
title = "Histograma de datos generados y la función teórica de la Normal"
plt.title(title)
plt.show()
