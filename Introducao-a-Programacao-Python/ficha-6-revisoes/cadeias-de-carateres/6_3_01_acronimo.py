"""
Ficha 6 · Problema 6.3.1 · Acrónimo de um nome

Dado um nome por extenso (ex: 'Random Access Memory'), constrói
o respetivo acrónimo com as primeiras letras em maiúsculas (ex: 'RAM').

Notas pedagógicas e convenções:
  - Palavras de ligação ('de', 'da', 'do', 'dos', 'das', 'e', 'à', 'and', 'of') são
    habitualmente omitidas para que 'Universidade de Coimbra' resulte em 'UC'
    e 'Introdução à Programação' em 'IP'.
  - Siglas institucionais/académicas consagradas podem seguir convenções específicas
    (ex.: 'Artificial Intelligence and Data Science' -> 'AIDTS' para evitar o acrónimo ambíguo 'AIDS').
"""

# Palavras de ligação e preposições ignoradas na construção de acrónimos
PALAVRAS_IGNORADAS = {'de', 'da', 'do', 'dos', 'das', 'e', 'a', 'o', 'em', 'à', 'and', 'of', 'for'}

# Acrónimos institucionais ou convenções académicas específicas
ACRONIMOS_CONVENCIONAIS = {
    "Artificial Intelligence and Data Science": "AIDTS",
    "Inteligência Artificial e Ciência de Dados": "IACD",
    "Universidade de Coimbra": "UC",
}


def acronimo(nome_extenso, ignorar_ligacoes=True, usar_convencoes=True):
    """Constrói o acrónimo a partir das palavras de um nome.

    - Se usar_convencoes for True (padrão), respeita convenções consagradas
      (ex.: 'Artificial Intelligence and Data Science' -> 'AIDTS', 'Universidade de Coimbra' -> 'UC').
    - Se ignorar_ligacoes for True (padrão), omite palavras como 'de', 'da', 'and', etc.
    """
    nome_limpo = nome_extenso.strip()
    if usar_convencoes and nome_limpo in ACRONIMOS_CONVENCIONAIS:
        return ACRONIMOS_CONVENCIONAIS[nome_limpo]

    palavras = nome_limpo.split()
    letras = []
    for p in palavras:
        if not p:
            continue
        if ignorar_ligacoes and p.lower() in PALAVRAS_IGNORADAS:
            continue
        letras.append(p[0].upper())
    return "".join(letras)


if __name__ == '__main__':
    exemplos = [
        "Random Access Memory",
        "Universidade de Coimbra",
        "Introdução à Programação",
        "Artificial Intelligence and Data Science",
        "Inteligência Artificial e Ciência de Dados",
    ]
    for ex in exemplos:
        print(f"'{ex}' -> {acronimo(ex)}")


