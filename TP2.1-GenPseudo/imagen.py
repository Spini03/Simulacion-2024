import numpy as np
import matplotlib.pyplot as plt

from gen_pseudo import generadores

def generar_imagen_ruido(generador, tamaño=(256, 256)):
    ruido = np.zeros(tamaño)
    
    for i in range(tamaño[0]):
        for j in range(tamaño[1]):
            ruido[i, j] = generador.get_random_number()
    
    plt.imshow(ruido, cmap='gray', interpolation='nearest')
    plt.title(f'Ruido con {generador.name()}')
    plt.axis('off')
    plt.show()

# Generar imágenes de ruido con cada generador
for generador in generadores:
    generar_imagen_ruido(generador)