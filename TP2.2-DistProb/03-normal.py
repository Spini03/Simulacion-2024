import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución normal
mu = 0  # Media
sigma = 1  # Desviación estándar

# Generación de números pseudoaleatorios uniformemente distribuidos entre 0 y 1
num_samples = 10000
u1 = np.random.uniform(0, 1, num_samples)
u2 = np.random.uniform(0, 1, num_samples)

# Aplicar el método de Box-Muller para obtener números con distribución normal
z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
z1 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)

# Adaptar los números generados a la distribución normal con media mu y desviación estándar sigma
normal_random_numbers = mu + sigma * z0

# Graficar el histograma de los números generados
plt.hist(normal_random_numbers, bins=30, density=True, alpha=0.6, color='g', label='Datos simulados')

# Graficar la función de densidad teórica
x = np.linspace(np.min(normal_random_numbers), np.max(normal_random_numbers), 10000)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
plt.plot(x, y, 'r-', lw=2, label='Función teórica')

# Configuración de la gráfica
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Normal')
plt.legend()

# Mostrar la gráfica
plt.show()
