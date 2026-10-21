"""
Ficha 4 · Problema 4.3.7 · Prefixos de uma cadeia de carateres

Dada uma cadeia de caracteres, obtém e imprime todos os seus prefixos
do menor para o maior.
Exemplo: 'Monty Python' -> 'M', 'Mo', 'Mon', ..., 'Monty Python'
"""


def prefixos(texto):
    """Devolve a lista de todos os prefixos não vazios de texto."""
    resultado = []
    for fim in range(1, len(texto) + 1):
        resultado.append(texto[:fim])
    return resultado


if __name__ == '__main__':
    frase = "Monty Python"
    for pref in prefixos(frase):
        print(pref)
