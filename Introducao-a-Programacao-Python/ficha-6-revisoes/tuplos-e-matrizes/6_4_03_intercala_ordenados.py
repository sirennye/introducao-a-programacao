"""
Ficha 6 · Problema 6.4.3 · Intercalar tuplos ordenados (Merge)

Dados dois tuplos de números já ordenados crescentemente, devolve um novo
tuplo contendo todos os elementos ordenados SEM usar funções de ordenação
pré-definidas (algoritmo Merge de dois apontadores em tempo O(n + m)).
Exemplo: intercala_ordenados((1, 4, 7), (2, 3, 8, 9)) -> (1, 2, 3, 4, 7, 8, 9)
"""


def intercala_ordenados(t1, t2):
    """Funde dois tuplos já ordenados mantendo a ordenação sem recorrer a sort."""
    resultado = []
    i = 0
    j = 0
    n1 = len(t1)
    n2 = len(t2)

    while i < n1 and j < n2:
        if t1[i] <= t2[j]:
            resultado.append(t1[i])
            i += 1
        else:
            resultado.append(t2[j])
            j += 1

    # Adiciona os elementos restantes
    while i < n1:
        resultado.append(t1[i])
        i += 1
    while j < n2:
        resultado.append(t2[j])
        j += 1

    return tuple(resultado)


if __name__ == '__main__':
    t1 = (1, 4, 7)
    t2 = (2, 3, 8, 9)
    res = intercala_ordenados(t1, t2)
    print("t1:", t1)
    print("t2:", t2)
    print("Intercalados ordenados:", res)
