"""
Ficha 4 · Problema 4.4.3 · Filtrar números pares num tuplo

Como os tuplos são imutáveis, acumulamos os pares num novo tuplo através
de concatenação de tuplo unitário (x,) ou convertendo um acumulador.
"""


def filtrar_pares(tuplo_inteiros):
    """Devolve um novo tuplo contendo apenas os números pares do tuplo de entrada."""
    resultado = ()
    for x in tuplo_inteiros:
        if x % 2 == 0:
            resultado = resultado + (x,)
    return resultado


if __name__ == '__main__':
    dados = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 22)
    pares = filtrar_pares(dados)
    print("Original:", dados)
    print("Apenas pares:", pares)
