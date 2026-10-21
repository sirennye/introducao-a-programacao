"""
Ficha 6 · Problema 6.3.4 · Anagramas

Duas cadeias de caracteres são anagramas se têm exatamente as mesmas letras
na mesma quantidade, ignorando espaços e diferenças entre maiúsculas/minúsculas.
Exemplo: "Amor" e "Roma" -> True
"""


def limpa_letras(texto):
    """Extrai apenas as letras em minúsculas de uma cadeia."""
    return [c.lower() for c in texto if c.isalpha()]


def sao_anagramas(s1, s2):
    """Verifica se s1 e s2 são anagramas uma da outra."""
    letras1 = limpa_letras(s1)
    letras2 = limpa_letras(s2)

    if len(letras1) != len(letras2):
        return False

    # Contagem de cada letra sem recorrer a bibliotecas externas
    contagem1 = {}
    for c in letras1:
        contagem1[c] = contagem1.get(c, 0) + 1

    contagem2 = {}
    for c in letras2:
        contagem2[c] = contagem2.get(c, 0) + 1

    return contagem1 == contagem2


if __name__ == '__main__':
    pares = [
        ("Amor", "Roma"),
        ("A gentleman", "Elegant man"),
        ("Python", "Java"),
        ("listen", "silent"),
    ]
    for p1, p2 in pares:
        print(f"'{p1}' e '{p2}' são anagramas? {sao_anagramas(p1, p2)}")
