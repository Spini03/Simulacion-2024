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
    parser.add_argument('-s', '--estrategia', type=str, choices=['m', 'd', 'f', 'o','ds', 'cons'], required=True,
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


def graficar(frec_rel, cant_tiradas, saldos_por_tirada, num_corrida, saldo_inicial, nombre_estrategia):
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle(f'Datos corrida {num_corrida} [{nombre_estrategia}]')

    # Flujo de cajas
    axs[0].set_title('Flujo de Cajas')
    axs[0].set_ylabel('Saldo')
    axs[0].plot(saldos_por_tirada, label='Saldo por Tirada')
    axs[0].scatter(range(len(saldos_por_tirada)), saldos_por_tirada, c='r', marker='o', label='Flujo de Cajas')
    axs[0].axhline(y=saldo_inicial, color='r', linestyle='--', label='Saldo Inicial')
    axs[0].set_xlabel('Número de tirada')
    axs[0].legend()

    # Gráfico de frecuencia relativa de obtener la respuesta favorable según n
    axs[1].set_title('Frecuencia Relativa')
    axs[1].set_ylabel('Frecuencia relativa')
    axs[1].hist(range(1, cant_tiradas + 1), bins=cant_tiradas, weights=frec_rel, align='left', rwidth=0.8, label='Frecuencia relativa de respuesta favorable según el n° de tiradas')
    axs[1].set_xlabel('Número de tirada')
    axs[1].legend()
    
    # Histograma de picos y valles entre cada tirada
    axs[2].set_title('Histograma Picos y Valles')
    axs[2].set_xlabel('Cambio en el Saldo')
    axs[2].set_ylabel('Frecuencia')
    cambios_en_saldo = np.diff(saldos_por_tirada)
    axs[2].hist(cambios_en_saldo, bins=20, alpha=0.7, color='b', edgecolor='black', linewidth=1.2)
    axs[2].axvline(x=0, color='r', linestyle='--', label='Cambio Neutral')
    axs[2].legend()

    plt.tight_layout()
    plt.show()


def corridas(cant_tiradas, cant_corridas, estrategia, capital_infinito, apuesta_par, saldo_inicial, apuesta_inicial):
    for corrida in range(cant_corridas):
        saldo = saldo_inicial

        # Variables para graficar
        ganadas = 0
        saldos_por_tirada = [saldo_inicial]
        saldos_por_corrida = []
        frecrel = []
        cant_actual_tiradas = 1

        print(f"=========== Corrida {corrida + 1} ================")
        es_ganador = corrida_por_pares(apuesta_par)
        if es_ganador:
            print(f"ganador! Saldo: {saldo} + {apuesta_inicial}")
            saldo += apuesta_inicial
        else:
            print(f"perdedor! Saldo: {saldo} - {apuesta_inicial}")
            saldo -= apuesta_inicial

        apuesta_anterior = apuesta_inicial
        sin_saldo = False

        saldos_por_tirada.append(saldo)
        ganadas += 1 if es_ganador else 0
        frecrel.append(ganadas / 1)

        for tirada in range(cant_tiradas - 1):

            apuesta_actual = estrategia(es_ganador, apuesta_inicial, apuesta_anterior)
            if not capital_infinito and saldo <= apuesta_actual:
                print("No tienes mas saldo para jugar")
                sin_saldo = True
                break
            
            cant_actual_tiradas += 1

            es_ganador = corrida_por_pares(apuesta_par)
            if es_ganador:
                print(f"ganador! Saldo: {saldo} + {apuesta_actual}")
                saldo += apuesta_actual
            else:
                print(f"perdedor! Saldo: {saldo} - {apuesta_actual}")
                saldo -= apuesta_actual

            apuesta_anterior = apuesta_actual

            saldos_por_tirada.append(saldo)
            ganadas += 1 if es_ganador else 0
            frecrel.append(ganadas / (tirada + 2))

        if sin_saldo:
            print(f"Saldo final: {saldo} (Saldo necesario: {apuesta_actual})")
        else:
            print(f"Saldo final: {saldo}")
        
        

        graficar(frecrel, cant_actual_tiradas, saldos_por_tirada, corrida + 1, saldo_inicial, estrategia.nombre)

        saldos_por_corrida.append(saldo)



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


def martin_gala(es_ganador, apuesta_inicial, apuesta_anterior):
    # Al perder se dobla la ultima apuesta, al ganar se vuelve a al monto inicial
    if es_ganador:
        proxima_apuesta = apuesta_inicial
    else:
        proxima_apuesta = apuesta_anterior * 2

    return proxima_apuesta


def dalamber(es_ganador, apuesta_inicial, apuesta_anterior):
    # Al perder se aumenta 1 unidad la apuesta, al ganar se disminuye una unidad hasta la inicial
    if es_ganador and apuesta_anterior == apuesta_inicial:
        proxima_apuesta = apuesta_inicial
    elif es_ganador:
        proxima_apuesta = apuesta_anterior - apuesta_inicial
    else:
        proxima_apuesta = apuesta_anterior + apuesta_inicial

    return proxima_apuesta


def fibonacci(es_ganador, apuesta_inicial, apuesta_anterior):
    golden = (1+5**0.5) / 2
    if es_ganador and apuesta_anterior == apuesta_inicial:
        proxima_apuesta = apuesta_inicial
    elif es_ganador:
        proxima_apuesta = round(
        apuesta_anterior / apuesta_inicial / golden ** 2) * apuesta_inicial
    else:
        proxima_apuesta = round(apuesta_anterior / apuesta_inicial * golden) * apuesta_inicial

    return proxima_apuesta

def despini(es_ganador, apuesta_inicial, apuesta_anterior):
    # Al perder se aumenta en 50% la apuesta, al ganar se disminuye el 20% de la apuesta.
    if es_ganador and apuesta_anterior == apuesta_inicial:
        proxima_apuesta = apuesta_inicial
    elif es_ganador:
        proxima_apuesta = round(apuesta_anterior - apuesta_anterior*(0.20))
    else:
        proxima_apuesta = round(apuesta_anterior + apuesta_anterior *(0.50))
    return proxima_apuesta

def conservadora(es_ganador, apuesta_inicial, apuesta_anterior):
    proxima_apuesta = apuesta_anterior  # Inicialmente, la próxima apuesta es la misma que la anterior
    ganancia_acumulada = 0

    # Inicialmente se apuesta el 10% del saldo inicial
    if es_ganador:
        proxima_apuesta = apuesta_inicial * 0.1
    else:
        proxima_apuesta = apuesta_inicial * 0.5

    # Si se ha ganado más del 50% del saldo inicial, se retira y reinicia la estrategia
    if ganancia_acumulada >= apuesta_inicial * 0.5:
        ganancia_acumulada -= apuesta_inicial * 0.5
        saldo += ganancia_acumulada
        ganancia_acumulada = 0
        proxima_apuesta = apuesta_inicial

    return proxima_apuesta





def main():
    saldo = 100000 
    #Suponiendo que son 100000 pesos argentinos. Como son 10000 tiradas nos pareció que tiene sentido.
    apuesta_inicial = 10
    apuesta_par = True
    capital_infinito = True

    cant_tiradas, cant_corridas, num_elegido, estrategia_elegida, capital_elegido = inicializar_valores()

    if capital_elegido == "f":
        capital_infinito = False

    if estrategia_elegida == 'm':
        estrategia = martin_gala
        estrategia.nombre = 'Martin Gala'
    elif estrategia_elegida == 'd':
        estrategia = dalamber
        estrategia.nombre = "D'Alembert"
    elif estrategia_elegida == 'f':
        estrategia = fibonacci
        estrategia.nombre = "Fibonacci"
    elif estrategia_elegida == 'ds':
        estrategia = despini
        estrategia.nombre = "D'Spini"
    elif estrategia_elegida == 'cons':
        estrategia = conservadora
        estrategia.nombre = "Conservadora"

    corridas(cant_tiradas, cant_corridas, estrategia, capital_infinito, apuesta_par, saldo, apuesta_inicial)


if __name__ == '__main__':
    main()

