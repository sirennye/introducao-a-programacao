"""
Ficha 6 · Problema 6.4.6 · Agrupar palavras por assinatura de vogais

Recebe um tuplo de cadeias de caracteres e agrupa-as num tuplo de tuplos
de acordo com a sua 'assinatura de vogais' (as vogais da palavra pela ordem
exata em que aparecem, em minúsculas).
Cada sub-tuplo tem o formato: (assinatura, (palavra1, palavra2, ...))

Exemplo:
  t = ("casa", "faca", "bolo", "rato", "pato", "foco")
  -> (('aa', ('casa', 'faca')), ('oo', ('bolo', 'foco')), ('ao', ('rato', 'pato')))
"""

VOGAIS = set("aeiou")


def assinatura_vogais(palavra):
    """Extrai a sequência de vogais em minúsculas de uma palavra."""
    return "".join(c.lower() for c in palavra if c.lower() in VOGAIS)


def agrupa_por_vogais(tuplo_palavras):
    """Agrupa palavras por assinatura de vogais mantendo a ordem de primeira aparição."""
    grupos = {}
    ordem_chaves = []

    for palavra in tuplo_palavras:
        sig = assinatura_vogais(palavra)
        if sig not in grupos:
            grupos[sig] = []
            ordem_chaves.append(sig)
        grupos[sig].append(palavra)

    # Converte para tuplo de tuplos com formato (assinatura, (palavras...))
    resultado = []
    for sig in ordem_chaves:
        resultado.append((sig, tuple(grupos[sig])))

    return tuple(resultado)


if __name__ == '__main__':
    t = ("casa", "faca", "bolo", "rato", "pato", "foco")
    resultado = agrupa_por_vogais(t)
    print("Tuplo original:", t)
    print("Agrupado por vogais:", resultado)
