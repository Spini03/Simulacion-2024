# Para la gestion de argumentos de linea de comandos
import argparse 
import sys

import random
import matplotlib.pyplot as plt
import numpy as np
import statistics as st


def inicializar_valores():
    parser = argparse.ArgumentParser(description='Script para procesar argumentos de línea de comandos')
    parser.add_argument('-c', '--cant_tiradas', type=int, required=True, help='Cantidad de tiradas')
    parser.add_argument('-n', '--cant_corridas', type=int, required=True, help='Número de corridas')
    parser.add_argument('-e', '--num_elegido', type=int, required=True, help='Número elegido')
    
    args = parser.parse_args()

    if args.cant_tiradas <= 0:
        print("Error: La cantidad de tiradas debe ser mayor que cero.")
        sys.exit(1)
        
    if args.cant_corridas <= 0:
        print("Error: El número de corridas debe ser mayor que cero.")
        sys.exit(1)
    
    return args.cant_tiradas, args.cant_corridas, args.num_elegido


def generar_listas_esperadas(cant_tiradas):

    ruleta = np.arange(37)

    prom_esperado = np.mean(ruleta)
    fr_esperada = 1 / 37
    var_esperada = np.var(ruleta)
    des_esperado = np.std(ruleta)

    list_prom_esperado = [prom_esperado] * cant_tiradas
    list_fr_esperada = [fr_esperada] * cant_tiradas
    list_var_esperada = [var_esperada] * cant_tiradas
    list_des_esperado = [des_esperado] * cant_tiradas

    return list_prom_esperado, list_fr_esperada, list_var_esperada, list_des_esperado


def graficar(promedio, frec_rel, varianza, desvio, cant_tiradas, valores, num_corrida):
    fig, axs = plt.subplots(nrows=3, ncols=2)
    axs = axs.flatten()

    list_prom_esperado, list_frec_esperada, list_var_esperada, list_des_esperado = generar_listas_esperadas(cant_tiradas)

    titulo = 'Datos corrida ' + str(num_corrida)
    fig.suptitle(titulo)

    # Frec Relativa
    axs[0].set_ylabel('Frecuencia relativa')
    axs[0].plot(frec_rel)
    axs[0].plot(list_frec_esperada)
    axs[0].set_xlabel('Número de tirada')

    # Promedio
    axs[1].set_ylabel('Promedio')
    axs[1].plot(promedio)
    axs[1].plot(list_prom_esperado)
    axs[1].set_xlabel('Número de tirada')

    # Desvio
    axs[2].set_ylabel('Desvio')
    axs[2].plot(desvio)
    axs[2].plot(list_des_esperado)
    axs[2].set_xlabel('Número de tirada')

    # Varianza
    axs[3].set_ylabel('Varianza')
    axs[3].plot(varianza)
    axs[3].plot(list_var_esperada)
    axs[3].set_xlabel('Número de tirada')

    # Frecuecnia Relativa
    axs[4].hist(valores, bins=range(38), density=True, alpha=0.75)
    axs[4].set_ylabel('Frecuencia')
    axs[4].set_xlabel('Número')

    # Frecuencia acumulada
    axs[5].bar(range(37), np.histogram(valores, bins=range(38))[0])
    axs[5].set_ylabel('Frecuencia')
    axs[5].set_xlabel('Número')

    # Otras posibles graficas podriasn ser (Histograma de resultados Frec absoluta de cada numero
    # Frec acumulada, grafico de porbabilidad acumulada, analisis de tendencia a lo largo del timepo)

    fig.tight_layout()
    plt.show()


def ejecutar_corridas(cant_tiradas, cant_corridas, num_elegido):
    aciertos = 0

    for i in range(cant_corridas):

        print(f"\n======== CORRIDA {i + 1} ========")
        
        valores = []
        promedio = []
        frecrel = []
        var = []
        des = []
        ganadas = 0

        for j in range(cant_tiradas):

            num = random.randint(0, 36)
            valores.append(num)
            promedio.append(np.mean(valores))

            ganadas += 1 if num_elegido == num else 0

            frecrel.append(ganadas / (j + 1))

            if j > 0: 
                var.append(st.variance(valores))
                des.append(st.stdev(valores))

        print("Valores Ruleta: ", valores)
        print("Aciertos corrida: ", ganadas)

        aciertos = aciertos + ganadas

        graficar(promedio, frecrel, var, des, cant_tiradas, valores, i + 1)

    print(f"\n======== FIN CORRIDAS ========\n")
    print("Aciertos totales: ", aciertos)


def main():
    cant_tiradas, cant_corridas, num_elegido = inicializar_valores()
    ejecutar_corridas(cant_tiradas, cant_corridas, num_elegido)
    
    # TODO: Agregar las graficas de todas las corridas

if __name__ == '__main__':
    main()
