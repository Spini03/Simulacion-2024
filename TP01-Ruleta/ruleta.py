import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import statistics as st
import argparse  # Para la gestion de argumentos de linea de comandos

rul = np.arange(37)
aciertos = 0
prom_esperado = np.mean(rul)
valor_fr_esperada = 1 / 37
valor_var_esperada = np.var(rul)
valor_desvio_esperado = np.std(rul)
todos_los_valores = []
todas_las_tiradas = []
valores = [1000]
prom = []
frecrel = []
var = []
des = []


def definir_valores():
    parser = argparse.ArgumentParser(description='Script para procesar argumentos de línea de comandos')
    parser.add_argument('-c', '--cant_tiradas', type=int, required=True, help='Cantidad de tiradas')
    parser.add_argument('-n', '--corridas', type=int, required=True, help='Número de corridas')
    parser.add_argument('-e', '--num_elegido', type=int, required=True, help='Número elegido')

    args = parser.parse_args()

    if args.cant_tiradas <= 0:
        print("Error: La cantidad de tiradas debe ser mayor que cero.")
        sys.exit(1)

    if args.corridas <= 0:
        print("Error: El número de corridas debe ser mayor que cero.")
        sys.exit(1)

    return args.cant_tiradas, args.corridas, args.num_elegido


cant_tiradas, corridas, num_elegido = definir_valores()

# listas valores esperados
list_prom_esperado = []
list_fr_esperada = []
list_var_esperada = []
list_des_esperado = []
for l in range(cant_tiradas):
    list_prom_esperado.append(prom_esperado)
    list_fr_esperada.append(valor_fr_esperada)
    list_var_esperada.append(valor_var_esperada)
    list_des_esperado.append(valor_desvio_esperado)


def graficar(i, prom, frecrel, var, des):
    fig, axs = plt.subplots(nrows=2, ncols=2)
    axs = axs.flatten()

    titulo = 'Datos corrida ' + str(i + 1)
    fig.suptitle(titulo)
    axs[0].plot(prom)
    axs[0].plot(list_prom_esperado)
    axs[0].set_xlabel('Número de tirada')
    axs[0].set_ylabel('Promedio')
    axs[1].plot(frecrel)
    axs[1].plot(list_fr_esperada)
    axs[1].set_xlabel('Número de tirada')
    axs[1].set_ylabel('Frecuencia relativa')
    axs[2].plot(var)
    axs[2].plot(list_var_esperada)
    axs[2].set_xlabel('Número de tirada')
    axs[2].set_ylabel('Varianza')
    axs[3].plot(des)
    axs[3].plot(list_des_esperado)
    axs[3].set_xlabel('Número de tirada')
    axs[3].set_ylabel('Desvio')
    fig.tight_layout()
    plt.show()


for i in range(corridas):
    valores.clear()
    prom.clear()
    frecrel.clear()
    var.clear()
    des.clear()
    ganadas = 0
    for j in range(cant_tiradas):
        num = random.randint(0, 36)
        valores.append(num)
        prom.append(np.mean(valores))
        if num_elegido == num:
            ganadas += 1
        frecrel.append(ganadas / (j + 1))
        if j > 0:
            var.append(st.variance(valores))
            des.append(st.stdev(valores))
    todos_los_valores.append(valores)
    print(valores)
    print("Aciertos corrida: ", ganadas)
    aciertos = aciertos + ganadas

    graficar(i, prom, frecrel, var, des)

print("Aciertos totales: ", aciertos)
