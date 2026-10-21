"""
Ficha 2 · Problema 2.2.5 · Tipo de cada valor
"""

valores = ("IPRP", -1.75, -198, 5 + 8j, "501056389", 501056389)

for valor in valores:
    # repr() mostra as aspas das strings: "501056389" (str) vs 501056389 (int)
    print(repr(valor), '->', type(valor))

# Resultado: str, float, int, complex, str, int
