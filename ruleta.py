import random
import sys
import matplotlib.pyplot as plt
import numpy as np

aciertos = 0
prom_esperado = 18
valor_fr_esperada = 1 / 37
valor_var_esperada = 114
valor_desvio_esperado = 10.67707825
todos_los_valores = []
todas_las_tiradas = []
valores = [1000]
prom = []
frecrel = []
var = []
des = []


def definir_valores():
    if len(sys.argv) != 7 or sys.argv[1] != "-c" or sys.argv[3] != "-n" or sys.argv[5] != "-e":
        print("Uso:python ruleta.py -c <cant_tiradas> -n <corridas> -e <num_elegido>")
        sys.exit(1)
    cant_tiradas = int(sys.argv[2])
    corridas = int(sys.argv[4])
    num_elegido = int(sys.argv[6])
    return cant_tiradas, corridas, num_elegido


cant_tiradas, corridas, num_elegido = definir_valores()


#listas valores esperados
list_prom_esperado = []
list_fr_esperada = []
list_var_esperada = []
list_des_esperado = []
for l in range(cant_tiradas):
    list_prom_esperado.append(prom_esperado)
    list_fr_esperada.append(valor_fr_esperada)
    list_var_esperada.append(valor_var_esperada)
    list_des_esperado.append(valor_desvio_esperado)


def prom_corrida(lista):
    promedios = []
    suma = 0
    for i, valor in enumerate(lista):
        suma += valor
        promedio = suma / (i + 1)
        promedios.append(round(promedio, 3))
    return promedios


def frecrel_corrida(lista):
    frec_rel = []
    acum = 0
    for i, valor in enumerate(lista):
        if valor == num_elegido:
            acum += 1
        fr = acum / (i + 1)
        frec_rel.append(round(fr, 3))
    return frec_rel


def var_corrida(lista, promedios):
    varianza = []
    for i, valor in enumerate(lista):
        var = ((valor - promedios[i]) ** 2) / (i + 1)
        varianza.append(round(var))
    return varianza


def des_corrida(lista):
    desvio = []
    for varianza in lista:
        desvio.append(round(np.sqrt(varianza), 3))
    return desvio


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
    # plt.plot(y1, label='Tiradas', color='blue')
    # plt.plot(frec_absoluta_esperada, label='Valor Constante', linestyle='--', color='red')
    # plt.grid(True)
    fig.tight_layout()
    plt.show()


for i in range(corridas):
    valores.clear()
    for j in range(cant_tiradas):
        valores.append(random.randint(0, 36))
    prom = prom_corrida(valores)
    frecrel = frecrel_corrida(valores)
    var = var_corrida(valores, prom)
    des = des_corrida(var)
    todos_los_valores.append(valores)
    print(valores)
    aciertos_corrida = valores.count(num_elegido)
    print("Aciertos corrida: ", aciertos_corrida)
    aciertos = aciertos + aciertos_corrida

    graficar(i, prom, frecrel, var, des)

print("Aciertos totales: ", aciertos)
print("Lista de los promedios de cada tirada: ", prom)
# valores_finales = dict(zip(todos_los_valores,map(lambda x: todos_los_valores.count(x),todos_los_valores)))
# print(sorted(valores_finales.items(), key=lambda x:x[1]))

# print(todos_los_valores)
