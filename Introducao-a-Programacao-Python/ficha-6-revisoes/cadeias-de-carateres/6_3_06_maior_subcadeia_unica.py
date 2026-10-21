"""
Ficha 6 · Problema 6.3.6 · Maior subcadeia sem caracteres repetidos

Devolve a maior subcadeia de caracteres contíguos que não contém nenhum
carácter repetido. Em caso de empate, devolve a primeira encontrada.
Exemplos:
  - "abcabcbb" -> "abc"
  - "pwwkew"   -> "wke"
  - "bbbbb"    -> "b"
"""


def maior_unica(texto):
    """Encontra a maior subcadeia contígua sem caracteres repetidos."""
    if not texto:
        return ""

    melhor_subcadeia = ""

    # Testa todas as subcadeias com dois apontadores / janela
    for inicio in range(len(texto)):
        vistos = set()
        fim = inicio
        while fim < len(texto) and texto[fim] not in vistos:
            vistos.add(texto[fim])
            fim += 1

        candidato = texto[inicio:fim]
        # Se for estritamente mais comprido, atualiza (mantém o primeiro em empate)
        if len(candidato) > len(melhor_subcadeia):
            melhor_subcadeia = candidato

    return melhor_subcadeia


if __name__ == '__main__':
    exemplos = ["abcabcbb", "pwwkew", "bbbbb", "abcdefg", "coimbra"]
    for ex in exemplos:
        print(f"'{ex}' -> Maior única: '{maior_unica(ex)}'")
