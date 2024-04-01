import random
import sys
import matplotlib.pyplot as plt

aciertos = 0
prom_esperado=18
valor_fr_esperada=1/37
valor_var_esperada=114
valor_desvio_esperado=10.67707825
todos_los_valores = []
todas_las_tiradas = []
valores = [1000]
y1 = [1000]

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
        promedios.append(round(promedio,3))
    return promedios


def frecrel_corrida(lista):
    frec_rel = []
    acum = 0
    for i, valor in enumerate(lista):
        if valor == num_elegido: 
            acum+=1  
        fr= acum/(i+1)
        frec_rel.append(round(fr,3))
    return frec_rel

def var_corrida(lista, promedios):
    varianza = []
    for i, valor in enumerate(lista):
        var = ((valor - promedios[i])**2)/(i+1)
        varianza.append(round(var))
    return varianza

def des_corrida(lista):
    desvio = []
    for varianza in lista:
        desvio.append(round(plt.sqrt(varianza), 3))
    return desvio

for i in range(corridas):
        valores[0] = random.randint(0, 36)
        y1[0] = valores[0] 
        for j in range(1,cant_tiradas):
            valores.append(random.randint(0, 36))
            y1.append((( y1[j-1] * j + valores[j] ) / (j + 1)))
        todos_los_valores.append(valores)
        print(valores)
        aciertos_corrida = valores.count(num_elegido)
        print("Aciertos corrida: ", aciertos_corrida)
        aciertos = aciertos + aciertos_corrida

print("Aciertos totales: ",aciertos)
print("Lista de los promedios de cada tirada: ", y1)
#valores_finales = dict(zip(todos_los_valores,map(lambda x: todos_los_valores.count(x),todos_los_valores)))
#print(sorted(valores_finales.items(), key=lambda x:x[1]))

#print(todos_los_valores)


total_tiradas = corridas*cant_tiradas

x1 = list(range(cant_tiradas))

frec_relativa_esperada = cant_tiradas / 36
frec_absoluta_esperada = 20

plt.figure(figsize=(10, 6))
plt.plot(y1, label='Tiradas', color='blue')
plt.plot(frec_absoluta_esperada, label='Valor Constante', linestyle='--', color='red')
plt.xlabel('Número de tirada')
plt.ylabel('Valor obtenido')
plt.title('Gráfico de los Valores de las tiradas con Valor Constante Intermitente')
plt.legend()
plt.grid(True)
plt.show()

