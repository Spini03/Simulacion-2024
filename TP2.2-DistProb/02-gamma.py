import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

def transform_uniform_to_gamma(uniform_samples, k, theta):
    # Aplicamos la función inversa de la CDF de la distribución gamma
    return gamma.ppf(uniform_samples, a=k, scale=theta)

# Parámetros de la distribución gamma deseada
k = 2.0
theta = 2.0

# Generamos una muestra de números aleatorios uniformemente distribuidos
uniform_samples = np.random.rand(1000)

# Transformamos la muestra uniforme en una muestra gamma
gamma_samples = transform_uniform_to_gamma(uniform_samples, k, theta)

# Graficamos los resultados
plt.hist(gamma_samples, bins=30, density=True, alpha=0.6, color='g', label='Datos simulados')

# Graficamos la función teórica
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = gamma.pdf(x, a=k, scale=theta)
plt.plot(x, p, 'k', linewidth=2, label='Función teórica')

# Configuración de la gráfica
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Gamma')
plt.legend()

# Mostrar la gráfica
plt.show()