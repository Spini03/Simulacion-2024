import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución binomial
p = .7  # Probabilidad de éxito
n = 10  # Cant intentos aleatorios
num_samples = 1000


def calcula_binomial(p, n, num_samples=1000):
    total = []
    for i in range(0, num_samples):
        xi = 0
        nums = np.random.uniform(0, 1, n)  # números aleatorios
        for r in nums:
            if r <= p:
                xi += 1
        total.append(xi)
    return total


# Guardar los resultados del binomial
binomial_random_numbers = calcula_binomial(p, n, num_samples)

# Graficar el histograma de los números generados
plt.hist(binomial_random_numbers, bins=20, density=False, alpha=0.6, color='g', label='Datos simulados')

# Graficar la función de densidad teórica


# Configuración de la gráfica
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Binomial')
plt.legend()

# Mostrar la gráfica
plt.show()
