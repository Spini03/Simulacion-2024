

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

class ERNIE:
    def __init__(self, seed):
        self.seed = seed
        self.current = seed

    def next(self):
        # Esta es una implementación ficticia de ERNIE basada en un GCL
        # Puedes reemplazar estos parámetros con los específicos de ERNIE si los conoces
        self.current = (self.current * 1103515245 + 12345) % (2**31)
        return self.current

    def random(self):
        return self.next() / (2**31)

    def randint(self, a, b):
        return a + int(self.random() * (b - a + 1))

    def uniform(self, a, b):
        return a + (b - a) * self.random()

    def choice(self, seq):
        return seq[self.randint(0, len(seq) - 1)]

    def shuffle(self, seq):
        for i in range(len(seq) - 1, 0, -1):
            j = self.randint(0, i)
            seq[i], seq[j] = seq[j], seq[i]

    def sample(self, population, k):
        return [self.choice(population) for _ in range(k)]

# Uso del generador ERNIE ficticio
ernie = ERNIE(seed=42)

# Generar un número pseudoaleatorio entre 0 y 1
numero = ernie.random()
print(f"Número pseudoaleatorio entre 0 y 1: {numero}")

# Generar un número entero pseudoaleatorio en un rango específico
numero_entero = ernie.randint(1, 10)
print(f"Número entero pseudoaleatorio entre 1 y 10: {numero_entero}")

# Generar un número flotante pseudoaleatorio en un rango específico
numero_flotante = ernie.uniform(1.5, 5.5)
print(f"Número flotante pseudoaleatorio entre 1.5 y 5.5: {numero_flotante}")

# Seleccionar un elemento aleatorio de una lista
elementos = ['rojo', 'azul', 'verde', 'amarillo']
elemento = ernie.choice(elementos)
print(f"Elemento aleatorio de la lista: {elemento}")

# Mezclar los elementos de una lista aleatoriamente
ernie.shuffle(elementos)
print(f"Lista mezclada aleatoriamente: {elementos}")

# Generar una muestra aleatoria de una lista
muestra = ernie.sample(elementos, 3)
print(f"Muestra aleatoria de 3 elementos de la lista: {muestra}")


class ItaRNG:
    def __init__(self, seed):
        self.seed = seed
        self.current = seed

    def next(self):
        # Esta fórmula es ficticia y para ilustración
        # Debes reemplazarla con la fórmula específica de Ita si está disponible
        self.current = (self.current * 6364136223846793005 + 1442695040888963407) % (2**64)
        return self.current

    def random(self):
        return self.next() / (2**64)

    def randint(self, a, b):
        return a + int(self.random() * (b - a + 1))

    def uniform(self, a, b):
        return a + (b - a) * self.random()

    def choice(self, seq):
        return seq[self.randint(0, len(seq) - 1)]

    def shuffle(self, seq):
        for i in range(len(seq) - 1, 0, -1):
            j = self.randint(0, i)
            seq[i], seq[j] = seq[j], seq[i]

    def sample(self, population, k):
        return [self.choice(population) for _ in range(k)]

# Uso del generador Ita ficticio
ita_rng = ItaRNG(seed=42)

# Generar un número pseudoaleatorio entre 0 y 1
numero = ita_rng.random()
print(f"Número pseudoaleatorio entre 0 y 1: {numero}")

# Generar un número entero pseudoaleatorio en un

