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

# Generar 10 números pseudoaleatorios
for _ in range(10):
    print(gcl.get_random_number())
