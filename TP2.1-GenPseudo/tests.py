import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

from gen_pseudo import generadores

# Prueba Chi-cuadrado (Chi-square test)
def chi_square_test(data, bins=10, alpha=0.05):
    observed, _ = np.histogram(data, bins=bins)
    expected = np.full_like(observed, len(data) / bins)
    chi_squared_stat = ((observed - expected) ** 2 / expected).sum()
    critical_value = scipy.stats.chi2.ppf(1 - alpha, bins - 1)
    return chi_squared_stat, critical_value, chi_squared_stat < critical_value

# Prueba de corridas arriba y abajo de la mediana (Test of runs above and below the median)
def runs_test(data, median, alpha=0.05):
    runs = [1 if x >= median else 0 for x in data]
    n1 = sum(runs)
    n2 = len(runs) - n1
    runs_test_stat = abs(n1 - n2) / np.sqrt(2 * len(runs) * (2 * len(runs) - 1) / 24)
    z_alpha = scipy.stats.norm.ppf(1 - alpha / 2)
    return runs_test_stat, z_alpha, abs(runs_test_stat) < z_alpha

# Prueba de arreglos inversos (Reverse arrangements test)
def reverse_arrangements_test(data, alpha=0.05):
    n = len(data)
    mean = np.mean(data)
    reverse_arrangements = sum(1 for x in data if x > mean) * sum(1 for x in data if x < mean)
    reverse_arrangements_test_stat = (reverse_arrangements - n * (n - 1) / 4) / np.sqrt(n * (n - 1) * (2 * n + 5) / 72)
    z_alpha = scipy.stats.norm.ppf(1 - alpha / 2)
    return reverse_arrangements_test_stat, z_alpha, abs(reverse_arrangements_test_stat) < z_alpha

# Prueba de sumas superpuestas (Overlapping sums test)
def overlapping_sums_test(data, m=10, alpha=0.05):
    n = len(data)
    s = np.zeros(m)
    for i in range(m):
        s[i] = sum(data[j] for j in range(i, n, m))
    s_mean = np.mean(s)
    s_std = np.std(s)
    overlapping_sums_test_stat = (np.sqrt(m) / s_std) * (s_mean - 0.5 * n)
    z_alpha = scipy.stats.norm.ppf(1 - alpha / 2)
    return overlapping_sums_test_stat, z_alpha, abs(overlapping_sums_test_stat) < z_alpha

def show_tests(generador):
    data= [generador.get_random_number() for _ in range(1000)]

    print('\n')
    print(f"***** Tests: {generador.name()} *****")
    print("Chi_square_test: ",chi_square_test(data))
    print("Runs_test: ", runs_test(data, np.median(data)))
    print("reverse_arrangements_test", reverse_arrangements_test(data))
    print("overlapping_sums_test", overlapping_sums_test(data))

for generador in generadores:
    show_tests(generador)


