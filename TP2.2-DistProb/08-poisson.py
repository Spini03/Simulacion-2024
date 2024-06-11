import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def generar_poisson(lambda_param, num_samples=1000):
    return np.random.poisson(lambda_param, size=num_samples)

# Parámetros de la distribución Poisson
lambda_param = 1.5
num_samples = 1000

# Generar números pseudoaleatorios
valores_poisson = generar_poisson(lambda_param, num_samples)

# Calcular la distribución teórica de Poisson
valores_teoricos = np.arange(0, np.max(valores_poisson) + 1)
probabilidades_teoricas = poisson.pmf(valores_teoricos, lambda_param)

# Graficar los resultados
plt.hist(valores_poisson, bins=20, density=True, alpha=0.6, color='g', label='Datos generados')

# Graficar la distribución teórica
plt.plot(valores_teoricos, probabilidades_teoricas, 'bo', ms=8, label='Distribución teórica')
plt.vlines(valores_teoricos, 0, probabilidades_teoricas, colors='b', lw=5, alpha=0.5)

# Configuración de la gráfica
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Poisson')
plt.legend()
plt.show()