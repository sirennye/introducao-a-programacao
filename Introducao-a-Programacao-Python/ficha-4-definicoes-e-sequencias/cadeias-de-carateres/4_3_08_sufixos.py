"""
Ficha 4 · Problema 4.3.8 · Sufixos de uma cadeia de carateres

Dada uma cadeia de caracteres, obtém todos os seus sufixos.
Versão genérica aplicável a qualquer cadeia de caracteres.
Exemplo: 'Monty Python' -> 'n', 'on', 'hon', ..., 'Monty Python'
(ou ordem decrescente de ponto de início).
"""


def sufixos(texto, ordem_crescente_tamanho=True):
    """Devolve todos os sufixos de um texto.

    Se ordem_crescente_tamanho for True, devolve do menor ('n') ao maior ('Monty Python').
    """
    resultado = []
    n = len(texto)
    if ordem_crescente_tamanho:
        for inicio in range(n - 1, -1, -1):
            resultado.append(texto[inicio:])
    else:
        for inicio in range(n):
            resultado.append(texto[inicio:])
    return resultado


if __name__ == '__main__':
    frase = "Monty Python"
    for suf in sufixos(frase):
        print(suf)
