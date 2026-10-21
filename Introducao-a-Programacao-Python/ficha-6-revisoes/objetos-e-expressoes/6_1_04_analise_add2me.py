"""
Ficha 6 · Problema 6.1.4 · Análise da função add2me (Polimorfismo em Python)

Definição:
    def add2me(x):
        return x + x

Resultados esperados e justificação:
  - add2me(23.4):
    O argumento é do tipo float. O operador '+' realiza a adição aritmética:
    23.4 + 23.4 = 46.8 (tipo float).

  - add2me('toto'):
    O argumento é do tipo str. O operador '+' realiza a concatenação de sequências:
    'toto' + 'toto' = 'totototo' (tipo str).

Conceito-chave:
  Em Python, o operador '+' é polimórfico — o seu comportamento depende
  do tipo (classe) dos operandos em tempo de execução (duck typing).
"""


def add2me(x):
    """Duplica um número (por soma) ou uma sequência (por concatenação)."""
    return x + x


if __name__ == '__main__':
    res_num = add2me(23.4)
    res_str = add2me('toto')
    print("add2me(23.4)   =", res_num, "-> tipo:", type(res_num))
    print("add2me('toto') =", repr(res_str), "-> tipo:", type(res_str))
