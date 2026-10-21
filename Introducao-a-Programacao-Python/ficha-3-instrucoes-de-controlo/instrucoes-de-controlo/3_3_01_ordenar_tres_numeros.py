"""
Ficha 3 · Problema 3.3.1 · Ordenar três números sem funções embutidas

Apresenta por ordem crescente três números inteiros dados como entrada,
minimizando o número de comparações (no máximo 3 comparações com árvore de decisão).
"""


def ordenar_tres(a, b, c):
    """Ordena 3 números minimizando o número de comparações (<= 3)."""
    if a <= b:
        if b <= c:
            return a, b, c
        else:  # c < b
            if a <= c:
                return a, c, b
            else:
                return c, a, b
    else:  # b < a
        if a <= c:
            return b, a, c
        else:  # c < a
            if b <= c:
                return b, c, a
            else:
                return c, b, a


if __name__ == '__main__':
    exemplos = [(9, 2, 5), (1, 2, 3), (3, 2, 1), (4, 4, 2)]
    for triplo in exemplos:
        ordenado = ordenar_tres(*triplo)
        print(f"Original: {triplo} -> Ordenado: {ordenado}")
