"""
Ficha 2 · Problema 2.2.8 · Tipo do resultado de cada expressão

Regras:
  - '/' devolve sempre float (mesmo entre inteiros).
  - Se aparecer um complexo, o resultado é complex.
"""

print(1 / 2, type(1 / 2))                                    # a) float
print(1 / 2.0, type(1 / 2.0))                                # b) float
print(1.0 / 2, type(1.0 / 2))                                # c) float
print(1.0 / 2 / 4, type(1.0 / 2 / 4))                        # d) float
print(4 ** .5, type(4 ** .5))                                # e) float
print(4.0 ** (1 / 2), type(4.0 ** (1 / 2)))                  # f) float
print((8 + 5j) * 2, type((8 + 5j) * 2))                      # g) complex
print((3 + 2j) * 2.0 / (2 - 3j), type((3 + 2j) * 2.0 / (2 - 3j)))  # h) complex
print((3 - 6j) ** 3, type((3 - 6j) ** 3))                    # i) complex
