"""
Ficha 2 · Problema 2.2.9 · Valor de um polinómio

Calcula x^4 + x^3 + 2x^2 - x para vários valores de x.
"""

for x in (1.1, 5, 2, -0.5):
    resultado = x ** 4 + x ** 3 + 2 * x ** 2 - x
    print('x =', x, '->', resultado)
