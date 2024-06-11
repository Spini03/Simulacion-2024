import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

def generar_hipergeometrica(total_population, total_successes, sample_size, num_samples=1000):
    return np.random.hypergeometric(total_population, total_successes, sample_size, size=num_samples)

# Parámetros de la distribución hipergeométrica
total_population = 100  # Población total (M)
total_successes = 30    # Número total de éxitos en la población (n)
sample_size = 20        # Tamaño de la muestra (N)
num_samples = 1000

# Generar números pseudoaleatorios
valores_hipergeometricos = generar_hipergeometrica(total_population, total_successes, sample_size, num_samples)

# Graficar los resultados
plt.hist(valores_hipergeometricos, bins=20, density=True, alpha=0.6, color='g')

# Configuración de la gráfica
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Hipergeométrica')
plt.show()

