"""
Ficha 4 · Problema 4.3.5 · Substituir vogais por espaços em branco

Desenvolva um programa que substitua as ocorrências de vogais numa cadeia
de caracteres por espaços em branco.
"""

VOGAIS = "aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕâêîôûÂÊÎÔÛ"


def substitui_vogais(texto):
    """Substitui todas as vogais por espaços em branco."""
    resultado = []
    for char in texto:
        if char in VOGAIS:
            resultado.append(" ")
        else:
            resultado.append(char)
    return "".join(resultado)


if __name__ == '__main__':
    frases = [
        "Introdução à Programação",
        "Python é uma linguagem fantástica",
        "Artificial Intelligence and Data Science",
    ]
    for f in frases:
        print(f"Original:   '{f}'")
        print(f"Modificado: '{substitui_vogais(f)}'\n")
