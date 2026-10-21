"""
Ficha 6 · Problema 6.4.1 · Imprimir elementos de uma matriz com posições

Representa uma matriz como um tuplo de tuplos e imprime cada elemento
antecedido pela sua coordenada (linha, coluna).
Exemplo: ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12))
"""


def imprime_matriz(matriz):
    """Imprime a matriz com as coordenadas (linha, coluna) de cada elemento."""
    for i, linha in enumerate(matriz):
        elementos_linha = [f"({i},{j}) : {val}" for j, val in enumerate(linha)]
        print("  ".join(elementos_linha))


if __name__ == '__main__':
    m = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12))
    imprime_matriz(m)
