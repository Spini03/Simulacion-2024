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

def calcular_frecuencias(valores):
    # Calcular la frecuencia absoluta de cada valor
    frecuencia_absoluta = {0: valores.count(0), 1: valores.count(1)}

    # Calcular la frecuencia relativa de cada valor
    frecuencia_relativa = {0: frecuencia_absoluta[0] / len(valores), 1: frecuencia_absoluta[1] / len(valores)}

    return frecuencia_absoluta, frecuencia_relativa

# Calcular frecuencias iniciales
frecuencia_absoluta, frecuencia_relativa = calcular_frecuencias(valores)

# Imprimir los resultados iniciales
print("Valores generados:", valores)
print("Frecuencia absoluta de 0:", frecuencia_absoluta[0])
print("Frecuencia absoluta de 1:", frecuencia_absoluta[1])
print("Frecuencia relativa de 0:", frecuencia_relativa[0])
print("Frecuencia relativa de 1:", frecuencia_relativa[1])

# Simular la adición de nuevos valores
while True:
    nuevo_valor = random.randint(0, 1)
    valores.append(nuevo_valor)
    frecuencia_absoluta, frecuencia_relativa = calcular_frecuencias(valores)
    print("\nNuevo valor generado:", nuevo_valor)
    print("Valores generados:", valores)
    print("Frecuencia absoluta de 0:", frecuencia_absoluta[0])
    print("Frecuencia absoluta de 1:", frecuencia_absoluta[1])
    print("Frecuencia relativa de 0:", frecuencia_relativa[0])
    print("Frecuencia relativa de 1:", frecuencia_relativa[1])