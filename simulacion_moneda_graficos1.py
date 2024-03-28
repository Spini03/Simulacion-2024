import random
import matplotlib.pyplot as plt

# Generar 100 valores aleatorios
random_values = [random.random() for _ in range(1000)]

# Generar una serie de valores constantes intermitentes
constant_values = [0.5 for i in range(1000)]

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(random_values, label='Valores Aleatorios', color='blue')
plt.plot(constant_values, label='Valor Constante', linestyle='--', color='red')
plt.xlabel('Número de tirada')
plt.ylabel('Valor obtenido')
plt.title('Gráfico de Valores Aleatorios con Valor Constante Intermitente')
plt.legend()
plt.grid(True)
plt.show()