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
    parser.add_argument('-n', '--corridas', type=int, required=True, help='Número de corridas')
    parser.add_argument('-s', '--estrategia', type=str, choices=['m', 'd', 'f', 'o'], required=True,
                        help='Opciones permitidas: m, d, f, o')
    parser.add_argument('-a', '--tipo_capital', type=str, choices=['i', 'f'], required=True,
                        help='Opciones permitidas: i, f')
    parser.add_argument('-e', '--num_elegido', type=int, required=False, help='Número elegido')

    args = parser.parse_args()

    if args.cant_tiradas <= 0:
        print("Error: La cantidad de tiradas debe ser mayor que cero.")
        sys.exit(1)

    if args.corridas <= 0:
        print("Error: El número de corridas debe ser mayor que cero.")
        sys.exit(1)

    return args.cant_tiradas, args.corridas, args.num_elegido, args.estrategia, args.tipo_capital


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

    list_prom_esperado, list_frec_esperada, list_var_esperada, list_des_esperado = generar_listas_esperadas(
        cant_tiradas)

    titulo = 'Datos corrida ' + str(num_corrida)
    fig.suptitle(titulo)

    # Frec Relativa
    axs[0].set_title('Frecuencia Relativa del numero 14')
    axs[0].set_ylabel('Frecuencia relativa')
    axs[0].plot(frec_rel)
    axs[0].plot(list_frec_esperada)
    axs[0].set_xlabel('Número de tirada')

    # Promedio
    axs[1].set_title('Promedio')
    axs[1].set_ylabel('Promedio')
    axs[1].plot(promedio)
    axs[1].plot(list_prom_esperado)
    axs[1].set_xlabel('Número de tirada')

    # Desvio
    axs[2].set_title('Desvíos')
    axs[2].set_ylabel('Desvio')
    axs[2].plot(desvio)
    axs[2].plot(list_des_esperado)
    axs[2].set_xlabel('Número de tirada')

    # Varianza
    axs[3].set_title('Varianza')
    axs[3].set_ylabel('Varianza')
    axs[3].plot(varianza)
    axs[3].plot(list_var_esperada)
    axs[3].set_xlabel('Número de tirada')

    # Frecuencia Acumulada
    axs[4].set_title('Frecuencia Acumulada')
    axs[4].bar(range(37), np.histogram(valores, bins=range(38))[0])
    axs[4].set_ylabel('Frecuencia')
    axs[4].set_xlabel('Número')

    # Frecuecnia Relativa
    axs[5].set_title('Frecuencia Relativa')
    axs[5].hist(valores, bins=range(38), density=True, alpha=0.75)
    axs[5].set_ylabel('Frecuencia')
    axs[5].set_xlabel('Número')

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

        # graficar(promedio, frecrel, var, des, cant_tiradas, valores, i + 1)

    print(f"\n======== FIN CORRIDAS ========\n")
    print("Aciertos totales: ", aciertos)


def corridas(cant_tiradas, cant_corridas, estrategia, capital_infinito, apuesta_par, saldo, apuesta_inicial):
    for corrida in range(cant_corridas):
        print(f"=========== Corrida {corrida + 1} ================")
        ganaste = corrida_por_pares(apuesta_par)
        if ganaste:
            saldo += apuesta_inicial
            print("ganador!")
        else:
            print("perdedor!")
            saldo -= apuesta_inicial

        apuesta_anterior = apuesta_inicial
        sin_saldo = False

        for tirada in range(cant_tiradas - 1):
            apuesta_actual = estrategia(ganaste, apuesta_inicial, apuesta_anterior)
            ganaste = corrida_por_pares(apuesta_par)
            if ganaste and not capital_infinito and saldo <= apuesta_actual:
                print("ganador!")
                saldo += saldo
            elif ganaste:
                print("ganador!")
                saldo += apuesta_actual
            else:
                print("perdedor!")
                if not capital_infinito and (saldo - apuesta_actual) <= 0:
                    print("No tienes mas saldo para jugar")
                    sin_saldo = True
                    break
                saldo -= apuesta_actual
            apuesta_anterior = apuesta_actual

        if sin_saldo:
            print(f"Saldo final: 0")
        else:
            print(f"Saldo final: {saldo}")


def corrida_por_pares(apuesta_par):
    num_ganador = random.randint(0, 36)

    if num_ganador == 0:
        return False

    ganador_par = (num_ganador % 2) == 0

    if apuesta_par and not ganador_par:
        return False

    if ganador_par and not apuesta_par:
        return False

    return True


def martin_gala(ganaste, apuesta_inicial, apuesta_anterior):
    # Al perder se dobla la ultima apuesta, al ganar se vuelve a al monto inicial
    if ganaste:
        proxima_apuesta = apuesta_inicial
    else:
        proxima_apuesta = apuesta_anterior * 2

    return proxima_apuesta


def dalamber(ganaste, apuesta_inicial, apuesta_anterior):
    # Al perder se aumenta 1 unidad la apuesta, al ganar se disminuye una unidad hasta la inicial
    if ganaste and apuesta_anterior >= apuesta_inicial:
        proxima_apuesta = apuesta_anterior - apuesta_inicial
    elif ganaste:
        proxima_apuesta = apuesta_inicial
    else:
        proxima_apuesta = apuesta_anterior + apuesta_inicial

    return proxima_apuesta



def fibonacci(ganaste, apuesta_inicial, apuesta_anterior):
    ''' 
    Al perder una apuesta de 1, la siguiente será de 1, luego 2, luego 3, luego 5, y así sucesivamente
    Al ganar se retrocede 2 pasos la secuencia 
    '''
    if ganaste and apuesta_anterior >= apuesta_inicial:
        # Vuelve 2 apuestas hacia atras
        # El número 0.618... aproxima (se puede precisar más) la relación entre un número de fibonacci y el siguiente
        proxima_apuesta = round(apuesta_anterior / apuesta_inicial * 0.618033988205325051470844819764 ** 2) * apuesta_inicial
    elif ganaste:
        # La apuesta es igual a la apuesta inicial
        proxima_apuesta = apuesta_inicial
    else:
        proxima_apuesta = round(apuesta_anterior / apuesta_inicial / 0.618033988205325051470844819764) * apuesta_inicial

    return proxima_apuesta


def main():
    saldo = 1000  # TODO: Justificar el minimo ingresado
    apuesta_inicial = 10
    apuesta_par = True
    capital_infinito = True

    cant_tiradas, cant_corridas, num_elegido, estrategia_elegida, capital_elegido = inicializar_valores()

    if capital_elegido == "f":
        capital_infinito = False

    if estrategia_elegida == 'm':
        estrategia = martin_gala
    elif estrategia_elegida == 'd':
        estrategia = dalamber
    elif estrategia_elegida == 'f':
        estrategia = fibonacci

    # ejecutar_corridas(cant_tiradas, cant_corridas, num_elegido, estrategia, capital)
    corridas(cant_tiradas, cant_corridas, estrategia, capital_infinito, apuesta_par, saldo, apuesta_inicial)


if __name__ == '__main__':
    main()
