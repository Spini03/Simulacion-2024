import random
import numpy as np
from numpy.random import Generator, PCG64, SeedSequence

class GCL: # De 1998
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
        return self.next() / self.m # Normaliza el número entre 0 y 1
    
    def name(self):
        return "GCL"
    

class ERNIE:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)

    def next(self):
        return random.randint(0, 2**31 - 1) # random.randint genera número aleatorio

    def get_random_number(self):
        return self.next() / (2**31 - 1)
    
    def name(self):
        return "ERNIE"


class ItaRNG: # De 2021
    def __init__(self, S0, S1, S2, N):
        self.S0 = S0
        self.S1 = S1
        self.S2 = S2
        self.N = N
        self.Xrn = 2.0  # Valor fijo cerca de 2, como se sugiere en la versión simplificada

    def next(self):
        # Paso del proceso n (Pn)
        Pn = abs(self.S2 - self.S0)
        
        # Cálculo final
        FRNSn = abs(self.N - (Pn * self.Xrn))

        # Actualización de las semillas
        self.S0, self.S1, self.S2 = self.S1, self.S2, FRNSn

        return FRNSn

    def get_random_number(self):
        return self.next() / self.N
    
    def name(self):
        return "Ita RNG"

    
class PCG64Wrapper: # Permuted Congruential Generator (Usando numpy) - De 2014
    def __init__(self, seed=None):
        self.seed_seq = SeedSequence(seed)
        self.bit_generator = PCG64(self.seed_seq)
        self.rng = Generator(self.bit_generator)

    def next(self):
        # Utiliza la capacidad de generar un entero de 64 bits
        return self.rng.integers(0, 2**64, dtype=np.uint64)

    def get_random_number(self):
        return self.rng.random()

    def name(self):
        return "PCG64"


## Parametros para los generadores
seed = 42 

# Parámetros para el GCL
multiplicador = 1664525    
incremento = 1013904223 
modulo = 2**32       #(normalmente una potencia de 2)

# Parámetros para ItaRNG
ItaRNG_seed_0, ItaRNG_seed_1, ItaRNG_seed_2 = 1, 2, 3  
max_range = 1000 

# Instancias de los generadores
gcl = GCL(seed, multiplicador, incremento, modulo)
ernie = ERNIE(seed)
pcg = PCG64Wrapper()
ita_rng = ItaRNG(ItaRNG_seed_0, ItaRNG_seed_1, ItaRNG_seed_2, max_range)
#pcg2 = PCG(seed)


# Para correr las imagenes y test, agregar los generadores a esta lista !!!
generadores = [gcl, ernie, ita_rng, pcg]