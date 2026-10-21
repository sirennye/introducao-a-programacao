"""
Ficha 6 · Problema 6.2.4 · Tabuada de um número até 10

Dado um número inteiro n <= 10, imprime a tabela da sua tabuada de 1 a 10.
"""


def tabuada(n):
    """Imprime a tabuada do número n de 1 a 10."""
    print(f"Tabuada do número {n}")
    print("--------------------")
    for i in range(1, 11):
        print(f"{n} x {i:2d} = {n * i:2d}")


if __name__ == '__main__':
    tabuada(7)
