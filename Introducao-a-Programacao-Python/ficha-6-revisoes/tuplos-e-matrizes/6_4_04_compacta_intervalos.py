"""
Ficha 6 · Problema 6.4.4 · Compactar intervalos consecutivos

Dado um tuplo de inteiros ordenados e sem duplicados, agrupa sequências
de números consecutivos em pares (inicio, fim).
Números isolados surgem como (n, n).
Exemplo: (1, 2, 3, 5, 7, 8, 10) -> ((1, 3), (5, 5), (7, 8), (10, 10))
"""


def compacta_intervalos(tuplo_ordenado):
    """Agrupa números consecutivos em intervalos fechados (inicio, fim)."""
    if not tuplo_ordenado:
        return ()

    intervalos = []
    inicio = tuplo_ordenado[0]
    anterior = tuplo_ordenado[0]

    for num in tuplo_ordenado[1:]:
        if num == anterior + 1:
            anterior = num
        else:
            intervalos.append((inicio, anterior))
            inicio = num
            anterior = num
    # Adiciona o último intervalo
    intervalos.append((inicio, anterior))

    return tuple(intervalos)


if __name__ == '__main__':
    dados = (1, 2, 3, 5, 7, 8, 10)
    resultado = compacta_intervalos(dados)
    print("Original:", dados)
    print("Intervalos compactados:", resultado)
