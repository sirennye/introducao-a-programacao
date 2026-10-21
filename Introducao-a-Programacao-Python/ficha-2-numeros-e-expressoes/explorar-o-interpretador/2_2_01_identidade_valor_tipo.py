"""
Ficha 2 · Problema 2.2.1 · Identidade, valor e tipo

Todos os objetos têm três atributos: identidade (id), valor e tipo (type).
Inspecionamos estes atributos para números de tipos diferentes.
"""

inteiro = 5
real = 5.0
complexo = 5 + 2j

print('Valor:', inteiro, '| Identidade:', id(inteiro), '| Tipo:', type(inteiro))
print('Valor:', real, '| Identidade:', id(real), '| Tipo:', type(real))
print('Valor:', complexo, '| Identidade:', id(complexo), '| Tipo:', type(complexo))

# Mesmo valor não significa mesmo objeto
print(inteiro == real)  # True  -> têm o mesmo valor
print(inteiro is real)  # False -> identidade (e tipo) diferentes
