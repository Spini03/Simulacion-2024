import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parámetros de la distribución de Pascal (binomial negativa)
r = 10  # Número de éxitos
p = .7  # Probabilidad de éxito en cada ensayo

# Generación de números pseudoaleatorios con distribución de Pascal
num_samples = 10000
pascal_random_numbers = np.random.negative_binomial(r, p, num_samples)

# Graficar el histograma de los números generados
plt.hist(pascal_random_numbers, bins=30, density=True, alpha=0.6, color='g', label='Datos simulados')

# Graficar la función de masa de probabilidad teórica
x = np.arange(0, np.max(pascal_random_numbers))
y = stats.nbinom.pmf(x, r, p)
plt.plot(x, y, 'k-', lw=2, label='Función teórica')  # Cambiamos el color de la línea a negro

# Configuración de la gráfica
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución de Pascal (Binomial Negativa)')
plt.legend()

# Mostrar la gráfica
plt.show()
