"""
Ficha 6 · Problema 6.2.1 · Fatorial de um número inteiro (sem math.factorial)

fact(n) = n * (n - 1) * ... * 1
fact(0) = 1
"""


def fatorial(n):
    """Calcula o fatorial de um inteiro positivo n recorrendo a um ciclo acumulador."""
    if n < 0:
        raise ValueError("O fatorial apenas está definido para inteiros não negativos.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


if __name__ == '__main__':
    for num in (0, 1, 5, 7, 10):
        print(f"{num}! = {fatorial(num)}")
