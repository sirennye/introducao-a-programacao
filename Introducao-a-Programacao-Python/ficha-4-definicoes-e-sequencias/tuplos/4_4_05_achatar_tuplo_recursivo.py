"""
Ficha 4 · Problema 4.4.5 · Achatar tuplo recursivo (Flatten tuple)

Recebe um tuplo com qualquer nível de aninhamento e devolve um único
tuplo linear apenas com os valores finais, mantendo a ordem original.
Exemplo: (1, (2, 3), (4, (5, 6))) -> (1, 2, 3, 4, 5, 6)
"""


def achatar_tuplo(t):
    """Achata recursivamente um tuplo com múltiplos níveis de aninhamento."""
    resultado = ()
    for elemento in t:
        if isinstance(elemento, tuple):
            # Chamada recursiva para sub-tuplos
            resultado = resultado + achatar_tuplo(elemento)
        else:
            # Caso base: elemento atómico
            resultado = resultado + (elemento,)
    return resultado


if __name__ == '__main__':
    tuplo_aninhado = (1, (2, 3), (4, (5, 6)), ((7,), 8))
    achatado = achatar_tuplo(tuplo_aninhado)
    print("Aninhado:", tuplo_aninhado)
    print("Achatado:", achatado)
