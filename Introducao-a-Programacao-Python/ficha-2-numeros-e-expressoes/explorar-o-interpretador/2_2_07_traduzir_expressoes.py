"""
Ficha 2 · Problema 2.2.7 · Traduzir expressões matemáticas para Python

a) 2 + (3 × 6/2)       b) (4 + 6) / (2 + 3)    c) (4/2)^5
d) (4/2)^(5+1)         e) (-3)^2               f) -(3^2)
"""

print(2 + (3 * (6 / 2)))   # a) 11.0
print((4 + 6) / (2 + 3))   # b) 2.0
print((4 / 2) ** 5)        # c) 32.0
print((4 / 2) ** (5 + 1))  # d) 64.0
print((-3) ** 2)           # e) 9
print(-(3 ** 2))           # f) -9

# Cuidado: -3 ** 2 dá -9, porque ** tem prioridade sobre o '-' unário.
print(-3 ** 2)
