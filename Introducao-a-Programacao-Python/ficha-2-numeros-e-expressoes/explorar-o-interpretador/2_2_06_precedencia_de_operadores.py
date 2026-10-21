"""
Ficha 2 · Problema 2.2.6 · Precedência de operadores

Ordem de prioridade (da maior para a menor):
  1. **            (associa da direita para a esquerda)
  2. - e + unários
  3. *  /  //  %
  4. +  -
Os parênteses alteram a ordem.
"""

print(2 + 3 * 1 + 2)      # a) 7
print(2 + 3 + 1 + 2)      # b) 8
print((2 + 3) * (1 + 2))  # c) 15
print((2 + 3) * 1 + 2)    # d) 7
print(4 ** 3 ** 2)        # e) 262144 -> 4 ** (3 ** 2) = 4 ** 9
print(- + - + 6)          # f) 6 -> os dois sinais '-' anulam-se
