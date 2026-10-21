"""
Ficha 3 · Problema 3.3.10 · Sequência de Fibonacci

Sequência: 1, 1, 2, 3, 5, 8, 13, 21, ...
Verifica se um dado número pertence ou não à sequência de Fibonacci.
"""


def pertence_fibonacci(numero):
    """Verifica se um número inteiro positivo pertence à sequência de Fibonacci."""
    if numero < 1:
        return False
    a, b = 1, 1
    while a < numero:
        a, b = b, a + b
    return a == numero


if __name__ == '__main__':
    testes = [1, 2, 3, 4, 5, 8, 10, 13, 20, 21, 34, 50]
    for num in testes:
        resultado = pertence_fibonacci(num)
        print(f"Número {num:2d} pertence a Fibonacci? {resultado}")
