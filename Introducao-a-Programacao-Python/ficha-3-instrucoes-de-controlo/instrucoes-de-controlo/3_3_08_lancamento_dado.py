"""
Ficha 3 · Problema 3.3.8 · Lançamento de um dado (módulo random)

Simula o lançamento repetido de um dado equilibrado de 6 faces (1 a 6)
e calcula a percentagem de vezes em que saiu um número par (2, 4 ou 6).
Teoricamente, a percentagem converge para 50%.
"""
import random


def simula_lancamentos(n_lancamentos=10000):
    """Simula n lançamentos e devolve a fração e percentagem de números pares."""
    pares = 0
    for _ in range(n_lancamentos):
        face = random.randint(1, 6)
        if face % 2 == 0:
            pares += 1
    percentagem = (pares / n_lancamentos) * 100
    return pares, percentagem


if __name__ == '__main__':
    random.seed(42)  # semente para reprodutibilidade
    for n in (100, 1000, 10000, 100000):
        pares, pct = simula_lancamentos(n)
        print(f"Lançamentos: {n:6d} | Pares: {pares:6d} | Percentagem: {pct:.2f}%")
