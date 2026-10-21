"""
Ficha 6 · Problema 6.3.3 · Parênteses Válidos e Balanceados

Verifica se os parênteses '(' e ')' numa expressão matemática estão
corretamente balanceados e fechados pela ordem certa.
Exemplo: "((a + b) * (c - d))" -> True; ") (a + b) (" -> False
"""


def parenteses_validos(expressao):
    """Verifica se os parênteses estão balanceados."""
    contador = 0
    for char in expressao:
        if char == '(':
            contador += 1
        elif char == ')':
            contador -= 1
            # Se contador for negativo, fechou um parêntese sem ter aberto
            if contador < 0:
                return False
    # No final, todos os parênteses abertos têm de ter sido fechados
    return contador == 0


if __name__ == '__main__':
    exemplos = [
        "((a + b) * (c - d))",
        ")(a + b)(",
        "(1 + 2) * (3 + (4 * 5))",
        "((a + b)",
        "a + b",
    ]
    for ex in exemplos:
        print(f"{ex:25s} -> Válido? {parenteses_validos(ex)}")
