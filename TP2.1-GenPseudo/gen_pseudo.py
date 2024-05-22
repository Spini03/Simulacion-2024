import numpy as np
import matplotlib.pyplot as plt


class GCL:
    def __init__(self, seed, a, c, m):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.current = seed

    def next(self):
        self.current = (self.a * self.current + self.c) % self.m
        return self.current

    def get_random_number(self):
        # Normaliza el número entre 0 y 1
        return self.next() / self.m
    
    def name(self):
        return "GCL"
    

class ERNIE:
    def __init__(self, seed):
        self.seed = seed
        self.current = seed

    def next(self):
        # Esta es una implementación ficticia de ERNIE basada en un GCL
        # Puedes reemplazar estos parámetros con los específicos de ERNIE si los conoces
        self.current = (self.current * 1103515245 + 12345) % (2**31)
        return self.current

    def get_random_number(self):
        return self.next() / (2**31)
    
    def name(self):
        return "ERNIE"


class ItaRNG:
    def __init__(self, seed):
        self.seed = seed
        self.current = seed

    def next(self):
        # Esta fórmula es ficticia y para ilustración
        # Debes reemplazarla con la fórmula específica de Ita si está disponible
        self.current = (self.current * 6364136223846793005 + 1442695040888963407) % (2**64)
        return self.current

    def get_random_number(self):
        return self.next() / (2**64)
    
    def name(self):
        return "Ita RNG"


def generar_imagen_ruido(generador, tamaño=(256, 256)):
    ruido = np.zeros(tamaño)
    
    for i in range(tamaño[0]):
        for j in range(tamaño[1]):
            ruido[i, j] = generador.get_random_number()
    
    plt.imshow(ruido, cmap='gray', interpolation='nearest')
    plt.title(f'Ruido con {generador.name()}')
    plt.axis('off')
    plt.show()


# Parametros para los generadores
seed = 42       # Semilla inicial

# Parámetros para el GCL
a = 1664525     # Multiplicador
c = 1013904223  # Incremento
m = 2**32       # Módulo (normalmente una potencia de 2)

# Instancias de los generadores
gcl = GCL(seed, a, c, m)
ernie = ERNIE(seed)
ita_rng = ItaRNG(seed)

# Generar imágenes de ruido con cada generador
generar_imagen_ruido(gcl)
generar_imagen_ruido(ernie)
generar_imagen_ruido(ita_rng)
