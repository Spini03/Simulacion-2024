import matplotlib.pyplot as plt
import random

# Generar datos aleatorios para la primera gráfica
x1 = list(range(1000))
y1 = [random.random() for _ in x1]

# Generar datos aleatorios para la segunda gráfica
x2 = list(range(1000))
y2 = [random.random() for _ in x2]

# Calcular el promedio de las dos primeras gráficas
y_avg = [(y1[i] + y2[i]) / 2 for i in range(1000)]

# Crear la figura y los subgráficos
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Graficar en el primer subgráfico
axs[0].plot(x1, y1, color='blue')
axs[0].set_title('Gráfico 1: Valores Aleatorios')
axs[0].set_xlabel('Índice')
axs[0].set_ylabel('Valor Aleatorio')

# Graficar en el segundo subgráfico
axs[1].plot(x2, y2, color='red')
axs[1].set_title('Gráfico 2: Valores Aleatorios')
axs[1].set_xlabel('Índice')
axs[1].set_ylabel('Valor Aleatorio')

# Graficar en el tercer subgráfico (promedio)
axs[2].plot(x1, y_avg, color='green', linewidth=3, linestyle='--')
axs[2].set_title('Gráfico 3: Promedio de los dos primeros')
axs[2].set_xlabel('Índice')
axs[2].set_ylabel('Valor Promedio')

# Ajustar diseño y mostrar gráficos
plt.tight_layout()

# Guardar la figura en disco
plt.savefig('tres_graficas_valores_aleatorios.png')

# Mostrar la figura
plt.show()