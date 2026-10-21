"""
Ficha 3 · Problema 3.3.7 · Aproximação da constante de Euler (e)

e = sum_{i=0}^inf 1 / i!
Calcula uma aproximação de e somando termos até que o termo adicionado
seja inferior a uma dada tolerância (precisão).
"""
import math


def aproxima_euler(precisao=1e-10):
    """Calcula o valor aproximado de e pela série de Taylor."""
    e_aprox = 0.0
    termo = 1.0
    i = 0
    while termo >= precisao:
        e_aprox += termo
        i += 1
        termo = termo / i  # 1 / i! recursivo a partir do termo anterior
    return e_aprox, i


if __name__ == '__main__':
    estimativa, iteracoes = aproxima_euler(1e-12)
    print(f"Valor aproximado de e: {estimativa:.15f}")
    print(f"Valor exato (math.e) : {math.e:.15f}")
    print(f"Número de termos somados: {iteracoes}")
