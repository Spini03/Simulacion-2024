

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

# Parámetros para el GCL
seed = 42       # Semilla inicial
a = 1664525     # Multiplicador
c = 1013904223  # Incremento
m = 2**32       # Módulo (normalmente una potencia de 2)

# Crear una instancia del GCL
gcl = GCL(seed, a, c, m)

# Generar 1 número pseudoaleatorio
numero = gcl.get_random_number()
print(f"[GCL] Número pseudoaleatorio entre 0 y 1: {numero}")


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

# Uso del generador ERNIE ficticio
ernie = ERNIE(seed=42)

# Generar un número pseudoaleatorio entre 0 y 1
numero = ernie.get_random_number()
print(f"[ERNIE] Número pseudoaleatorio entre 0 y 1: {numero}")


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

# Uso del generador Ita ficticio
ita_rng = ItaRNG(seed=42)

# Generar un número pseudoaleatorio entre 0 y 1
numero = ita_rng.get_random_number()
print(f"[ITA_RNG] Número pseudoaleatorio entre 0 y 1: {numero}")


