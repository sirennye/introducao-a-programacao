"""
Ficha 4 · Problema 4.3.3 · Cadeia complementar de ADN

Bases: A, T, C, G
Complementos: A <-> T, C <-> G
"""


def cadeia_complementar_adn(cadeia):
    """Devolve a cadeia complementar de uma sequência de ADN."""
    tabela = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
              'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    complementar = []
    for base in cadeia:
        complementar.append(tabela.get(base, base))
    return "".join(complementar)


if __name__ == '__main__':
    adn = "ATCGGCTA"
    comp = cadeia_complementar_adn(adn)
    print(f"Original:     {adn}")
    print(f"Complementar: {comp}")
