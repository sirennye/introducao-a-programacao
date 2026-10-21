"""
Ficha 4 · Problema 4.3.9 · Palavras Amigas

Duas palavras de igual comprimento dizem-se amigas se o número de posições
em que os respetivos carateres diferem for inferior a 10%.
Se o comprimento for diferente, não são amigas (ou levanta erro).
"""


def palavras_amigas(p1, p2):
    """Verifica se duas palavras de igual tamanho diferem em menos de 10% dos carateres."""
    if len(p1) != len(p2):
        return False
    if len(p1) == 0:
        return True

    diferencas = 0
    for c1, c2 in zip(p1, p2):
        if c1 != c2:
            diferencas += 1

    percentagem_dif = (diferencas / len(p1)) * 100
    return percentagem_dif < 10.0


if __name__ == '__main__':
    pares = [
        ("computador", "computador"),  # 0%
        ("abcdefghij", "xbcdefghij"),  # 1/10 = 10% -> False (< 10%)
        ("abcdefghijklmnop", "xbcdefghijklmnop"),  # 1/16 = 6.25% -> True
        ("python", "cython"),          # 1/6 = 16.67% -> False
    ]
    for w1, w2 in pares:
        amigas = palavras_amigas(w1, w2)
        print(f"'{w1}' e '{w2}' são amigas? {amigas}")
