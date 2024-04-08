import statistics as st
import numpy as np
import matplotlib.pyplot as plt

def simular_ruleta(valor, cant_tiradas=500):
    cant_ganadas = 0
    valores_ruleta = []
    f_relativa = []
    media = []
    varianza = []
    desvio = []

    for s in range(cant_tiradas):
        num = np.random.randint(0, 37)
        valores_ruleta.append(num)
        if num == valor:
            cant_ganadas += 1
        f_relativa.append(cant_ganadas / (s + 1))
        media.append(np.mean(valores_ruleta))
        if s > 0:
            varianza.append(st.variance(valores_ruleta))
            desvio.append(st.stdev(valores_ruleta))

    return valores_ruleta, f_relativa, media, varianza, desvio

def graficar_resultados(valor, valores_ruleta, f_relativa, media, varianza, desvio):
    cant_tiradas = len(f_relativa)
    tiradas = range(cant_tiradas)

    plt.plot(tiradas, f_relativa, label='Frecuencia Relativa')
    plt.plot(tiradas, [1/37] * cant_tiradas, label='Frecuencia Relativa Esperada')

    plt.title(f"Frecuencias Relativas - Valor de ruleta elegido: {valor}")
    plt.xlabel("N° de tirada")
    plt.ylabel("Frecuencia Relativa")
    plt.legend()
    plt.show()

    plt.plot(tiradas, media, label='Promedio')
    plt.plot(tiradas, [18] * cant_tiradas, label='Promedio Esperado')

    plt.title("Gráfica del Promedio de los valores de las tiradas")
    plt.xlabel("N° de tirada")
    plt.ylabel("Promedio")
    plt.legend()
    plt.show()

    nro_tirada_x = range(1, len(varianza) + 1)
    plt.plot(nro_tirada_x, varianza, label='Varianza')
    plt.plot(nro_tirada_x, [114] * len(nro_tirada_x), label='Varianza Esperada')

    plt.title("Gráfica de la Varianza de los valores de las tiradas")
    plt.xlabel("N° de tirada")
    plt.ylabel("Varianza")
    plt.legend()
    plt.show()

    plt.plot(nro_tirada_x, desvio, label='Desvío Estándar')
    plt.plot(nro_tirada_x, [10.67707825] * len(nro_tirada_x), label='Desvío Estándar Esperado')

    plt.title("Gráfica del Desvío de los valores de las tiradas")
    plt.xlabel("N° de tirada")
    plt.ylabel("Desvío Estándar")
    plt.legend()
    plt.show()

def main():
    valor = int(input("Ingrese valor entre 0 y 36: "))
    if 0 <= valor <= 36:
        valores_ruleta, f_relativa, media, varianza, desvio = simular_ruleta(valor)
        graficar_resultados(valor, valores_ruleta, f_relativa, media, varianza, desvio)
    else:
        print("Error, número introducido inválido.")

if __name__ == "__main__":
    main()
