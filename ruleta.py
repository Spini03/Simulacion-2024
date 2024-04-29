import random
import sys
import matplotlib.pyplot as plt

aciertos = 0

if len(sys.argv) != 7 or sys.argv[1] != "-c" or sys.argv[3] != "-n" or sys.argv[5] != "-e":
    print("Uso:python ruleta.py -c <cant_tiradas> -n <corridas> -e <num_elegido>")
    sys.exit(1)
cant_tiradas = int(sys.argv[2])
corridas = int(sys.argv[4])
num_elegido = int(sys.argv[6])
valores = list()
y1 = list()
#valores = [random.randint(0, 36) for _ in range(cant_tiradas)]
for i in range(corridas):
    valores[0] = random.randint(0, 36)
    y1[0] = valores[0] / 1
    for j in range(1,cant_tiradas):
        valores[j] = random.randint(0, 36)
        y1[j] = ( y1[j-1] * j-1 + valores[j] ) / j
    print(valores)
    aciertos_corrida = valores.count(num_elegido)
    print("Aciertos corrida: ", aciertos_corrida)
    aciertos = aciertos + aciertos_corrida

print(aciertos)

total_tiradas = corridas*cant_tiradas

x1 = list(range(cant_tiradas))





