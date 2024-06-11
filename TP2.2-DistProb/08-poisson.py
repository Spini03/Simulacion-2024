import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


def generar_poisson(lambda_param, num_samples=1000):
    return np.random.poisson(lambda_param, size=num_samples)


# Parámetros de la distribución poisson
lambda_param = 10

# Generar números pseudoaleatorios
valores_poisson = generar_poisson(lambda_param)

# Graficar los resultados
plt.hist(valores_poisson, bins=20, density=True, alpha=0.6, color='g')

# Configuración de la gráfica
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Poisson')
plt.show()
