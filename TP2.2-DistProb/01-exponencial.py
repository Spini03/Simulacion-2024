import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución exponencial
lambda_param = 1.0  # Tasa (lambda)

# Generación de números pseudoaleatorios uniformemente distribuidos entre 0 y 1
num_samples = 1000
uniform_random_numbers = np.random.uniform(0, 1, num_samples)

# Aplicar la transformación inversa para obtener números con distribución exponencial
exponential_random_numbers = -np.log(1 - uniform_random_numbers) / lambda_param


# Graficar el histograma de los números generados
plt.hist(exponential_random_numbers, bins=30, density=True, alpha=0.6, color='g', label='Datos simulados')

# Graficar la función de densidad teórica
x = np.linspace(0, np.max(exponential_random_numbers), 10000)
y = lambda_param * np.exp(-lambda_param * x)
plt.plot(x, y, 'k-', lw=2, label='Función teórica')  # Cambiamos el color de la línea a negro

# Configuración de la gráfica
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Exponencial')
plt.legend()

# Mostrar la gráfica
plt.show()
