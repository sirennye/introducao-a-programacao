"""
Ficha 6 · Problema 6.4.5 · Pontos de sela numa matriz

Representando uma matriz como um tuplo de tuplos, devolve um tuplo
com as coordenadas (linha, coluna) de todos os pontos de sela.
Um elemento é ponto de sela se for, em simultâneo:
  - o menor elemento da sua linha (<= a todos os elementos da linha)
  - o maior elemento da sua coluna (>= a todos os elementos da coluna)

Exemplo:
  m = ((9, 8, 7),
       (5, 3, 2),
       (6, 6, 7))
  Linha 0: mínimo é 7 (coluna 2). Coluna 2: max é 7 (linha 0 e linha 2).
  Logo (0, 2) é ponto de sela.
"""


def pontos_de_sela(matriz):
    """Devolve as coordenadas (linha, coluna) dos pontos de sela da matriz."""
    if not matriz or not matriz[0]:
        return ()

    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    pontos = []

    for i in range(num_linhas):
        min_linha = min(matriz[i])
        for j in range(num_colunas):
            val = matriz[i][j]
            if val == min_linha:
                # Verifica se também é o maior elemento da coluna j
                coluna = [matriz[k][j] for k in range(num_linhas)]
                if val == max(coluna):
                    pontos.append((i, j))

    return tuple(pontos)


if __name__ == '__main__':
    m = ((9, 8, 7), (5, 3, 2), (6, 6, 7))
    resultado = pontos_de_sela(m)
    print("Matriz:", m)
    print("Pontos de sela:", resultado)
