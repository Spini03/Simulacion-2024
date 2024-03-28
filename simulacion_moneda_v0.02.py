import random

def lanzar_moneda():
    # Generar un número aleatorio entre 0 y 1
    resultado = random.random()
    
    # Comprobar si el resultado es menor o igual a 0.5
    if resultado <= 0.5:
        print("Cara")
    else:
        print("Cruz")

# Llamar a la función para lanzar la moneda
lanzar_moneda()