import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_discrete

# Definir los valores y sus probabilidades correspondientes
valores = np.array([1, 2, 3, 4, 5])
probabilidades = np.array([0.1, 0.2, 0.3, 0.2, 0.2])

# Crear la distribución empírica
distribucion_empirica = rv_discrete(name='distribucion_empirica', values=(valores, probabilidades))

# Generar muestras de la distribución empírica
num_samples = 1000
muestras = distribucion_empirica.rvs(size=num_samples)

# Graficar las muestras generadas
plt.hist(muestras, bins=np.arange(1, 7) - 0.5, density=True, alpha=0.6, color='g', label='Muestras generadas')

# Graficar la distribución empírica teórica
plt.plot(valores, probabilidades, 'bo', ms=8, label='Distribución empírica teórica')
plt.vlines(valores, 0, probabilidades, colors='b', lw=5, alpha=0.5)

# Configuración de la gráfica
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Discreta Empírica')
plt.legend()
plt.show()