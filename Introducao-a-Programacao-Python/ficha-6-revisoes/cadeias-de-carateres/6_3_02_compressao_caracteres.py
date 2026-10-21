"""
Ficha 6 · Problema 6.3.2 · Compressão de caracteres repetidos consecutivos (Run-Length)

Substitui sequências de caracteres idênticos consecutivos pelo carácter
seguido do número de ocorrências.
Exemplo: 'aaabbcdddd' -> 'a3b2c1d4'
"""


def comprime(texto):
    """Comprime texto substituindo repetições consecutivas por char + contagem."""
    if not texto:
        return ""

    resultado = []
    char_atual = texto[0]
    contagem = 1

    for c in texto[1:]:
        if c == char_atual:
            contagem += 1
        else:
            resultado.append(f"{char_atual}{contagem}")
            char_atual = c
            contagem = 1
    # Adiciona o último grupo
    resultado.append(f"{char_atual}{contagem}")

    return "".join(resultado)


if __name__ == '__main__':
    exemplos = ["aaabbcdddd", "wwwwaaadexxxxxx", "a", "abcdef"]
    for ex in exemplos:
        print(f"Original: '{ex}' -> Comprimido: '{comprime(ex)}'")
