"""
Ficha 6 · Problema 6.3.5 · Substituição manual (sem .replace())

Implementa uma função equivalente a texto.replace(alvo, novo), substituindo
todas as ocorrências da subcadeia alvo por novo usando apenas
fatiamento (slicing), concatenação e condicionais.
Exemplo: substitui("banana", "na", "no") -> "banono"
"""


def substitui(texto, alvo, novo):
    """Substitui ocorrências de alvo por novo sem usar str.replace."""
    if not alvo:
        return texto

    resultado = []
    i = 0
    tamanho_alvo = len(alvo)
    tamanho_texto = len(texto)

    while i < tamanho_texto:
        # Fatiamento para verificar se a subcadeia coincide com o alvo
        if texto[i:i + tamanho_alvo] == alvo:
            resultado.append(novo)
            i += tamanho_alvo
        else:
            resultado.append(texto[i])
            i += 1

    return "".join(resultado)


if __name__ == '__main__':
    exemplos = [
        ("banana", "na", "no"),
        ("o rato roeu a rolha", "ro", "XX"),
        ("aaaa", "aa", "b"),
    ]
    for txt, alvo, novo in exemplos:
        res = substitui(txt, alvo, novo)
        print(f"substitui('{txt}', '{alvo}', '{novo}') = '{res}'")
