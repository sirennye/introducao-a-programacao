"""
Ficha 4 · Problema 4.4.4 · Intercalar dois tuplos

Recebe dois tuplos do mesmo tamanho e devolve um novo tuplo que combina
os seus elementos alternadamente: (a[0], b[0], a[1], b[1], ...).
"""


def intercalar_tuplos(tuplo_a, tuplo_b):
    """Intercala os elementos de dois tuplos do mesmo tamanho."""
    if len(tuplo_a) != len(tuplo_b):
        raise ValueError("Os tuplos têm de ter o mesmo tamanho.")

    resultado = ()
    for el_a, el_b in zip(tuplo_a, tuplo_b):
        resultado = resultado + (el_a, el_b)
    return resultado


if __name__ == '__main__':
    t1 = (1, 3, 5, 7)
    t2 = (2, 4, 6, 8)
    intercalado = intercalar_tuplos(t1, t2)
    print("Tuplo A:    ", t1)
    print("Tuplo B:    ", t2)
    print("Intercalado:", intercalado)
