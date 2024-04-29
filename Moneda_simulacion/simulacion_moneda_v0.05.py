import random
import sys

# Verificar si se proporciona el número de valores como argumento
if len(sys.argv) != 3 or sys.argv[1] != "-n":
    print("Uso: python programa.py -n <num_valores>")
    sys.exit(1)

# Obtener el número de valores de los argumentos de la línea de comandos
num_valores = int(sys.argv[2])

# Generar los valores aleatorios entre 0 y 1 y almacenarlos en una lista
valores = [random.randint(0, 1) for _ in range(num_valores)]

# Imprimir la lista de valores generados
print("Valores generados:", valores)