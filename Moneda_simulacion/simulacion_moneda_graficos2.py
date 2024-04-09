import matplotlib.pyplot as plt
import random

# Número de lanzamientos de la moneda
num_lanzamientos = 1000

# Simular lanzamientos de la moneda
resultados = ['Cara' if random.randint(0, 1) == 1 else 'Cruz' for _ in range(num_lanzamientos)]

# Calcular el valor teórico esperado
valor_teorico_esperado = num_lanzamientos / 2

# Crear el histograma
plt.figure(figsize=(8, 6))
plt.hist(resultados, bins=2, color='green', edgecolor='black', alpha=0.7)
plt.axhline(valor_teorico_esperado, color='red', linestyle='--', linewidth=2, label='Valor Teórico Esperado')
plt.xlabel('Resultado')
plt.ylabel('Frecuencia Absoluta')
plt.title('Histograma de Lanzamiento de Moneda (Cara o Cruz)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.show()