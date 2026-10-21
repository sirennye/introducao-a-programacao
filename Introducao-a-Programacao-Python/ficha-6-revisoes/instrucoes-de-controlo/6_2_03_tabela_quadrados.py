"""
Ficha 6 · Problema 6.2.3 · Tabela de Quadrados (parametrizável com n linhas)

Imprime uma tabela de duas colunas: Número e Quadrado.
O programa é parametrizável para qualquer número de linhas n.
"""


def tabela_quadrados(linhas=5):
    """Imprime a tabela de números e respetivos quadrados até n linhas."""
    print("Número  Quadrado")
    print("----------------")
    for i in range(1, linhas + 1):
        print(f"{i:4d}    {i ** 2:6d}")


if __name__ == '__main__':
    tabela_quadrados(7)
