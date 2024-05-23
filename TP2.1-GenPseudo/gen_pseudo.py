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
        # Normaliza el número entre 0 y 1
        return self.next() / self.m
    
    def name(self):
        return "GCL"
    

class ERNIE:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)

    def next(self):
        # Utiliza random.randint para simular la generación de un número aleatorio
        return random.randint(0, 2**31 - 1)

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

"""
class PCG: # Permuted Congruential Generator (Sin usar numpy)
    def __init__(self, seed, state=0):
        self.state = state
        self.inc = (seed << 1) | 1  # Incremento debe ser impar

    def next(self):
        # Estado del generador PCG
        oldstate = self.state
        self.state = oldstate * 6364136223846793005 + self.inc

        # Permutación de bits (permute) en el PCG
        xorshifted = ((oldstate >> 18) ^ oldstate) >> 27
        rot = oldstate >> 59
        return (xorshifted >> rot) | (xorshifted << ((-rot) & 31)) & ((1 << 32) - 1)  # Limitando a 32 bits

    def get_random_number(self):
        return self.next() / (2**32)

    def name(self):
        return "PCG"
"""
    
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

# Parametros para los generadores
seed = 42       # Semilla inicial

# Parámetros para el GCL
a = 1664525     # Multiplicador
c = 1013904223  # Incremento
m = 2**32       # Módulo (normalmente una potencia de 2)

# Instancias de los generadores
gcl = GCL(seed, a, c, m)
ernie = ERNIE(seed)
pcg = PCG64Wrapper()
#pcg2 = PCG(seed)

# Parámetros para ItaRNG
S0, S1, S2 = 1, 2, 3  # Semillas iniciales para ItaRNG
N = 1000  # Máximo valor deseado en el rango

ita_rng = ItaRNG(S0, S1, S2, N)

generadores = [gcl, ernie, ita_rng, pcg]