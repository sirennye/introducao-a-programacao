"""
Ficha 4 · Problema 4.3.10 · Cifra de César (com deslocamento arbitrário)

Substitui cada carácter pelo carácter a uma distância k no alfabeto,
com enrolamento circular nas extremidades (usando aritmética modular % 26).
Suporta distâncias positivas ou negativas.
"""


def cifra_cesar(texto, distancia):
    """Codifica texto com um deslocamento circular no alfabeto."""
    resultado = []
    for c in texto:
        if 'a' <= c <= 'z':
            base = ord('a')
            novo = chr(base + (ord(c) - base + distancia) % 26)
            resultado.append(novo)
        elif 'A' <= c <= 'Z':
            base = ord('A')
            novo = chr(base + (ord(c) - base + distancia) % 26)
            resultado.append(novo)
        else:
            resultado.append(c)
    return "".join(resultado)


def descifra_cesar(texto, distancia):
    """Descodifica texto com o deslocamento inverso."""
    return cifra_cesar(texto, -distancia)


if __name__ == '__main__':
    original = "Hello, World! Python em Coimbra."
    k = 3
    cifrado = cifra_cesar(original, k)
    des = descifra_cesar(cifrado, k)
    print(f"Original:    {original}")
    print(f"Cifrado (+{k}): {cifrado}")
    print(f"Decifrado:   {des}")
