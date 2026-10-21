"""
Ficha 4 · Problema 4.3.2 · Cifra de Substituição

Cada letra do alfabeto é mapeada para outra com base numa chave de permutação.
A descodificação inverte esse mapeamento.
"""

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def descodifica_substituicao(texto_cifrado, chave_permutacao):
    """Descodifica um texto cifrado com base na chave de substituição."""
    # chave_permutacao mapeia ALFABETO[i] -> chave_permutacao[i]
    # Para descodificar, fazemos o mapeamento inverso: chave_permutacao[i] -> ALFABETO[i]
    mapa_inverso = {}
    for letra_orig, letra_cifra in zip(ALFABETO, chave_permutacao.upper()):
        mapa_inverso[letra_cifra] = letra_orig

    resultado = []
    for char in texto_cifrado:
        char_upper = char.upper()
        if char_upper in mapa_inverso:
            letra_dec = mapa_inverso[char_upper]
            resultado.append(letra_dec if char.isupper() else letra_dec.lower())
        else:
            resultado.append(char)
    return "".join(resultado)


if __name__ == '__main__':
    # Chave de exemplo (alfabeto invertido)
    chave = ALFABETO[::-1]
    cifrado = "ROOÉ KVOÍ"
    original = descodifica_substituicao(cifrado, chave)
    print(f"Chave: {chave}")
    print(f"Cifrado: '{cifrado}' -> Descodificado: '{original}'")
