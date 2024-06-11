import numpy as np
import matplotlib.pyplot as plt

def generar_uniforme(a, b, size=1000):
    return np.random.uniform(a, b, size)

# Parámetros de la distribución uniforme
a = 0
b = 10

# Generar números pseudoaleatorios
valores_uniforme = generar_uniforme(a, b, 1000000)

# Graficar los resultados
plt.hist(valores_uniforme, bins=30, density=True, alpha=0.6, color='g', label='Datos simulados')

# Graficar la función teórica
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = [1 / (b - a) if a <= val <= b else 0 for val in x]
plt.plot(x, p, 'k', linewidth=2, label='Función teórica')

# Configuración de la gráfica
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Uniforme')
plt.legend()

# Mostrar la gráfica
plt.show()
