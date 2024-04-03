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
y = []
prom1, prom2, prom3, prom4 = [], [], [], []
frecrel1, frecrel2, frecrel3, frecrel4 = [], [], [], []
var1, var2, var3, var4 = [], [], [], []
des1, des2, des3, des4 = [], [], [], []


def definir_valores():
    if len(sys.argv) != 7 or sys.argv[1] != "-c" or sys.argv[3] != "-n" or sys.argv[5] != "-e":
        print("Uso:python ruleta.py -c <cant_tiradas> -n <corridas> -e <num_elegido>")
        sys.exit(1)
    cant_tiradas = int(sys.argv[2])
    corridas = int(sys.argv[4])
    num_elegido = int(sys.argv[6])
    return cant_tiradas, corridas, num_elegido


cant_tiradas, corridas, num_elegido = definir_valores()


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


for i in range(corridas):
    y.clear()
    valores[0] = random.randint(0, 36)
    for j in range(1, cant_tiradas):
        valores.append(random.randint(0, 36))
    if i == 0:
        prom1 = prom_corrida(valores)
        frecrel1 = frecrel_corrida(valores)
        var1 = var_corrida(valores, prom1)
        des1 = des_corrida(valores)
    elif i == 1:
        prom2 = prom_corrida(valores)
        frecrel2 = frecrel_corrida(valores)
        var2 = var_corrida(valores, prom2)
        des2 = des_corrida(valores)
    elif i == 2:
        prom3 = prom_corrida(valores)
        frecrel3 = frecrel_corrida(valores)
        var3 = var_corrida(valores, prom3)
        des3 = des_corrida(valores)
    elif i == 3:
        prom4 = prom_corrida(valores)
        frecrel4 = frecrel_corrida(valores)
        var4 = var_corrida(valores, prom4)
        des4 = des_corrida(valores)
    todos_los_valores.append(valores)
    print(valores)
    aciertos_corrida = valores.count(num_elegido)
    print("Aciertos corrida: ", aciertos_corrida)
    aciertos = aciertos + aciertos_corrida

print("Aciertos totales: ", aciertos)
print("Lista de los promedios de cada tirada: ", prom1)
# valores_finales = dict(zip(todos_los_valores,map(lambda x: todos_los_valores.count(x),todos_los_valores)))
# print(sorted(valores_finales.items(), key=lambda x:x[1]))

# print(todos_los_valores)


total_tiradas = corridas * cant_tiradas

x1 = list(range(cant_tiradas))

frec_relativa_esperada = cant_tiradas / 36
frec_absoluta_esperada = 20

fig, axs = plt.subplots(nrows=2, ncols=2)
axs = axs.flatten()

axs[0].plot(prom1)
axs[0].set_title('Gráficos de primera corrida')
axs[0].set_xlabel('Número de tirada')
axs[0].set_ylabel('Promedio')
axs[1].plot(frecrel1)
axs[1].set_xlabel('Número de tirada')
axs[1].set_ylabel('Frecuencia relativa')
axs[2].plot(var1)
axs[2].set_xlabel('Número de tirada')
axs[2].set_ylabel('Varianza')
axs[3].plot(des1)
axs[3].set_xlabel('Número de tirada')
axs[3].set_ylabel('Desvio')
# plt.plot(y1, label='Tiradas', color='blue')
# plt.plot(frec_absoluta_esperada, label='Valor Constante', linestyle='--', color='red')
# plt.grid(True)
fig.tight_layout()
plt.show()
